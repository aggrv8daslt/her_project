import requests
import json

def extract_memory_from_input(user_input):
    prompt = f"""
You are a memory extraction assistant. Read the user's message and return a JSON object with only actual facts they mention.

Extract only if mentioned:
- birthday
- age
- favorite_color
- emotional_state (e.g., tired, excited, happy, sad, anxious)
- pet_names
- name
- location
- interests

Do not guess. Only include what's stated. Return raw JSON only. No explanation.

Example:
User: "I'm feeling really tired but excited to meet you."

Response:
{{
  "emotional_state": ["tired", "excited"]
}}

User: "{user_input}"
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        raw_output = data.get("response", "")

        # Safeguard against empty output
        if not raw_output.strip():
            return {}

        return json.loads(raw_output)

    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error extracting memory: {e}")
        return {}
