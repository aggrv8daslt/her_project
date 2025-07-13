import os
import torch
import numpy as np
import soundfile as sf
from kokoro.kokoro_wrapper import KokoroTTS
from kokoro.model import KModel

# === Voice Setup ===
voices_dir = r"C:\AI\her_project\kokoro\my_model\hub\models\snapshots\model\voices"
voicepack = {}

for file in os.listdir(voices_dir):
    if file.endswith(".pt"):
        voice_name = file[:-3]
        voice_path = os.path.join(voices_dir, file)
        voicepack[voice_name] = torch.load(voice_path, map_location="cpu")
        print(f"Loaded voice: {voice_name}")

default_voice = "af_bella"

# === Load Model ===
model = KModel()  # No config provided; assumes default HF fallback or internal defaults
tts = KokoroTTS(model, lang="en", speed=1.0)

# === Synthesis ===
text = "Hello world!"
audio, phonemes = tts.synthesize(text, speaker_embedding=voicepack[default_voice])

if audio is None:
    print("[ERROR] Synthesis returned None. Something went wrong.")
    exit(1)

print(f"Phonemes: {phonemes}")

# === Save Audio ===
if isinstance(audio, tuple):
    audio = audio[0]

audio_np = audio if isinstance(audio, np.ndarray) else audio.cpu().numpy()
if audio_np.ndim == 1:
    audio_np = audio_np[:, np.newaxis]

sf.write("output.wav", audio_np, samplerate=22050)
print("Synthesis complete! Output saved as output.wav")
