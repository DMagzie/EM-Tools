def export_results_to_plotly_format(scenario_data):
    return {
        "scenario_id": scenario_data.get("id", "default"),
        "metrics": scenario_data.get("metrics", {})
    }
