import json

from app.services.answer_evaluation_service import AnswerEvaluationService

service = AnswerEvaluationService()

result = service.evaluate_answer(
    question=("Explain Angular " "change detection strategy."),
    answer=(
        "Angular change detection "
        "tracks UI updates using "
        "Zone.js and supports "
        "OnPush strategy for "
        "performance optimization."
    ),
)

print(json.dumps(result, indent=2))
