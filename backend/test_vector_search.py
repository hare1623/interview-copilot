import json

from app.services.vector_service import VectorService

vector_service = VectorService()

results = vector_service.search_questions(
    query="Angular performance optimization", limit=3
)

print(json.dumps(results, indent=2))
