import os
import json
import pandas as pd

from src.pipeline import run

DATA_DIR = "data"
NOVEL_DIR = os.path.join(DATA_DIR, "novels")
BACKSTORY_DIR = os.path.join(DATA_DIR, "backstories")
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

results = []

for file in sorted(os.listdir(NOVEL_DIR)):
    if not file.endswith(".txt"):
        continue

    story_id = file.replace(".txt", "")
    novel_path = os.path.join(NOVEL_DIR, file)
    backstory_path = os.path.join(BACKSTORY_DIR, f"{story_id}.json")

    with open(backstory_path, "r", encoding="utf-8") as f:
        backstory = json.load(f)["backstory"]

    prediction = run(novel_path, backstory)

    results.append({
        "story_id": story_id,
        "prediction": prediction
    })

df = pd.DataFrame(results)
df.to_csv(os.path.join(OUTPUT_DIR, "results.csv"), index=False)

print("✅ results.csv generated successfully")
