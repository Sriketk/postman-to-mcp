
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Items_mcp = FastMCP(name="Items")



def GetItem(item_id) -> Dict:
    """Get an item by a given `item_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/items/{{item_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetItems(limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Cannabis", item_class: str = "Plants", item_category: None = "Concentrate", item_name: str = "ItemX", strain_required: bool = "True", strain_name: str = "OG Kush", retail_display_name: str = "ItemY", uom: Literal["ea", "g", "kg", "mg", "oz", "lb", "t", "in", "cm", "ml", "l", "fl oz", "gal", "pt", "qt"] = "g", sellable: bool = "True", is_medical: bool = "False", active: bool = "True", is_external: bool = "True", brand_name: str = "My Brand", brand_id: int = "420", last_updated_timestamp_start: str = "2022-08-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", ecommerce_active: bool = "False", ecommerce_item_name: str = "Full Spectrum Cart 1g", ecommerce_category_name: str = "Vapes", ecommerce_sub_category_name: str = "Full Spectrum Carts", item_strain_type_name: Optional[Literal["Sativa", "Indica", "Hybrid", "CBD", "THC"]] = "Sativa", strain_type_name: Optional[Literal["Sativa", "Indica", "Hybrid", "CBD", "THC"]] = "Hybrid") -> Dict:
    """Get items based on query parameters."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/items/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", inventory_type: Literal["Cannabis", "Raw Materials", "Supplies"] = "Cannabis", item_class: str = "Plants", item_category: None = "Concentrate", item_name: str = "ItemX", strain_required: bool = "True", strain_name: str = "OG Kush", retail_display_name: str = "ItemY", uom: Literal["ea", "g", "kg", "mg", "oz", "lb", "t", "in", "cm", "ml", "l", "fl oz", "gal", "pt", "qt"] = "g", sellable: bool = "True", is_medical: bool = "False", active: bool = "True", is_external: bool = "True", brand_name: str = "My Brand", brand_id: int = "420", last_updated_timestamp_start: str = "2022-08-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", ecommerce_active: bool = "False", ecommerce_item_name: str = "Full Spectrum Cart 1g", ecommerce_category_name: str = "Vapes", ecommerce_sub_category_name: str = "Full Spectrum Carts", item_strain_type_name: Optional[Literal["Sativa", "Indica", "Hybrid", "CBD", "THC"]] = "Sativa", strain_type_name: Optional[Literal["Sativa", "Indica", "Hybrid", "CBD", "THC"]] = "Hybrid"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetItemClasses(limit: int = "50", offset: int = "0") -> Dict:
    """Get all available item classifications."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/itemclasses/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetItemCategories(limit: int = "50", offset: int = "0") -> Dict:
    """Get all item categories."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/itemcategories/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetItemVariation() -> Dict:
    """Get an item variation for the given `item_variation_pk`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/itemvariations/:item_variation_pk/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetItemVariationsForItem(limit: int = "50", offset: int = "0") -> Dict:
    """Get all active item variations for a particular item."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/items/:item_id/itemvariations/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetItemArt(expire: str = "8h") -> Dict:
    """Get links for the various images that can be associated with a given item.  Will return a link to the image with an expiration for:  - Product      - Label      - Packaging       Expect status code `204` if the item has no art."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/items/:item_id/art/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            expire: str = "8h"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetBom(bom) -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/{{bom}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetBoms(item_id: int = "206", nickname: str = "FEAT1-9611-Test", is_active: bool = "True", is_primary: bool = "False", item_name: str = "Packaged Diva Eighths", effective_date_start: str = "2022-01-02T15:04:05.000Z", effective_date_end: str = "2024-01-02T15:04:05.000Z") -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            item_id: int = "206", nickname: str = "FEAT1-9611-Test", is_active: bool = "True", is_primary: bool = "False", item_name: str = "Packaged Diva Eighths", effective_date_start: str = "2022-01-02T15:04:05.000Z", effective_date_end: str = "2024-01-02T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostBom() -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutBom(bom_id) -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/{{bom_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostBomDtl(bom_id) -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/{{bom_id}}/details/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostBomDtlW/Category(bom_id) -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/{{bom_id}}/details/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutBomDtlW/Category(bom_id, bom_detail_id) -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/{{bom_id}}/details/{{bom_detail_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def DeleteBomDtl(bom_id, bom_dtl_id) -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/boms/{{bom_id}}/details/{{bom_dtl_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
