
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Manufacturing_Runs_mcp = FastMCP(name="Manufacturing_Runs")



def GetWorkOrders(token: str, limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: Literal["In Progress", "Completed", "Planned", "Cancelled"] = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "11783 WO with BOM", manufacturing_run_type_name: Literal["Pilot", "Production", "Development"] = "TypeA", machine_name: str = "Oil Extractor Machine", lot_number: int = "4321", ref_field_1: int = "11784", ref_field_2: str = "Field2Value", ref_field_3: str = "IG", manufacturing_reference_id: str = "Ref1234", completed_timestamp: str = "2022-01-02T15:04:05.000Z", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "oil") -> Dict:
    """Gets information about all of the work orders at a given facility."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'sortOrder': sortOrder, 'sortBy': sortBy, 'status': status, 'status_description': status_description, 'input_packages': input_packages, 'output_packages': output_packages, 'name': name, 'manufacturing_run_type_name': manufacturing_run_type_name, 'machine_name': machine_name, 'lot_number': lot_number, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3, 'manufacturing_reference_id': manufacturing_reference_id, 'completed_timestamp': completed_timestamp, 'completed_timestamp_operator': completed_timestamp_operator, 'q': q}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/workorders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetWorkOrderById(token: str, manufacturing_run_id) -> Dict:
    """Get manufacturing run by ID."""
    params = {'token': token, 'manufacturing_run_id': manufacturing_run_id}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/workorders/{{manufacturing_run_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostWorkOrder(token: str, scheduled_datetime: datetime = " ", machine_id: int = " ", bom_hdr_pk: int = " ", expected_qty_to_create: int = " ", lot_number: Optional[str] = "None", name: str = " ", note: Optional[str] = "None", pressure: Optional[float] = "None", temperature: Optional[float] = "None", sequence: Optional[int] = "None", processing_duration: Optional[float] = "None", ref_field_1: Optional[str] = " ", ref_field_2: Optional[str] = " ", ref_field_3: Optional[str] = "None") -> Dict:
    """Gets information about all of the manufacturing runs available for a given facility."""
    params = {'token': token, 'scheduled_datetime': scheduled_datetime, 'machine_id': machine_id, 'bom_hdr_pk': bom_hdr_pk, 'expected_qty_to_create': expected_qty_to_create, 'lot_number': lot_number, 'name': name, 'note': note, 'pressure': pressure, 'temperature': temperature, 'sequence': sequence, 'processing_duration': processing_duration, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3}
    body = {'scheduled_datetime': scheduled_datetime, 'machine_id': machine_id, 'bom_hdr_pk': bom_hdr_pk, 'expected_qty_to_create': expected_qty_to_create, 'lot_number': lot_number, 'name': name, 'note': note, 'pressure': pressure, 'temperature': temperature, 'sequence': sequence, 'processing_duration': processing_duration, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/workorders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutWorkOrder(token: str, scheduled_datetime: datetime = " ", is_work_order: Literal["true", "false"] = " ", status: int = " ", machine_id: int = " ", bom_hdr_pk: int = " ", expected_qty_to_create: int = " ", lot_number: Optional[str] = " ", name: str = " ", note: Optional[str] = " ", pressure: Optional[float] = " ", temperature: Optional[float] = " ", sequence: Optional[int] = " ", processing_duration: Optional[float] = " ", ref_field_1: Optional[str] = " ", ref_field_2: Optional[str] = " ", ref_field_3: Optional[str] = " ") -> Dict:
    """Gets information about all of the manufacturing runs available for a given facility."""
    params = {'token': token, 'scheduled_datetime': scheduled_datetime, 'is_work_order': is_work_order, 'status': status, 'machine_id': machine_id, 'bom_hdr_pk': bom_hdr_pk, 'expected_qty_to_create': expected_qty_to_create, 'lot_number': lot_number, 'name': name, 'note': note, 'pressure': pressure, 'temperature': temperature, 'sequence': sequence, 'processing_duration': processing_duration, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3}
    body = {'scheduled_datetime': scheduled_datetime, 'is_work_order': is_work_order, 'status': status, 'machine_id': machine_id, 'bom_hdr_pk': bom_hdr_pk, 'expected_qty_to_create': expected_qty_to_create, 'lot_number': lot_number, 'name': name, 'note': note, 'pressure': pressure, 'temperature': temperature, 'sequence': sequence, 'processing_duration': processing_duration, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/workorders/52/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingRuns(token: str, limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: Literal["In Progress", "Completed", "Scheduled", "Cancelled"] = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "RunName", manufacturing_run_type_name: Literal["Pilot", "Production", "Development"] = "TypeA", machine_name: str = "MachineX", lot_number: int = "1001", ref_field_1: str = "Field1Value", ref_field_2: str = "Field2Value", ref_field_3: str = "Field3Value", manufacturing_reference_id: str = "Ref1234", created_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", created_timestamp_operator: Literal["lt", "gt"] = "gt", last_updated_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", last_updated_timestamp_operator: Literal["lt", "gt"] = "gt", completed_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "searchQuery") -> Dict:
    """Gets information about all of the manufacturing runs available for a given facility."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'sortOrder': sortOrder, 'sortBy': sortBy, 'status': status, 'status_description': status_description, 'input_packages': input_packages, 'output_packages': output_packages, 'name': name, 'manufacturing_run_type_name': manufacturing_run_type_name, 'machine_name': machine_name, 'lot_number': lot_number, 'ref_field_1': ref_field_1, 'ref_field_2': ref_field_2, 'ref_field_3': ref_field_3, 'manufacturing_reference_id': manufacturing_reference_id, 'created_timestamp': created_timestamp, 'created_timestamp_operator': created_timestamp_operator, 'last_updated_timestamp': last_updated_timestamp, 'last_updated_timestamp_operator': last_updated_timestamp_operator, 'completed_timestamp': completed_timestamp, 'completed_timestamp_operator': completed_timestamp_operator, 'q': q}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/runs/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingRunById(token: str, manufacturing_run_id, offset: int = "0", limit: int = "50", brand_id: int = "19", brand_name: str = "Top Shelf", active: bool = "False") -> Dict:
    """Get manufacturing run by ID."""
    params = {'token': token, 'manufacturing_run_id': manufacturing_run_id, 'offset': offset, 'limit': limit, 'brand_id': brand_id, 'brand_name': brand_name, 'active': active}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/runs/{{manufacturing_run_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingMachines(token: str, limit: int = "50", offset: int = "0", sortBy: str = "machine_id", sortOrder: str = "asc", is_active: int = "1") -> Dict:
    """Get manufacturing machines."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'sortBy': sortBy, 'sortOrder': sortOrder, 'is_active': is_active}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/machines/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingMachineById(token: str, machine_id) -> Dict:
    """Get manufacturing machine by ID."""
    params = {'token': token, 'machine_id': machine_id}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/machines/{{machine_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingWasteReasons(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Get waste reasons."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/waste-reasons/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingRunTypes(token: str) -> Dict:
    """Get manufacturing run types."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/manufacturing/run-types/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
