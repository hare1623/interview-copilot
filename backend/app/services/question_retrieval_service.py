import random

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.models import InterviewQuestion


class QuestionRetrievalService:

    def __init__(self):

        self.db: Session = SessionLocal()

    def get_questions(self, skill, difficulty, limit=5):

        questions = (
            self.db.query(InterviewQuestion)
            .filter(InterviewQuestion.skill.ilike(skill))
            .filter(InterviewQuestion.difficulty == difficulty)
            .all()
        )
        print(
            f"Skill: {skill}, " f"Difficulty: {difficulty}, " f"Found: {len(questions)}"
        )

        random.shuffle(questions)

        return questions[:limit]

    def remove_duplicates(self, questions):

        seen = set()

        unique_questions = []

        for question in questions:

            if question.question not in seen:

                seen.add(question.question)

                unique_questions.append(question)

        return unique_questions

    def build_interview_set(self, skills):

        final_questions = []

        for skill in skills:

            easy_questions = self.get_questions(skill=skill, difficulty="easy", limit=2)

            medium_questions = self.get_questions(
                skill=skill, difficulty="medium", limit=2
            )

            advanced_questions = self.get_questions(
                skill=skill, difficulty="advanced", limit=1
            )

            final_questions.extend(easy_questions)

            final_questions.extend(medium_questions)

            final_questions.extend(advanced_questions)

        final_questions = self.remove_duplicates(final_questions)

        random.shuffle(final_questions)

        return final_questions
