
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Inbound_Purchase_Orders_mcp = FastMCP(name="Inbound_Purchase_Orders")



def GetPurchaseOrders(token: str, limit: int = "50", offset: int = "0", purchase_order_status: Literal["Created", "Receiving partial", "Receiving complete", "Closed", "Cancelled"] = "Complete", vendor_name: str = "Vendor Name", shipping_method_id: int = "1", ref_field_1: str = "ABC1", ref_field_2: str = "DEF2", ref_field_3: str = "GHI3", ref_field_4: str = "JKL4", ref_field_5: str = "MNO5", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get inbound purchase orders."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'purchase_order_status': purchase_order_status, 'vendor_name': vendor_name, 'shipping_method_id': shipping_method_id, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3, 'ref_field_4': ref_field_4, 'ref_field_5': ref_field_5, 'created_timestamp_start': created_timestamp_start, 'created_timestamp_end': created_timestamp_end, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/purchase-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetPurchaseOrder(token: str) -> Dict:
    """Get the details for a single purchase order by the given `purchase_order_id`."""
    params = {'token': token}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/purchase-orders/{purchase_order_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def CreatePurchaseOrder(token: str, purchase_order_status_id: int = " ", shipping_method_id: Literal["1", "2", "3", "4", "5", "6", "7"] = " ", vendor_id: str = " ", ref_field_1: str = " ", ref_field_2: str = " ", ref_field_3: str = " ", ref_field_4: str = " ", ref_field_5: str = " ", gross_total: float = " ", created_from_metrc_transfer: Literal["0", "1"] = " ", created_from_intercompany_transfer: Literal["0", "1"] = " ", expected_timestamp: datetime = " ", purchase_order_lines: object = " ", po_status_id: int = " ", total_taxes: float = " ", total_cost: float = " ", total_price: float = " ") -> Dict:
    """Create an inbound purchase order"""
    params = {'token': token, 'purchase_order_status_id': purchase_order_status_id, 'shipping_method_id': shipping_method_id, 'vendor_id': vendor_id, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3, 'ref_field_4': ref_field_4, 'ref_field_5': ref_field_5, 'gross_total': gross_total, 'created_from_metrc_transfer': created_from_metrc_transfer, 'created_from_intercompany_transfer': created_from_intercompany_transfer, 'expected_timestamp': expected_timestamp, 'purchase_order_lines': purchase_order_lines, 'po_status_id': po_status_id, 'total_taxes': total_taxes, 'total_cost': total_cost, 'total_price': total_price}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/purchase-orders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def EditPurchaseOrder(token: str, purchase_order_id, purchase_order_status_id: Optional[int] = " ", shipping_method_id: Optional[int] = " ", vendor_id: str = " ", ref_field_1: Optional[str] = " ", ref_field_2: Optional[str] = " ", ref_field_3: Optional[str] = " ", ref_field_4: Optional[str] = " ", ref_field_5: Optional[str] = " ", gross_total: Optional[float] = " ", purchase_order_lines: object = " ", po_status_id: Optional[int] = " ", total_taxes: Optional[float] = " ", total_cost: Optional[float] = " ", total_price: Optional[float] = " ", notes: Optional[str] = " ", created_from_metrc_transfer: Optional[int] = " ", created_from_intercompany_transfer: Optional[int] = " ", receive_completed_by: Optional[str] = " ") -> Dict:
    """This endpoint updates an existing inbound purchase order. It requires a FacilityID header and accepts various fields in the request body to update the purchase order details."""
    params = {'token': token, 'purchase_order_id': purchase_order_id, 'purchase_order_status_id': purchase_order_status_id, 'shipping_method_id': shipping_method_id, 'vendor_id': vendor_id, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3, 'ref_field_4': ref_field_4, 'ref_field_5': ref_field_5, 'gross_total': gross_total, 'purchase_order_lines': purchase_order_lines, 'po_status_id': po_status_id, 'total_taxes': total_taxes, 'total_cost': total_cost, 'total_price': total_price, 'notes': notes, 'created_from_metrc_transfer': created_from_metrc_transfer, 'created_from_intercompany_transfer': created_from_intercompany_transfer, 'receive_completed_by': receive_completed_by}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/purchase-orders/{{purchase_order_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
