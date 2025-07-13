import os
import torch

# Set this to the path of your voices folder
voices_dir = r"C:\AI\her_project\kokoro\voices"

# List files to confirm what's inside
print("Listing files in voices directory:")
for filename in os.listdir(voices_dir):
    print("  -", filename)

# Attempt to load each file and inspect its contents
for filename in os.listdir(voices_dir):
    if filename.endswith(".pt"):
        path = os.path.join(voices_dir, filename)
        print(f"\nLoading: {filename}")
        try:
            data = torch.load(path, map_location='cpu')
            print("Type:", type(data))
            if isinstance(data, dict):
                print("Keys:", data.keys())
            elif isinstance(data, list):
                print("Length:", len(data))
            elif isinstance(data, torch.Tensor):
                print("Tensor shape:", data.shape)
            else:
                print("Unknown format.")
        except Exception as e:
            print("Failed to load:", e)
