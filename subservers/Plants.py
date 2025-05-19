
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Plants_mcp = FastMCP(name="Plants")



def GetPlants(limit: int = "50", offset: int = "0", strain_id: str = "945c2062", group_id: str = "20171212-000", group_name: str = "G-171201", group_status_id: int = "50", harvest_id: str = "FR001-20180209-001", harvest_name: str = "H-1712011", harvest_status_id: int = "20", status: Literal["Cloned or Planted", "Vegetative", "Mother", "Flowering", "Harvested", "Drying", "In Processing", "Consumed To Batch", "Dead", "Packaged"] = "Cloned or Planted", status_id: int = "10", current_area_id: str = "DR000", plant_timestamp_start: str = "2020-01-03T15:04:05.000Z", plant_timestamp_end: str = "2020-01-03T15:04:05.000Z", vegetative_timestamp_start: str = "2020-01-03T15:04:05.000Z", vegetative_timestamp_end: str = "2020-01-03T15:04:05.000Z", mother_timestamp_start: str = "2020-01-03T15:04:05.000Z", mother_timestamp_end: str = "2020-01-03T15:04:05.000Z", flower_timestamp_start: str = "2020-01-03T15:04:05.000Z", flower_timestamp_end: str = "2020-01-03T15:04:05.000Z", dry_timestamp_start: str = "2020-01-03T15:04:05.000Z", dry_timestamp_end: str = "2020-01-03T15:04:05.000Z", processing_timestamp_start: str = "2020-01-03T15:04:05.000Z", processing_timestamp_end: str = "2020-01-03T15:04:05.000Z", packaged_timestamp_start: str = "2020-01-03T15:04:05.000Z", packaged_timestamp_end: str = "2020-01-03T15:04:05.000Z", expected_flower_timestamp_start: str = "2020-01-03T15:04:05.000Z", expected_flower_timestamp_end: str = "2020-01-03T15:04:05.000Z", expected_harvest_timestamp_start: str = "2020-01-03T15:04:05.000Z", expected_harvest_timestamp_end: str = "2020-01-03T15:04:05.000Z", harvest_timestamp_start: str = "2020-01-03T15:04:05.000Z", harvest_timestamp_end: str = "2020-01-03T15:04:05.000Z", destroyed_timestamp_start: str = "2020-01-03T15:04:05.000Z", destroyed_timestamp_end: str = "2020-01-03T15:04:05.000Z", created_timestamp_start: str = "2020-01-03T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2010-01-03T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get plants for a single facility based on query parameters. This request requires the `FacilityID` header."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/plants/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", strain_id: str = "945c2062", group_id: str = "20171212-000", group_name: str = "G-171201", group_status_id: int = "50", harvest_id: str = "FR001-20180209-001", harvest_name: str = "H-1712011", harvest_status_id: int = "20", status: Literal["Cloned or Planted", "Vegetative", "Mother", "Flowering", "Harvested", "Drying", "In Processing", "Consumed To Batch", "Dead", "Packaged"] = "Cloned or Planted", status_id: int = "10", current_area_id: str = "DR000", plant_timestamp_start: str = "2020-01-03T15:04:05.000Z", plant_timestamp_end: str = "2020-01-03T15:04:05.000Z", vegetative_timestamp_start: str = "2020-01-03T15:04:05.000Z", vegetative_timestamp_end: str = "2020-01-03T15:04:05.000Z", mother_timestamp_start: str = "2020-01-03T15:04:05.000Z", mother_timestamp_end: str = "2020-01-03T15:04:05.000Z", flower_timestamp_start: str = "2020-01-03T15:04:05.000Z", flower_timestamp_end: str = "2020-01-03T15:04:05.000Z", dry_timestamp_start: str = "2020-01-03T15:04:05.000Z", dry_timestamp_end: str = "2020-01-03T15:04:05.000Z", processing_timestamp_start: str = "2020-01-03T15:04:05.000Z", processing_timestamp_end: str = "2020-01-03T15:04:05.000Z", packaged_timestamp_start: str = "2020-01-03T15:04:05.000Z", packaged_timestamp_end: str = "2020-01-03T15:04:05.000Z", expected_flower_timestamp_start: str = "2020-01-03T15:04:05.000Z", expected_flower_timestamp_end: str = "2020-01-03T15:04:05.000Z", expected_harvest_timestamp_start: str = "2020-01-03T15:04:05.000Z", expected_harvest_timestamp_end: str = "2020-01-03T15:04:05.000Z", harvest_timestamp_start: str = "2020-01-03T15:04:05.000Z", harvest_timestamp_end: str = "2020-01-03T15:04:05.000Z", destroyed_timestamp_start: str = "2020-01-03T15:04:05.000Z", destroyed_timestamp_end: str = "2020-01-03T15:04:05.000Z", created_timestamp_start: str = "2020-01-03T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2010-01-03T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetPlant(plant_id) -> Dict:
    """Get plant by id, for a single facility. This request requires the `FacilityID` header."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/plants/{{plant_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
