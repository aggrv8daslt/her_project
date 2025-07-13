import asyncio
import edge_tts

async def main():
    text = "Hello, I am using a different voice!"
    voice = "en-GB-MiaNeural" # British English
    output_file = "voice_output.mp3"

    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        print(f"Audio saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
