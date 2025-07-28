from typing import Optional

from pydantic import BaseModel, Field


class Zone(BaseModel):
    zone_id: str
    area_ft2: float
    system_type: str | None = None

class Envelope(BaseModel):
    walls: list[dict]
    roof: list[dict]
    floors: list[dict]

class DHWSystem(BaseModel):
    system_type: str
    fuel_type: str
    efficiency: float

class Building(BaseModel):
    name: str
    climate_zone: str
    area_ft2: float
    stories: int
    building_type: str

class BuildingModel(BaseModel):
    project_id: str
    building: Building
    zones: list[Zone]
    envelope: Envelope
    dhw_systems: list[DHWSystem]
    schema_version: str = Field(default="1.0")
