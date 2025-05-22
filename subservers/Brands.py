
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Brands_mcp = FastMCP(name="Brands")



def GetBrands(token: str, offset: int = "0", limit: int = "50", brand_id: int = "19", brand_name: str = "Top Shelf", active: bool = "False") -> Dict:
    """Get details for all item brands."""
    params = {'token': token, 'offset': offset, 'limit': limit, 'brand_id': brand_id, 'brand_name': brand_name, 'active': active}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/brands/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
