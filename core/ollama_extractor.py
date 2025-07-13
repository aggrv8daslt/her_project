import requests
import json
import re

def extract_memory_from_input(user_input):
    prompt = (
        "Extract key personal memory data from this input in valid JSON format.\n"
        "Only return a JSON object. If there's nothing useful to extract, return an empty JSON: {}\n\n"
        f"Input: {user_input}"
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
    except Exception as e:
        print(f"[Extractor] Connection error: {e}")
        return None

    if response.status_code != 200:
        print(f"[Extractor] API Error: {response.status_code} — {response.text}")
        return None

    try:
        data = response.json()
        raw_response = data.get("response", "")
        print(f"[Extractor] Raw memory response: {raw_response}")

        memory_data = json.loads(raw_response)
        if isinstance(memory_data, dict):
            return memory_data
        else:
            print("[Extractor] Warning: Extracted memory is not a valid JSON object.")
            return None
    except json.JSONDecodeError as e:
        print(f"[Extractor] JSON decode error (memory): {e}")
        return None

def extract_emotional_state(user_input):
    prompt = (
        "Given the following user input, extract any emotional states "
        "they are expressing in pure JSON format like this:\n\n"
        '{ "emotional_state": ["happy", "anxious"] }\n\n'
        "Only return valid JSON. Do not include any explanations or comments.\n\n"
        f"User input: {user_input}"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        headers={"Content-Type": "application/json"},
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        print(f"[Extractor] Emotion API Error: {response.status_code}")
        return None

    raw = response.json().get("response", "")
    print(f"[Extractor] Raw emotion response:\n{raw}")

    # 🧠 Extract first valid JSON object found
    try:
        match = re.search(r'\{.*?\}', raw, re.DOTALL)
        if not match:
            raise ValueError("No JSON object found.")
        json_data = json.loads(match.group())
        return json_data.get("emotional_state", [])
    except Exception as e:
        print(f"[Extractor] JSON decode error (emotion): {e}")
        return None
