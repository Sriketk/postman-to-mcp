
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Deliveries_mcp = FastMCP(name="Deliveries")



def GetDeliveries(limit: int = "50", offset: int = "0", delivery_id: str = "{{delivery_id}}", delivery_id: str = "20180910-001", delivery_status_id: int = "10", vehicle_id: str = "80694a13", vehicle_id: str = "fd86ae68") -> Dict:
    """Get deliveries.  Required Headers:   **FacilityID**  | Param | Example | Description | | --- | --- | --- | | limit | 50 |  | | offset | 0 |  | | delivery_status_id | 10 | Status of the delivery.  <br>  <br>Options: 10(Created), 20(Orders assigned), 30(Manifest printed), 40(Shipped), 99(Cancelled).  <br>  <br>type: \[int\] | | delivery_id | 0001234 | ID of a delivery. To specify multiple delivery IDs, multiple `delivery_id` parameters are required. Ex: `delivery_id=123&delivery_id=abc`.  <br>  <br>type: \[string\] | | vehicle_id | 0001234 | ID of a vehicle. To specify multiple vehicle IDs, multiple `vehicle_id` parameters are required. Ex: `vehicle_id=123&vehicle_id=abc`.  <br>  <br>type: \[string\] | | driver_id | 0001234 | ID of a driver.  <br>  <br>type: \[string\] |"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/deliveries/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", delivery_id: str = "{{delivery_id}}", delivery_id: str = "20180910-001", delivery_status_id: int = "10", vehicle_id: str = "80694a13", vehicle_id: str = "fd86ae68"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetDelivery(delivery_id) -> Dict:
    """Endpoint to retrieve a single delivery. Pass the delivery ID in the URL as the only parameter like:  `v1/deliveries/20180216-001`"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/deliveries/{{delivery_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostDelivery() -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/deliveries/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutDelivery(delivery_id) -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/deliveries/{{delivery_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
