
# EM Tools – Full Master Roadmap (as of July 26, 2025)

This file outlines all modules, tracks, development milestones, responsibilities, and post-MVP plans across the EM Tools suite.

---

## 🧩 Tracks Overview

| Track Name         | Focus Area                                     | Owner/Lead               |
|--------------------|------------------------------------------------|---------------------------|
| EM Core Tools      | Baseline logic, scenario management, QA        | ChatGPT                   |
| EnergyPlus         | IDF, OSM, E+ sim, OpenStudio batch             | ChatGPT                   |
| Explorer           | GUI, Streamlit interface, dashboards           | ChatGPT                   |
| LCCA               | Financial metrics, ECON-1, LCA integration     | ChatGPT                   |
| Modeling Guides    | User training and modeling protocol docs       | ChatGPT + User            |
| Reference Datasets | Validation and compliance model QA             | ChatGPT                   |
| Optimization Tools | Post-MVP decision support tools (DecarbSNO)    | ChatGPT                   |

---

## ✅ MVP Deliverables (Phase 1)

### EM Core Tools Track

- [x] `baseline_generator.py`
- [x] `scenario_manager.py`
- [x] `manual_j_module.py`
- [x] `em_model.py` (shared schema)
- [x] `shoebox_generator.py`
- [x] Prescriptive standards database (ASHRAE + T24 + ZIP-based)

### EnergyPlus Track

- [x] `export_to_idf.py`
- [x] `export_to_iesve.py`
- [x] `export_to_cbecc_ief.py`
- [x] `export_to_osm.py`
- [x] `batch_run_openstudio.py`

### Explorer Track

- [x] `streamlit_app.py` (MVP GUI)
- [x] Scenario toggling
- [x] Simulation registry integration
- [x] Export button logic

### LCCA Track

- [x] `generate_econ1.py`
- [x] `cuac_module.py`
- [x] Cost database (RSMeans/MHSRA baseline)
- [x] `lcca_main_v0_05.py`
- [x] `write_to_excel.py`

---

## 🔄 In Progress (Phase 2 Automation)

- [x] IESVE HVAC + envelope parsing from `.asp`
- [x] CBECC `.cbid22` + `ap.xml` plugin-aware logic
- [x] Unified simulation result QA framework
- [x] Cost database high-granularity mode (Option B toggle)
- [x] GUI registry simulation handler (multi-engine)

---

## 📈 Post-MVP Roadmap Highlights

- **Optimization Tools**
  - [ ] DecarbSNO (Savings Nexus Optimizer)
  - [ ] Scenario comparison engine

- **LCCA Extensions**
  - [ ] EC3/OneClick import/export
  - [ ] Whole Life Carbon logic (LEED v5 / BREEAM v7)
  - [ ] ESG report module
  - [ ] Financial metrics mapping (C-PACE, LEED, NYSERDA)

- **Explorer Dashboard**
  - [ ] Scenario Dashboard with Plotly
  - [ ] Import OneClick/EC3 results
  - [ ] Electric readiness QA interface

- **Modeling Guides Track**
  - [ ] CBECC, IESVE, E+ guides
  - [ ] DHW Zoning and ventilation updates (T24 2025)
  - [ ] LEED modeling protocols
  - [ ] ApacheHVAC DHW plant setup for MF

---

## 📦 Validation Dataset Integration

Datasets being added under `EM-Assets/`:

| Dataset Source                  | Status     | Linked Module(s)                     |
|--------------------------------|------------|--------------------------------------|
| CBECC Public Sample Models     | ✅ Done     | `export_to_cbecc_ief.py`, QA         |
| IESVE Reference Models         | ✅ Done     | `export_to_iesve.py`, QA             |
| ASHRAE 90.1 Appendix G         | 🔄 Manual   | `export_to_idf.py`, baseline logic   |
| MAEDBS Appliance Database      | 🔄 Ingest   | DHW + electric readiness logic       |
| CLF WBLCA Dataset v2           | 🔄 Planned  | LCCA Track + Scenario Comparison     |
| OpenStudio Plugin Exports      | 🔄 Ingest   | `export_to_osm.py`                   |

Validation scripts automated by category:
- Geometry QA
- Energy results QA (EUI, unmet load)
- HVAC object check
- Carbon + cost scenario alignment

---

## 📅 Timing Matrix

| Task                         | Responsible | Target Date  |
|------------------------------|-------------|--------------|
| All MVP Scripts              | ChatGPT     | ✅ July 22    |
| GUI Integration (Streamlit)  | ChatGPT     | ✅ July 23    |
| Dataset Packaging            | ChatGPT     | ⏳ July 27    |
| Scenario Dashboard           | ChatGPT     | Aug 2025     |
| DecarbSNO + Optimizer Tools  | ChatGPT     | Aug–Sept     |
| Modeling Guides Full Release | ChatGPT     | Sept 2025    |

---

## 🔒 Final Notes

- All post-MVP features proceeding under automation unless user flags otherwise.
- User is managing all downloads, file storage, and repo syncing manually.
- GitHub support can be enabled after user finalizes repo structure.
