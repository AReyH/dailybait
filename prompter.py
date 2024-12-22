import requests


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
