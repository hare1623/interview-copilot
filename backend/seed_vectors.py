from app.db.database import SessionLocal

from app.db.models import InterviewQuestion

from app.services.vector_service import VectorService

db = SessionLocal()

vector_service = VectorService()

questions = db.query(InterviewQuestion).all()


for question in questions:

    vector_service.add_question(
        question_id=question.id,
        question_text=question.question,
        metadata={
            "question_id": question.id,
            "skill": question.skill,
            "difficulty": (question.difficulty),
        },
    )

    print(f"Seeded: {question.question}")


print("Vector seeding completed.")
