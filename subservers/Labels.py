
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Labels_mcp = FastMCP(name="Labels")



def GetPackageLabelData() -> Dict:
    """Endpoint to retrieve all of the data available for a label for a given package ID. Pass the package ID in the URL as the only parameter like:  `v1/package-labels/CADS-20210128-004`  This does require a `FacilityID` header to be sent along with the request."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/package-labels/{package_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
