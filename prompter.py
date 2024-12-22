import requests

api_key = "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"
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is GPT-3.5 Turbo?"},
    ],
    "temperature": 0.7,
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
