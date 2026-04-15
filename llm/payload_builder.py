from config import MODEL_NAME, TEMP

def build_payload(messages):
    return {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": TEMP
    }