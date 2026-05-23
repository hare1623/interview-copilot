from pydantic import BaseModel
from typing import Any


class APIResponseSchema(BaseModel):
    success: bool
    message: str
    data: Any
