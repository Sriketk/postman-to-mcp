
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Drivers_mcp = FastMCP(name="Drivers")



def GetDrivers(limit: int = "50", offset: int = "0") -> Dict:
    """Get all of the drivers associated with a given facility."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/drivers/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
