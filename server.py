from subservers.Retail_Orders import Retail_Orders_mcp
from subservers.Retail_Customers import Retail_Customers_mcp
from subservers.Packages import Packages_mcp
from subservers.Inventory import Inventory_mcp
from subservers.Facilities import Facilities_mcp

from typing import Any, Dict, Literal
from fastapi import Request, HTTPException
from fastmcp import FastMCP
import os
import requests
import base64
from datetime import datetime
from pydantic import BaseModel
mcp = FastMCP("Flourish External API - Docs")

# Mount Facilities Subservers
mcp.mount("Facilities", Facilities_mcp)

# Mount Inventory Subservers
mcp.mount("Inventory", Inventory_mcp)

# Mount Packages Subservers
mcp.mount("Packages", Packages_mcp)

# Mount Retail_Customers Subservers
mcp.mount("Retail_Customers", Retail_Customers_mcp)

# Mount Retail_Orders Subservers
mcp.mount("Retail_Orders", Retail_Orders_mcp)
