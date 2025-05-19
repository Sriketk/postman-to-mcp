
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal


Finance Accounts_mcp = FastMCP(name="Finance Accounts")



def GetFinanceAccounts(limit: int = "50", offset: int = "0", id: str = "", name: str = "", fully_qualified_name: str = "", account_type_id: str = "", account_type: Literal["savings", "checking", "investment"] = "", finance_account_class: Literal["asset", "equity", "expense", "liability", "revenue"] = "", include_inactive: str = "") -> Dict:
    """Endpoint to retrieve finance accounts configured for a company."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/finance/accounts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0", id: str = "", name: str = "", fully_qualified_name: str = "", account_type_id: str = "", account_type: Literal["savings", "checking", "investment"] = "", finance_account_class: Literal["asset", "equity", "expense", "liability", "revenue"] = "", include_inactive: str = ""
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetFinanceAccount() -> Dict:
    """Endpoint to retrieve all of the data available for a given finance account by its ID."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/finance/accounts/1/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {

        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()

def GetFinanceAccountTypes(limit: int = "50", offset: int = "0") -> Dict:
    """Endpoint to retrieve finance accounts types for a company."""
    response = requests.get(
        f"https://app.flourishsoftware.com/external/apiv1/finance/account_types/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params={k: v for k, v in {
            limit: int = "50", offset: int = "0"
        }.items() if v is not None},
    )
    response.raise_for_status()
    return response.json()
