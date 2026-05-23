import requests
from app.config import settings

OLLAMA_URL = settings.OLLAMA_URL
OLLAMA_MODEL = settings.OLLAMA_MODEL


class OllamaService:

    def generate(self, prompt, model=None):

        response = requests.post(
            OLLAMA_URL,
            json={"model": model or OLLAMA_MODEL, "prompt": prompt, "stream": False},
        )

        data = response.json()

        return data.get("response", "")
