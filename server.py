
from fastmcp import FastMCP
import requests
from typing import Dict, Optional

mcp = FastMCP(name="InventoryAPI")


@mcp.tool()
def get_getfacility(token: str, facility_id: str) -> Dict:
    """Get a single facility by facility_id."""
    response = requests.get(
        url=f"https://api.url/v1/facilities/{{facility_id}}",
        headers={
            "Authorization": f"Basic {token}",
            "Accept": "application/json"
        },
        
        
    )
    response.raise_for_status()
    return response.json()

@mcp.tool()
def get_getfacilities(token: str) -> Dict:
    """Get facilities based on query parameters."""
    response = requests.get(
        url=f"https://api.url/v1/facilities",
        headers={
            "Authorization": f"Basic {token}",
            "Accept": "application/json"
        },
        
        
    )
    response.raise_for_status()
    return response.json()
