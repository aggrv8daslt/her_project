from kokoro.core import generate

class KokoroTTS:
    def __init__(self, model, lang="en", speed=1.0, voicepack=None):
        self.model = model
        self.lang = lang
        self.speed = speed
        self.voicepack = voicepack

    def synthesize(self, text, speaker_embedding=None):
        return generate(
            self.model,
            text,
            self.voicepack,
            self.lang,
            self.speed,
            speaker_embedding
        )
