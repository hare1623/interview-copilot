from app.services.question_retrieval_service import QuestionRetrievalService

service = QuestionRetrievalService()

questions = service.build_interview_set(skills=["Angular"])


for question in questions:

    print(f"{question['metadata']['difficulty'].upper()} " f"- {question['question']}")
