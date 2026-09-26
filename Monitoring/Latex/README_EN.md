# NEBIOT Monitoring Report — completion guide

**Monitoring template edition 1.3 · NEBIOT Standard 0.8.2**

## Purpose and document relationship

The Monitoring Report (MR) is the main period-specific monitoring submission. It explains what was implemented, what was observed, how the approved monitoring plan was applied, what changed, and how the evidence supports the environmental account. It accompanies the Project Description (PD), the dated Ex-Ante Estimate (EA), and the Ex-Post Outcome Report (EP).

Use the PD as the design reference and retain the dated ex-ante forecast. Attach the controlled Ex-Post report as the quantitative annex, or embed the equivalent controlled report and identify its location. The MR summarizes the same account: its values are not added to those of the Ex-Post report. The MR supports G2. Independent verification at G3 and the program decision at G4 remain separate.

The governing standard remains version 0.8.2. The existing PD, Ex-Ante, Ex-Post, Migration Reconciliation and Environmental Accounts files remain edition 1.2. This edition adds the Monitoring Report; it does not modify those documents, workbook formulas or the standard.

## Files and working master

- `Word/NEBIOT_Monitoring_Report_EN_Template_v1_3.docx` is directly editable.
- `Word_Templates/NEBIOT_Monitoring_Report_EN_Template_v1_3.dotx` is a reusable Word template master.
- `Overleaf/NEBIOT_Monitoring_Report_EN.tex` is the English LaTeX entry point; the Spanish entry point ends in `_ES.tex`.
- The PDFs are reading previews, not interactive forms. The initial blank document has no maximum submission length.

Choose Word or LaTeX as the controlled report master. There is no automatic synchronization between Word, LaTeX and Excel. Preserve the file version, fingerprint, worksheet, cell and report-table links when transferring results.

## Completing the report

Start with the cover and document-control page: project identity, report number and version, monitoring interval, interval convention, evidence cut-off, submission date, preparer, reviewer, and distribution. Distinguish these dates from the project lifetime and from the period covered by an attached calculation.

Section 02 establishes the exact PD, EA, EP, profile and previous-decision references. Sections 03–10 record responsibility, implementation, monitoring coverage, spatial and material evidence, data quality, substitutions and changes. Sections 11–19 reconcile the counterfactual, project emissions, leakage, cohorts, signed net account, uncertainty, risk, liabilities and forecast comparison. Sections 20–26 address continuing additionality, overlapping initiatives, participation, safeguards, separate environmental and social results, migration, NVEU scope, findings, and evidence handover.

Expand each table to cover every applicable item. Use explicit missing-data or unresolved status, not a fabricated zero. A non-applicability decision needs its reason and reviewer disposition. Complete every applicable row of the approved FRM-05 profile, or reference the exact unchanged record. Do not import a percentage, confidence level, horizon, threshold or denomination from a worked example.

## Mathematical notation and calculation records

Calculation-related tables reproduce the notation from the edition 1.2 mathematical catalog and identify its governing clauses and workbook location. Table identifiers such as `MR-15-T01` locate report records; they are not new standard requirements.

In each calculation, preserve the distinction among raw observations, model conversions, assumed inputs, ex-ante projections, ex-post reported quantities, independently verified scope and authorized NVEUs. Retain the units, included pools, gas characterization, spatial support and time interval. State each subtotal's meaning; do not import a subtotal already net of project emissions as a gross baseline and deduct those emissions again.

The CALC appendix provides a repeatable traceability record. Link each reported number to its original data, exact source expression, inputs, units, transformations, receiving equation, unrounded result, workbook cell, report row and reviewer comparison. Numerical tolerances are software-comparison settings, not materiality thresholds. Differences caused by justified method or scope changes must be explained rather than forced to zero.

Worksheet references use the unchanged Environmental Accounts edition 1.2 layout. In particular, `ExPost!F:I` contains the baseline, project, leakage and signed net account; `ExPost!J:L` records the uncertainty interface; `Comparison!D:J` holds the forecast comparison; `Settlement`, `CarryForward` and `Results` retain the candidate-versus-executed and conditional-denomination distinctions. Enter the exact populated row and file version. Respect that workbook's range capacities or use a separately controlled, tested extension; the report does not extend its formulas.

Negative results and continuing liabilities remain visible. Apply the full-bound carry-forward only when expressly adopted. Actual settlement and reserve cancellation require execution evidence. Do not change a posted liability through a candidate allocation. Do not treat an uncertainty-driven negative bound automatically as a physical reversal.

## PD-to-monitoring crosswalk

The XREF appendix maps every substantive MR section to the actual section identifiers in the PD, EA and EP templates, edition 1.2. Project documents may have different pagination or section labels after completion: record their exact locations in Section 02. A reference to the PD does not replace observations and implementation records for the monitoring interval.

The registers repeat this mapping in CSV form and identify the calculation notation and workbook location of each relevant table. Existing requirement, equation, AP and FRM identifiers refer to the governing standard, not to missing sections of the MR.

## Editing Word

Click the bracketed fields to enter information. The blank fields are native Word text content controls; the mathematical expressions are editable Office Math, not images. Tables are not locked. Add rows as needed and repeat the relevant headers. Long responses can flow onto later pages. Refresh fields and inspect page numbering, tables, mathematics and headers after editing.

The linked contents and XREF entries navigate to report sections. Keep their bookmarks when modifying section titles. Use a new report version for changes that affect an assessment record, and retain the superseded version.

## Editing in Overleaf

Upload the Overleaf-only ZIP, choose XeLaTeX, and select `NEBIOT_Monitoring_Report_EN.tex` or `NEBIOT_Monitoring_Report_ES.tex`. Cover fields are in the selected root file. The editable report body is in `content/`; the shared layout is in `style/nebiot-monitoring.sty`.

Set `\MonitoringStart`, `\MonitoringEnd`, and `\MonitoringReportID` along with the project identity. Record the interval convention on the document-control page. Replace the reserved map with a properly referenced project map. Retain the bibliography and normative references when completing the template.

## Logos and identity

The original NEBIOT image and license appear in each language edition. Preserve the NEBIOT image's aspect ratio. Three optional cover spaces identify the implementing entity, proponent and rights holders or stakeholders.

In Word, insert an authorized inline image in the corresponding cover-table cell and retain the organization's role. In LaTeX, upload the image to `assets/` and set `\ImplementerLogo`, `\ProponentLogo` or `\StakeholderLogo` to the exact path. Leave the path empty to retain the reserved space. Remove unused partner spaces from the completed submission. A logo does not establish ownership, consent, endorsement, validation or admission.

## Submission, assessment and confidentiality

The proponent submits the report with the technical preparer's record and the applicable internal review. The independent OVV controls its own assessment and opinion. The report references a separately issued opinion or program decision when available; the preparer must not prefill those conclusions or sign on another function's behalf.

Public reporting may summarize protected personal, cultural or location information. Preserve a controlled evidence index with authorized reviewer access to the full record. Include evidence references, not confidential material belonging to an unrelated project. Reconcile the report summary, quantitative annex, raw-data files, prior claims and opening/closing balances before submission.
