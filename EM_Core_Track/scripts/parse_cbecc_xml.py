import xml.etree.ElementTree as ET

def parse_xml_summary(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    results = []
    for zone in root.findall(".//Zone"):
        zone_name = zone.get("Name")
        elec = float(zone.findtext("ElectricityUse", default="0"))
        results.append({"Zone": zone_name, "ElectricityUse": elec})
    return results
