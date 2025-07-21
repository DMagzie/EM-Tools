# 📦 Module Status (as of July 2025)

| Module                    | Track              | Purpose                                 | Status       | Notes                                      |
|---------------------------|--------------------|------------------------------------------|--------------|---------------------------------------------|
| baseline_generator.py     | EM Core Tools      | Generate ASHRAE/Title 24 compliant baselines | ✅ MVP Ready | Will be enhanced with multifamily logic     |
| scenario_manager.py       | EM Core Tools      | Define/edit baseline and design scenarios | ✅ MVP Ready | GUI integration in progress                 |
| manual_j_module.py        | EM Core Tools      | Placeholder for load calcs (Manual J)     | ⚠️ Stub       | Post-MVP development                        |
| export_to_iesve.py        | EnergyPlus Track   | Export to IESVE MIT + Apache files        | ⚠️ In Progress | Needs model mapping validation              |
| export_to_cbecc_ief.py    | EnergyPlus Track   | Export to CBECC ab.xml or .cbid           | ⚠️ In Progress | Includes baseline toggle logic              |
| em_model.py               | EnergyPlus Track   | Schema for normalized EM JSON             | ✅ MVP Ready | Used for validation and translation         |
| streamlit_app.py          | Explorer Track     | MVP GUI for scenario viewing              | ⚠️ Stub       | GUI tabs in place, logic partial            |
| explorer_dashboard_stub.py| Explorer Track     | Future scenario dashboard (Plotly)        | ⚠️ Stub       | Planned for post-MVP                        |
| lcca_main_v0_05.py        | LCCA Track         | Core cost engine                          | ✅ MVP Ready | Integrates with costdb and Excel writer     |
| write_to_excel.py         | LCCA Track         | Populate .xlsm with scenario outputs      | ✅ MVP Ready | Needs QA review                             |
| CostDB_v0.05.xlsx         | LCCA Track         | Reference construction cost database      | ✅ MVP Ready | Based on public sources                     |
