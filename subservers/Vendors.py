
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Vendors_mcp = FastMCP(name="Vendors")



def GetVendor() -> Dict:
    """Get information for a single vendor by a given `vendor_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/vendors/:vendor_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetVendors(limit: int = "50", offset: int = "0", vendor_name: str = "Supplies%20and%20Such", alias: Optional[str] = "Supplies%20and%20Such", license_number: Optional[int] = "1234567", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get vendor information based on query parameters."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/vendors/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", vendor_name: str = "Supplies%20and%20Such", alias: Optional[str] = "Supplies%20and%20Such", license_number: Optional[int] = "1234567", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostVendor() -> Dict:
    """Create a new vendor.  Note on addresses:  *   If provided, the value for the `shipping.state` and `billing.state` fields (if any) should be sent as a valid two-letter state abbreviation. *   If provided, the value for the `shipping.country` and `billing.country` fields should be sent as the full, capitalized country name: e.g., `"United States"`, `"Canada"`, etc."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/vendors/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutVendor() -> Dict:
    """Update an existing vendor with a given `vendor_id`.  See `PostVendor` for guidelines on specific fields in the request body."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/vendors/:vendor_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetVendorContacts(limit: int = "50", offset: int = "0") -> Dict:
    """Gets the contacts for a vendor for a given `vendor_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/vendors/:vendor_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostVendorContacts() -> Dict:
    """Create a vendor contact or many vendor contacts for a vendor with a given `vendor_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/vendors/:vendor_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutVendorContacts() -> Dict:
    """Update a contact, or multiple contacts, for a vendor for a given `vendor_id`. Each contact should contain a `vendor_contact_id` to indicate which vendor contact should be updated."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/vendors/:vendor_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
