from langchain_core.messages import SystemMessage


baseImports = """
from fastmcp import FastMCP
import requests
from typing import Dict, Optional, List, Literal
from datetime import datetime

"""


literal_system_prompt = SystemMessage(content="You are a helpful assistant in determining if the description of a field implies a fixed set of allowed values (e.g., multiple options to choose from, like 'Options: A, B, C'). "
    "If so, set is_literal to True. If the field is open-ended or accepts any value (like free text, booleans, numbers, or date limits), set is_literal to False. ")

post_endpoint_system_prompt = SystemMessage(content="You are a helpful assistant in determining the fields in the request body of a POST endpoint. "
    "The request body is a JSON object. The fields in the request body are described in the description of the endpoint. "
    "The fields are described in the description of the endpoint. "
   
    )
