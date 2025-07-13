from kokoro.phonemizer import phonemize

text = "Hello world!"
lang = 'a'  # or whatever language code you are using

phonemes = phonemize(text, lang)
print(f"Phonemes from text '{text}': {phonemes}")
