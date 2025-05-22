
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Outbound_Orders_mcp = FastMCP(name="Outbound_Orders")



def GetOutboundOrder(token: str) -> Dict:
    """Get information about an existing outbound order by a given `order_id`."""
    params = {'token': token}
    body = {}
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
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/outbound-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

                                class Sales_repModel(BaseModel):
                                
                            
                                class DestinationModel(BaseModel):
                                
                            
def PostOutboundOrder(token: str, original_order_id: Optional[string] = " ", order_timestamp: string = " ", pretax_discounts: Optional[Literal["true", "false"]] = " ", invoice_date: Optional[string] = " ", sales_rep: Optional[Sales_repModel] = " ", destination: DestinationModel = " ", notes: Optional[array] = " ", charges: Optional[array] = " ", discounts: Optional[array] = " ", order_lines: array = " ") -> Dict:
    """This endpoint creates a new outbound, business-to-business order. If the facility is configured to require sales reps for outbound orders, it will be required on creation. The endpoint includes logic for existing entity search and creation."""
    params = {'token': token, 'original_order_id': original_order_id, 'order_timestamp': order_timestamp, 'pretax_discounts': pretax_discounts, 'invoice_date': invoice_date, 'sales_rep': sales_rep, 'destination': destination, 'notes': notes, 'charges': charges, 'discounts': discounts, 'order_lines': order_lines}
    body = {'original_order_id': original_order_id, 'order_timestamp': order_timestamp, 'pretax_discounts': pretax_discounts, 'invoice_date': invoice_date, 'sales_rep': sales_rep, 'destination': destination, 'notes': notes, 'charges': charges, 'discounts': discounts, 'order_lines': order_lines}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/outbound-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()
