from pydantic import BaseModel
from typing import List


class CandidateProfileSchema(BaseModel):
    id: int
    name: str
    role: str
    skills: List[str]
    domains: List[str]
    summary: str
