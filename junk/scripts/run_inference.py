import pandas as pd

PRED_PATH = "outputs/results.csv"
GT_PATH = "data/ground_truth.csv"  # optional

pred = pd.read_csv(PRED_PATH)
gt = pd.read_csv(GT_PATH)

merged = pred.merge(gt, on="story_id")

accuracy = (merged["prediction"] == merged["label"]).mean()

print(f"✅ Accuracy: {accuracy:.4f}")

