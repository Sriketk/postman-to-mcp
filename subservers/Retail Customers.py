
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Retail Customers_mcp = FastMCP(name="Retail Customers")



def GetRetailCustomer() -> Dict:
    """Get information on a single customer for a given `customer_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/customers/{customer_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetRetailCustomers(limit: int = "50", offset: int = "0", first_name: str = "John", last_name: str = "Smith", dob: datetime = "%Y-%m-%d", state: Literal["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"] = "CA", patient_id: str = "1a2b3c", phone_number: int = "5558675309", email: str = "joe%40cannabatopia.com", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get customers.  This request is scoped to the company. You can optionally filter by query parameters."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/customers/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", first_name: str = "John", last_name: str = "Smith", dob: datetime = "%Y-%m-%d", state: Literal["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"] = "CA", patient_id: str = "1a2b3c", phone_number: int = "5558675309", email: str = "joe%40cannabatopia.com", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostRetailCustomer() -> Dict:
    """Create a new retail customer  Request Fields:  *   email: string - REQUIRED     *   The primary email for the customer to be created. Must be unique. *   alternate_email: string     *   Additional, optional email for the customer to be created. *   first_name: string - REQUIRED *   last_name: string - REQUIRED *   middle_name: string *   preferred_name: string *   dob: date - REQUIRED       The customer Date of Birth. *   allergies: string *   state: string       Two letter state abbreviation. *   medical_card_state: string       Two letter state abbreviation. *   medical_card_expiration: date *   patient_id: string       The customer's ID in the the state patient registry. If provided state is REQUIRED *   phone: string     *   Primary phone number for customer, expected to be mobile number. *   home_phone: string     *   Additional, optional phone number for customer, expected to be home number. *   alternate_phone: string     *   Additional, optional phone number for customer. *   address: an array of zero to three addresses each containing:     *   first_name: string           Defaults to customer's fist_name if not passed     *   last_name: string           Defaults to customer's last_name if not passed     *   address_line_1: string - REQUIRED     *   address_line_2: string     *   city: string - REQUIRED     *   state: string - REQUIRED     *   postcode: string - REQUIRED     *   country: string - REQUIRED     *   type: string           If provided, must be either `shipping` or `billing` *   is_verified: boolean *   state_id: string *   state_id_expiration_timestamp: date *   customer_group: string       If provided, must be one of `veteran`, `student`, `first responder`, employee`,`industry\`. *   customer_disciplinary_status: string       If provided, must be one of `no issues`, `warning - level 1`, `warning - level 2`, `banned`.       It is possible that the customer will be created correctly in the Flourish, but not found in the MMUR. In that case, the response will be a normal success response, except the message will be different and code will be set. The possible code/message combinations are:  *   CUS0002: customer was created in flourish, but was not found in the MMUR       occurs when the MMUR was searched, but the customer was not found *   CUS0003: customer was created in flourish, but MMUR lookup is disabled       occurs when the MMUR was not searched becuase it is not configured"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/customers/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutRetailCustomer() -> Dict:
    """Edit an existing retail customer by ID.  Request Fields:  *   email: string - REQUIRED     *   The primary email for the customer being updated. Must be unique. *   alternate_email: string     *   Additional, optional email for the customer being updated. *   first_name: string - REQUIRED *   last_name: string - REQUIRED *   middle_name: string *   dob: date - REQUIRED       The customer Date of Birth. *   patient_id: string       The customer's ID in the the state patient registry. If provided state is REQUIRED *   state: string *   phone: string     *   Primary phone number for customer, expected to be mobile number. *   home_phone: string     *   Additional, optional phone number for customer, expected to be home number. *   alternate_phone: string     *   Additional, optional phone number for customer. *   address: an array of zero to three addresses each containing:     *   id : int           If passed, the address with this id will be updated. If not passed, a new address will be created. Any address whose id is not passed will be deactivated     *   first_name: string           Defaults to customer's fist_name if not passed     *   last_name: string           Defaults to customer's last_name if not passed     *   address_line_1: string - REQUIRED     *   address_line_2: string     *   city: string - REQUIRED     *   state: string - REQUIRED     *   postcode: string - REQUIRED     *   country: string - REQUIRED     *   type: string           If provided, must be either `shipping` or `billing` *   is_verified: boolean *   medical_card_expiration: date *   state_id: string *   state_id_expiration_timestamp: date *   customer_group: string       If provided, must be one of     *   veteran     *   student     *   first responder     *   employee     *   industry *   customer_disciplinary_status: string       If provided, must be one of     *   veteran     *   no issues     *   warning - level 1     *   warning - level 2     *   banned *   allergies: string       It is possible that the customer will be created correctly in the Flourish, but not found in the MMUR. In that case, the response will be a normal success response, except the message will be different and code will be set. The possible code/message combinations are:  *   CUS0002: customer was created in flourish, but was not found in the MMUR       occurs when the MMUR was searched, but the customer was not found *   CUS0003: customer was created in flourish, but MMUR lookup is disabled       occurs when the MMUR was not searched becuase it is not configured."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/customers/:customer_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
