
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Lab_Test_Results_mcp = FastMCP(name="Lab_Test_Results")



def GetLabTestResult_V1(token: str) -> Dict:
    """Get details about a lab test result from a given `lab_test_result_id`."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/lab-test-results/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResult_V2(token: str) -> Dict:
    """Get details about a lab test result from a given `lab_test_result_id`."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v2/lab-test-results/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResultPDFs(token: str) -> Dict:
    """Get S3 links to PDFs associated with a `lab_test_result_id`. The links expire in 5 minutes from time of generation so it is expected that the client downloads the assets shortly after generating the links."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v2/lab-test-results/pdf/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResultPDFQRCodeV2(token: str) -> Dict:
    """Gets a PDF link for a lab test COA for a given `lab_test_qr_code`. Also returns the lab test result ID associated with the QR code for looking up further information."""
    params = {'token': token}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v2/lab-test-results/pdf/:lab_test_qr_code/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResults_V1(token: str, limit: int = "50", offset: int = "0", lab_test_result_id: int = "3473", source_package_id: str = "1a2b3c", lot_number: str = "Davy Jones - FL3 - 2022", sample_package_id: str = "1a2b3c", laboratory_id: str = "laba-id321", lab_test_id: str = "laba-id321a", lab_test_result_status: Literal["Pass", "In-Progress", "Fail"] = "pass", tac_percentage_lt: int = "10", tac_percentage_gt: int = "5", thc_percentage_lt: int = "10", thc_percentage_gt: int = "5", cbd_percentage_lt: int = "10", cbd_percentage_gt: int = "5", cbda_percentage_lt: int = "10", cbda_percentage_gt: int = "5", cbdn_percentage_lt: int = "10", cbdn_percentage_gt: int = "5", cbg_percentage_lt: int = "10", cbg_percentage_gt: int = "5", cbn_percentage_lt: int = "10", cbn_percentage_gt: int = "5", has_pesticides: bool = "True", has_solvents: bool = "False", is_final: bool = "True", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", sample_analyzed_timestamp_start: str = "2020-01-02T15:04:05.000Z", sample_analyzed_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get lab test results."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'lab_test_result_id': lab_test_result_id, 'source_package_id': source_package_id, 'lot_number': lot_number, 'sample_package_id': sample_package_id, 'laboratory_id': laboratory_id, 'lab_test_id': lab_test_id, 'lab_test_result_status': lab_test_result_status, 'tac_percentage_lt': tac_percentage_lt, 'tac_percentage_gt': tac_percentage_gt, 'thc_percentage_lt': thc_percentage_lt, 'thc_percentage_gt': thc_percentage_gt, 'cbd_percentage_lt': cbd_percentage_lt, 'cbd_percentage_gt': cbd_percentage_gt, 'cbda_percentage_lt': cbda_percentage_lt, 'cbda_percentage_gt': cbda_percentage_gt, 'cbdn_percentage_lt': cbdn_percentage_lt, 'cbdn_percentage_gt': cbdn_percentage_gt, 'cbg_percentage_lt': cbg_percentage_lt, 'cbg_percentage_gt': cbg_percentage_gt, 'cbn_percentage_lt': cbn_percentage_lt, 'cbn_percentage_gt': cbn_percentage_gt, 'has_pesticides': has_pesticides, 'has_solvents': has_solvents, 'is_final': is_final, 'created_timestamp_start': created_timestamp_start, 'created_timestamp_end': created_timestamp_end, 'last_updated_timestamp_start': last_updated_timestamp_start, 'last_updated_timestamp_end': last_updated_timestamp_end, 'sample_analyzed_timestamp_start': sample_analyzed_timestamp_start, 'sample_analyzed_timestamp_end': sample_analyzed_timestamp_end}
    body = {}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/lab-test-results/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def PostLabTestResult(token: str, source_package_id: Optional[str] = " ", lot_number: str = " ", sample_package_id: Optional[str] = " ", sample_analyzed_timestamp: datetime = " ", laboratory_id: str = " ", lab_test_id: str = " ", thc_percentage: float = " ", delta_9_thc_percentage: Optional[float] = " ", cbd_percentage: float = " ", base_cbd_percentage: Optional[float] = " ", cbda_percentage: float = " ", cbdn_percentage: float = " ", thca_percentage: float = " ", tac_percentage: Optional[float] = " ", cbg_percentage: Optional[float] = " ", cbn_percentage: Optional[float] = " ", moisture_percentage: Optional[float] = " ", has_pesticides: Literal["0", "1"] = " ", has_solvents: Literal["0", "1"] = " ", is_final: Literal["0", "1"] = " ", lab_test_result_status_id: int = " ", origin_id: int = " ", origin_type_id: int = " ", pdf_url_1: Optional[str] = " ", status: Literal["Pass", "Fail"] = " ") -> Dict:
    """This endpoint is used to create a new lab test result. It accepts various parameters related to the lab test, including source and sample package IDs, lot number, timestamps, laboratory information, test results for different compounds, and status information."""
    params = {'token': token, 'source_package_id': source_package_id, 'lot_number': lot_number, 'sample_package_id': sample_package_id, 'sample_analyzed_timestamp': sample_analyzed_timestamp, 'laboratory_id': laboratory_id, 'lab_test_id': lab_test_id, 'thc_percentage': thc_percentage, 'delta_9_thc_percentage': delta_9_thc_percentage, 'cbd_percentage': cbd_percentage, 'base_cbd_percentage': base_cbd_percentage, 'cbda_percentage': cbda_percentage, 'cbdn_percentage': cbdn_percentage, 'thca_percentage': thca_percentage, 'tac_percentage': tac_percentage, 'cbg_percentage': cbg_percentage, 'cbn_percentage': cbn_percentage, 'moisture_percentage': moisture_percentage, 'has_pesticides': has_pesticides, 'has_solvents': has_solvents, 'is_final': is_final, 'lab_test_result_status_id': lab_test_result_status_id, 'origin_id': origin_id, 'origin_type_id': origin_type_id, 'pdf_url_1': pdf_url_1, 'status': status}
    body = {'source_package_id': source_package_id, 'lot_number': lot_number, 'sample_package_id': sample_package_id, 'sample_analyzed_timestamp': sample_analyzed_timestamp, 'laboratory_id': laboratory_id, 'lab_test_id': lab_test_id, 'thc_percentage': thc_percentage, 'delta_9_thc_percentage': delta_9_thc_percentage, 'cbd_percentage': cbd_percentage, 'base_cbd_percentage': base_cbd_percentage, 'cbda_percentage': cbda_percentage, 'cbdn_percentage': cbdn_percentage, 'thca_percentage': thca_percentage, 'tac_percentage': tac_percentage, 'cbg_percentage': cbg_percentage, 'cbn_percentage': cbn_percentage, 'moisture_percentage': moisture_percentage, 'has_pesticides': has_pesticides, 'has_solvents': has_solvents, 'is_final': is_final, 'lab_test_result_status_id': lab_test_result_status_id, 'origin_id': origin_id, 'origin_type_id': origin_type_id, 'pdf_url_1': pdf_url_1, 'status': status}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/lab-test-results/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def PutLabTestResult(token: str, lab_test_result_id: int = " ", source_package_id: str = " ", lot_number: str = " ", sample_package_id: Optional[str] = " ", sample_analyzed_timestamp: datetime = " ", laboratory_id: str = " ", lab_test_id: str = " ", thc_percentage: float = " ", delta_9_thc_percentage: Optional[float] = " ", cbd_percentage: float = " ", base_cbd_percentage: Optional[float] = " ", cbda_percentage: float = " ", cbdn_percentage: float = " ", thca_percentage: float = " ", tac_percentage: Optional[float] = " ", cbg_percentage: Optional[float] = " ", cbn_percentage: Optional[float] = " ", moisture_percentage: Optional[float] = " ", has_pesticides: Literal["0", "1"] = " ", has_solvents: Literal["0", "1"] = " ", is_final: Literal["0", "1"] = " ", lab_test_result_status_id: int = " ", origin_id: int = " ", origin_type_id: int = " ", pdf_url_1: Optional[str] = " ", status: Literal["Pass", "Fail"] = " ") -> Dict:
    """This endpoint allows updating an existing lab test result by ID. It accepts various parameters related to the lab test, including identifiers, test results, and status information."""
    params = {'token': token, 'lab_test_result_id': lab_test_result_id, 'source_package_id': source_package_id, 'lot_number': lot_number, 'sample_package_id': sample_package_id, 'sample_analyzed_timestamp': sample_analyzed_timestamp, 'laboratory_id': laboratory_id, 'lab_test_id': lab_test_id, 'thc_percentage': thc_percentage, 'delta_9_thc_percentage': delta_9_thc_percentage, 'cbd_percentage': cbd_percentage, 'base_cbd_percentage': base_cbd_percentage, 'cbda_percentage': cbda_percentage, 'cbdn_percentage': cbdn_percentage, 'thca_percentage': thca_percentage, 'tac_percentage': tac_percentage, 'cbg_percentage': cbg_percentage, 'cbn_percentage': cbn_percentage, 'moisture_percentage': moisture_percentage, 'has_pesticides': has_pesticides, 'has_solvents': has_solvents, 'is_final': is_final, 'lab_test_result_status_id': lab_test_result_status_id, 'origin_id': origin_id, 'origin_type_id': origin_type_id, 'pdf_url_1': pdf_url_1, 'status': status}
    body = {'lab_test_result_id': lab_test_result_id, 'source_package_id': source_package_id, 'lot_number': lot_number, 'sample_package_id': sample_package_id, 'sample_analyzed_timestamp': sample_analyzed_timestamp, 'laboratory_id': laboratory_id, 'lab_test_id': lab_test_id, 'thc_percentage': thc_percentage, 'delta_9_thc_percentage': delta_9_thc_percentage, 'cbd_percentage': cbd_percentage, 'base_cbd_percentage': base_cbd_percentage, 'cbda_percentage': cbda_percentage, 'cbdn_percentage': cbdn_percentage, 'thca_percentage': thca_percentage, 'tac_percentage': tac_percentage, 'cbg_percentage': cbg_percentage, 'cbn_percentage': cbn_percentage, 'moisture_percentage': moisture_percentage, 'has_pesticides': has_pesticides, 'has_solvents': has_solvents, 'is_final': is_final, 'lab_test_result_status_id': lab_test_result_status_id, 'origin_id': origin_id, 'origin_type_id': origin_type_id, 'pdf_url_1': pdf_url_1, 'status': status}
    response = requests.put(
        f"https://app.flourishsoftware.com/external/api/v1/lab-test-results/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()

def UploadLabTestResultPDF(token: str, pdf: object = " ") -> Dict:
    """This endpoint allows uploading a lab test result PDF. The request body should be form-data with a key named 'pdf' containing the PDF file to upload."""
    params = {'token': token, 'pdf': pdf}
    body = {'pdf': pdf}
    response = requests.post(
        f"https://app.flourishsoftware.com/external/api/v1/lab-test-results/upload/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        data=body
    )
    response.raise_for_status()
    return response.json()
