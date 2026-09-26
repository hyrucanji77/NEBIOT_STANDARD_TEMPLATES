# NEBIOT project and outcome templates — edition 1.2

Governing standard: NEBIOT Standard 0.8.2. The standard is not amended by this template edition.

## Contents
Four project stages (NIP, Prefeasibility, Feasibility, PD) and three accounting products (ExAnte, ExPost, Migration_Reconciliation), each in American English and Spanish. Each has DOCX, DOTX, complete Overleaf source and a compiled PDF preview. Two calculation workbooks provide matching English and Spanish instructions with identical formulas. Use one language and one controlled editing format; do not complete parallel copies unnecessarily.

## Which product belongs where?
- **NIP:** identify available estimates and evidence gaps; no complete future monitoring account is required for concept screening.
- **Prefeasibility:** attach a supported indicative ExAnte account and study plan. Unquantified gaps stay explicit.
- **Feasibility and PD:** attach the controlled ExAnte report, calculation workbook, evidence and applicable profile. Preserve the estimate and its original assumptions as a dated snapshot.
- **Monitoring submission:** complete ExPost for the actual reporting period, with a retained counterfactual, measured or qualified evidence, the signed result, uncertainty, obligations and separate assessment records. An ex-post calculation is not automatically a verified result.
- **Migration:** use Migration_Reconciliation alongside ExAnte and/or ExPost as appropriate. Retain the original calculation, record any harmonization, and show the effect of the NEBIOT method separately. Preserve other external carbon units and their original status in the migration records; do not rename them NVEUs.

The new appendix A in every project-stage template identifies its related account products. These are template identifiers, not new mandatory requirements or new stages of the standard. All clause and equation references point to NEBIOT Standard 0.8.2.

## Word
Open a DOCX to edit a project copy, or open a DOTX to create a fresh document. Enter text in the bracketed content controls. Tables and narrative areas expand; their initial number of rows and pages is not a submission limit. Add evidence tables and annexes where needed. Replace the three cover logo fields with authorized images for the implementer, proponent and stakeholders, maintaining aspect ratio and accurate role labels. Do not alter the NEBIOT logo. Update Word fields before final PDF export and inspect the completed pages.

## Overleaf
Upload the Overleaf folder as its own ZIP/project, select XeLaTeX, and select one of these roots:

NEBIOT_NIP_EN.tex / NEBIOT_NIP_ES.tex
NEBIOT_Prefeasibility_EN.tex / NEBIOT_Prefeasibility_ES.tex
NEBIOT_Feasibility_EN.tex / NEBIOT_Feasibility_ES.tex
NEBIOT_PD_EN.tex / NEBIOT_PD_ES.tex
NEBIOT_ExAnte_EN.tex / NEBIOT_ExAnte_ES.tex
NEBIOT_ExPost_EN.tex / NEBIOT_ExPost_ES.tex
NEBIOT_Migration_Reconciliation_EN.tex / NEBIOT_Migration_Reconciliation_ES.tex

Cover fields and optional logo paths are in each root; full responses are in its content file. Shared formatting is in style/nebiot-template.sty. The three optional commands are ImplementerLogo, ProponentLogo and StakeholderLogo. Upload the image into assets and set its path. Empty paths retain a labeled field. Do not overwrite the NEBIOT asset files. PDF previews are reading copies, not interactive forms.

## Calculation workbooks
Use NEBIOT_Environmental_Accounts_EN_v1_2.xlsx or its ES counterpart. They are standalone workbooks; neither links to a private source workbook or to the other language edition. Stable sheet names and input codes are shared across languages.

