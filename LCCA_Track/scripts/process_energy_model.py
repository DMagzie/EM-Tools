import xml.etree.ElementTree as ET

def extract_annual_energy_from_cbecc_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    annual_kwh = {}
    for zone in root.findall(".//Zone"):
        name = zone.get("Name")
        elec = zone.findtext("ElectricityUse")
        if elec:
            annual_kwh[name] = float(elec)
    return annual_kwh
