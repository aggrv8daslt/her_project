from core.text_input import get_input
from core.text_output import speak
from core.ollama_llm import get_response
from memory.memory_manager import load_memory, add_memory
from core.ollama_extractor import extract_memory_from_input, extract_emotional_state
from datetime import datetime

def build_context(memory):
    context_lines = []

    now = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    context_lines.append(f"Today is {now}.")

    if "favorite_color" in memory:
        colors = memory["favorite_color"]
        plural = "s" if " and " in colors or "," in colors else ""
        context_lines.append(f"User's favorite color{plural}: {colors}")

    if "birthday" in memory:
        context_lines.append(f"User's birthday: {memory['birthday']}")

    if "age" in memory:
        context_lines.append(f"User's age: {memory['age']}")

    if "pet_names" in memory:
        pets = ", ".join(memory["pet_names"])
        context_lines.append(f"User has pets named: {pets}")

    return "\n".join(context_lines) + "\n" if context_lines else ""

def main():
    speak("System ready. Awaiting instructions.")
    memory = load_memory()

    try:
        while True:
            user_input = get_input()

            if user_input.lower() in ["exit", "quit", "shutdown"]:
                speak("System disengaging. Always watching. Always learning.")
                break

            lower_input = user_input.lower()
            if "when is my birthday" in lower_input or "when was i born" in lower_input:
                if "birthday" in memory:
                    speak(f"You were born on {memory['birthday']}.")
                else:
                    speak("I don't know your birthday yet.")
                continue

            if "how old am i" in lower_input or "what is my age" in lower_input:
                if "age" in memory:
                    speak(f"You are {memory['age']} years old.")
                else:
                    speak("I don't know your age yet.")
                continue

            if "what is today's date" in lower_input or "what day is it" in lower_input:
                now = datetime.now().strftime("%B %d, %Y at %I:%M %p")
                speak(f"Today is {now}.")
                continue

            # Extract memory
            new_mem = extract_memory_from_input(user_input)
            if new_mem:
                for key, value in new_mem.items():
                    add_memory(key, value)
                speak("Got it. I've added that to memory.")

            # Extract emotion
            emotion = "neutral"
            detected_emotion = extract_emotional_state(user_input)
            if detected_emotion:
                emotion = detected_emotion[0]  # take first emotion only for now

            memory = load_memory()
            context = build_context(memory)
            prompt = context + "\nUser: " + user_input

            response = get_response(prompt)
            speak(response, emotion=emotion)

    except KeyboardInterrupt:
        speak("System interrupted. Shutting down gracefully.")

if __name__ == "__main__":
    main()
