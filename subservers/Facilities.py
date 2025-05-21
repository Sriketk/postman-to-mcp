
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Facilities_mcp = FastMCP(name="Facilities")



def GetFacility(token: str, facility_id) -> Dict:
    """Get a single facility by `facility_id`."""
    params = {'token': token, 'facility_id': facility_id}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/facilities/{{facility_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetFacilities(token: str, limit: int = "50", offset: int = "0", facility_type: Literal["Laboratory", "Processor", "Grower", "Dispensary", "Distributor", "Manufacturer", "Other", "Microbusiness"] = "Dispensary", active: Optional[bool] = "True") -> Dict:
    """Get facilities based on query parameters."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'facility_type': facility_type, 'active': active}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/facilities/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
