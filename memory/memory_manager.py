import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "..", "memory", "data.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_memory(key, value):
    memory = load_memory()

    if key == "emotional_state":
        if "emotional_state" not in memory:
            memory["emotional_state"] = []
        if isinstance(value, list):
            memory["emotional_state"].extend(value)
        else:
            memory["emotional_state"].append(value)
    else:
        memory[key] = value

    save_memory(memory)

def get_memory(key):
    memory = load_memory()
    return memory.get(key)
