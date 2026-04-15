import requests
from config import API_URL

def check_model():
    response = requests.get(f"{API_URL}/health")
    if response.status_code == 200:
        return True
    return False

def send_message(payload):
    response = requests.post(f"{API_URL}/v1/chat/completions", json=payload)
    if response.status_code == 200:
        data = response.json()["choices"][0]["message"]["content"]
        return data
    else:
        raise Exception(f"Error: {response.json()}")