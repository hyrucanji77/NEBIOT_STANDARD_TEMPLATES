"""Read-only mathematical notation for the exact cell expressions in an XLSX workbook.

Output is a cell-address mathematical rendition, not an inferred environmental model.
Excel absolute/relative copy flags remain available in the original-formula column.
"""
from __future__ import annotations
import ast,csv,gzip,json,re,argparse
from pathlib import Path
from source_audit import REF,read,rc

def textext(x):
    return str(x).replace('\\',r'\textbackslash{}').replace('_',r'\_').replace('&',r'\&').replace('%',r'\%').replace('#',r'\#').replace('$',r'\$')

def celltex(sh,addr):
    return r'v_{\text{'+textext(sh)+r'},\text{'+textext(addr.replace('$',''))+'}}'

def mathematical(formula,sh):
    def ref(m):return 'GET('+repr((m[1].replace("''", "'") if m[1] else m[2]) or sh)+','+repr(m[3])+(','+repr(m[4]) if m[4] else '')+')'
    tree=ast.parse(REF.sub(ref,formula.lstrip('=')).replace('^','**'),mode='eval')
    def visit(n):
        if isinstance(n,ast.Expression):return visit(n.body)
        if isinstance(n,ast.Constant):return str(n.value) if not isinstance(n.value,str) else r'\text{'+textext(n.value)+'}'
        if isinstance(n,ast.Name):return r'\mathrm{'+textext(n.id)+'}'
        if isinstance(n,ast.UnaryOp):return ('-' if isinstance(n.op,ast.USub) else '+')+r'\left('+visit(n.operand)+r'\right)'
        if isinstance(n,ast.BinOp):
            a,b=visit(n.left),visit(n.right)
            if isinstance(n.op,ast.Div):return r'\frac{'+a+'}{'+b+'}'
            if isinstance(n.op,ast.Pow):return r'\left('+a+r'\right)^{'+b+'}'
            op={ast.Add:'+',ast.Sub:'-',ast.Mult:r'\cdot'}[type(n.op)]
            return r'\left('+a+' '+op+' '+b+r'\right)'
        if isinstance(n,ast.Call):
            name=n.func.id
            if name=='GET':
                sheet=n.args[0].value;start=n.args[1].value
                if len(n.args)==2:return celltex(sheet,start)
                return r'\mathcal R_{\text{'+textext(sheet)+r'},\text{'+textext(start+':'+n.args[2].value)+'}}'
            if name=='PI':return r'\pi'
            if name=='POWER':return r'\left('+visit(n.args[0])+r'\right)^{'+visit(n.args[1])+'}'
            return r'\operatorname{'+textext(name)+r'}\!\left('+', '.join(visit(x) for x in n.args)+r'\right)'
        raise ValueError('Unsupported syntax '+type(n).__name__)
    return visit(tree)

def relative_family(f,sheet,addr):
    c,r=rc(addr)
    def rep(m):
        def coord(x):
            cc,rr=rc(x);p=re.fullmatch(r'(\$?)([A-Z]+)(\$?)(\d+)',x)
            return ('C'+str(cc) if p[1] else 'C['+str(cc-c)+']')+('R'+str(rr) if p[3] else 'R['+str(rr-r)+']')
        sh=(m[1] or m[2]) or '@same'
        return repr(sh)+'!'+coord(m[3])+(':'+coord(m[4]) if m[4] else '')
    return REF.sub(rep,f)

def produce(source,alias,existing,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True);families={};count=0
    with gzip.open(existing,'rt',encoding='utf-8-sig',newline='') as src,gzip.open(out/(alias+'_Formula_Mathematics.csv.gz'),'wt',encoding='utf-8-sig',newline='') as dst:
        reader=csv.DictReader(src);writer=csv.DictWriter(dst,fieldnames=reader.fieldnames+['mathematical_cell_equation_latex']);writer.writeheader()
        for row in reader:
            f=row['source_formula'].lstrip('=');sh=row['worksheet'];a=row['cell']
            expression=celltex(sh,a)+' = '+mathematical(f,sh)
            writer.writerow(dict(row,mathematical_cell_equation_latex=expression));count+=1
            key=(sh,relative_family(f,sh,a))
            if key not in families:families[key]={'worksheet':sh,'first_cell':a,'last_cell':a,'count':0,'first_formula':'='+f,'first_math':expression}
            families[key]['last_cell']=a;families[key]['count']+=1
    with (out/(alias+'_Formula_Families.csv')).open('w',encoding='utf-8-sig',newline='') as f:
        fields=['worksheet','first_cell','last_cell','count','first_formula','first_math'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(dict(row,first_formula="'"+row['first_formula']) for row in families.values())
    return {'source_alias':alias,'formula_equations':count,'relative_formula_families':len(families),'meaning':'Literal cell mathematics; environmental symbol assignments remain separate.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source');p.add_argument('--alias',required=True);p.add_argument('--replay-ledger',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    print(json.dumps(produce(a.source,a.alias,a.replay_ledger,a.output),indent=2))
