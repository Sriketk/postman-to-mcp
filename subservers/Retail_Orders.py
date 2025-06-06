
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Retail_Orders_mcp = FastMCP(name="Retail_Orders")



def GetRetailOrder(token: str) -> Dict:
    """Get information about an existing retail order for a given `order_id`."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/retail-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetRetailOrders(token: str, limit: int = "50", offset: int = "0", customer_id: int = "111", patient_id: str = "1a2b3c", order_status: Literal["Created", "Submitted", "Packed", "Out for Delivery", "Completed", "Cancelled", "Undeliverable"] = "Completed", order_origin: Literal["Flourish", "Online", "Cultivate", "Leaflink", "Order Management System"] = "Online", order_fulfillment_type: Literal["Delivery", "In-Store", "Pickup"] = "Delivery", order_payment_status: Literal["Awaiting Payment", "Paid", "Partially Paid", "Partially Refunded", "Refunded"] = "Paid", order_id: int = "1234", is_backorder: bool = "True", is_preorder: bool = "False", needs_review: bool = "True", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", submitted_timestamp_start: str = "2020-01-02T15:04:05.000Z", submitted_timestamp_end: str = "2020-01-03T15:04:05.000Z", packed_timestamp_start: str = "2020-01-02T15:04:05.000Z", packed_timestamp_end: str = "2020-01-03T15:04:05.000Z", completed_timestamp_start: str = "2020-01-02T15:04:05.000Z", completed_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get retail orders based on query parameters.  This request may be scoped to a single facility with the `FacilityID` header, or the company as a whole."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'customer_id': customer_id, 'patient_id': patient_id, 'order_status': order_status, 'order_origin': order_origin, 'order_fulfillment_type': order_fulfillment_type, 'order_payment_status': order_payment_status, 'order_id': order_id, 'is_backorder': is_backorder, 'is_preorder': is_preorder, 'needs_review': needs_review, 'created_timestamp_start': created_timestamp_start, 'created_timestamp_end': created_timestamp_end, 'submitted_timestamp_start': submitted_timestamp_start, 'submitted_timestamp_end': submitted_timestamp_end, 'packed_timestamp_start': packed_timestamp_start, 'packed_timestamp_end': packed_timestamp_end, 'completed_timestamp_start': completed_timestamp_start, 'completed_timestamp_end': completed_timestamp_end}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/retail-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

                                class Delivery_addressModel(BaseModel):
                                
                            
def PostRetailOrder(token: str, original_order_id: Optional[string] = " ", customer_id: string = " ", is_backorder: Optional[Literal["true", "false"]] = " ", is_preorder: Optional[Literal["true", "false"]] = " ", is_replacement: Optional[Literal["true", "false"]] = " ", is_approved: Optional[Literal["true", "false"]] = " ", is_recreational: Optional[Literal["true", "false"]] = " ", notes: Optional[string] = " ", order_timestamp: Optional[string] = " ", order_status: Optional[Literal["created", "submitted"]] = " ", fulfillment_type: Literal["delivery", "in-store", "pickup"] = " ", expected_delivery_timestamp: Optional[string] = " ", expected_pickup_timestamp: Optional[string] = " ", delivery_address_id: Optional[string] = " ", delivery_address: Optional[Delivery_addressModel] = " ", delivery_contact_no: Optional[string] = " ", delivery_text_contact_no: Optional[string] = " ", delivery_email: Optional[string] = " ", delivery_fee: Optional[number] = " ", total_paid: Optional[number] = " ", order_lines: array = " ", applied_discounts: Optional[array] = " ") -> Dict:
    """This endpoint creates a new retail order. It requires customer identification, fulfillment details, and order line items. Optional fields include various order flags, timestamps, delivery information, and applied discounts."""
    params = {'token': token, 'original_order_id': original_order_id, 'customer_id': customer_id, 'is_backorder': is_backorder, 'is_preorder': is_preorder, 'is_replacement': is_replacement, 'is_approved': is_approved, 'is_recreational': is_recreational, 'notes': notes, 'order_timestamp': order_timestamp, 'order_status': order_status, 'fulfillment_type': fulfillment_type, 'expected_delivery_timestamp': expected_delivery_timestamp, 'expected_pickup_timestamp': expected_pickup_timestamp, 'delivery_address_id': delivery_address_id, 'delivery_address': delivery_address, 'delivery_contact_no': delivery_contact_no, 'delivery_text_contact_no': delivery_text_contact_no, 'delivery_email': delivery_email, 'delivery_fee': delivery_fee, 'total_paid': total_paid, 'order_lines': order_lines, 'applied_discounts': applied_discounts}
    body = {'original_order_id': original_order_id, 'customer_id': customer_id, 'is_backorder': is_backorder, 'is_preorder': is_preorder, 'is_replacement': is_replacement, 'is_approved': is_approved, 'is_recreational': is_recreational, 'notes': notes, 'order_timestamp': order_timestamp, 'order_status': order_status, 'fulfillment_type': fulfillment_type, 'expected_delivery_timestamp': expected_delivery_timestamp, 'expected_pickup_timestamp': expected_pickup_timestamp, 'delivery_address_id': delivery_address_id, 'delivery_address': delivery_address, 'delivery_contact_no': delivery_contact_no, 'delivery_text_contact_no': delivery_text_contact_no, 'delivery_email': delivery_email, 'delivery_fee': delivery_fee, 'total_paid': total_paid, 'order_lines': order_lines, 'applied_discounts': applied_discounts}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/retail-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

                                class Delivery_addressModel(BaseModel):
                                    __root__: Dict[str, Any]
                            
def PostRetailOrderV2(token: str, original_order_id: string = " ", customer_id: string = " ", is_preorder: Literal["true", "false"] = " ", notes: Optional[string] = " ", order_status: Literal["submitted"] = " ", fulfillment_type: Literal["pickup", "delivery"] = " ", is_recreational: Literal["true", "false"] = " ", order_lines: array = " ", applied_discounts: Optional[array] = " ", delivery_fee: Optional[number] = " ", delivery_address: Optional[Delivery_addressModel] = " ", expected_pickup_timestamp: Optional[string] = " ", expected_delivery_timestamp: Optional[string] = " ") -> Dict:
    """The PostRetailOrderV2 endpoint is an enhanced version of PostRetailOrder, designed to create retail orders with advanced discount capabilities. It processes the order through Flourish's internal discounting engine, allowing for automatic application of more complex discounts such as BOGOs, single-use promo codes, customer group-targeted discounts, and birthday discounts. The request and response JSON structures are identical to the PostRetailOrder endpoint."""
    params = {'token': token, 'original_order_id': original_order_id, 'customer_id': customer_id, 'is_preorder': is_preorder, 'notes': notes, 'order_status': order_status, 'fulfillment_type': fulfillment_type, 'is_recreational': is_recreational, 'order_lines': order_lines, 'applied_discounts': applied_discounts, 'delivery_fee': delivery_fee, 'delivery_address': delivery_address, 'expected_pickup_timestamp': expected_pickup_timestamp, 'expected_delivery_timestamp': expected_delivery_timestamp}
    body = {'original_order_id': original_order_id, 'customer_id': customer_id, 'is_preorder': is_preorder, 'notes': notes, 'order_status': order_status, 'fulfillment_type': fulfillment_type, 'is_recreational': is_recreational, 'order_lines': order_lines, 'applied_discounts': applied_discounts, 'delivery_fee': delivery_fee, 'delivery_address': delivery_address, 'expected_pickup_timestamp': expected_pickup_timestamp, 'expected_delivery_timestamp': expected_delivery_timestamp}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v2/retail-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

                                class Delivery_addressModel(BaseModel):
                                
                            
