import json

from app.services.question_retrieval_service import QuestionRetrievalService

service = QuestionRetrievalService()

results = service.semantic_question_search(skill="Angular optimization", limit=5)

print(json.dumps(results, indent=2))
