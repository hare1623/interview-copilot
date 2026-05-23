from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    session_id: int

    question: str

    answer: str
