from app.services.ollama_service import OllamaService

service = OllamaService()

response = service.generate(
    "Explain RxJS briefly"
)

print(response)