
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Destinations_mcp = FastMCP(name="Destinations")



def GetDestination(token: str) -> Dict:
    """Get a destination from a given `destination_id`."""
    params = {'token': token}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/destinations/:destination_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetDestinations(token: str, limit: int = "50", offset: int = "0", destination_type: Literal["Laboratory", "Processor", "Grower", "Dispensary", "Distributor", "Manufacturer", "Other", "Microbusiness"] = "Laboratory", facility_name: Optional[str] = "Distribution", alias: Optional[str] = "Cal Distro", license_number: Optional[int] = "1234567", search: str = "dist", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get destinations based on query parameters."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'destination_type': destination_type, 'facility_name': facility_name, 'alias': alias, 'license_number': license_number, 'search': search, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/destinations/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostDestination(token: str, type: Literal["Laboratory", "Processor", "Grower", "Dispensary", "Distributor", "Manufacturer", "Other", "Microbusiness"] = " ", name: str = " ", alias: str = " ", company_email: str = " ", company_phone_number: str = " ", website: str = " ", address_line_1: str = " ", address_line_2: Optional[str] = " ", city: str = " ", state: str = " ", zip_code: str = " ", country: str = " ", billing: Optional[object] = " ", local_license_number: str = " ", license_number: str = " ", notes: Optional[str] = " ") -> Dict:
    """Creates a new destination. The endpoint allows for the creation of various types of destinations such as Laboratory, Processor, Grower, Dispensary, Distributor, Manufacturer, Other, and Microbusiness. It requires detailed information about the destination, including contact details, address, and licensing information."""
    params = {'token': token, 'type': type, 'name': name, 'alias': alias, 'company_email': company_email, 'company_phone_number': company_phone_number, 'website': website, 'address_line_1': address_line_1, 'address_line_2': address_line_2, 'city': city, 'state': state, 'zip_code': zip_code, 'country': country, 'billing': billing, 'local_license_number': local_license_number, 'license_number': license_number, 'notes': notes}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/destinations/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PutDestination(token: str, type: Literal["Laboratory"] = " ", name: str = " ", alias: str = " ", company_email: str = " ", company_phone_number: str = " ", website: str = " ", address_line_1: str = " ", address_line_2: Optional[str] = " ", city: str = " ", state: str = " ", zip_code: str = " ", country: str = " ", billing: object = " ", local_license_number: str = " ", license_number: str = " ", notes: Optional[str] = " ") -> Dict:
    """Update a destination for the given `destination_id`. This endpoint allows modification of an existing destination's details including type, name, contact information, address, billing information, and licensing details."""
    params = {'token': token, 'type': type, 'name': name, 'alias': alias, 'company_email': company_email, 'company_phone_number': company_phone_number, 'website': website, 'address_line_1': address_line_1, 'address_line_2': address_line_2, 'city': city, 'state': state, 'zip_code': zip_code, 'country': country, 'billing': billing, 'local_license_number': local_license_number, 'license_number': license_number, 'notes': notes}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/destinations/:destination_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetDestinationContacts(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get all of the contacts for a given destination by `destination_id`."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/destinations/:destination_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostDestinationContacts(token: str, first_name: str = " ", last_name: str = " ", email: str = " ", phone_number: Optional[str] = "None", department: Optional[str] = "None", notes: Optional[str] = "None", is_primary: Literal["0", "1"] = " ") -> Dict:
    """Create one or many contacts for a destination for the given `destination_id`."""
    params = {'token': token, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'department': department, 'notes': notes, 'is_primary': is_primary}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/destinations/:destination_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PutDestinationContacts(token: str, facility_contact_id: int = " ", first_name: str = " ", last_name: str = " ", email: str = " ", phone_number: str = " ", department: str = " ", notes: Optional[str] = " ", is_primary: Literal["0", "1"] = " ") -> Dict:
    """Update one or many destination contacts for a destination for the given `destination_id`."""
    params = {'token': token, 'facility_contact_id': facility_contact_id, 'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'department': department, 'notes': notes, 'is_primary': is_primary}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/destinations/:destination_id/contacts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
