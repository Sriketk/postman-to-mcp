
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Manufacturing Runs_mcp = FastMCP(name="Manufacturing Runs")



def GetWorkOrders(limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "11783 WO with BOM", manufacturing_run_type_name: Literal["Pilot", "Production", "Development"] = "TypeA", machine_name: str = "Oil Extractor Machine", lot_number: int = "4321", ref_field_1: int = "11784", ref_field_2: str = "Field2Value", ref_field_3: str = "IG", manufacturing_reference_id: str = "Ref1234", completed_timestamp: str = "2022-01-02T15:04:05.000Z", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "oil") -> Dict:
    """Gets information about all of the work orders at a given facility."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/workorders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "11783 WO with BOM", manufacturing_run_type_name: Literal["Pilot", "Production", "Development"] = "TypeA", machine_name: str = "Oil Extractor Machine", lot_number: int = "4321", ref_field_1: int = "11784", ref_field_2: str = "Field2Value", ref_field_3: str = "IG", manufacturing_reference_id: str = "Ref1234", completed_timestamp: str = "2022-01-02T15:04:05.000Z", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "oil"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetWorkOrderById(manufacturing_run_id) -> Dict:
    """Get manufacturing run by ID."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/workorders/{{manufacturing_run_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostWorkOrder(limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "RunName", manufacturing_run_type_name: Literal["Pilot", "Production", "R&D"] = "TypeA", machine_name: str = "MachineX", lot_number: int = "1001", ref_field_1: str = "Field1Value", ref_field_2: str = "Field2Value", ref_field_3: str = "Field3Value", manufacturing_reference_id: str = "Ref1234", completed_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "searchQuery") -> Dict:
    """Gets information about all of the manufacturing runs available for a given facility."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/workorders/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "RunName", manufacturing_run_type_name: Literal["Pilot", "Production", "R&D"] = "TypeA", machine_name: str = "MachineX", lot_number: int = "1001", ref_field_1: str = "Field1Value", ref_field_2: str = "Field2Value", ref_field_3: str = "Field3Value", manufacturing_reference_id: str = "Ref1234", completed_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "searchQuery"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutWorkOrder(limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "RunName", manufacturing_run_type_name: Literal["Pilot", "Production", "R&D"] = "TypeA", machine_name: str = "MachineX", lot_number: int = "1001", ref_field_1: str = "Field1Value", ref_field_2: str = "Field2Value", ref_field_3: str = "Field3Value", manufacturing_reference_id: str = "Ref1234", completed_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "searchQuery") -> Dict:
    """Gets information about all of the manufacturing runs available for a given facility."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/workorders/52/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "RunName", manufacturing_run_type_name: Literal["Pilot", "Production", "R&D"] = "TypeA", machine_name: str = "MachineX", lot_number: int = "1001", ref_field_1: str = "Field1Value", ref_field_2: str = "Field2Value", ref_field_3: str = "Field3Value", manufacturing_reference_id: str = "Ref1234", completed_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "searchQuery"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingRuns(limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "RunName", manufacturing_run_type_name: Literal["Pilot", "Production", "R&D"] = "TypeA", machine_name: str = "MachineX", lot_number: int = "1001", ref_field_1: str = "Field1Value", ref_field_2: str = "Field2Value", ref_field_3: str = "Field3Value", manufacturing_reference_id: str = "Ref1234", created_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", created_timestamp_operator: Literal["lt", "gt"] = "gt", last_updated_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", last_updated_timestamp_operator: Literal["lt", "gt"] = "gt", completed_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "searchQuery") -> Dict:
    """Gets information about all of the manufacturing runs available for a given facility."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/runs/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", sortOrder: Literal["asc", "desc"] = "asc", sortBy: Optional[str] = "manufacturing_run_id", status: int = "10", status_description: str = "In Progress", input_packages: str = "input123", output_packages: str = "output456", name: str = "RunName", manufacturing_run_type_name: Literal["Pilot", "Production", "R&D"] = "TypeA", machine_name: str = "MachineX", lot_number: int = "1001", ref_field_1: str = "Field1Value", ref_field_2: str = "Field2Value", ref_field_3: str = "Field3Value", manufacturing_reference_id: str = "Ref1234", created_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", created_timestamp_operator: Literal["lt", "gt"] = "gt", last_updated_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", last_updated_timestamp_operator: Literal["lt", "gt"] = "gt", completed_timestamp: datetime = "%Y-%m-%dT%H:%M:%SZ", completed_timestamp_operator: Literal["lt", "gt"] = "gt", q: str = "searchQuery"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingRunById(manufacturing_run_id, offset: int = "0", limit: int = "50", brand_id: int = "19", brand_name: str = "Top Shelf", active: Optional[bool] = "False") -> Dict:
    """Get manufacturing run by ID."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/runs/{{manufacturing_run_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            offset: int = "0", limit: int = "50", brand_id: int = "19", brand_name: str = "Top Shelf", active: Optional[bool] = "False"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingMachines(limit: int = "50", offset: int = "0", sortBy: str = "machine_id", sortOrder: str = "asc", is_active: int = "1") -> Dict:
    """Get manufacturing machines."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/machines/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", sortBy: str = "machine_id", sortOrder: str = "asc", is_active: int = "1"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingMachineById(machine_id) -> Dict:
    """Get manufacturing machine by ID."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/machines/{{machine_id}}/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingWasteReasons(limit: int = "50", offset: int = "0") -> Dict:
    """Get waste reasons."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/waste-reasons/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetManufacturingRunTypes() -> Dict:
    """Get manufacturing run types."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/manufacturing/run-types/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
