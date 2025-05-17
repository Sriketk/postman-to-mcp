import json
from pathlib import Path
from typing import Dict, Any, Optional, Literal, List
from pydantic import BaseModel, Field
import os
from datetime import datetime
from typing import Literal
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage



llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.5,
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

llm_with_prompt = llm.bind(messages=[
    SystemMessage(content="You are a helpful assistant in determining if the description of a field implies a fixed set of allowed values (e.g., multiple options to choose from, like 'Options: A, B, C'). "
    "If so, set is_literal to True. If the field is open-ended or accepts any value (like free text, booleans, numbers, or date limits), set is_literal to False. ")
])

from pydantic import BaseModel, Field
from typing import List, Optional




class LiteralAnalysisResult(BaseModel):
    name : str = Field(..., description="Name of the field")
    type: Literal["str", "int", "bool", "float", "datetime"] = Field(..., description="""Type of the field (e.g., string, integer, boolean)""")
    is_literal: bool = Field( ..., description=(
            "Set to True if the description implies a fixed set of allowed values (e.g., multiple options to choose from, like 'Options: A, B, C'). "
            "Set to False if the field is open-ended or accepts any value (like free text, numbers, or date limits)."
        ) )
    optional: bool = Field(
        default=False,
        description="Set to True if the field is optional (e.g., not required)."
    )
    options: Optional[List[str]] = Field(
        default=None,
        description="The list of literal string options (only if is_literal is True). Omit or set to null if not a literal."
    )

def is_datetime(date_str):
    known_formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%d %b %Y",
        "%B %d, %Y",
        "%Y/%m/%d %H:%M",
        "%m-%d-%Y",
        "%Y.%m.%d"
    ]
    
    for fmt in known_formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False
    
def get_datetime_format(date_str):
    known_formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%d %b %Y",
        "%B %d, %Y",
        "%Y/%m/%d %H:%M",
        "%m-%d-%Y",
        "%Y.%m.%d"
    ]
    
    for fmt in known_formats:
        try:
            datetime.strptime(date_str, fmt)
            return fmt
        except ValueError:
            continue
    return None

def format_literal_type(values):
    if not values:
        return None  # or return "" if you prefer empty string

    cleaned = [v for v in values if v and v.strip()]
    if not cleaned:
        return None

    return 'Literal[' + ', '.join(f'"{v}"' for v in cleaned) + ']'



def generate_facility_type():
    return """
from typing import Literal

FacilityType = Literal[
    "Laboratory",
    "Processor",
    "Grower",
    "Dispensary",
    "Distributor",
    "Manufacturer",
    "Other",
    "Microbusiness"
]
""".strip()

def main():
    with open("flourish.json") as f:
        collection = json.load(f)
        
    authType = collection["auth"]["type"]    
        
    itemGroup = collection["item"]
    base_url = collection["variable"][0]["value"]
    for item in itemGroup:
        mcpSubServer = item["name"]
        endpoints = item["item"]
        print("---------------------------------------------")
        print(f"Generating MCP for {mcpSubServer}...")
        for endpoint in endpoints:
            parameters = []
            toolName = endpoint["name"]
            headers = {
                "Accept": "application/json",
                "Authorization": f"Basic {{token}}"
            }
            isliteral = False
            requestEndpoint = base_url
            response = ""
            toolDocString = endpoint["request"].get("description", "").strip().replace('\n', ' ')
            paths = endpoint["request"]["url"]["path"]
            for path in paths:
                requestEndpoint += (path + "/")
                if path.startswith("{{") and path.endswith("}}"):
                    path = path[2:-2]
                    parameters.append(path)
            if endpoint["request"]["url"].get("query"):
                for queryParam in endpoint["request"]["url"]["query"]:
                    key = queryParam["key"]
                    value = queryParam.get("value", "")
                    paramType = "str"
                    isOptional = False
                    if value == "true" or value == "false":
                        value = value.lower() == "true"
                        paramType = "bool"
                    elif value.isdigit():
                        value = int(value)
                        paramType = "int"
                    elif is_datetime(value):
                        value = get_datetime_format(value)
                        paramType = "datetime"
                    if queryParam.get("description"):
                        response = llm.with_structured_output(LiteralAnalysisResult).invoke(
                           queryParam['description'])
                        isOptional = response.optional
                        if response.is_literal:
                            print(f"response: {response}")
                            # print(response.options)
                            if response.type != "int" and paramType != "int" and response.type != "bool" and paramType != "bool":
                                paramType = format_literal_type(response.options)
                            # print(f"paramType: {paramType}")
                    if isOptional:
                        temp = f"{key}: Optional[{paramType}] = \"{value}\""
                    else:
                        temp = f"{key}: {paramType} = \"{value}\""
                    parameters.append(temp)    
            print(f"Tool Name: {toolName}")           
            print(f"Request Endpoint: {requestEndpoint}")
            print(f"Parameters: {parameters}")
            print(f"Tool Docstring: {toolDocString}")
            print("--------------------------------------------")

                        
                    
        
    

    output = [
        "from fastmcp import FastMCP",
        "import requests",
        "from typing import Dict, Optional",
        "",
        "facilities_mcp = FastMCP(name=\"Facilities\")",
        "",
    ]

    base_url = "https://api.flourishsoftware.com/external/api"
    mcp_name = "packages_mcp"

    print("✅ Generated: facilities_mcp.py")

if __name__ == "__main__":
    main() 
    with open("flourish.json") as f:
        collection = json.load(f)
    itemGroup = collection["item"][0]
    with open("item_group.json", "w") as output_file:
        json.dump(itemGroup, output_file, indent=4)

