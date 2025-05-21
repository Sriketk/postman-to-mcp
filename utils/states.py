from pydantic import BaseModel, Field
from typing import Literal, Optional, List



class LiteralAnalysisResult(BaseModel):
    name : str = Field(..., description="Name of the field")
    type: Literal["str", "int", "bool", "float", "datetime", "List[str]", "object"] = Field(..., description="""Type of the field (e.g., string, integer, boolean, float, datetime, List[str], object)""")
    is_literal: bool = Field( ..., description=(
            "Set to True if the description implies a fixed set of allowed values (e.g., multiple options to choose from, like 'Options: A, B, C'). "
            "Set to False if the field is open-ended or accepts any value (like free text, numbers, or date limits)."
            "The other options must be present in the description for the field to be literal."
        ) )
    optional: bool = Field(
        default=False,
        description="Set to True if the field is optional (e.g., not required)."
    )
    options: Optional[List[str]] = Field(
        default=None,
        description="The list of literal string options (only if is_literal is True). Omit or set to null if not a literal."
    )
    defaultValue: Optional[str] = Field(
        default=" ",
        description="The default value for the field. Set to empty string if there is no default value suggested."
    )



class PostEndpointAnalysisResult(BaseModel):
    description: str = Field(..., description="Description of the endpoint")
    requestFields: List[LiteralAnalysisResult] = Field(..., description="List of fields in the request body")