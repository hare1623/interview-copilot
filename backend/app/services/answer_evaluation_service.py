from app.services.ollama_service import OllamaService
from app.utils.logger import logger

from app.utils.json_parser import JSONParser


class AnswerEvaluationService:

    def __init__(self):

        self.ollama_service = OllamaService()

    def evaluate_answer(self, question, answer):

        prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate answer.

Question:
{question}

Candidate Answer:
{answer}

Return ONLY valid JSON.

Format:

{{
  "score": 0-10,
  "strengths": [
    "..."
  ],
  "weaknesses": [
    "..."
  ],
  "improvements": [
    "..."
  ]
}}

Rules:
- Return valid JSON only
- Be concise
- Evaluate technical accuracy
- No markdown
"""

        response = self.ollama_service.generate(prompt)

        try:
            logger.info("Evaluating candidate answer")

            parsed_response = JSONParser.parse_json(response)

        except Exception:
            logger.error(f"JSON parsing failed: {response}")

            parsed_response = {
                "score": 0,
                "strengths": [],
                "weaknesses": ["Failed to parse AI response"],
                "improvements": [],
            }

        return parsed_response
