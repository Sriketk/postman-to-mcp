
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Inventory_mcp = FastMCP(name="Inventory")



def GetInventoryTypes(limit: int = "50", offset: int = "0") -> Dict:
    """Get all inventory types."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/inventorytypes/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetInventory(limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Supplies", item_class: str = "Plants", item_category: None = "Concentrate", item_id: int = "45734", item_name: str = "ItemX", item_variation_id: int = "123456", variation_name: str = "ItemX_10Pack", strain_id: str = "1a2b3c", strain_name: str = "OG Kush", item_retail_display_name: str = "ItemY", variation_retail_display_name: str = "ItemY_10Pack", lot_number: str = "SOME LOT NUMBER", uom: str = "Gram", sku: str = "1.2.3.4", package_id: str = "1a2b3c", package_status: Literal["Created", "Assigned to order", "Consumed", "Cancelled"] = "Created", include_consumed: Optional[bool] = "True", include_shipped: Optional[bool] = "True", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", has_available_qty: bool = "True", is_external: bool = "True", is_sample: bool = "True", include_origin_harvest: bool = "False") -> Dict:
    """Get current inventory for a single facility. `inventory_id` is the unique identifier for the inventory record returned. Currently, if the record is of a package that was shipped, this field will be `null`. Shipped packages are included in this endpoint if the `package_status` query parameter is shipped or if `include_shipped` query parameter is defined as `true`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/inventory/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Supplies", item_class: str = "Plants", item_category: None = "Concentrate", item_id: int = "45734", item_name: str = "ItemX", item_variation_id: int = "123456", variation_name: str = "ItemX_10Pack", strain_id: str = "1a2b3c", strain_name: str = "OG Kush", item_retail_display_name: str = "ItemY", variation_retail_display_name: str = "ItemY_10Pack", lot_number: str = "SOME LOT NUMBER", uom: str = "Gram", sku: str = "1.2.3.4", package_id: str = "1a2b3c", package_status: Literal["Created", "Assigned to order", "Consumed", "Cancelled"] = "Created", include_consumed: Optional[bool] = "True", include_shipped: Optional[bool] = "True", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", has_available_qty: bool = "True", is_external: bool = "True", is_sample: bool = "True", include_origin_harvest: bool = "False"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetInventorySummary(limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Raw Materials", inventory_type: str = "Cannabis", item_class: str = "Buds", item_category: None = "Flower", item_id: int = "151", item_name: str = "CR Packaging Vaporizer Pen Tubes", item_variation_id: int = "456", variation_name: str = "Some Variation Name", strain_id: str = "abc123", strain_name: str = "G13 Haze", item_retail_display_name: str = "Ice Cream", variation_retail_display_name: str = "Ponderosa", lot_number: str = "SOME LOT NUMBER", uom: str = "Gram", sku: str = "2.8.34.75.0", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", include_all_items: bool = "True", group_by: Literal["item_name", "lot_number"] = "lot_number", has_available_qty: bool = "True", is_external: bool = "True") -> Dict:
    """Get summary of inventory quantities for items from all packages. This includes quantity values for:  *   Available *   Non-available *   Sellable"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/inventory/summary/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Raw Materials", inventory_type: str = "Cannabis", item_class: str = "Buds", item_category: None = "Flower", item_id: int = "151", item_name: str = "CR Packaging Vaporizer Pen Tubes", item_variation_id: int = "456", variation_name: str = "Some Variation Name", strain_id: str = "abc123", strain_name: str = "G13 Haze", item_retail_display_name: str = "Ice Cream", variation_retail_display_name: str = "Ponderosa", lot_number: str = "SOME LOT NUMBER", uom: str = "Gram", sku: str = "2.8.34.75.0", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", include_all_items: bool = "True", group_by: Literal["item_name", "lot_number"] = "lot_number", has_available_qty: bool = "True", is_external: bool = "True"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetInventoryAdjustments(limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Raw Materials", inventory_type: str = "Cannabis", item_class: str = "Buds", item_category: str = "Bulk%20Flower", item_id: int = "712", item_variation_id: int = "456", variation_name: str = "Some Variation Name", strain_id: str = "abc123", strain_name: str = "Afghan Kush", retail_display_name: str = "Afghan Kush - Dry Cannabis", lot_number: str = "SN230703RE1-0707", uom: str = "g", sku: str = "FLO-BUD-FT-PRE-GFU", created_timestamp_start: str = "2025-01-01T00:00:00.000Z", created_timestamp_end: str = "2025-01-02T23:59:59.999Z", package_id: str = "1A4FF0300000259000005315", adjustment_reason_code: str = "Compliance System Discrepancy", item_name: str = "Some Item") -> Dict:
    """Get summary of inventory quantities for items from all packages. This includes quantity values for:  *   Available *   Non-available *   Sellable"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/inventory/adjustments/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Raw Materials", inventory_type: str = "Cannabis", item_class: str = "Buds", item_category: str = "Bulk%20Flower", item_id: int = "712", item_variation_id: int = "456", variation_name: str = "Some Variation Name", strain_id: str = "abc123", strain_name: str = "Afghan Kush", retail_display_name: str = "Afghan Kush - Dry Cannabis", lot_number: str = "SN230703RE1-0707", uom: str = "g", sku: str = "FLO-BUD-FT-PRE-GFU", created_timestamp_start: str = "2025-01-01T00:00:00.000Z", created_timestamp_end: str = "2025-01-02T23:59:59.999Z", package_id: str = "1A4FF0300000259000005315", adjustment_reason_code: str = "Compliance System Discrepancy", item_name: str = "Some Item"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
