from src.sampler import sample_dataset
import os
import shutil

AUGMENTED_DIR = "data/augmented"

def main():
    print("🚀 Starting data pipeline...")

    # STEP 1 — clear old augmented data
    if os.path.exists(AUGMENTED_DIR):
        shutil.rmtree(AUGMENTED_DIR)

    os.makedirs(AUGMENTED_DIR, exist_ok=True)

    # STEP 2 — run sampling for each split directly into augmented/
    for split in ["train", "val", "test"]:
        source_dir = f"data/original/{split}"

        if not os.path.exists(source_dir):
            print(f"⚠️ Skipping missing folder: {source_dir}")
            continue

        print(f"📂 Processing: {split}")

        sample_dataset(
            source_dir=source_dir,
            output_dir=AUGMENTED_DIR,   # direct write
            samples_per_class=30
        )

    print("\n✅ Augmented data ready at:", AUGMENTED_DIR)

    print("\n👉 Now run:")
    print("dvc add data/")
    print("dvc push")

    print("\n🎉 Done\n")


if __name__ == "__main__":
    main()