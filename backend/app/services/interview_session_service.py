from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.db.models import CandidateProfile

from app.services.question_retrieval_service import QuestionRetrievalService
import json


class InterviewSessionService:

    def __init__(self):

        self.db: Session = SessionLocal()

        self.question_service = QuestionRetrievalService()

    def create_interview_session(self, candidate_id):

        candidate = (
            self.db.query(CandidateProfile)
            .filter(CandidateProfile.id == candidate_id)
            .first()
        )

        if not candidate:

            raise Exception("Candidate not found")

        skills = json.loads(candidate.skills)

        supported_skills = ["Angular"]

        skills = [skill for skill in skills if skill in supported_skills]

        print(skills)

        questions = self.question_service.build_interview_set(skills)

        interview_questions = []

        for question in questions:

            interview_questions.append(
                {
                    "id": question.id,
                    "skill": question.skill,
                    "difficulty": (question.difficulty),
                    "question": (question.question),
                    "tags": question.tags,
                }
            )

        return {
            "candidate": {
                "id": candidate.id,
                "name": candidate.name,
                "role": candidate.role,
            },
            "questions": (interview_questions),
        }
