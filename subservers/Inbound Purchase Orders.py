
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Inbound Purchase Orders_mcp = FastMCP(name="Inbound Purchase Orders")



def GetPurchaseOrders(limit: int = "50", offset: int = "0", purchase_order_status: Literal["Created", "Receiving partial", "Receiving complete", "Closed", "Cancelled"] = "Complete", vendor_name: str = "Vendor Name", shipping_method_id: int = "1", ref_field_1: str = "ABC1", ref_field_2: str = "DEF2", ref_field_3: str = "GHI3", ref_field_4: str = "JKL4", ref_field_5: str = "MNO5", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get inbound purchase orders."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/purchase-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", purchase_order_status: Literal["Created", "Receiving partial", "Receiving complete", "Closed", "Cancelled"] = "Complete", vendor_name: str = "Vendor Name", shipping_method_id: int = "1", ref_field_1: str = "ABC1", ref_field_2: str = "DEF2", ref_field_3: str = "GHI3", ref_field_4: str = "JKL4", ref_field_5: str = "MNO5", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetPurchaseOrder() -> Dict:
    """Get the details for a single purchase order by the given `purchase_order_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/purchase-orders/{purchase_order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def CreatePurchaseOrder() -> Dict:
    """Create an inbound purchase orders.  Required Headers:   **FacilityID**  | Field | Example | Description | | --- | --- | --- | | purchase_order_status_id | 10 | Status of the purchase order.  <br>  <br>type: \[int\] | | shipping_method_id | 1 | Method of shipping the purchase order.  <br>  <br>Options:  <br>  <br>1 - USPS  <br>2 - UPS  <br>3 - FedEx  <br>4 - LTL  <br>5 - Local Delivery  <br>6 - Pickup  <br>7 Other  <br>  <br>type: \[int\] | | vendor_id | 0001234 | ID of a vendor.  <br>  <br>type: \[string\] | | ref_field_1 | ABC1 | Ref Field 1.  <br>  <br>type: \[string\] | | ref_field_2 | ABC1 | Ref Field 2.  <br>  <br>type: \[string\] | | ref_field_3 | ABC1 | Ref Field 3.  <br>  <br>type: \[string\] | | ref_field_4 | ABC1 | Ref Field 4.  <br>  <br>type: \[string\] | | ref_field_5 | ABC1 | Ref Field 5.  <br>  <br>type: \[string\] | | gross_total | 20.0 | Gross total value.  <br>  <br>type: \[float\] | | created_from_metrc_transfer | 1 or 0 | Whether purchase order was created from METRC transfer. | |   <br>  <br>type: \[int\] |  |  | | created_from_metrc_transfer | 1 or 0 | Whether purchase order was created from Intercompany transfer.  <br>  <br>type: \[int\] | | expected_timestamp | 2020-01-02T15:04:05.000Z | Expected date/time of purchase order.  <br>  <br>type: \[datetime\] | | purchase_order_lines | \[Order Items\] | Orders information with purchase order. |"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/purchase-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def EditPurchaseOrder(purchase_order_id) -> Dict:
    """Update an existing inbound purchase order.   Required Headers: **FacilityID**  |Field|Example|Description| |---|---|---| |purchase_order_status_id|10|Status of the purchase order.<br><br>type: [int]| |shipping_method_id|10|Method of shipping the purchase order.<br><br>type: [int]| |vendor_id|0001234|ID of a vendor.<br><br>type: [string]| |ref_field_1|ABC1|Ref Field 1.<br><br>type: [string]| |ref_field_2|ABC1|Ref Field 2.<br><br>type: [string]| |ref_field_3|ABC1|Ref Field 3.<br><br>type: [string]| |ref_field_4|ABC1|Ref Field 4.<br><br>type: [string]| |ref_field_5|ABC1|Ref Field 5.<br><br>type: [string]| |gross_total|20.0|Gross total value.<br><br>type: [float]| |purchase_order_lines|[Order Items]|Orders information with purchase order.|"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/purchase-orders/{{purchase_order_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
