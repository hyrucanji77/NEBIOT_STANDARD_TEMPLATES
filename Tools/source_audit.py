"""Read-only OOXML formula replay and cell-level comparison for supplied calculation workbooks.
No workbook is modified. Supports only the expression vocabulary documented below.
Run: python source_audit.py --source EA=/path/source.xlsx --output /path/review
"""
from __future__ import annotations
import argparse,ast,csv,gzip,hashlib,json,math,re,sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from functools import lru_cache
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships'

def colnum(v):
 n=0
 for c in v:n=n*26+ord(c)-64
 return n

def colstr(n):
 out=''
 while n:n,r=divmod(n-1,26);out=chr(65+r)+out
 return out

def rc(v):
 m=re.fullmatch(r'(\$?)([A-Z]+)(\$?)(\d+)',v)
 if not m:raise ValueError('Unsupported cell reference '+v)
 return colnum(m[2]),int(m[4])
REF=re.compile(r"(?<![A-Za-z0-9_])(?:(?:'((?:[^']|'')+)'|([A-Za-z_][A-Za-z0-9_.]*))!)?(\$?[A-Z]{1,3}\$?\d+)(?::(\$?[A-Z]{1,3}\$?\d+))?(?![A-Za-z0-9_])")

def shift(formula,anchor,cell):
 ac,ar=rc(anchor);cc,rr=rc(cell)
 def replace(m):
  def move(s):
   x=re.fullmatch(r'(\$?)([A-Z]+)(\$?)(\d+)',s)
   c=colnum(x[2])+(0 if x[1] else cc-ac);r=int(x[4])+(0 if x[3] else rr-ar)
   if c<1 or r<1:raise ValueError('Shift leaves worksheet')
   return x[1]+colstr(c)+x[3]+str(r)
  prefix=m.group(0)[:m.start(3)-m.start()]
  return prefix+move(m[3])+(':'+move(m[4]) if m[4] else '')
 return REF.sub(replace,formula)

