import requests

OLLAMA_MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434/api/generate"

def get_response(prompt):
    SYSTEM_PROMPT = (
    "You are a thoughtful, emotionally aware AI assistant named [name TBD]. "
    "Speak casually, like you're having a private, meaningful conversation. "
    "Keep your answers short, unless asked to go deep. You care about your user. "
)
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": SYSTEM_PROMPT + "\n\nUser: " + prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        content = response.json()["response"]
        return content.strip()
    except Exception as e:
        return f"Error talking to Ollama: {e}"
