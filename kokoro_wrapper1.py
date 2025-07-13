print("Loaded kokoro_wrapper.py")

class KokoroTTS:
    def __init__(self, model, lang="en", speed=1.0):
        self.model = model
        self.lang = lang
        self.speed = speed

    def synthesize(self, text, speaker_embedding=None):
    return generate(
        self.model,
        text,
        self.voicepack,
        self.lang,
        self.speed,
        speaker_embedding
    )
