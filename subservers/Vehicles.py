
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Vehicles_mcp = FastMCP(name="Vehicles")



def GetVehicles(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get all of the vehicles associated with a given facility."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/vehicles/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
