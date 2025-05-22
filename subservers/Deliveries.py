
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Deliveries_mcp = FastMCP(name="Deliveries")



def GetDeliveries(token: str, limit: int = "50", offset: int = "0", delivery_id: str = "{{delivery_id}}", delivery_id: str = "20180910-001", delivery_status_id: int = "10", vehicle_id: str = "80694a13", vehicle_id: str = "fd86ae68") -> Dict:
    """Get deliveries.  Required Headers:   **FacilityID**  | Param | Example | Description | | --- | --- | --- | | limit | 50 |  | | offset | 0 |  | | delivery_status_id | 10 | Status of the delivery.  <br>  <br>Options: 10(Created), 20(Orders assigned), 30(Manifest printed), 40(Shipped), 99(Cancelled).  <br>  <br>type: \[int\] | | delivery_id | 0001234 | ID of a delivery. To specify multiple delivery IDs, multiple `delivery_id` parameters are required. Ex: `delivery_id=123&delivery_id=abc`.  <br>  <br>type: \[string\] | | vehicle_id | 0001234 | ID of a vehicle. To specify multiple vehicle IDs, multiple `vehicle_id` parameters are required. Ex: `vehicle_id=123&vehicle_id=abc`.  <br>  <br>type: \[string\] | | driver_id | 0001234 | ID of a driver.  <br>  <br>type: \[string\] |"""
    params = {'token': token, 'limit': limit, 'offset': offset, 'delivery_id': delivery_id, 'delivery_id': delivery_id, 'delivery_status_id': delivery_status_id, 'vehicle_id': vehicle_id, 'vehicle_id': vehicle_id}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/deliveries/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetDelivery(token: str, delivery_id) -> Dict:
    """Endpoint to retrieve a single delivery. Pass the delivery ID in the URL as the only parameter like:  `v1/deliveries/20180216-001`"""
    params = {'token': token, 'delivery_id': delivery_id}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/deliveries/{{delivery_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostDelivery(token: str, vehicle_id: str = " ", delivery_timestamp: datetime = " ", planned_route: str = " ", drivers: List[str] = " ", stops: List[str] = " ", stops.estimated_arrival_time: Optional[datetime] = " ", stops.orders: List[str] = " ") -> Dict:
    """This endpoint appears to be for submitting delivery route information for a vehicle. It includes details about the vehicle, delivery timestamp, planned route, assigned drivers, and stops with associated orders."""
    params = {'token': token, 'vehicle_id': vehicle_id, 'delivery_timestamp': delivery_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders}
    body = {'vehicle_id': vehicle_id, 'delivery_timestamp': delivery_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/deliveries/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutDelivery(token: str, delivery_id, vehicle_id: str = " ", delivery_timestamp: datetime = " ", planned_route: str = " ", drivers: List[str] = " ", stops: object = " ", stops.estimated_arrival_time: Optional[datetime] = " ", stops.orders: List[str] = " ", notes: Optional[object] = " ", notes.subject: Optional[str] = " ", notes.note: str = " ") -> Dict:
    """This endpoint appears to be for submitting delivery route information. It includes details about the vehicle, delivery timestamp, planned route, drivers, stops, and additional notes."""
    params = {'token': token, 'delivery_id': delivery_id, 'vehicle_id': vehicle_id, 'delivery_timestamp': delivery_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders, 'notes': notes, 'notes.subject': notes.subject, 'notes.note': notes.note}
    body = {'vehicle_id': vehicle_id, 'delivery_timestamp': delivery_timestamp, 'planned_route': planned_route, 'drivers': drivers, 'stops': stops, 'stops.estimated_arrival_time': stops.estimated_arrival_time, 'stops.orders': stops.orders, 'notes': notes, 'notes.subject': notes.subject, 'notes.note': notes.note}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/deliveries/{{delivery_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()
