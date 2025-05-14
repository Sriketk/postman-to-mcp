from fastmcp import FastMCP
import requests
from typing import Dict, Optional

facilities_mcp = FastMCP(name="Facilities")

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

@facilities_mcp.tool()
def getfacility(facility_id: str, token: str) -> Dict:
    """Get a single facility by facility_id."""
    response = requests.get(
        f"https://api.flourishsoftware.com/external/api/v1/facilities/{facility_id}",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" }
    )
    response.raise_for_status()
    return response.json()

@facilities_mcp.tool()
def getfacilities(token: str, limit: Optional[int] = 50, offset: Optional[int] = 0, facility_type: FacilityType = "Dispensary", active: Optional[bool] = True) -> Dict:
    """Get facilities based on query parameters."""
    response = requests.get(
        f"https://api.flourishsoftware.com/external/api/v1/facilities",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" }
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            "facility_type": facility_type,
            "active": active
        }.items() if v is not None},
        params=params
    )
    response.raise_for_status()
    return response.json()


