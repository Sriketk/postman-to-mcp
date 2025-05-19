
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Facilities_mcp = FastMCP(name="Facilities")



def GetFacility(facility_id) -> Dict:
    """Get a single facility by `facility_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/facilities/{{facility_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetFacilities(limit: int = "50", offset: int = "0", facility_type: Literal["Laboratory", "Processor", "Grower", "Dispensary", "Distributor", "Manufacturer", "Other", "Microbusiness"] = "Dispensary", active: Optional[bool] = "True") -> Dict:
    """Get facilities based on query parameters."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/facilities/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", facility_type: Literal["Laboratory", "Processor", "Grower", "Dispensary", "Distributor", "Manufacturer", "Other", "Microbusiness"] = "Dispensary", active: Optional[bool] = "True"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
