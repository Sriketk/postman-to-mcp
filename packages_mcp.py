from fastmcp import FastMCP
import requests
from typing import Dict, Optional

facilities_mcp = FastMCP(name="Facilities")

@packages_mcp.tool()
def getpackagedetails(token: str) -> Dict:
    """Get the origin info of a cannabis package by its ID."""
    response = requests.get(
        f"https://api.flourishsoftware.com/external/api/v1/packages/:package_id/details",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" }
    )
    response.raise_for_status()
    return response.json()

@packages_mcp.tool()
def getpackages(token: str, limit: Optional[int] = 50, offset: Optional[int] = 0, package_id: Optional[str] = "1A40X0900002906000099999", package_status: Optional[str] = "Shipped", include_origin_harvest: Optional[bool] = False, last_updated_timestamp_start: Optional[str] = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: Optional[str] = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get current cannabis packages for a single facility. `package_id` is the unique identifier for the package record returned."""
            response = requests.get(
        f"https://api.flourishsoftware.com/external/api/v1/packages",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" }
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            "package_id": package_id,
            "package_status": package_status,
            "include_origin_harvest": include_origin_harvest,
            "last_updated_timestamp_start": last_updated_timestamp_start,
            "last_updated_timestamp_end": last_updated_timestamp_end
        }.items() if v is not None}

        ,
        params=params
    )
    response.raise_for_status()
    return response.json()

@packages_mcp.tool()
def getpackage(token: str, include_origin_harvest: Optional[bool] = False) -> Dict:
    """Get a cannabis package by it's ID in Flourish."""
            response = requests.get(
        f"https://api.flourishsoftware.com/external/api/v1/packages/{package_id}",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" }
        params = {k: v for k, v in {
            "include_origin_harvest": include_origin_harvest
        }.items() if v is not None}

        ,
        params=params
    )
    response.raise_for_status()
    return response.json()

from typing import Literal

FacilityType = Literal[
    "Laboratory",
    "Processor",
    "Grower",
    "Dispensary",
    "Distributor",
    "Manufacturer",
    "Other",
    "Microbusiness"
]