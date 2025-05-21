
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Outbound_Orders_mcp = FastMCP(name="Outbound_Orders")



def GetOutboundOrder(token: str) -> Dict:
    """Get information about an existing outbound order by a given `order_id`."""
    params = {'token': token}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/outbound-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetOutboundOrders(token: str, limit: int = "50", offset: int = "50", order_status: Literal["Created", "Partially Allocated", "Allocated", "Shipped", "Cancelled"] = "Created", order_origin: Literal["Flourish", "Online", "Cultivate", "Leaflink", "Order Management System"] = "Online", order_payment_status: Literal["Awaiting Payment", "Paid", "Partially Paid", "Partially Refunded", "Refunded"] = "Paid", order_id: int = "1234", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2022-08-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", completed_timestamp_start: str = "2020-01-02T15:04:05.000Z", completed_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get outbound orders. This request may be scoped to a single facility with the `FacilityID` header, or the company as a whole."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'order_status': order_status, 'order_origin': order_origin, 'order_payment_status': order_payment_status, 'order_id': order_id, 'created_timestamp_start': created_timestamp_start, 'created_timestamp_end': created_timestamp_end, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end, 'completed_timestamp_start': completed_timestamp_start, 'completed_timestamp_end': completed_timestamp_end}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/outbound-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostOutboundOrder(token: str, original_order_id: Optional[str] = " ", order_timestamp: datetime = " ", pretax_discounts: Literal["true", "false"] = " ", invoice_date: Optional[datetime] = " ", sales_rep: Optional[object] = " ", destination: object = " ", notes: Optional[List[str]] = " ", charges: Optional[List[str]] = " ", discounts: Optional[List[str]] = " ", order_lines: List[str] = " ") -> Dict:
    """This endpoint creates a new outbound, business-to-business order. If the facility is configured to require sales reps for outbound orders, a sales rep will be required on creation. The endpoint includes functionality for existing entity search for destination, distribution, and sales rep."""
    params = {'token': token, 'original_order_id': original_order_id, 'order_timestamp': order_timestamp, 'pretax_discounts': pretax_discounts, 'invoice_date': invoice_date, 'sales_rep': sales_rep, 'destination': destination, 'notes': notes, 'charges': charges, 'discounts': discounts, 'order_lines': order_lines}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/outbound-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PutOutboundOrder(token: str, id: str = " ", original_order_id: Optional[str] = " ", shipment_id: Optional[str] = " ", order_timestamp: Optional[datetime] = " ", sub_total_price: Optional[float] = " ", taxes: Optional[float] = " ", excise_tax_rate: Optional[float] = " ", total_discounts: Optional[float] = " ", total_charges: Optional[float] = " ", total_price: Optional[float] = " ", total_paid: Optional[float] = " ", delivery_fee: Optional[float] = " ", shipped_timestamp: Optional[datetime] = " ", delivered_timestamp: Optional[datetime] = " ", requested_delivery_date: Optional[str] = " ", last_updated_timestamp: Optional[datetime] = " ", created_by: Optional[str] = " ", created_timestamp: Optional[datetime] = " ", invoice_date: Optional[str] = " ", total_refund: Optional[float] = " ", ref_field_1: Optional[str] = " ", ref_field_2: Optional[str] = " ", ref_field_3: Optional[str] = " ", ref_field_4: Optional[str] = " ", ref_field_5: Optional[str] = " ", is_approved: Optional[bool] = " ", pretax_discounts: Optional[bool] = " ", total_returns: Optional[float] = " ", order_status: Optional[Literal["Cancelled"]] = " ", payment_status: Optional[str] = " ", origin_type: Optional[str] = " ", tax_type: Optional[str] = " ", tax_payment_direction: Optional[str] = " ", payment_term: Optional[str] = " ", origin_facility: Optional[object] = " ", distributor: Optional[object] = " ", destination: Optional[object] = " ", sales_rep: Optional[object] = " ", order_lines: Optional[List[str]] = " ", charges: Optional[List[str]] = " ", discounts: Optional[List[str]] = " ", notes: Optional[List[str]] = " ") -> Dict:
    """This endpoint allows updating an outbound, business-to-business order by ID. It supports order modification but with certain limitations. Orders can only be updated when nothing is allocated in Flourish at the time of update. Order status changes are not supported via this endpoint, except for order cancellation. If the facility configuration requires sales reps for outbound orders, it will be required (except for cancellations). Modification of sub-types like destination, distributor, sales_rep, and contact is not supported. Orders can be cancelled by setting the order_status to "Cancelled"."""
    params = {'token': token, 'id': id, 'original_order_id': original_order_id, 'shipment_id': shipment_id, 'order_timestamp': order_timestamp, 'sub_total_price': sub_total_price, 'taxes': taxes, 'excise_tax_rate': excise_tax_rate, 'total_discounts': total_discounts, 'total_charges': total_charges, 'total_price': total_price, 'total_paid': total_paid, 'delivery_fee': delivery_fee, 'shipped_timestamp': shipped_timestamp, 'delivered_timestamp': delivered_timestamp, 'requested_delivery_date': requested_delivery_date, 'last_updated_timestamp': last_updated_timestamp, 'created_by': created_by, 'created_timestamp': created_timestamp, 'invoice_date': invoice_date, 'total_refund': total_refund, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3, 'ref_field_4': ref_field_4, 'ref_field_5': ref_field_5, 'is_approved': is_approved, 'pretax_discounts': pretax_discounts, 'total_returns': total_returns, 'order_status': order_status, 'payment_status': payment_status, 'origin_type': origin_type, 'tax_type': tax_type, 'tax_payment_direction': tax_payment_direction, 'payment_term': payment_term, 'origin_facility': origin_facility, 'distributor': distributor, 'destination': destination, 'sales_rep': sales_rep, 'order_lines': order_lines, 'charges': charges, 'discounts': discounts, 'notes': notes}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/outbound-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetOrderPaymentTerm(token: str) -> Dict:
    """Fetch an order payment term by its ID"""
    params = {'token': token}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/order-payment-terms/{order_payment_term_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetOrderPaymentTerms(token: str, limit: int = "50", offset: int = "0", order_payment_term: Optional[str] = "cod", search: str = "net") -> Dict:
    """Get order payment terms for a company, filterable by query parameters."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'order_payment_term': order_payment_term, 'search': search}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/order-payment-terms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostOrderPaymentTerms(token: str, order_payment_term: str = " ", due_num_days: Optional[int] = " ", due_day_of_month: Optional[int] = " ", due_next_month_cond_num_days: Optional[int] = " ") -> Dict:
    """This endpoint creates an order payment term for a company. It allows setting up payment terms with either a specific number of days for payment or a standard day of the month when payments are due."""
    params = {'token': token, 'order_payment_term': order_payment_term, 'due_num_days': due_num_days, 'due_day_of_month': due_day_of_month, 'due_next_month_cond_num_days': due_next_month_cond_num_days}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/order-payment-terms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetSalesReps(token: str, Limit: str = "", Offset: str = "") -> Dict:
    """Gets the sales reps that are available for a given `FacilityID` sent in the header of the request."""
    params = {'token': token, 'Limit': Limit, 'Offset': Offset}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/sales-reps/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
