
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


UOMs_mcp = FastMCP(name="UOMs")



def GetUOMs(limit: int = "50", offset: int = "0", : str = "") -> Dict:
    """Get all company UOMs (unit of measure)."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/uoms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", : str = ""
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
