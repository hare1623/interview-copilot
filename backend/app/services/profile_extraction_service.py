import json

from app.services.ollama_service import OllamaService


class ProfileExtractionService:

    def __init__(self):

        self.ollama_service = OllamaService()

    def extract_profile(self, resume_text):

        prompt = f"""
You are an expert resume analyzer.

Extract information ONLY from the provided resume.

Do NOT hallucinate or assume skills.

Return ONLY valid JSON.

Rules:
- Do not add technologies not explicitly mentioned.
- Domains should represent industries/business areas only.
- Skills should contain technical skills only.
- Keep summary concise.

Required JSON structure:

{{
  "name": "",
  "role": "",
  "experience_years": "",
  "skills": [],
  "domains": [],
  "summary": ""
}}

Resume:
{resume_text}
"""

        response = self.ollama_service.generate(prompt)

        return response
