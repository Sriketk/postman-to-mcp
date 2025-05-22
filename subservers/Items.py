
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Items_mcp = FastMCP(name="Items")



def GetItem(token: str, item_id) -> Dict:
    """Get an item by a given `item_id`."""
    params = {'token': token, 'item_id': item_id}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/items/{{item_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetItems(token: str, limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Cannabis", item_class: str = "Plants", item_category: Literal["Electronics", "Clothing", "Home & Garden", "Books", "Toys", "Sports & Outdoors"] = "Concentrate", item_name: str = "ItemX", strain_required: bool = "True", strain_name: str = "OG Kush", retail_display_name: str = "ItemY", uom: Literal["ea", "g", "kg", "mg", "oz", "lb", "t", "in", "cm", "ml", "l", "fl oz", "gal", "pt", "qt"] = "g", sellable: bool = "True", is_medical: bool = "False", active: bool = "True", is_external: bool = "True", brand_name: str = "My Brand", brand_id: int = "420", last_updated_timestamp_start: str = "2022-08-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", ecommerce_active: bool = "False", ecommerce_item_name: str = "Full Spectrum Cart 1g", ecommerce_category_name: str = "Vapes", ecommerce_sub_category_name: str = "Full Spectrum Carts", item_strain_type_name: Optional[Literal["Sativa", "Indica", "Hybrid", "CBD", "THC"]] = "Sativa", strain_type_name: Optional[Literal["Sativa", "Indica", "Hybrid", "CBD", "THC"]] = "Hybrid") -> Dict:
    """Get items based on query parameters."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'inventory_type': inventory_type, 'item_class': item_class, 'item_category': item_category, 'item_name': item_name, 'strain_required': strain_required, 'strain_name': strain_name, 'retail_display_name': retail_display_name, 'uom': uom, 'sellable': sellable, 'is_medical': is_medical, 'active': active, 'is_external': is_external, 'brand_name': brand_name, 'brand_id': brand_id, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end, 'ecommerce_active': ecommerce_active, 'ecommerce_item_name': ecommerce_item_name, 'ecommerce_category_name': ecommerce_category_name, 'ecommerce_sub_category_name': ecommerce_sub_category_name, 'item_strain_type_name': item_strain_type_name, 'strain_type_name': strain_type_name}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/items/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetItemClasses(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get all available item classifications."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/itemclasses/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetItemCategories(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get all item categories."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/itemcategories/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetItemVariation(token: str) -> Dict:
    """Get an item variation for the given `item_variation_pk`."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/itemvariations/:item_variation_pk/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetItemVariationsForItem(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get all active item variations for a particular item."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/items/:item_id/itemvariations/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetItemArt(token: str, expire: str = "8h") -> Dict:
    """Get links for the various images that can be associated with a given item.  Will return a link to the image with an expiration for:  - Product      - Label      - Packaging       Expect status code `204` if the item has no art."""
    params = {'token': token, 'expire': expire}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/items/:item_id/art/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetBom(token: str, bom) -> Dict:
    """"""
    params = {'token': token, 'bom': bom}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/boms/{{bom}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetBoms(token: str, item_id: int = "206", nickname: str = "FEAT1-9611-Test", is_active: bool = "True", is_primary: bool = "False", item_name: str = "Packaged Diva Eighths", effective_date_start: str = "2022-01-02T15:04:05.000Z", effective_date_end: str = "2024-01-02T15:04:05.000Z") -> Dict:
    """"""
    params = {'token': token, 'item_id': item_id, 'nickname': nickname, 'is_active': is_active, 'is_primary': is_primary, 'item_name': item_name, 'effective_date_start': effective_date_start, 'effective_date_end': effective_date_end}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/boms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostBom(token: str, active: Literal["0", "1"] = " ", effective_date: datetime = " ", is_primary: Literal["0", "1"] = " ", item_id: int = " ", nickname: str = " ", qty_to_create: int = " ", work_instructions: str = " ") -> Dict:
    """This endpoint appears to be related to creating or updating a Bill of Materials (BOM) item. It includes fields for activation status, effective date, primary status, item identification, nickname, quantity to create, and work instructions."""
    params = {'token': token, 'active': active, 'effective_date': effective_date, 'is_primary': is_primary, 'item_id': item_id, 'nickname': nickname, 'qty_to_create': qty_to_create, 'work_instructions': work_instructions}
    body = {'active': active, 'effective_date': effective_date, 'is_primary': is_primary, 'item_id': item_id, 'nickname': nickname, 'qty_to_create': qty_to_create, 'work_instructions': work_instructions}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/boms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutBom(token: str, bom_id, active: Literal["0", "1"] = " ", effective_date: datetime = " ", is_primary: Literal["0", "1"] = " ", item_id: int = " ", nickname: str = " ", qty_to_create: int = " ", work_instructions: str = " ") -> Dict:
    """This endpoint appears to be related to updating or creating a Bill of Materials (BOM) item. It includes fields for activation status, effective date, primary status, item identification, nickname, quantity to create, and work instructions."""
    params = {'token': token, 'bom_id': bom_id, 'active': active, 'effective_date': effective_date, 'is_primary': is_primary, 'item_id': item_id, 'nickname': nickname, 'qty_to_create': qty_to_create, 'work_instructions': work_instructions}
    body = {'active': active, 'effective_date': effective_date, 'is_primary': is_primary, 'item_id': item_id, 'nickname': nickname, 'qty_to_create': qty_to_create, 'work_instructions': work_instructions}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/boms/{{bom_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PostBomDtl(token: str, bom_id, qty: int = "1", qty_uom_id: int = " ", notes: str = " ", item_id: int = " ") -> Dict:
    """This endpoint appears to be for adding or updating a Bill of Materials (BOM) detail item. It allows specifying the quantity, unit of measure, notes, and the item ID for the BOM detail."""
    params = {'token': token, 'bom_id': bom_id, 'qty': qty, 'qty_uom_id': qty_uom_id, 'notes': notes, 'item_id': item_id}
    body = {'qty': qty, 'qty_uom_id': qty_uom_id, 'notes': notes, 'item_id': item_id}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/boms/{{bom_id}}/details/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PostBomDtlW/Category(token: str, bom_id, qty: int = " ", qty_uom_id: int = " ", notes: str = " ", item_category_id: int = " ") -> Dict:
    """This endpoint appears to be related to creating or updating a Bill of Materials (BOM) detail. It includes quantity, unit of measure, notes, and item category information."""
    params = {'token': token, 'bom_id': bom_id, 'qty': qty, 'qty_uom_id': qty_uom_id, 'notes': notes, 'item_category_id': item_category_id}
    body = {'qty': qty, 'qty_uom_id': qty_uom_id, 'notes': notes, 'item_category_id': item_category_id}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/boms/{{bom_id}}/details/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutBomDtlW/Category(token: str, bom_id, bom_detail_id, qty: int = "1", qty_uom_id: int = "18", notes: str = " ", item_category_id: int = " ") -> Dict:
    """This endpoint appears to be related to updating or creating a Bill of Materials (BOM) detail. It includes quantity, unit of measure, notes, and an item category."""
    params = {'token': token, 'bom_id': bom_id, 'bom_detail_id': bom_detail_id, 'qty': qty, 'qty_uom_id': qty_uom_id, 'notes': notes, 'item_category_id': item_category_id}
    body = {'qty': qty, 'qty_uom_id': qty_uom_id, 'notes': notes, 'item_category_id': item_category_id}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/boms/{{bom_id}}/details/{{bom_detail_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def DeleteBomDtl(token: str, bom_id, bom_dtl_id) -> Dict:
    """"""
    params = {'token': token, 'bom_id': bom_id, 'bom_dtl_id': bom_dtl_id}
    body = {}
    response = requests.delete(
        f"https://app.flourishsoftware.com/external/api/v1/boms/{{bom_id}}/details/{{bom_dtl_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },

    )
    response.raise_for_status()
    return response.json()
