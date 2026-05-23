from fastapi import APIRouter

from app.services.interview_session_service import InterviewSessionService
from app.services.answer_evaluation_service import AnswerEvaluationService
from app.services.interview_persistence_service import InterviewPersistenceService

from app.schemas.interview_schema import EvaluationRequest

router = APIRouter()

service = InterviewSessionService()
evaluation_service = AnswerEvaluationService()
persistence_service = InterviewPersistenceService()


@router.get("/start/{candidate_id}")
def start_interview(candidate_id: int):
    session = persistence_service.create_session(candidate_id)

    result = service.create_interview_session(candidate_id)

    return {
        "success": True,
        "message": ("Interview session created"),
        "data": {"session_id": session.id, **result},
    }


@router.post("/evaluate")
def evaluate_answer(request: EvaluationRequest):

    result = evaluation_service.evaluate_answer(
        question=request.question, answer=request.answer
    )
    persistence_service.save_answer(
        session_id=request.session_id,
        question=request.question,
        answer=request.answer,
        evaluation=result,
    )

    return {
        "success": True,
        "message": ("Answer evaluated successfully"),
        "data": result,
    }


@router.get("/session/{session_id}")
def get_session(session_id: int):

    result = persistence_service.get_session_details(session_id)

    return {"success": True, "message": ("Interview session retrieved"), "data": result}
