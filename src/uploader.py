#uploader.py can be removed(boto3 no longer needed)

import os
import boto3

s3 = boto3.client("s3")

def file_exists(bucket, key):
    try:
        s3.head_object(Bucket=bucket, Key=key)
        return True
    except:
        return False


def upload_folder(local_folder, bucket, prefix):
    for root, _, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)

            s3_key = os.path.join(
                prefix,
                os.path.relpath(local_path, local_folder)
            ).replace("\\", "/")

            # ✅ CACHE: skip if already uploaded
            if file_exists(bucket, s3_key):
                print(f"Skipped (exists): {s3_key}")
                continue

            s3.upload_file(local_path, bucket, s3_key)
            print(f"Uploaded: {s3_key}")

    print("\n✅ Upload complete")