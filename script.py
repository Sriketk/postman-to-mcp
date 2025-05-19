import json
from pathlib import Path
from typing import Dict, Any, Optional, Literal, List
from pydantic import BaseModel, Field
import os
from datetime import datetime
from typing import Literal
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
import textwrap


# Load environment variables from .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass



# llm = ChatOpenAI(
#     model="gpt-4o",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,   
# )

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.5,
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

baseImports = """
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal

"""


llm_with_prompt = llm.bind(messages=[
    SystemMessage(content="You are a helpful assistant in determining if the description of a field implies a fixed set of allowed values (e.g., multiple options to choose from, like 'Options: A, B, C'). "
    "If so, set is_literal to True. If the field is open-ended or accepts any value (like free text, booleans, numbers, or date limits), set is_literal to False. ")
])

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


def main():
    # Specify the directory where output files will be saved
    output_dir = Path("subservers")  # Change this to your desired directory
    output_dir.mkdir(exist_ok=True)  # Create the directory if it doesn't exist

    with open("flourish.json") as f:
        collection = json.load(f)
        
    authType = collection["auth"]["type"]    
    itemGroup = collection["item"]
    base_url = collection["variable"][0]["value"]
    
    for item in itemGroup:
        mcpSubServer = item["name"]
        endpoints = item["item"]
        
        # Define the full file path for each MCP server
        output_filename = output_dir / f"{mcpSubServer}.py"
        with open(output_filename, "w") as output_file:
            baseServer = textwrap.dedent(f"""
                {mcpSubServer}_mcp = FastMCP(name="{mcpSubServer}")
                \n
            """)
            output_file.write(baseImports)
            output_file.write(baseServer)
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
                                if response.type != "int" and paramType != "int" and response.type != "bool" and paramType != "bool":
                                    paramType = format_literal_type(response.options)
                        if isOptional:
                            temp = f"{key}: Optional[{paramType}] = \"{value}\""
                        else:
                            temp = f"{key}: {paramType} = \"{value}\""
                        parameters.append(temp)
                
                baseServer = textwrap.dedent(f"""
                    def {toolName}({', '.join(parameters)}) -> Dict:
                        \"\"\"{toolDocString}\"\"\"
                        response = requests.get(
                            f"{requestEndpoint}",
                            headers={{ "Accept": "application/json", "Authorization": f"Basic {{token}}" }},
                            params={{k: v for k, v in {{
                                {', '.join([param.split(': ')[0] + ': ' + param.split(': ')[1] for param in parameters if ':' in param])}
                            }}.items() if v is not None}},
                        )
                        response.raise_for_status()
                        return response.json()
                    """)
                output_file.write(baseServer)
        
        print(f"✅ Output for {mcpSubServer} written to {output_filename}")


if __name__ == "__main__":
    main()
