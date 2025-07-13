import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_memory_from_input(user_input, model="llama3"):
    prompt = f"""
Your task is to extract meaningful personal facts from what the user says. 
Return only structured JSON. If there's nothing meaningful, return null.

Look for:
- Emotional statements or moods
- Preferences or dislikes
- Relationships, names, locations
- Goals or life details
- Birthdays or age
- Anything that helps understand the user

User: "{user_input}"
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    text = result.get("response", "").strip()

    try:
        data = json.loads(text)
        return data
    except json.JSONDecodeError:
        return None
