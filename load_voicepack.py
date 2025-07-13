import os
import torch

def load_voicepack(voices_dir):
    voicepack = {}
    for filename in os.listdir(voices_dir):
        if filename.endswith(".pt"):
            try:
                path = os.path.join(voices_dir, filename)
                ref = torch.load(path, map_location='cpu')
                # voicepack key is length of token input
                # you can adjust this if necessary
                voicepack[100] = ref  # 100 is placeholder, update if needed
                print(f"Loaded voice: {filename}")
            except Exception as e:
                print(f"Failed to load {filename}: {e}")
    return voicepack
