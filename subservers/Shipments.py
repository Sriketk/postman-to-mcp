
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Shipments_mcp = FastMCP(name="Shipments")



def GetShipments(token: str, shipment_id: str = "20180830-003", shipment_id: str = "20180910-001", shipment_status_id: int = "10", limit: int = "60", offset: int = "0", vehicle_id: str = "80694a13", vehicle_id: str = "fd86ae68") -> Dict:
    """Get shipments.  Required Headers:   **FacilityID**  | Param | Example | Description | | --- | --- | --- | | limit | 50 |  | | offset | 0 |  | | shipment_status_id | 10 | Status of the shipment.  <br>  <br>Options: 10(Created), 20(Orders assigned), 30(Manifest printed), 40(Shipped), 99(Cancelled).  <br>  <br>type: \[int\] | | shipment_id | 0001234 | ID of a shipment. To specify multiple shipment IDs, multiple `shipment_id` parameters are required. Ex: `shipment_id=123&shipment_id=abc`.  <br>  <br>type: \[string\] | | vehicle_id | 0001234 | ID of a vehicle. To specify multiple vehicle IDs, multiple `vehicle_id` parameters are required. Ex: `vehicle_id=123&vehicle_id=abc`.  <br>  <br>type: \[string\] | | driver_id | 0001234 | ID of a driver.  <br>  <br>type: \[string\] |"""
    params = {'token': token, 'shipment_id': shipment_id, 'shipment_id': shipment_id, 'shipment_status_id': shipment_status_id, 'limit': limit, 'offset': offset, 'vehicle_id': vehicle_id, 'vehicle_id': vehicle_id}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/shipments/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetShipment(token: str) -> Dict:
    """Endpoint to retrieve a single shipment. Pass the shipment ID in the URL as the only parameter like:  `v1/shipments/20180216-001`"""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/shipments/{shipment_id}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostShipment(token: str, vehicle_id: str = " ", shipment_timestamp: datetime = " ", planned_route: str = " ", drivers: List[str] = " ", stops: object = " ", stops.estimated_arrival_time: Optional[datetime] = "None", stops.orders: List[str] = " ") -> Dict:
    """This endpoint appears to be for submitting shipment or delivery information. It includes details about the vehicle, shipment time, planned route, drivers, and stops with associated orders."""
    params = {'token': token, 'vehicle_id': vehicle_id, 'shipment_timestamp': shipment_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders}
    body = {'vehicle_id': vehicle_id, 'shipment_timestamp': shipment_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/shipments/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutShipment(token: str, vehicle_id: str = " ", shipment_timestamp: datetime = " ", planned_route: str = " ", drivers: List[str] = " ", stops: List[str] = " ", stops.estimated_arrival_time: Optional[datetime] = "None", stops.orders: List[str] = " ", notes: Optional[List[str]] = " ", notes.note: str = " ", notes.subject: Optional[str] = " ") -> Dict:
    """This endpoint appears to be for creating or updating a shipment or delivery route. It includes details about the vehicle, timestamp, planned route, drivers, stops, and additional notes."""
    params = {'token': token, 'vehicle_id': vehicle_id, 'shipment_timestamp': shipment_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders, 'notes': notes, 'notes.note': notes.note, 'notes.subject': notes.subject}
    body = {'vehicle_id': vehicle_id, 'shipment_timestamp': shipment_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders, 'notes': notes, 'notes.note': notes.note, 'notes.subject': notes.subject}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/shipments/20220119-003/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()