def PutRetailOrder(token: str, original_order_id: string = " ", customer_id: string = " ", is_backorder: Literal["true", "false"] = " ", is_preorder: Literal["true", "false"] = " ", is_replacement: Literal["true", "false"] = " ", is_approved: Literal["true", "false"] = " ", is_recreational: Literal["true", "false"] = " ", notes: string = " ", order_timestamp: string = " ", order_status: Literal["created", "submitted"] = " ", fulfillment_type: Literal["delivery"] = " ", delivery_fee: number = " ", delivery_address: Delivery_addressModel = " ", total_paid: number = " ", order_lines: array = " ", applied_discounts: array = " ") -> Dict:
    """This endpoint updates a retail order by ID. Orders can only be updated if they are in the 'Created' or 'Submitted' statuses. The endpoint does not support modification of order status. This operation will fully replace the record, and all fields required in the POST must be provided. Users should reference the PostRetailOrder endpoint for specific behavior details and request fields."""
    params = {'token': token, 'original_order_id': original_order_id, 'customer_id': customer_id, 'is_backorder': is_backorder, 'is_preorder': is_preorder, 'is_replacement': is_replacement, 'is_approved': is_approved, 'is_recreational': is_recreational, 'notes': notes, 'order_timestamp': order_timestamp, 'order_status': order_status, 'fulfillment_type': fulfillment_type, 'delivery_fee': delivery_fee, 'delivery_address': delivery_address, 'total_paid': total_paid, 'order_lines': order_lines, 'applied_discounts': applied_discounts}
    body = {'original_order_id': original_order_id, 'customer_id': customer_id, 'is_backorder': is_backorder, 'is_preorder': is_preorder, 'is_replacement': is_replacement, 'is_approved': is_approved, 'is_recreational': is_recreational, 'notes': notes, 'order_timestamp': order_timestamp, 'order_status': order_status, 'fulfillment_type': fulfillment_type, 'delivery_fee': delivery_fee, 'delivery_address': delivery_address, 'total_paid': total_paid, 'order_lines': order_lines, 'applied_discounts': applied_discounts}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/retail-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def _(token: str, payment_type: Literal["Cash", "Manual"] = " ", amount: number = " ", automatic_complete: boolean = " ", manual_payment_type: Optional[Literal["CanPay"]] = " ", reference_id: Optional[string] = " ") -> Dict:
    """Create a new payment against a retail order. Response is identical to GetRetailOrder call."""
    params = {'token': token, 'payment_type': payment_type, 'amount': amount, 'automatic_complete': automatic_complete, 'manual_payment_type': manual_payment_type, 'reference_id': reference_id}
    body = {'payment_type': payment_type, 'amount': amount, 'automatic_complete': automatic_complete, 'manual_payment_type': manual_payment_type, 'reference_id': reference_id}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/retail-orders/{order_id}/payment/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def GetEligibleDiscounts(token: str) -> Dict:
    """Get all available, e-commerce eligible retail discounts for a given facility at the current moment. If there are item inclusion rules for a given discount, those items must also be e-commerce eligible or the discount will not be returned.  Takes into account:  *   e-commerce eligibility *   limitations on availability by facility (or facility tag) *   limitations on availability by specific dates/times/days of week       **Note on date/time fields:**  *   `start_date` and `end_date` are the dates when a discount becomes/ceases to be available. One or both can be empty if those values are indefinite. *   `start_date_time` and `end_date_time` are only applicable if the corresponding `start_date` and `end_date` are populated, and they would come into play for discounts that start at, say, 9am on Memorial Day and end at 6am the next day. *   `start_time` and `end_time` are daily start and end times. e.g. a happy hour discount available from 4-6pm every day. *   All the time fields are formatted as `HH:MM` and are irrespective of timezone, so a `start_time` of `16:00` means the discount becomes available at 4pm EDT for facilities in eastern timezone, 4pm PDT for facilities in pacific, and so on."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/retail-discounts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
