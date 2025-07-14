# LCCA Track v0.05 – Expected Outputs & Artifacts

## ✅ 1. Excel Tool
- `LCCA_Tool_v0.05.xlsm` with:
  - Summary_Financials tab: NPV, IRR, ROI, SPP, SIR
  - Scenario_Compare tab: Baseline vs Proposed results
  - Config_Overrides tab: User-adjustable dispatch logic

## ✅ 2. Python Modules
| Script                     | Purpose                                  |
|----------------------------|------------------------------------------|
| `generate_financials.py`   | Computes NPV, IRR, ROI, SPP               |
| `write_to_excel.py`        | Injects metrics + scenario data into Excel |
| `format_lcca_inputs.py`    | Adds scenario tagging + config awareness |
| `utility_emissions.py`     | Reused from v0.04                        |

## ✅ 3. Scenario Management
- `scenario_config.json` defines:
  - Scenario type: baseline/proposed
  - Overrides: PV toggle, battery logic, region, TOU

## ✅ 4. Automation + Export
- `run_lcca.py` CLI or automation script
- Export bundle with:
  - `summary.xlsx`
  - `inputs_used.csv`
  - `results.json`

## ✅ 5. Documentation
- `README.md` for v0.05
- `CHANGELOG_v0.05.md`
- Optional test report

## ✅ 6. What You’ll Have
A testable Excel-linked LCCA tool with:
- Structured inputs and overrides
- Configurable financial evaluation
- Scenario control + reproducible results
- Output bundling for audit/reporting
