
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Strains_mcp = FastMCP(name="Strains")



def GetStrains(limit: int = "50", offset: int = "0") -> Dict:
    """Get details on all registered strains."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/strains/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetStrainById() -> Dict:
    """Gets the details of a strain by a given ID."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/strains/:strain_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
