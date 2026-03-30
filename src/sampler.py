import os
import random
import shutil

CLASSES = ['benign', 'malignant', 'normal']

def sample_dataset(source_dir, output_dir, samples_per_class=30):
    """
    Samples images from source_dir and writes directly into output_dir
    without creating timestamp folders.
    """

    for cls in CLASSES:
        src_cls = os.path.join(source_dir, cls)
        tgt_cls = os.path.join(output_dir, cls)

        os.makedirs(tgt_cls, exist_ok=True)

        if not os.path.exists(src_cls):
            print(f"⚠️ Skipping missing class folder: {src_cls}")
            continue

        images = [
            f for f in os.listdir(src_cls)
            if f.endswith(".png") and "_mask" not in f
        ]

        if not images:
            print(f"⚠️ No images found in {src_cls}")
            continue

        selected = random.sample(images, min(samples_per_class, len(images)))

        for img in selected:
            base = img.replace(".png", "")

            img_src  = os.path.join(src_cls, img)
            mask_src = os.path.join(src_cls, base + "_mask.png")

            img_dst  = os.path.join(tgt_cls, img)
            mask_dst = os.path.join(tgt_cls, base + "_mask.png")

            # skip if already exists
            if os.path.exists(img_dst):
                continue

            shutil.copy(img_src, img_dst)

            if os.path.exists(mask_src):
                shutil.copy(mask_src, mask_dst)

        print(f"{cls}: {len(selected)} sampled")

    print(f"\n📁 Sampled dataset written to: {output_dir}")
    return output_dir