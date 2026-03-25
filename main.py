from src.sampler import sample_dataset
from src.uploader import upload_folder
from dotenv import load_dotenv
import os

load_dotenv()

SOURCE_DIR = "data/generated"
OUTPUT_BASE = "data/sampled"
BUCKET = "ml-training-breast-cancer-data"

def main():
    print("KEY:", os.getenv("AWS_ACCESS_KEY_ID"))

    # STEP 1 — Sampling
    sampled_path = sample_dataset(
        source_dir=SOURCE_DIR,
        output_base=OUTPUT_BASE,
        samples_per_class=30   # small dataset for demo
    )

    timestamp = os.path.basename(sampled_path)

    # STEP 2 — Upload
    upload_folder(
        local_folder=sampled_path,
        bucket=BUCKET,
        prefix=f"augmented/{timestamp}"
    )

    print("\n🎉 Done: Sampled + Versioned + Uploaded\n")

if __name__ == "__main__":
    main()