
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Vendors_mcp = FastMCP(name="Vendors")



def GetVendor(token: str) -> Dict:
    """Get information for a single vendor by a given `vendor_id`."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/vendors/:vendor_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetVendors(token: str, limit: int = "50", offset: int = "0", vendor_name: str = "Supplies%20and%20Such", alias: Optional[str] = "Supplies%20and%20Such", license_number: Optional[int] = "1234567", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get vendor information based on query parameters."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'vendor_name': vendor_name, 'alias': alias, 'license_number': license_number, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/vendors/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostVendor(token: str, name: str = " ", vendor_type_name: Literal["Dispensary"] = " ", company_email: str = " ", company_phone_number: str = " ", shipping: object = " ", shipping.address: str = " ", shipping.city: str = " ", shipping.state: str = " ", shipping.zip_code: str = " ", shipping.country: str = " ", billing: object = " ", billing.address: str = " ", billing.city: str = " ", billing.state: str = " ", billing.zip_code: str = " ", billing.country: str = " ", license_number: str = " ", website: Optional[str] = " ", note: Optional[str] = " ", alias: Optional[str] = " ", account_number: Optional[str] = " ", ref_field_1: Optional[str] = " ", ref_field_2: Optional[str] = " ", diverse_supplier: Optional[Literal["0", "1"]] = " ", state_expiration_date: Optional[str] = " ") -> Dict:
    """This endpoint creates a new vendor. It requires various details about the vendor, including name, type, contact information, shipping and billing addresses, license information, and other optional fields."""
    params = {'token': token, 'name': name, 'vendor_type_name': vendor_type_name, 'company_email': company_email, 'company_phone_number': company_phone_number, 'shipping': shipping, 'shipping.address': shipping.address, 'shipping.city': shipping.city, 'shipping.state': shipping.state, 'shipping.zip_code': shipping.zip_code, 'shipping.country': shipping.country, 'billing': billing, 'billing.address': billing.address, 'billing.city': billing.city, 'billing.state': billing.state, 'billing.zip_code': billing.zip_code, 'billing.country': billing.country, 'license_number': license_number, 'website': website, 'note': note, 'alias': alias, 'account_number': account_number, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'diverse_supplier': diverse_supplier, 'state_expiration_date': state_expiration_date}
    body = {'name': name, 'vendor_type_name': vendor_type_name, 'company_email': company_email, 'company_phone_number': company_phone_number, 'shipping': shipping, 'shipping.address': shipping.address, 'shipping.city': shipping.city, 'shipping.state': shipping.state, 'shipping.zip_code': shipping.zip_code, 'shipping.country': shipping.country, 'billing': billing, 'billing.address': billing.address, 'billing.city': billing.city, 'billing.state': billing.state, 'billing.zip_code': billing.zip_code, 'billing.country': billing.country, 'license_number': license_number, 'website': website, 'note': note, 'alias': alias, 'account_number': account_number, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'diverse_supplier': diverse_supplier, 'state_expiration_date': state_expiration_date}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/vendors/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutVendor(token: str, name: str = " ", company_email: str = " ", vendor_type_name: Literal["Dispensary"] = " ", shipping: object = " ", billing: object = " ", license_number: str = " ", website: Optional[str] = " ", note: Optional[str] = " ", active: Literal["true", "false"] = " ", account_number: Optional[str] = " ", alias: Optional[str] = " ", diverse_supplier: Optional[Literal["0", "1"]] = " ", company_phone_number: Optional[str] = " ", business_id: Optional[str] = " ", external_vendor_id: Optional[str] = " ", ref_field_1: Optional[str] = " ", ref_field_2: Optional[str] = " ") -> Dict:
    """Update an existing vendor with a given `vendor_id`. This endpoint allows modification of various vendor details including name, contact information, address, license information, and other relevant fields."""
    params = {'token': token, 'name': name, 'company_email': company_email, 'vendor_type_name': vendor_type_name, 'shipping': shipping, 'billing': billing, 'license_number': license_number, 'website': website, 'note': note, 'active': active, 'account_number': account_number, 'alias': alias, 'diverse_supplier': diverse_supplier, 'company_phone_number': company_phone_number, 'business_id': business_id, 'external_vendor_id': external_vendor_id, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2}
    body = {'name': name, 'company_email': company_email, 'vendor_type_name': vendor_type_name, 'shipping': shipping, 'billing': billing, 'license_number': license_number, 'website': website, 'note': note, 'active': active, 'account_number': account_number, 'alias': alias, 'diverse_supplier': diverse_supplier, 'company_phone_number': company_phone_number, 'business_id': business_id, 'external_vendor_id': external_vendor_id, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/vendors/:vendor_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def GetVendorContacts(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Gets the contacts for a vendor for a given `vendor_id`."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/vendors/:vendor_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostVendorContacts(token: str, first_name: str = " ", last_name: str = " ", email: str = " ", phone_number: Optional[str] = " ", department: Optional[str] = " ", notes: Optional[str] = " ", is_primary: Literal["0", "1"] = " ") -> Dict:
    """Create a vendor contact or many vendor contacts for a vendor with a given `vendor_id`."""
    params = {'token': token, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'department': department, 'notes': notes, 'is_primary': is_primary}
    body = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'department': department, 'notes': notes, 'is_primary': is_primary}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/vendors/:vendor_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutVendorContacts(token: str, vendor_contact_id: int = " ", first_name: str = " ", last_name: str = " ", email: str = " ", phone_number: str = " ", department: str = " ", notes: Optional[str] = " ", is_primary: Literal["0", "1"] = " ") -> Dict:
    """Update a contact, or multiple contacts, for a vendor for a given `vendor_id`. Each contact should contain a `vendor_contact_id` to indicate which vendor contact should be updated."""
    params = {'token': token, 'vendor_contact_id': vendor_contact_id, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'department': department, 'notes': notes, 'is_primary': is_primary}
    body = {'vendor_contact_id': vendor_contact_id, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'department': department, 'notes': notes, 'is_primary': is_primary}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/vendors/:vendor_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()
