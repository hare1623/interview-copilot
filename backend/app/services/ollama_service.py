import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


class OllamaService:

    def generate(self, prompt, model="qwen2.5:3b"):

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data.get("response", "")