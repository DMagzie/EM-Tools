import os
import json
import dropbox
from hashlib import md5

VERSION_FOLDER = "v0.4"
UPLOAD_ROOT = f"/EM_Explorer/{VERSION_FOLDER}"
CACHE_FILE = f".last_uploaded_{VERSION_FOLDER}.json"
DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")

# Initialize Dropbox
if not DROPBOX_TOKEN:
    raise EnvironmentError("❌ DROPBOX_TOKEN not set in environment.")
dbx = dropbox.Dropbox(DROPBOX_TOKEN)

# Load previous file hashes
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
else:
    cache = {}

def file_hash(path):
    with open(path, "rb") as f:
        return md5(f.read()).hexdigest()

def should_upload(path):
    rel_path = os.path.relpath(path, VERSION_FOLDER)
    current_hash = file_hash(path)
    return cache.get(rel_path) != current_hash

def upload_file(local_path):
    rel_path = os.path.relpath(local_path, VERSION_FOLDER)
    dropbox_path = f"{UPLOAD_ROOT}/{rel_path.replace(os.sep, '/') }"
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    print(f"✅ Uploaded: {rel_path}")
    cache[rel_path] = file_hash(local_path)

def main():
    print(f"Scanning {VERSION_FOLDER}/ for changed files...")
    for root, _, files in os.walk(VERSION_FOLDER):
        for file in files:
            if file.startswith(".") or file.endswith(".DS_Store") or file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            if should_upload(full_path):
                upload_file(full_path)
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)
    print("\n✅ Sync complete.")

if __name__ == "__main__":
    main()
