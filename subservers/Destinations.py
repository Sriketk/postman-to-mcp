
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Destinations_mcp = FastMCP(name="Destinations")



def GetDestination() -> Dict:
    """Get a destination from a given `destination_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/destinations/:destination_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetDestinations(limit: int = "50", offset: int = "0", destination_type: Literal["Laboratory", "Processor", "Grower", "Dispensary", "Distributor", "Manufacturer", "Other", "Microbusiness"] = "Laboratory", facility_name: str = "Distribution", alias: str = "Cal Distro", license_number: int = "1234567", search: str = "dist", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get destinations based on query parameters."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/destinations/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", destination_type: Literal["Laboratory", "Processor", "Grower", "Dispensary", "Distributor", "Manufacturer", "Other", "Microbusiness"] = "Laboratory", facility_name: str = "Distribution", alias: str = "Cal Distro", license_number: int = "1234567", search: str = "dist", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostDestination() -> Dict:
    """Creates a new destination.  Valid destination types for the `type` field are:  *   Laboratory *   Processor *   Grower *   Dispensary *   Distributor *   Manufacturer *   Other *   Microbusiness       Note on addresses:  *   The `state` field at the top level of the JSON request, along with the `billing.state` , if any, should be sent as a valid two-letter state abbreviation. *   The `country` and `billing.country` fields should be sent as the full, capitalized country name: e.g., "United States", "Canada", etc."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/destinations/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutDestination() -> Dict:
    """Update a destination for the given `destination_id`.  See `PostDestination` for guidelines on specific fields in the request body."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/destinations/:destination_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetDestinationContacts(limit: int = "50", offset: int = "0") -> Dict:
    """Get all of the contacts for a given destination by `destination_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/destinations/:destination_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostDestinationContacts() -> Dict:
    """Create one or many contacts for a destination for the given `destination_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/destinations/:destination_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutDestinationContacts(FacilityID: str = "04bb2a7c") -> Dict:
    """Update one or many destination contacts for a destination for the given `destination_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/destinations/:destination_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            FacilityID: str = "04bb2a7c"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
