
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Shipments_mcp = FastMCP(name="Shipments")



def GetShipments(shipment_id: str = "20180830-003", shipment_id: str = "20180910-001", shipment_status_id: int = "10", limit: int = "60", offset: int = "0", vehicle_id: str = "80694a13", vehicle_id: str = "fd86ae68") -> Dict:
    """Get shipments.  Required Headers:   **FacilityID**  | Param | Example | Description | | --- | --- | --- | | limit | 50 |  | | offset | 0 |  | | shipment_status_id | 10 | Status of the shipment.  <br>  <br>Options: 10(Created), 20(Orders assigned), 30(Manifest printed), 40(Shipped), 99(Cancelled).  <br>  <br>type: \[int\] | | shipment_id | 0001234 | ID of a shipment. To specify multiple shipment IDs, multiple `shipment_id` parameters are required. Ex: `shipment_id=123&shipment_id=abc`.  <br>  <br>type: \[string\] | | vehicle_id | 0001234 | ID of a vehicle. To specify multiple vehicle IDs, multiple `vehicle_id` parameters are required. Ex: `vehicle_id=123&vehicle_id=abc`.  <br>  <br>type: \[string\] | | driver_id | 0001234 | ID of a driver.  <br>  <br>type: \[string\] |"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/shipments/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            shipment_id: str = "20180830-003", shipment_id: str = "20180910-001", shipment_status_id: int = "10", limit: int = "60", offset: int = "0", vehicle_id: str = "80694a13", vehicle_id: str = "fd86ae68"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetShipment() -> Dict:
    """Endpoint to retrieve a single shipment. Pass the shipment ID in the URL as the only parameter like:  `v1/shipments/20180216-001`"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/shipments/{shipment_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostShipment() -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/shipments/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutShipment() -> Dict:
    """"""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/shipments/20220119-003/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
