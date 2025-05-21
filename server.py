from subservers.Finance_Accounts import Finance_Accounts_mcp
from subservers.Labels import Labels_mcp
from subservers.Manufacturing_Runs import Manufacturing_Runs_mcp
from subservers.Brands import Brands_mcp
from subservers.Deliveries import Deliveries_mcp
from subservers.Drivers import Drivers_mcp
from subservers.Plants import Plants_mcp
from subservers.Vehicles import Vehicles_mcp
from subservers.Shipments import Shipments_mcp
from subservers.Inbound_Purchase_Orders import Inbound_Purchase_Orders_mcp
from subservers.UOMs import UOMs_mcp
from subservers.Strains import Strains_mcp
from subservers.Items import Items_mcp
from subservers.Destinations import Destinations_mcp
from subservers.Vendors import Vendors_mcp
from subservers.Lab_Test_Results import Lab_Test_Results_mcp
from subservers.Outbound_Orders import Outbound_Orders_mcp
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

# Mount Outbound_Orders Subservers
mcp.mount("Outbound_Orders", Outbound_Orders_mcp)

# Mount Lab_Test_Results Subservers
mcp.mount("Lab_Test_Results", Lab_Test_Results_mcp)

# Mount Vendors Subservers
mcp.mount("Vendors", Vendors_mcp)

# Mount Destinations Subservers
mcp.mount("Destinations", Destinations_mcp)

# Mount Items Subservers
mcp.mount("Items", Items_mcp)

# Mount Strains Subservers
mcp.mount("Strains", Strains_mcp)

# Mount UOMs Subservers
mcp.mount("UOMs", UOMs_mcp)

# Mount Inbound_Purchase_Orders Subservers
mcp.mount("Inbound_Purchase_Orders", Inbound_Purchase_Orders_mcp)

# Mount Shipments Subservers
mcp.mount("Shipments", Shipments_mcp)

# Mount Vehicles Subservers
mcp.mount("Vehicles", Vehicles_mcp)

# Mount Plants Subservers
mcp.mount("Plants", Plants_mcp)

# Mount Drivers Subservers
mcp.mount("Drivers", Drivers_mcp)

# Mount Deliveries Subservers
mcp.mount("Deliveries", Deliveries_mcp)

# Mount Brands Subservers
mcp.mount("Brands", Brands_mcp)

# Mount Manufacturing_Runs Subservers
mcp.mount("Manufacturing_Runs", Manufacturing_Runs_mcp)

# Mount Labels Subservers
mcp.mount("Labels", Labels_mcp)

# Mount Finance_Accounts Subservers
mcp.mount("Finance_Accounts", Finance_Accounts_mcp)
