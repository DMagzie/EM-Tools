import os
import json
import dropbox
from hashlib import md5

# Define folders to sync
VERSION_FOLDERS = ["v0.3", "v0.4"]
ROOT_UPLOAD_PATH = "/EM_Explorer"
DROPBOX_TOKEN = "jWaRcQHUpm4AAAAAAAAAAVd4r7om_M8BqjsgMsPFWzjpu5tJ7rwFEkIweuwAXRTL"

# Initialize Dropbox
if not DROPBOX_TOKEN or DROPBOX_TOKEN.startswith("your_dropbox_token_here"):
    raise ValueError("❌ Please set your actual DROPBOX_TOKEN in the script.")
dbx = dropbox.Dropbox(DROPBOX_TOKEN)

def file_hash(path):
    with open(path, "rb") as f:
        return md5(f.read()).hexdigest()

def should_upload(path, rel_path, cache):
    current_hash = file_hash(path)
    return cache.get(rel_path) != current_hash

def upload_file(local_path, rel_path, version_folder, cache):
    dropbox_path = f"{ROOT_UPLOAD_PATH}/{version_folder}/{rel_path.replace(os.sep, '/')}"
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    print(f"✅ Uploaded: {version_folder}/{rel_path}")
    cache[rel_path] = file_hash(local_path)

def sync_version_folder(version_folder):
    print(f"\n📁 Scanning {version_folder}/ for changed files...")
    cache_file = f".last_uploaded_{version_folder}.json"
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            cache = json.load(f)
    else:
        cache = {}

    for root, _, files in os.walk(version_folder):
        for file in files:
            if file.startswith(".") or file.endswith(".DS_Store") or file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, version_folder)
            if should_upload(full_path, rel_path, cache):
                upload_file(full_path, rel_path, version_folder, cache)

    with open(cache_file, "w") as f:
        json.dump(cache, f, indent=2)
    print(f"✅ {version_folder} sync complete.")

def main():
    for folder in VERSION_FOLDERS:
        if os.path.exists(folder):
            sync_version_folder(folder)
        else:
            print(f"⚠️ Skipping missing folder: {folder}")

if __name__ == "__main__":
    main()
