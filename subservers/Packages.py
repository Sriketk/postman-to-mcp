
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Packages_mcp = FastMCP(name="Packages")



def GetPackageDetails() -> Dict:
    """Get the origin info of a cannabis package by its ID."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/packages/:package_id/details/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetPackages(limit: int = "50", offset: int = "0", package_id: str = "1A40X0900002906000099999", package_status: Literal["Created", "Assigned to order", "Shipped", "Consumed", "Archived", "Cancelled"] = "Shipped", include_origin_harvest: Optional[bool] = "False", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get current cannabis packages for a single facility. `package_id` is the unique identifier for the package record returned."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/packages/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", package_id: str = "1A40X0900002906000099999", package_status: Literal["Created", "Assigned to order", "Shipped", "Consumed", "Archived", "Cancelled"] = "Shipped", include_origin_harvest: Optional[bool] = "False", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetPackage(include_origin_harvest: Optional[bool] = "False") -> Dict:
    """Get a cannabis package by it's ID in Flourish."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/packages/{package_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            include_origin_harvest: Optional[bool] = "False"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
