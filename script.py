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
from utils.states import LiteralAnalysisResult, PostEndpointAnalysisResult
from utils.helper import is_datetime, get_datetime_format, format_literal_type
from utils.constants import baseImports, literal_system_prompt, post_endpoint_system_prompt
import textwrap
import json



# Load environment variables from .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.5,
    max_tokens=2048,
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

llm_for_get = llm.bind(messages=[literal_system_prompt])

llm_for_post = llm.bind(messages=[post_endpoint_system_prompt])


def main():
    # Specify the directory where output files will be saved
    output_dir = Path("subservers")  # Change this to your desired directory
    output_dir.mkdir(exist_ok=True)  # Create the directory if it doesn't exist

    with open("flourish.json") as f:
        collection = json.load(f)
    with open("server.py", "w") as output_file:

        mainServerBase = textwrap.dedent(f"""
        from typing import Any, Dict, Literal
        from fastapi import Request, HTTPException
        from fastmcp import FastMCP
        import os
        import requests
        import base64
        from datetime import datetime
        from pydantic import BaseModel
        mcp = FastMCP(\"{collection['info']['name']}\")
        """)
        output_file.write(mainServerBase)
    authType = collection["auth"]["type"]    
    itemGroup = collection["item"]
    base_url = collection["variable"][0]["value"]
    
    for item in itemGroup:
        mcpSubServer = item["name"].replace(" ", "_")
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
                parameters = ["token: str"]
                body = {}
                toolName = endpoint["name"]
                headers = {
                    "Accept": "application/json",
                    "Authorization": f"Basic {{token}}"
                }
                isliteral = False
                requestEndpoint = base_url + '/'
                response = ""
                toolDocString = endpoint["request"].get("description", "").strip().replace('\n', ' ')
                paths = endpoint["request"]["url"]["path"]
                
                for path in paths:
                    requestEndpoint += (path + "/")
                    if path.startswith("{{") and path.endswith("}}"):
                        path = path[2:-2]
                        parameters.append(path)
                if endpoint["request"]["method"] == "GET" and endpoint["request"]["url"].get("query"):
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
                            response = llm_for_get.with_structured_output(LiteralAnalysisResult).invoke(
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
                elif endpoint["request"]["method"] == "POST" or endpoint["request"]["method"] == "PUT":
                    postEndpointDescription = ""
                    postEndpointSampleBody = ""
                    if endpoint["request"].get("description"):
                        postEndpointDescription = endpoint["request"]["description"]
                    if endpoint["request"].get("body"):
                        postEndpointSampleBody = endpoint["request"]["body"]["raw"]
                    response = llm_for_post.with_structured_output(PostEndpointAnalysisResult).invoke(
                        f"this is the description of the body for the endpoint {postEndpointDescription}, "
                        f"and this is a sample body for this endpoint {postEndpointSampleBody}"
                    )
                    toolDocString = response.description
                    requestFields = response.requestFields
                    
                    for field in requestFields:
                        isLiteral = field.is_literal
                        isOptional = field.optional
                        if isLiteral:
                            literal_type = format_literal_type(field.options)
                            if isOptional:
                                parameters.append(f"{field.name}: Optional[{literal_type}] = \"{field.defaultValue}\"")
                            else:
                                parameters.append(f"{field.name}: {literal_type} = \"{field.defaultValue}\"")
                        else:
                            if isOptional:
                                parameters.append(f"{field.name}: Optional[{field.type}] = \"{field.defaultValue}\"")
                            else:
                                parameters.append(f"{field.name}: {field.type} = \"{field.defaultValue}\"")
                params = {}
                for param in parameters:
                    param_name = param.split(':')[0].strip()
                    params[param_name] = param_name
                params_str = ", ".join([f"'{k}': {k}" for k in [param.split(':')[0].strip() for param in parameters]])
                baseServer = textwrap.dedent(f"""
                    def {toolName.replace(' ', '_')}({', '.join(parameters)}) -> Dict:
                        \"\"\"{toolDocString}\"\"\"
                        params = {{{params_str}}}
                        response = requests.{endpoint["request"]["method"].lower()}(
                            f"{requestEndpoint}",
                            headers={{ "Accept": "application/json", "Authorization": f"Basic {{token}}" }},
                            params=params
                        )
                        response.raise_for_status()
                        return response.json()
                    """)
                output_file.write(baseServer)
        with open("server.py", "r+") as output_file:
            content = output_file.read()
            output_file.seek(0)
            output_file.write(f"from subservers.{mcpSubServer} import {mcpSubServer}_mcp\n")
            output_file.write(content)
            
        # Write mount statements in a separate section
        with open("server.py", "a") as output_file:
            output_file.write(f"\n# Mount {mcpSubServer} Subservers\nmcp.mount(\"{mcpSubServer}\", {mcpSubServer}_mcp)\n")
        print(f"✅ Output for {mcpSubServer} written to {output_filename}")


if __name__ == "__main__":
    main()
