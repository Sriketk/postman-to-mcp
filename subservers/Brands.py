
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Brands_mcp = FastMCP(name="Brands")



def GetBrands(offset: int = "0", limit: int = "50", brand_id: int = "19", brand_name: str = "Top Shelf", active: Optional[bool] = "False") -> Dict:
    """Get details for all item brands."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/brands/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            offset: int = "0", limit: int = "50", brand_id: int = "19", brand_name: str = "Top Shelf", active: Optional[bool] = "False"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
