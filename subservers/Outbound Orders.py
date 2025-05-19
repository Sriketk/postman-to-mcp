
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Outbound Orders_mcp = FastMCP(name="Outbound Orders")



def GetOutboundOrder() -> Dict:
    """Get information about an existing outbound order by a given `order_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/outbound-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetOutboundOrders(limit: int = "50", offset: int = "50", order_status: Literal["Created", "Partially Allocated", "Allocated", "Shipped", "Cancelled"] = "Created", order_origin: Literal["Flourish", "Online", "Cultivate", "Leaflink", "Order Management System"] = "Online", order_payment_status: Literal["Awaiting Payment", "Paid", "Partially Paid", "Partially Refunded", "Refunded"] = "Paid", order_id: int = "1234", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2022-08-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", completed_timestamp_start: str = "2020-01-02T15:04:05.000Z", completed_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get outbound orders. This request may be scoped to a single facility with the `FacilityID` header, or the company as a whole."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/outbound-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "50", order_status: Literal["Created", "Partially Allocated", "Allocated", "Shipped", "Cancelled"] = "Created", order_origin: Literal["Flourish", "Online", "Cultivate", "Leaflink", "Order Management System"] = "Online", order_payment_status: Literal["Awaiting Payment", "Paid", "Partially Paid", "Partially Refunded", "Refunded"] = "Paid", order_id: int = "1234", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2022-08-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", completed_timestamp_start: str = "2020-01-02T15:04:05.000Z", completed_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostOutboundOrder() -> Dict:
    """Create a new outbound, business-to-business order. If your facility is configured to require sales reps for outbound orders, it will be required on creation.  Existing Entity Search:  - If passing the `id` field for `destination`, `distribution`, or `sales_rep` no other fields may be passed. - For `destination` and `distributor`, if defined a search will be done by `facility_name` and if found a new facility will not be created. - For `sales_rep`, if defined a search will be done by `email` and if found a new sales rep will not be created. - For `contact` on `destination` or `distributor`, if defined a search will be done by `email` and if found a new contact will not be created."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/outbound-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutOutboundOrder() -> Dict:
    """Update an outbound, business-to-business order by ID.  - Orders can only be updated when nothing is allocated in Flourish at the time of update. - We do not currently support order status changes via this endpoint, except for order cancellation (below).      - If your facility configuration requires sales reps for outbound orders, it will be required.       Note that order modification is supported, but modification of sub-types like `destination`, `distributor`, `sales_rep`, and `contact` is not supported at this time.  Existing Entity Search:  - If passing the `id` field for `destination`, `distribution`, or `sales_rep` no other fields may be passed.       Orders can be Cancelled by updating the order status to `Cancelled`. Simply include the following in the request body:  ``` json "order_status": "Cancelled"   ```  When cancelling an order, the sales rep is not required even if your facility configuration requires sales reps for outbound orders. These validation errors are returned when we do not support cancellation:  - `Order has already been shipped` - When a user attempts to cancel a `Shipped` order. - `Order has already been completed` - When a user attempts to cancel a `Completed` order. - `Order has already been cancelled` - When a user attempts to cancel a `Cancelled` order."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/outbound-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetOrderPaymentTerm() -> Dict:
    """Fetch an order payment term by its ID"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/order-payment-terms/{order_payment_term_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetOrderPaymentTerms(limit: int = "50", offset: int = "0", order_payment_term: Optional[str] = "cod", search: str = "net") -> Dict:
    """Get order payment terms for a company, filterable by query parameters."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/order-payment-terms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", order_payment_term: Optional[str] = "cod", search: str = "net"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostOrderPaymentTerms() -> Dict:
    """Create an order payment term for a company.  Request body fields:  - `order_payment_term`: string **\[REQUIRED\]**     - The name of the payment term to create - `due_num_days`: integer     - The number of days after the invoice is issued when payment is due - `due_day_of_month`: integer     - The standard day of the month when payments are due, e.g. 1 for the first of every month - `due_next_month_cond_num_days`: integer     - If the invoice is issued within a certain number of days of the standard `due_day_of_month`, then payment is expected the following month  **Note**: Either `due_num_days` by itself **OR** `due_day_of_month` and `due_next_month_cond_num_days` together should be passed in the request."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/order-payment-terms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetSalesReps(Limit: str = "", Offset: str = "") -> Dict:
    """Gets the sales reps that are available for a given `FacilityID` sent in the header of the request."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/sales-reps/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            Limit: str = "", Offset: str = ""
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
