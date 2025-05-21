
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Retail_Customers_mcp = FastMCP(name="Retail_Customers")



def GetRetailCustomer(token: str) -> Dict:
    """Get information on a single customer for a given `customer_id`."""
    params = {'token': token}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/customers/{customer_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetRetailCustomers(token: str, limit: int = "50", offset: int = "0", first_name: str = "John", last_name: str = "Smith", dob: datetime = "%Y-%m-%d", state: Literal["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"] = "CA", patient_id: str = "1a2b3c", phone_number: int = "5558675309", email: str = "joe%40cannabatopia.com", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get customers.  This request is scoped to the company. You can optionally filter by query parameters."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'first_name': first_name, 'last_name': last_name, 'dob': dob, 'state': state, 'patient_id': patient_id, 'phone_number': phone_number, 'email': email, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/customers/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostRetailCustomer(token: str, email: str = " ", alternate_email: Optional[str] = " ", first_name: str = " ", last_name: str = " ", middle_name: Optional[str] = " ", preferred_name: Optional[str] = " ", dob: datetime = " ", allergies: Optional[str] = " ", state: Optional[Literal["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]] = " ", medical_card_state: Optional[Literal["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]] = " ", medical_card_expiration: Optional[datetime] = " ", patient_id: Optional[str] = " ", phone: Optional[str] = " ", home_phone: Optional[str] = " ", alternate_phone: Optional[str] = " ", address: Optional[object] = " ", is_verified: Optional[bool] = " ", state_id: Optional[str] = " ", state_id_expiration_timestamp: Optional[datetime] = " ", customer_group: Optional[Literal["veteran", "student", "first responder", "employee", "industry"]] = " ", customer_disciplinary_status: Optional[Literal["no issues", "warning - level 1", "warning - level 2", "banned"]] = " ") -> Dict:
    """This endpoint creates a new retail customer in the system. It requires various personal information fields, some of which are mandatory while others are optional. The endpoint can handle multiple addresses and has specific requirements for certain fields."""
    params = {'token': token, 'email': email, 'alternate_email': alternate_email, 'first_name': first_name, 'last_name': last_name, 'middle_name': middle_name, 'preferred_name': preferred_name, 'dob': dob, 'allergies': allergies, 'state': state, 'medical_card_state': medical_card_state, 'medical_card_expiration': medical_card_expiration, 'patient_id': patient_id, 'phone': phone, 'home_phone': home_phone, 'alternate_phone': alternate_phone, 'address': address, 'is_verified': is_verified, 'state_id': state_id, 'state_id_expiration_timestamp': state_id_expiration_timestamp, 'customer_group': customer_group, 'customer_disciplinary_status': customer_disciplinary_status}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/customers/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PutRetailCustomer(token: str, email: str = " ", alternate_email: Optional[str] = " ", first_name: str = " ", last_name: str = " ", middle_name: Optional[str] = " ", dob: datetime = " ", patient_id: Optional[str] = " ", state: Optional[str] = " ", phone: Optional[str] = " ", home_phone: Optional[str] = " ", alternate_phone: Optional[str] = " ", address: Optional[object] = " ", is_verified: Optional[bool] = " ", medical_card_expiration: Optional[datetime] = " ", state_id: Optional[str] = " ", state_id_expiration_timestamp: Optional[datetime] = " ", customer_group: Optional[Literal["veteran", "student", "first responder", "employee", "industry"]] = " ", customer_disciplinary_status: Optional[Literal["veteran", "no issues", "warning - level 1", "warning - level 2", "banned"]] = " ", allergies: Optional[str] = " ", preferred_name: Optional[str] = " ", medical_card_state: Optional[str] = " ", is_active: Optional[bool] = " ", available_credit: Optional[float] = " ") -> Dict:
    """This endpoint allows editing an existing retail customer by ID. It updates various customer details including personal information, contact details, addresses, and customer status."""
    params = {'token': token, 'email': email, 'alternate_email': alternate_email, 'first_name': first_name, 'last_name': last_name, 'middle_name': middle_name, 'dob': dob, 'patient_id': patient_id, 'state': state, 'phone': phone, 'home_phone': home_phone, 'alternate_phone': alternate_phone, 'address': address, 'is_verified': is_verified, 'medical_card_expiration': medical_card_expiration, 'state_id': state_id, 'state_id_expiration_timestamp': state_id_expiration_timestamp, 'customer_group': customer_group, 'customer_disciplinary_status': customer_disciplinary_status, 'allergies': allergies, 'preferred_name': preferred_name, 'medical_card_state': medical_card_state, 'is_active': is_active, 'available_credit': available_credit}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/customers/:customer_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
