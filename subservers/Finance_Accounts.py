
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime


Finance_Accounts_mcp = FastMCP(name="Finance_Accounts")



def GetFinanceAccounts(token: str, limit: int = "50", offset: int = "0", id: str = "", name: str = "", fully_qualified_name: str = "", account_type_id: str = "", account_type: Literal["savings", "checking", "credit"] = "", finance_account_class: Literal["asset", "equity", "expense", "liability", "revenue"] = "", include_inactive: str = "") -> Dict:
    """Endpoint to retrieve finance accounts configured for a company."""
    params = {'token': token, 'limit': limit, 'offset': offset, 'id': id, 'name': name, 'fully_qualified_name': fully_qualified_name, 'account_type_id': account_type_id, 'account_type': account_type, 'finance_account_class': finance_account_class, 'include_inactive': include_inactive}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/finance/accounts/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetFinanceAccount(token: str) -> Dict:
    """Endpoint to retrieve all of the data available for a given finance account by its ID."""
    params = {'token': token}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/finance/accounts/1/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()

def GetFinanceAccountTypes(token: str, limit: int = "50", offset: int = "0") -> Dict:
    """Endpoint to retrieve finance accounts types for a company."""
    params = {'token': token, 'limit': limit, 'offset': offset}
    response = requests.get(
        f"https://app.flourishsoftware.com/external/api/v1/finance/account_types/",
        headers={ "Accept": "application/json", "Authorization": f"Basic {token}" },
        params=params
    )
    response.raise_for_status()
    return response.json()
