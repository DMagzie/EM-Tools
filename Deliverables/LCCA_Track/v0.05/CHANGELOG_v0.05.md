# CHANGELOG – LCCA Track v0.05 (Planned)

## 🆕 Objectives

- Add core financial metrics to Excel (NPV, IRR, ROI, SPP)
- Enable dynamic scenario configuration and override logic
- Automate generation of structured summary exports
- Begin CLI- or script-based automation of full runs

## 📦 Planned Feature Areas

### 🔢 Financial Calculations
- [ ] Implement NPV using discounted cash flows across project life
- [ ] Add IRR and ROI formulas to dashboard
- [ ] Include simple payback (SPP) and savings-to-investment ratio (SIR)
- [ ] Validate Python-calculated results vs Excel equivalents

### 🔄 Scenario Configuration
- [ ] Add `scenario_config.json` to define base and proposed case logic
- [ ] Enable override of PV/battery toggles from config
- [ ] Wire scenario tags to inputs and outputs

### 🧠 Dispatch + Override Enhancements
- [ ] Add logic-driven control table to Excel (e.g., hourly ruleset)
- [ ] Support CSV import of dispatch override curves
- [ ] Enable PV switch and TOU strategy toggle fields

### 🧪 Automation + Output Bundling
- [ ] Add command-line interface (`run_lcca.py --config scenario_config.json`)
- [ ] Export output bundle: `summary.xlsx`, `inputs_used.csv`, `results.json`
- [ ] Optionally generate PDF summary using template

## 📁 Files and Modules Affected

| File / Tool                 | Change Summary                          |
|----------------------------|------------------------------------------|
| `LCCA_Tool_v0.05.xlsm`     | Add new dashboard rows and override tabs |
| `write_to_excel.py`        | Add support for financial field injection |
| `scenario_config.json`     | New — scenario config + dispatch rules    |
| `generate_financials.py`   | New — calculate NPV, IRR, ROI from cashflows |
| `Docs/README.md`           | Updated to describe scenario config usage |

## ⏳ Tasks

- [ ] Scaffold `v0.05/` folder with Excel + script templates
- [ ] Create base config file structure
- [ ] Begin financial logic calculator
- [ ] Validate scenario toggles and override rule import
- [ ] Push interim test case bundle

## 📅 Target Version: v0.05
