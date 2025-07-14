import requests

def get_hourly_pv(production_kw, lat, lon, api_key):
    url = "https://developer.nrel.gov/api/pvwatts/v6.json"
    params = {
        "api_key": api_key,
        "lat": lat,
        "lon": lon,
        "system_capacity": production_kw,
        "azimuth": 180,
        "tilt": 20,
        "array_type": 1,
        "module_type": 0,
        "losses": 14,
        "timeframe": "hourly"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["outputs"]["ac"]
