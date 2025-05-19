
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Retail Orders_mcp = FastMCP(name="Retail Orders")



def GetRetailOrder() -> Dict:
    """Get information about an existing retail order for a given `order_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/retail-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetRetailOrders(limit: int = "50", offset: int = "0", customer_id: int = "111", patient_id: str = "1a2b3c", order_status: Literal["Created", "Submitted", "Packed", "Out for Delivery", "Completed", "Cancelled", "Undeliverable"] = "Completed", order_origin: Literal["Flourish", "Online", "Cultivate", "Leaflink", "Order Management System"] = "Online", order_fulfillment_type: Literal["Delivery", "In-Store", "Pickup"] = "Delivery", order_payment_status: Literal["Awaiting Payment", "Paid", "Partially Paid", "Partially Refunded", "Refunded"] = "Paid", order_id: int = "1234", is_backorder: bool = "True", is_preorder: bool = "False", needs_review: bool = "True", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", submitted_timestamp_start: str = "2020-01-02T15:04:05.000Z", submitted_timestamp_end: str = "2020-01-03T15:04:05.000Z", packed_timestamp_start: str = "2020-01-02T15:04:05.000Z", packed_timestamp_end: str = "2020-01-03T15:04:05.000Z", completed_timestamp_start: str = "2020-01-02T15:04:05.000Z", completed_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get retail orders based on query parameters.  This request may be scoped to a single facility with the `FacilityID` header, or the company as a whole."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/retail-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", customer_id: int = "111", patient_id: str = "1a2b3c", order_status: Literal["Created", "Submitted", "Packed", "Out for Delivery", "Completed", "Cancelled", "Undeliverable"] = "Completed", order_origin: Literal["Flourish", "Online", "Cultivate", "Leaflink", "Order Management System"] = "Online", order_fulfillment_type: Literal["Delivery", "In-Store", "Pickup"] = "Delivery", order_payment_status: Literal["Awaiting Payment", "Paid", "Partially Paid", "Partially Refunded", "Refunded"] = "Paid", order_id: int = "1234", is_backorder: bool = "True", is_preorder: bool = "False", needs_review: bool = "True", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", submitted_timestamp_start: str = "2020-01-02T15:04:05.000Z", submitted_timestamp_end: str = "2020-01-03T15:04:05.000Z", packed_timestamp_start: str = "2020-01-02T15:04:05.000Z", packed_timestamp_end: str = "2020-01-03T15:04:05.000Z", completed_timestamp_start: str = "2020-01-02T15:04:05.000Z", completed_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostRetailOrder() -> Dict:
    """Create a new retail order.  - The FacilityID header is required if fulfillment_type is not `delivery`.       Request Fields:  - original_order_id: string       Identifier for an order originating outside of Flourish.      - customer_id: string - REQUIRED       Identifies the specific customer. Customers can be created and retrieved through the retail customers endpoints.      - is_backorder: boolean      - is_preorder: boolean      - is_replacement: boolean      - is_approved: boolean      - is_recreational: boolean       Indicates that the purchase is recreational (as opposed to medical), subject to the compliance rules of the origin facility state      - notes: string      - order_timestamp: datetime       Indicates when the order was originally created. The current timestamp will be used when not given.       (Expected format `2022-04-20T12:34:56.789Z`)      - order_status: string       Defaults to created status if none provided. Valid values are `created` or `submitted`.      - fulfillment_type: string - REQUIRED       Must be one of `delivery`, `in-store`, or `pickup`.      - expected_delivery_timestamp: datetime       Indicates when the order is expected to be delivered.       (Expected format `2022-04-20T12:34:56.789Z`)      - expected_pickup_timestamp: datetime       Indicates when the order is expected to be picked up.       (Expected format `2022-04-20T12:34:56.789Z`)      - delivery_address_id: If the fulfillment type is `delivery`, you may provide the ID of the customer address where the order is to be delivered. The ID must be an existing address that corresponds to the customer for the order.      - delivery_address: Alternatively, you can provide the full delivery address for the order. Only one of `delivery_address_id` or `delivery_address` will be respected, with preference given to `delivery_address_id`. If a valid delivery address is passed and cannot be matched against the existing addresses for the order customer, the address will be automatically created and set as the primary shipping address for the customer. If included in the request, the delivery address should include the following fields:          - address_line_1: string - REQUIRED              - address_line_1: string              - city: string - REQUIRED              - state: string - REQUIRED              - postcode: string - REQUIRED              - country: string - REQUIRED          - delivery_contact_no: For orders with `fulfillment_type` "delivery", the number provided by the customer for contact by phone for updates, if necessary      - delivery_text_contact_no: For orders with `fulfillment_type` "delivery", the number provided by the customer for contact by text/SMS for updates, if necessary      - delivery_email: For orders with `fulfillment_type` "delivery", the address provided by the customer for contact by email for updates, if necessary      - delivery_fee: number       A charge for delivery of the order.      - total_paid: number       Represents the amount a customer has paid on the order. The response field payment_status depends on this amount.      - order_lines: array - REQUIRED          - item_id: string - REQUIRED if SKU not given.              - item_variation_pk: string - REQUIRED for item variations if SKU not given.              - sku: string - REQUIRED if item_id not given.              - strain_id: string - REQUIRED for cannabis products.              - order_qty: number - Amount of this item on the order.              - unit_price: number           Price of the item. If not given the item's current price will be used.          - applied_discounts: array          - For custom discounts, provide:                  - method: string               Must be one of `dollar` or `percentage`.                      - promo_code: string               A special promotional code for the discount.                      - amount: number               When discounts are given the response will return 2 values related to the amount. The amount is the dollar or percentage set and discount_value is the actual dollar value of the discount. When the method is `dollar` the amount and discount_value should be equal.                  - For pre-configured discounts, i.e. those returned by the `GetEligibleDiscounts` endpoint, provide:                  - discount_id: number - REQUIRED               The ID of the pre-configured discount in Flourish                      - discount_name: string               The name of the pre-configured discount in Flourish                      - method: string               Must be one of `dollar` or `percentage`.                      - promo_code: string               If the Flourish discount requires a promo code, the configured promotion code for the discount.                      - amount: number               The dollar or percentage amount applied                      - approved_by: string               The email/username of the user approving/applying the discount                      - sku: string               If a line-level discount, the item SKU for the order line against which the discount will be applied"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/retail-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostRetailOrderV2() -> Dict:
    """The request and response JSON for **PostRetailOrderV2** are identical to the **PostRetailOrder** JSON.  While the `v1` endpoint supports creating retail orders with eCommerce eligible discounts applied, the `v2` endpoint enhances discount capabilities by further passing the order through Flourish's internal discounting engine, allowing for automatic application of more advanced discounts like:  - BOGOs, - single-use promo codes, - discounts that target customer groups, - customer birthday discounts, - etc."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv2/retail-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutRetailOrder() -> Dict:
    """Update a retail order by ID.  - Orders can only be updated if they are in the `Created` or `Submitted` statuses. - We do not currently support modification of order status with this endpoint.       This will fully replace the record, and all fields required in the POST must be given. Reference **PostRetailOrder** for specific behavior details and request fields."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/retail-orders/{order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostRetailOrderPayment() -> Dict:
    """Create a new payment against a retail order. Response is identical to GetRetailOrder call.  Request Fields:  - payment_type: string\ Options: Cash, Manual - amount: number\ Payment Amount. Cannot be greater than current Total Price minus Total Paid for the order. - automatic_complete: boolean\ If sent as true and the order is paid in full after processing this payment, the following steps will be taken:     - Changing order status to complete 	- Decrementing inventory 	- Syncing with state system - manual_payment_type: string\ Options: CanPay\ Required if payment type is set as Manual - reference_id: string\ Required if payment type is set as Manual. Reference ID of payment transaction."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/retail-orders/{order_id}/payment/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetEligibleDiscounts() -> Dict:
    """Get all available, e-commerce eligible retail discounts for a given facility at the current moment. If there are item inclusion rules for a given discount, those items must also be e-commerce eligible or the discount will not be returned.  Takes into account:  *   e-commerce eligibility *   limitations on availability by facility (or facility tag) *   limitations on availability by specific dates/times/days of week       **Note on date/time fields:**  *   `start_date` and `end_date` are the dates when a discount becomes/ceases to be available. One or both can be empty if those values are indefinite. *   `start_date_time` and `end_date_time` are only applicable if the corresponding `start_date` and `end_date` are populated, and they would come into play for discounts that start at, say, 9am on Memorial Day and end at 6am the next day. *   `start_time` and `end_time` are daily start and end times. e.g. a happy hour discount available from 4-6pm every day. *   All the time fields are formatted as `HH:MM` and are irrespective of timezone, so a `start_time` of `16:00` means the discount becomes available at 4pm EDT for facilities in eastern timezone, 4pm PDT for facilities in pacific, and so on."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/retail-discounts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
