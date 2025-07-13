from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", gpu=False)
tts.tts_to_file(text="This is a test of your TTS system. Can you hear this?", file_path="sanity.wav")

print("✅ sanity.wav generated.")
