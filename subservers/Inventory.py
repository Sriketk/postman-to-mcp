
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Inventory_mcp = FastMCP(name="Inventory")



def GetInventoryTypes(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get all inventory types."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/inventorytypes/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetInventory(token: str, limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Supplies", item_class: Literal["string"] = "Plants", item_category: Literal["Electronics", "Clothing", "Home & Garden", "Books", "Toys", "Sports & Outdoors"] = "Concentrate", item_id: int = "45734", item_name: str = "ItemX", item_variation_id: int = "123456", variation_name: str = "ItemX_10Pack", strain_id: str = "1a2b3c", strain_name: str = "OG Kush", item_retail_display_name: str = "ItemY", variation_retail_display_name: str = "ItemY_10Pack", lot_number: str = "SOME LOT NUMBER", uom: str = "Gram", sku: str = "1.2.3.4", package_id: str = "1a2b3c", package_status: Literal["Created", "Assigned to order", "Consumed", "Cancelled"] = "Created", include_consumed: Optional[bool] = "True", include_shipped: Optional[bool] = "True", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", has_available_qty: bool = "True", is_external: bool = "True", is_sample: bool = "True", include_origin_harvest: Optional[bool] = "False") -> Dict:
    """Get current inventory for a single facility. `inventory_id` is the unique identifier for the inventory record returned. Currently, if the record is of a package that was shipped, this field will be `null`. Shipped packages are included in this endpoint if the `package_status` query parameter is shipped or if `include_shipped` query parameter is defined as `true`."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'inventory_type': inventory_type, 'item_class': item_class, 'item_category': item_category, 'item_id': item_id, 'item_name': item_name, 'item_variation_id': item_variation_id, 'variation_name': variation_name, 'strain_id': strain_id, 'strain_name': strain_name, 'item_retail_display_name': item_retail_display_name, 'variation_retail_display_name': variation_retail_display_name, 'lot_number': lot_number, 'uom': uom, 'sku': sku, 'package_id': package_id, 'package_status': package_status, 'include_consumed': include_consumed, 'include_shipped': include_shipped, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end, 'has_available_qty': has_available_qty, 'is_external': is_external, 'is_sample': is_sample, 'include_origin_harvest': include_origin_harvest}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/inventory/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetInventorySummary(token: str, limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Raw Materials", inventory_type: str = "Cannabis", item_class: Literal["string"] = "Buds", item_category: Literal["Electronics", "Clothing", "Home & Garden", "Books", "Toys", "Sports & Outdoors"] = "Flower", item_id: int = "151", item_name: str = "CR Packaging Vaporizer Pen Tubes", item_variation_id: int = "456", variation_name: str = "Some Variation Name", strain_id: str = "abc123", strain_name: str = "G13 Haze", item_retail_display_name: str = "Ice Cream", variation_retail_display_name: str = "Ponderosa", lot_number: str = "SOME LOT NUMBER", uom: str = "Gram", sku: str = "2.8.34.75.0", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", include_all_items: bool = "True", group_by: Literal["item_name", "lot_number"] = "lot_number", has_available_qty: bool = "True", is_external: bool = "True") -> Dict:
    """Get summary of inventory quantities for items from all packages. This includes quantity values for:  *   Available *   Non-available *   Sellable"""
    params = {'token': token, 'limit': limit, 'offset': offset, 'inventory_type': inventory_type, 'inventory_type': inventory_type, 'item_class': item_class, 'item_category': item_category, 'item_id': item_id, 'item_name': item_name, 'item_variation_id': item_variation_id, 'variation_name': variation_name, 'strain_id': strain_id, 'strain_name': strain_name, 'item_retail_display_name': item_retail_display_name, 'variation_retail_display_name': variation_retail_display_name, 'lot_number': lot_number, 'uom': uom, 'sku': sku, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end, 'include_all_items': include_all_items, 'group_by': group_by, 'has_available_qty': has_available_qty, 'is_external': is_external}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/inventory/summary/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetInventoryAdjustments(token: str, limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Raw Materials", inventory_type: str = "Cannabis", item_class: Literal["string"] = "Buds", item_category: str = "Bulk%20Flower", item_id: int = "712", item_variation_id: int = "456", variation_name: str = "Some Variation Name", strain_id: str = "abc123", strain_name: str = "Afghan Kush", retail_display_name: str = "Afghan Kush - Dry Cannabis", lot_number: str = "SN230703RE1-0707", uom: Literal["item", "UOM"] = "g", sku: str = "FLO-BUD-FT-PRE-GFU", created_timestamp_start: str = "2025-01-01T00:00:00.000Z", created_timestamp_end: str = "2025-01-02T23:59:59.999Z", package_id: str = "1A4FF0300000259000005315", adjustment_reason_code: str = "Compliance System Discrepancy", item_name: str = "Some Item") -> Dict:
    """Get summary of inventory quantities for items from all packages. This includes quantity values for:  *   Available *   Non-available *   Sellable"""
    params = {'token': token, 'limit': limit, 'offset': offset, 'inventory_type': inventory_type, 'inventory_type': inventory_type, 'item_class': item_class, 'item_category': item_category, 'item_id': item_id, 'item_variation_id': item_variation_id, 'variation_name': variation_name, 'strain_id': strain_id, 'strain_name': strain_name, 'retail_display_name': retail_display_name, 'lot_number': lot_number, 'uom': uom, 'sku': sku, 'created_timestamp_start': created_timestamp_start, 'created_timestamp_end': created_timestamp_end, 'package_id': package_id, 'adjustment_reason_code': adjustment_reason_code, 'item_name': item_name}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/inventory/adjustments/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
