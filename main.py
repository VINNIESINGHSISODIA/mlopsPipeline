from src.sampler import sample_dataset
import os
import shutil

AUGMENTED_DIR = "data/augmented"

def main():
    print(" Starting data pipeline...")

    temp_dirs = []

    # STEP 1 — run sampling for each split
    for split in ["train", "val", "test"]:
        source_dir = f"data/original/{split}"

        if not os.path.exists(source_dir):
            print(f" Skipping missing folder: {source_dir}")
            continue

        print(f" Processing: {split}")

        temp_output = sample_dataset(
            source_dir=source_dir,
            output_base=f"temp_{split}",
            samples_per_class=30
        )

        temp_dirs.append(temp_output)

    # STEP 2 — merge into augmented/
    print(" Merging into augmented dataset...")

    if os.path.exists(AUGMENTED_DIR):
        shutil.rmtree(AUGMENTED_DIR)

    os.makedirs(AUGMENTED_DIR, exist_ok=True)

    for temp_dir in temp_dirs:
        for cls in os.listdir(temp_dir):
            src_cls = os.path.join(temp_dir, cls)
            dst_cls = os.path.join(AUGMENTED_DIR, cls)

            os.makedirs(dst_cls, exist_ok=True)

            for file in os.listdir(src_cls):
                shutil.copy(
                    os.path.join(src_cls, file),
                    os.path.join(dst_cls, file)
                )

    print(" Augmented data ready at:", AUGMENTED_DIR)

    print("\n Now run:")
    print("dvc add data/")
    print("dvc push")

    print("\n Done\n")


if __name__ == "__main__":
    main()