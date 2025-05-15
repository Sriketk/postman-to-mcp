import json
from pathlib import Path
from typing import Dict, Any, Optional, Literal, List
from pydantic import BaseModel
import os
from datetime import datetime
from typing import Literal
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3.5-sonnet",
    temperature=0.5,
    openai_api_key=os.getenv("ANTHROPIC_API_KEY"),
)
class LiteralAnalysisResult(BaseModel):
    var_name: str
    is_literal: bool
    options: Optional[List[str]] = None
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
    return 'Literal[' + ', '.join(f'"{v}"' for v in values) + ']'

def generate_function(item: Dict[str, Any], base_url: str, mcp_name: str) -> str:
    name = item["name"]
    request = item["request"]
    method = request["method"].lower()
    description = request.get("description", "").strip().replace('\n', ' ')
    path_parts = request["url"]["path"]
    raw_url = request["url"]["raw"]

    # Path parameters
    path_vars = [p for p in path_parts if p.startswith("{{") and p.endswith("}}")]
    func_args = []
    url_path = "/".join([f'{{{p[2:-2]}}}' if p.startswith("{{") else p for p in path_parts])

    for p in path_vars:
        var_name = p[2:-2]
        func_args.append(f"{var_name}: str")

    # Auth token as standard
    func_args.append("token: str")

    # Query parameters
    query_params = request["url"].get("query", [])
    query_dict = {}
    for q in query_params:
        key = q["key"]
        default_val = q.get("value", "")
        q_type = "str"
        if default_val == "true" or default_val == "false":
            q_type = "bool"
            default_val = default_val.lower() == "true"
        elif default_val.isdigit():
            q_type = "int"
            default_val = int(default_val)
        query_dict[key] = (q_type, default_val)

    for key, (typ, val) in query_dict.items():
        if key == "facility_type":
            func_args.append(f"{key}: FacilityType = \"{val}\"")
        elif typ == "str":
            func_args.append(f"{key}: Optional[str] = \"{val}\"")
        else:
            func_args.append(f"{key}: Optional[{typ}] = {val}")

    func_sig = f"def {name.lower()}({', '.join(func_args)}) -> Dict:"

    # Build URL and params
    url_line = f'f"{base_url}/{url_path}"'
    headers = '''headers={ "Accept": "application/json", "Authorization": f"Basic {token}" }'''

    params_line = ""
    if query_dict:
        dynamic_param_build = "\n        params = {k: v for k, v in {\n" + \
            ",\n".join(f'            "{k}": {k}' for k in query_dict.keys()) + \
            "\n        }.items() if v is not None}"
        params_line = f"{dynamic_param_build}\n\n        "
        params_line += ",\n        params=params"

    body = f'''
@{mcp_name}.tool()
{func_sig}
    """{description}"""
    {"" if not query_dict else "        "}response = requests.{method}(
        {url_line},
        {headers}{params_line}
    )
    response.raise_for_status()
    return response.json()
    '''.strip()

    return body

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
        
    itemGroup = collection["item"][0]
    parameters = []
    base_url = collection["variables"][0]["value"]
    for item in itemGroup["item"]:
        mcpSubServer = item["name"]
        endpoints = item["item"]
        for endpoint in endpoints:
            toolName = endpoint["name"]
            headers = {
                "Accept": "application/json",
                "Authorization": f"Basic {{token}}"
            }
            params = {}
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
                           f"Is the following parameter a literal? {queryParam['description']}")
                        
                    
                    params[key] = value
                    parameters.append(key)
    

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

    for item in collection["item"]:
        output.append(generate_function(item, base_url=base_url, mcp_name=mcp_name))
        output.append("")

    output.append(generate_facility_type())

    Path("packages_mcp.py").write_text("\n".join(output))
    print("✅ Generated: facilities_mcp.py")

if __name__ == "__main__":
    with open("flourish.json") as f:
        collection = json.load(f)
    itemGroup = collection["item"][0]
    with open("item_group.json", "w") as output_file:
        json.dump(itemGroup, output_file, indent=4)

