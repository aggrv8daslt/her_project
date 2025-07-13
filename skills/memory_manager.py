import json
import os

MEMORY_FILE = "memory/data.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            f.write("{}")
    with open(MEMORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def add_memory(key, value):
    memory = load_memory()
    memory[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)
