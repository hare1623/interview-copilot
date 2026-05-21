import requests
import json

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:3b",
        "prompt": "Explain Angular Signals briefly",
        "stream": False
    }
)

print("STATUS CODE:")
print(response.status_code)

print("\nRAW RESPONSE:")
print(response.text)

print("\nJSON RESPONSE:")
print(json.dumps(response.json(), indent=2))