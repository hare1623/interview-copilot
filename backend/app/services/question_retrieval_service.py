import random

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.models import InterviewQuestion
from app.services.vector_service import VectorService


class QuestionRetrievalService:

    def __init__(self):

        self.db: Session = SessionLocal()
        self.vector_service = VectorService()

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
            question_text = question["question"]

            if question_text not in seen:

                seen.add(question_text)

                unique_questions.append(question)

        return unique_questions

    def build_interview_set(self, skills):

        final_questions = []

        for skill in skills:

            easy_questions = self.hybrid_question_search(
                skill=skill, difficulty="easy", limit=2
            )

            medium_questions = self.hybrid_question_search(
                skill=skill, difficulty="medium", limit=2
            )

            advanced_questions = self.hybrid_question_search(
                skill=skill, difficulty="advanced", limit=1
            )

            final_questions.extend(easy_questions)

            final_questions.extend(medium_questions)

            final_questions.extend(advanced_questions)

        final_questions = self.remove_duplicates(final_questions)

        random.shuffle(final_questions)

        return final_questions

    def semantic_question_search(self, skill, limit=5):

        results = self.vector_service.search_by_skill(skill=skill, limit=limit)

        documents = results.get("documents", [[]])[0]

        metadatas = results.get("metadatas", [[]])[0]

        retrieved_questions = []

        for doc, metadata in zip(documents, metadatas):

            retrieved_questions.append(
                {
                    "question_id": (metadata.get("question_id")),
                    "question": doc,
                    "metadata": metadata,
                }
            )

        return retrieved_questions

    def hybrid_question_search(self, skill, difficulty=None, limit=5):

        semantic_results = self.semantic_question_search(skill=skill, limit=limit * 2)

        filtered_questions = []

        for result in semantic_results:

            metadata = result["metadata"]

            if difficulty:

                if metadata["difficulty"] != difficulty:
                    continue

            filtered_questions.append(result)

        return filtered_questions[:limit]
