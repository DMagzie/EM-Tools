# 📘 EM Tools Changelog

All notable changes to this project will be documented in this file.

---

## [v0.9-MVP] – 2025-07-20
🎯 **Initial MVP Testable Release**

### ✅ Core Modules Added
- `baseline_generator.py`: ASHRAE/Title 24 baseline generation logic
- `scenario_manager.py`: Scenario definition and locking system
- `manual_j_module.py`: Stub for load calculation integration

### ✅ Exporters (EnergyPlus Track)
- `export_to_iesve.py`: Draft exporter for IESVE .mit/.apc files
- `export_to_cbecc_ief.py`: Partial XML exporter for CBECC workflows
- `em_model.py`: EM JSON schema definition for model normalization

### ✅ Explorer GUI
- `streamlit_app.py`: Stub GUI with sidebar toggles
- `explorer_dashboard_stub.py`: Dashboard placeholder

### ✅ LCCA Track
- `lcca_main_v0_05.py`: Financial scenario processor
- `write_to_excel.py`: Output writer to Excel `.xlsm`
- `CostDB_v0.05.xlsx`: Initial construction cost database

### ✅ Testing + CI
- GitHub Actions workflow (`python-app.yml`)
- Unit test stubs for all major modules in `tests/`
- Codecov integration + Ruff linting

### ✅ Documentation
- `README.md`: Project overview, usage, CI instructions
- `STATUS.md`: Module-level progress tracker
- `ROADMAP_MVP.md`: MVP goals and post-MVP targets
- `Reference_Documents/`: CostDB, standards, modeling guide index
- `docs/`: Dev-facing architecture docs

---

## [Unreleased]
🔄 Planned for v0.10-beta:
- GUI HVAC & schedule editor (Explorer)
- `export_to_osm.py` and `batch_run_openstudio.py`
- QA logic and unmet hours validation
- Reference model test cases

