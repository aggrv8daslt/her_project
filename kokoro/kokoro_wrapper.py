# kokoro/kokoro_wrapper.py

from kokoro.core import generate

class KokoroTTS:
    def __init__(self, model, lang='a', speed=1.0):
        self.model = model
        self.lang = lang
        self.speed = speed

    def synthesize(self, text, speaker_embedding, ps=None):
        print(f"[DEBUG] synthesize() received ps type: {type(ps)}")
        
        audio, phonemes = generate(
            self.model,
            text,
            speaker_embedding,
            lang=self.lang,
            speed=self.speed,
            ps=ps
        )

        return audio, phonemes
