
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Lab Test Results_mcp = FastMCP(name="Lab Test Results")



def GetLabTestResult V1() -> Dict:
    """Get details about a lab test result from a given `lab_test_result_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/lab-test-results/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResult V2() -> Dict:
    """Get details about a lab test result from a given `lab_test_result_id`."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv2/lab-test-results/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResultPDFs() -> Dict:
    """Get S3 links to PDFs associated with a `lab_test_result_id`. The links expire in 5 minutes from time of generation so it is expected that the client downloads the assets shortly after generating the links."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv2/lab-test-results/pdf/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResultPDFQRCodeV2() -> Dict:
    """Gets a PDF link for a lab test COA for a given `lab_test_qr_code`. Also returns the lab test result ID associated with the QR code for looking up further information."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv2/lab-test-results/pdf/:lab_test_qr_code/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetLabTestResults V1(limit: int = "50", offset: int = "0", lab_test_result_id: int = "3473", source_package_id: str = "1a2b3c", lot_number: str = "Davy Jones - FL3 - 2022", sample_package_id: str = "1a2b3c", laboratory_id: str = "laba-id321", lab_test_id: str = "laba-id321a", lab_test_result_status: Literal["Pass", "In-Progress", "Fail"] = "pass", tac_percentage_lt: int = "10", tac_percentage_gt: int = "5", thc_percentage_lt: int = "10", thc_percentage_gt: int = "5", cbd_percentage_lt: int = "10", cbd_percentage_gt: int = "5", cbda_percentage_lt: int = "10", cbda_percentage_gt: int = "5", cbdn_percentage_lt: int = "10", cbdn_percentage_gt: int = "5", cbg_percentage_lt: int = "10", cbg_percentage_gt: int = "5", cbn_percentage_lt: int = "10", cbn_percentage_gt: int = "5", has_pesticides: bool = "True", has_solvents: bool = "False", is_final: bool = "True", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", sample_analyzed_timestamp_start: str = "2020-01-02T15:04:05.000Z", sample_analyzed_timestamp_end: str = "2020-01-03T15:04:05.000Z") -> Dict:
    """Get lab test results."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/lab-test-results/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", lab_test_result_id: int = "3473", source_package_id: str = "1a2b3c", lot_number: str = "Davy Jones - FL3 - 2022", sample_package_id: str = "1a2b3c", laboratory_id: str = "laba-id321", lab_test_id: str = "laba-id321a", lab_test_result_status: Literal["Pass", "In-Progress", "Fail"] = "pass", tac_percentage_lt: int = "10", tac_percentage_gt: int = "5", thc_percentage_lt: int = "10", thc_percentage_gt: int = "5", cbd_percentage_lt: int = "10", cbd_percentage_gt: int = "5", cbda_percentage_lt: int = "10", cbda_percentage_gt: int = "5", cbdn_percentage_lt: int = "10", cbdn_percentage_gt: int = "5", cbg_percentage_lt: int = "10", cbg_percentage_gt: int = "5", cbn_percentage_lt: int = "10", cbn_percentage_gt: int = "5", has_pesticides: bool = "True", has_solvents: bool = "False", is_final: bool = "True", created_timestamp_start: str = "2020-01-02T15:04:05.000Z", created_timestamp_end: str = "2020-01-03T15:04:05.000Z", last_updated_timestamp_start: str = "2020-01-02T15:04:05.000Z", last_updated_timestamp_end: str = "2020-01-03T15:04:05.000Z", sample_analyzed_timestamp_start: str = "2020-01-02T15:04:05.000Z", sample_analyzed_timestamp_end: str = "2020-01-03T15:04:05.000Z"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PostLabTestResult() -> Dict:
    """Create a new lab test result."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/lab-test-results/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def PutLabTestResult() -> Dict:
    """Update an existing lab test result by ID."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/lab-test-results/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def UploadLabTestResultPDF() -> Dict:
    """Upload a lab test result PDF.  The request body should be [form-data](https://en.wikipedia.org/wiki/MIME#Form-Data) with a key named `pdf` and a value containing the PDF file to upload."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/lab-test-results/upload/:lab_test_result_id/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
