
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Strains_mcp = FastMCP(name="Strains")



def GetStrains(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get details on all registered strains."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/strains/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetStrainById(token: str) -> Dict:
    """Gets the details of a strain by a given ID."""
    params = {'token': token}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/strains/:strain_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