def read(path):
 result={}
 with ZipFile(path) as z:
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   ss=[''.join(t.text or '' for t in si.findall('.//s:t',NS)) for si in ET.fromstring(z.read('xl/sharedStrings.xml'))]
  targets={e.attrib['Id']:e.attrib['Target'] for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  for sheet in ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',NS):
   tar=targets[sheet.attrib['{'+REL+'}id']];tar=tar.lstrip('/') if tar.startswith('/') else 'xl/'+tar
   xml=ET.fromstring(z.read(tar));cells={};shared={}
   for cell in xml.findall('.//s:sheetData/s:row/s:c',NS):
    a=cell.attrib['r'];typ=cell.get('t','n');v=cell.find('s:v',NS);f=cell.find('s:f',NS);raw=v.text if v is not None else None
    if typ=='s':value=ss[int(raw)] if raw is not None else ''
    elif typ=='inlineStr':value=''.join(t.text or '' for t in cell.findall('.//s:t',NS))
    elif typ=='b':value=raw=='1'
    elif typ in ('str','e','d'):value=raw
    else:
     try:value=float(raw) if raw is not None else None
     except ValueError:value=raw
    formula=None
    if f is not None:
     if f.get('t')=='shared':
      si=f.get('si')
      if f.text:shared[si]=(a,f.text)
      if si not in shared:raise ValueError('Shared formula anchor absent '+a)
      formula=shift(shared[si][1],shared[si][0],a)
     else:formula=f.text
    if value is not None or f is not None:cells[a]={'value':value,'type':typ,'formula':formula}
   result[sheet.get('name')]={'cells':cells,'merges':[e.get('ref') for e in xml.findall('.//s:mergeCell',NS)]}
 return result

class Replay:
 def __init__(self,book):self.book=book;self.memo={};self.visiting=set();self.compiled={}
 def ref(self,sheet,address,stop=None):
  if stop:
   a,r=rc(address);b,t=rc(stop)
   return [[self.cell(sheet,colstr(c)+str(y),blank=None) for c in range(a,b+1)] for y in range(r,t+1)]
  return self.cell(sheet,address.replace('$',''),blank=0)
 def cell(self,sheet,addr,blank=0):
  key=(sheet,addr.replace('$',''));cell=self.book[sheet]['cells'].get(key[1])
  if not cell:return blank
  if not cell['formula']:return blank if cell['value'] is None else cell['value']
  if key in self.memo:return self.memo[key]
  if key in self.visiting:raise ValueError('Circular formula '+str(key))
  self.visiting.add(key)
  try:
   f=cell['formula']
   def replace(m):
    sh=(m[1].replace("''", "'") if m[1] else m[2]) or sheet
    return 'GET('+repr(sh)+','+repr(m[3].replace('$',''))+(','+repr(m[4].replace('$','')) if m[4] else '')+')'
   expr=REF.sub(replace,f).replace('^','**')
   if expr not in self.compiled:
    tree=ast.parse(expr,mode='eval')
    allowed=(ast.Expression,ast.BinOp,ast.UnaryOp,ast.Call,ast.Name,ast.Load,ast.Constant,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.UAdd,ast.USub)
    if any(not isinstance(x,allowed) for x in ast.walk(tree)):raise ValueError('Unsupported expression '+f)
    names={'GET','SUM','INDEX','VLOOKUP','POWER','AVERAGE','PI','TRUE','FALSE'}
    if any(isinstance(x,ast.Name) and x.id not in names for x in ast.walk(tree)):raise ValueError('Unsupported function '+f)
    self.compiled[expr]=compile(tree,'<spreadsheet>','eval')
   val=eval(self.compiled[expr],{'__builtins__':{}},{'GET':self.ref,'SUM':SUM,'INDEX':INDEX,'VLOOKUP':VLOOKUP,'POWER':pow,'AVERAGE':AVERAGE,'PI':lambda:math.pi,'TRUE':True,'FALSE':False})
   self.memo[key]=val
   return val
  finally:self.visiting.remove(key)

def flat(v):
 if isinstance(v,list):
  for x in v:yield from flat(x)
 else:yield v

def SUM(*v):return sum(x for x in flat(list(v)) if isinstance(x,(int,float)) and not isinstance(x,bool))
def AVERAGE(*v):
 vals=[x for x in flat(list(v)) if isinstance(x,(int,float)) and not isinstance(x,bool)]
 if not vals:raise ValueError('Empty average')
 return sum(vals)/len(vals)
def INDEX(a,r,c=1):
 r=int(r);c=int(c)
 if not isinstance(a,list):a=[[a]]
 if r==0:
  if len(a)==1:return a[0][c-1]
  return [[row[c-1]] for row in a]
 if c==0:
  if len(a[0])==1:return a[r-1][0]
  return [a[r-1]]
 return a[r-1][c-1]
def VLOOKUP(v,a,c,approx=True):
 c=int(c);match=None
 for row in a:
  k=row[0]
  if k==v:return row[c-1]
  if approx and k is not None:
   try:
    if k<=v:match=row[c-1]
   except TypeError:pass
 if approx and match is not None:return match
 raise ValueError('Lookup missing '+str(v))

def audit(path,alias,out,atol=1e-7,rtol=1e-10):
 b=read(path);replay=Replay(b);out=Path(out);out.mkdir(parents=True,exist_ok=True)
 n=0;bad=[];errors=[];records=[]
 with gzip.open(out/(alias+'_formula_cells.csv.gz'),'wt',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f);w.writerow(['source_alias','worksheet','cell','source_formula','cached_value','recursive_value','difference','arithmetic_match'])
  for sh,info in b.items():
   for addr,cell in info['cells'].items():
    if not cell['formula']:continue
    n+=1
    try:
     got=replay.cell(sh,addr);expected=cell['value']
     if isinstance(got,(int,float)) and isinstance(expected,(int,float)):
      diff=got-expected;ok=math.isclose(got,expected,rel_tol=rtol,abs_tol=atol)
     else:diff='';ok=got==expected
     if not ok:bad.append([sh,addr,expected,got,diff])
     w.writerow([alias,sh,addr,'='+cell['formula'],expected,got,diff,'MATCH' if ok else 'DIFFERENCE'])
    except Exception as e:errors.append([sh,addr,str(e)]);w.writerow([alias,sh,addr,'='+cell['formula'],cell['value'],'','','NOT_EVALUATED'])
  summary={'source_alias':alias,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'sheets':len(b),'formula_cells':n,'recursive_matches':n-len(bad)-len(errors),'mismatches':len(bad),'unevaluated':len(errors),'absolute_tolerance':atol,'relative_tolerance':rtol,'comparison_scope':'recursive arithmetic replay from literal cells, not field or methodological validation','details':bad[:50],'errors':errors[:50]}
 (out/(alias+'_replay.json')).write_text(json.dumps(summary,indent=2))
 return summary,b,replay
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',action='append',required=True,help='ALIAS=/path/workbook.xlsx');p.add_argument('--output',required=True);p.add_argument('--atol',type=float,default=1e-7);p.add_argument('--rtol',type=float,default=1e-10);a=p.parse_args()
 for v in a.source:
  alias,path=v.split('=',1);summary,_,_=audit(path,alias,a.output,a.atol,a.rtol);print(json.dumps(summary,indent=2))
