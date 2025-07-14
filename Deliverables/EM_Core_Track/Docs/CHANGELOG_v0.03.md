# CHANGELOG – LCCA Track v0.03

**Release Date:** July 7, 2025  
**Track:** LCCA (Life Cycle Cost Analysis)  
**Repo:** https://github.com/DMagzie/EM-Tools

---

## ✅ Summary of v0.03 Deliverables

This version finalizes the foundational components of the LCCA Track, including preprocessing scripts, structured inputs/outputs, validation tools, and interim Excel design files.

### 🚀 Completed

- Created folder structure: `v0.03/` under `LCCA_Track/`
- Added Python scripts:
  - `lcca_main_v0_03.py`
  - `data_parser.py`
  - `battery_dispatch.py`
- Added placeholder scripts for v0.04 development:
  - `generate_pvwatts_hourly.py`
  - `format_lcca_inputs.py`
- Included input samples and PVWatts outputs in `/Inputs/`
- Exported sample summary output to `/Outputs/`
- Added reference data (cost database, utility rates)
- Rebuilt missing `.docx` documentation and validated `.xlsx` files
- Deployed file validator script with logging to `validation_log.txt`
- Installed Git pre-commit hook for automatic file validation
- Added interim Excel bundle:
  - `LCCA_Tool_v0.03_stub.xlsm`
  - `Battery_Logic_Template.xlsx`
  - `Dashboard_Mockup_v0.03.pdf`

---

## ⏭ Deferred to v0.04

- Final Excel dashboard integration and macros
- Dynamic battery override interface
- Scenario comparison logic with savings metrics
- Real-time PVWatts and TDV-linked UI toggles

---

## 📁 Folder Structure (Key)

- `Scripts/`: Python logic for input processing and dispatch
- `Inputs/`: Model inputs, PVWatts, hourly CSVs
- `Outputs/`: Final Excel summaries
- `Reference/`: Cost and utility datasets
- `Docs/`: Overview doc, changelog, interim deliverables

---

## 🧪 Validation

- All `.docx`, `.xlsx`, and `.csv` files scanned with `validate_office_files.py`
- Git pre-commit hook blocks corrupted Office file commits
- Logged validations to `validation_log.txt`

---

## 🔗 Repository

[📂 View on GitHub » DMagzie/EM-Tools](https://github.com/DMagzie/EM-Tools)