1. **Profile:** record project, category, applicable FRM-05 profile and evidence. d_u remains blank until a compatible carbon category is approved. FULL_BOUND operates only with a recorded F-R05 adoption; OTHER_PROFILE requires a separately documented calculation.
2. **Evidence / Spatial / Factors:** identify exact source objects, dates, pools, units and spatial support. Optional pixel-area and biomass/carbon conversions do not establish classification accuracy, carbon calibration or annual mitigation.
3. **Components:** enter disjoint signed contributions for EA or EP and period key. BL is net baseline emissions; PJ is net project emissions; LK is attributable leakage. A quantity already reduced by project emissions is not a gross baseline. For a precomputed t CO2e amount, use factor 1 and identify the full upstream routine and evidence. Include at least one evidenced row for each of BL/PJ/LK, including a justified zero where applicable. NO means deliberately excluded; document the exclusion in the report.
4. **ExAnte / ExPost:** assign matching period keys, actual scope and evidence status. Q_hat = BL − PJ − LK. DEDUCTION uses a supplied justified nonnegative amount; BOUND uses a supplied conservative value not exceeding the point estimate. Neither route computes uncertainty or replaces its independent assessment. ExAnte reserve and liability inputs are planning scenarios, not ledger postings.
5. **Settlement:** computes eligible mass and candidate settlement/reserve base under F-R03. Executed settlement is a separate input, limited to the compatible candidate allocation and requiring execution evidence when positive. A reserve requirement above the candidate base remains a shortfall; it is not silently capped or treated as funded.
6. **CarryForward:** under FULL_BOUND, computes the negative magnitude, removes only separately evidenced prior recognition and executed compatible reserve cancellation, and adds the remaining new obligation to existing unpaid liability. The previous-period link tests the opening balance. The first balance requires the identified opening ledger. No posting is authenticated or executed by this workbook.
7. **Results:** reports candidate quantities. Candidate NVEU count is suppressed when its upstream consistency checks fail or denomination/profile is missing. A calculated count is never issuance. Whole-unit precision and rounding, when required, must be implemented in the approved category-specific account and retain the residual.
8. **Comparison:** compares a frozen ex-ante record with ex-post on matched support. Its signed bridge is ΔQ = ΔBL − ΔPJ − ΔLK before uncertainty/reserve adjustments. A difference is not proof of additionality or a material error by itself.
9. **Migration:** retains original, harmonized-old-method and NEBIOT-method quantities separately. Basis adjustment plus method difference must equal total difference. The table does not create replacement units, erase prior liabilities or approve historical periods.
10. **Allocation:** distributes a parent net result using explicit weights. Parent/basis weights sum to one. Allocation is not new monthly observation, and an annual result must not be counted again as additional monthly mitigation.
11. **Checks / Examples / Formula_Map:** inspect held rows, synthetic arithmetic cases and the precise computational scope. An empty workbook is EMPTY, not approved.

Blue text identifies inputs; pale-green cells are calculations. Validation codes: EA/EP, BL/PJ/LK, YES/NO, DEDUCTION/BOUND, FULL_BOUND/OTHER_PROFILE, OBSERVED/MODELED/ASSUMED/REPORTED/OVV_ASSESSED. COMPLETE and CALCULATED concern the bounded input/arithmetic check only; they are not conformity, verification or authorization decisions.

There are 50 period rows, 300 component rows and 150 allocation rows. These capacities are not program limits or crediting horizons. Before adding records beyond them, extend every dependent formula range, validation range and check, and retest the expanded workbook. Keep an original, unedited file for every formally submitted calculation and record corrections separately. There are no macros or workbook passwords; protect the controlled copy through the actual document-management arrangements.

## What the workbooks do not calculate
They do not fit a vegetation classifier, reconstruct trees, estimate driver probabilities, select a counterfactual, estimate covariance or confidence levels, perform independent verification, authenticate signatures, fund/cancel a reserve, or authorize NVEUs. Those calculations and decisions remain in their qualified methods and evidence records. The Components interface accepts their traceable outputs. Missing evidence never becomes a zero.

## Source and evidence references
[1] NEBIOT. NEBIOT Standard, controlled version 0.8.2, integrated edition NEB-DOC-000 and its named companions. The template crosswalk preserves the exact clause, formula and record identifiers. Every completed project must add its own applicable source, dataset, license, observation, calculation and decision references. Blank templates contain no project results.


## Calculation notation
Every quantitative table has a local notation ID, native mathematical expressions, units, governing references, and account-cell mappings. The CALC appendix provides a repeatable record for substitutions, unrounded results, source coordinates, numerical differences and reviewer conclusions. Refer to the edition 1.2 completion guide and Registers/Math_Notation_Catalog.json. Word and LaTeX copies do not automatically synchronize values with Excel.
