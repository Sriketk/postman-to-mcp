
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


UOMs_mcp = FastMCP(name="UOMs")



def GetUOMs(token: str, limit: int = "50", offset: int = "0", : str = "") -> Dict:
    """Get all company UOMs (unit of measure)."""
    params = {'token': token, 'limit': limit, 'offset': offset, '': }
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/uoms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
