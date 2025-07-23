# simulation_engine_registry.py

from collections.abc import Callable
from typing import Optional


class SimulationEngine:
    def __init__(self, name: str,
                 export_func: Callable,
                 run_func: Callable | None,
                 parse_results_func: Callable | None):
        self.name = name
        self.export_func = export_func
        self.run_func = run_func
        self.parse_results_func = parse_results_func

# Placeholder function stubs for each engine

def export_to_osm(scenario, outdir):
    print(f"[EnergyPlus] Exporting OSM for scenario {scenario} to {outdir}")

def run_openstudio(osm_path, outdir):
    print(f"[EnergyPlus] Running OpenStudio simulation with {osm_path} to {outdir}")

def parse_eplus_results(outdir):
    print(f"[EnergyPlus] Parsing results from {outdir}")

def export_to_cbecc_xml(scenario, outdir):
    print(f"[CBECC] Exporting XML for scenario {scenario} to {outdir}")

def parse_cbecc_results_xml(result_path):
    print(f"[CBECC] Parsing results from {result_path}")

def export_to_iesve(scenario, outdir):
    print(f"[IESVE] Exporting IESVE files for scenario {scenario} to {outdir}")

def run_iesve_cli(mit_path, outdir):
    print(f"[IESVE] Running IESVE with {mit_path} to {outdir}")

def parse_iesve_results(outdir):
    print(f"[IESVE] Parsing results from {outdir}")

def export_to_cse(scenario, outdir):
    print(f"[CSE] Exporting .cse file for scenario {scenario} to {outdir}")

def run_cse_cli(cse_path, outdir):
    print(f"[CSE] Running CSE with {cse_path} to {outdir}")

def parse_cse_results(outdir):
    print(f"[CSE] Parsing results from {outdir}")

def export_to_radiance(scenario, outdir):
    print(f"[Radiance] Exporting Radiance files for scenario {scenario} to {outdir}")

def run_radiance_cli(rad_path, outdir):
    print(f"[Radiance] Running Radiance with {rad_path} to {outdir}")

def parse_radiance_results(outdir):
    print(f"[Radiance] Parsing results from {outdir}")

# Registry of engines
SIMULATION_ENGINES = {
    "EnergyPlus": SimulationEngine(
        name="EnergyPlus",
        export_func=export_to_osm,
        run_func=run_openstudio,
        parse_results_func=parse_eplus_results
    ),
    "CBECC": SimulationEngine(
        name="CBECC",
        export_func=export_to_cbecc_xml,
        run_func=None,
        parse_results_func=parse_cbecc_results_xml
    ),
    "IESVE": SimulationEngine(
        name="IESVE",
        export_func=export_to_iesve,
        run_func=run_iesve_cli,
        parse_results_func=parse_iesve_results
    ),
    "CSE": SimulationEngine(
        name="CSE",
        export_func=export_to_cse,
        run_func=run_cse_cli,
        parse_results_func=parse_cse_results
    ),
    "Radiance": SimulationEngine(
        name="Radiance",
        export_func=export_to_radiance,
        run_func=run_radiance_cli,
        parse_results_func=parse_radiance_results
    )
}
