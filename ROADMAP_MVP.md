# 🚀 EM Tools MVP Roadmap

## 🎯 MVP Purpose
Establish end-to-end modeling flow: translation → baseline → scenario → export → financial + visual outputs.

---

## ✅ Included in MVP
- **EM Core Tools**
  - `baseline_generator.py` – baseline generation logic
  - `scenario_manager.py` – scenario creation and locking
- **EnergyPlus Track**
  - `export_to_iesve.py` – IESVE exporter stub
  - `export_to_cbecc_ief.py` – partial CBECC exporter
  - `em_model.py` – shared schema
- **Explorer Track**
  - `streamlit_app.py` – GUI with scenario toggle
- **LCCA Track**
  - `lcca_main_v0_05.py` – scenario cost evaluator
  - `write_to_excel.py` – Excel writer
  - `CostDB_v0.05.xlsx` – cost reference data

---

## 🔜 Post-MVP Targets
- `export_to_osm.py`, `batch_run_openstudio.py`
- GUI HVAC + schedule editor
- EC3 + OneClick LCA integration
- Radiance, SAM, QA report tools
- Full GUI scenario dashboard

---

## 📅 Timeline
- July 20–22: MVP testing and packaging
- July 23–25: Validation + QA logic
- July 28+: Begin Post-MVP Modules

