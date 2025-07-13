import asyncio
import edge_tts

VOICE = "en-US-JennyNeural"

EMOTION_STYLE_MAP = {
    "happy": "cheerful",
    "cheerful": "cheerful",
    "sad": "sad",
    "angry": "angry",
    "friendly": "friendly",
    "hopeful": "hopeful",
    "shouting": "angry",
    "whispering": "whispering",
    "embarrassed": "embarrassed",
    "terrified": "fearful",
    "neutral": "general",
}

def speak(text, emotion="happy"):
    print(f"[Assistant]: {text}")
    asyncio.run(speak_async(text, emotion))

async def speak_async(text, emotion):
    style = EMOTION_STYLE_MAP.get(emotion.lower(), "general")

    text = '<speak><prosody rate="x-slow" volume="x-loud" pitch="+20Hz">This is a slow, loud, and high-pitched voice.</prosody> <expressive style="cheerful">And this is a cheerful voice!</expressive></speak>'

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("edge_output.mp3")

    # Playback
    import playsound
    playsound.playsound("edge_output.mp3")
