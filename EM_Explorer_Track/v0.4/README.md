# EM Explorer Track – v0.3

**Formerly:** CBECC-to-IESVE Converter

## 🎯 Purpose
Convert CBECC simulation data into IESVE-ready formats and serve as a cross-platform EM simulation and QA/QC viewer.

## 🧩 Key Modules
- `geometry_mapper.py`: Maps geometry from CBECC outputs to IESVE-compatible structure.
- `system_mapping.py`: Applies ruleset to convert systems and assemblies.
- `eui_ghg_viewer.py`: Displays energy use and emissions by end use and space type.
- `qaqc_heatmap.py`: QA/QC visualization tool for outliers in model data.
- `hvac_explorer.py`: Interactive explorer for HVAC systems and components.
- `manual_j_viewer.py`: Views and compares Manual J-calculated loads.

## 📦 Status
- QA/QC module in active development.
- IDF export planned for EnergyPlus integration.
- Manual J integration partially complete.
