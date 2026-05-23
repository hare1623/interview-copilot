import json

from requests import session
from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.db.models import InterviewSession, InterviewAnswer


class InterviewPersistenceService:

    def __init__(self):

        self.db: Session = SessionLocal()

    def create_session(self, candidate_id):

        session = InterviewSession(candidate_id=candidate_id)

        self.db.add(session)

        self.db.commit()

        self.db.refresh(session)

        return session

    def save_answer(self, session_id, question, answer, evaluation):

        interview_answer = InterviewAnswer(
            session_id=session_id,
            question=question,
            answer=answer,
            score=evaluation.get("score"),
            feedback=json.dumps(evaluation),
        )

        self.db.add(interview_answer)

        self.db.commit()

        self.db.refresh(interview_answer)

        return interview_answer

    def get_session_details(self, session_id):

        session = (
            self.db.query(InterviewSession)
            .filter(InterviewSession.id == session_id)
            .first()
        )

        if not session:

            raise Exception("Interview session not found")

        answers = (
            self.db.query(InterviewAnswer)
            .filter(InterviewAnswer.session_id == session_id)
            .all()
        )

        formatted_answers = []

        for answer in answers:

            formatted_answers.append(
                {
                    "question": (answer.question),
                    "answer": (answer.answer),
                    "score": (answer.score),
                    "feedback": json.loads(answer.feedback),
                }
            )

        return {
            "session_id": session.id,
            "candidate_id": (session.candidate_id),
            "status": session.status,
            "started_at": str(session.started_at),
            "answers": formatted_answers,
        }
