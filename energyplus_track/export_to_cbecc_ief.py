
import os
import xml.etree.ElementTree as ElementTree
from pathlib import Path

from shared.em_model import BuildingModel


def export_to_cbecc(model: BuildingModel, output_dir: Path = Path("exports")) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{model.project_id}_export.xml"

    root = ElementTree.Element("CBECCProject")
    building = ElementTree.SubElement(root, "Building", {
        "name": model.building.name,
        "climate_zone": model.building.climate_zone,
        "area_m2": str(model.building.area_m2),
        "stories": str(model.building.stories),
        "type": model.building.type
    })

    # Zones
    for zone in model.zones:
        ElementTree.SubElement(building, "Zone", {
            "id": zone.zone_id,
            "area_m2": str(zone.area_m2),
            "system_type": zone.system_type or "undefined"
        })

    # Envelope
    if model.envelope:
        for wall in model.envelope.walls:
            ElementTree.SubElement(building, "Wall", {
                "id": wall.id,
                "construction": wall.construction or "unspecified",
                "area_m2": str(wall.area_m2),
                "orientation": wall.orientation or "undefined"
            })
        for roof in model.envelope.roofs:
            ElementTree.SubElement(building, "Roof", {
                "id": roof.id,
                "construction": roof.construction or "unspecified",
                "area_m2": str(roof.area_m2)
            })
        for floor in model.envelope.floors:
            ElementTree.SubElement(building, "Floor", {
                "id": floor.id,
                "construction": floor.construction or "unspecified",
                "area_m2": str(floor.area_m2)
            })
        for window in model.envelope.windows:
            ElementTree.SubElement(building, "Window", {
                "id": window.id,
                "glazing_type": window.glazing_type or "unspecified",
                "area_m2": str(window.area_m2),
                "orientation": window.orientation or "undefined"
            })

    # DHW Systems
    for dhw in model.dhw_systems:
        ElementTree.SubElement(building, "DHWSystem", {
            "id": dhw.system_id,
            "type": dhw.type,
            "zones": ",".join(dhw.served_zones),
            "efficiency": str(dhw.efficiency or 1.0)
        })

    tree = ElementTree.ElementTree(root)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

    return output_path
