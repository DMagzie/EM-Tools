import os
import json
import dropbox
import requests
from hashlib import md5

# === 🔐 Dropbox App credentials (SkunkET) ===
APP_KEY = "ywb1x3c744ot17c"
APP_SECRET = "1wzcm1xituufgox"
REFRESH_TOKEN = "jWaRcQHUpm4AAAAAAAAAAVd4r7om_M8BqjsgMsPFWzjpu5tJ7rwFEkIweuwAXRTL"

# === 📁 Local/Dropbox roots ===
LOCAL_ROOT = "EM-Tools"
DROPBOX_ROOT = "/EM_Explorer/EM-Tools"
CACHE_FILE = ".last_uploaded_em_tools.json"

EXCLUDE_PATTERNS = [".DS_Store", ".env", "__pycache__", ".git", ".ipynb_checkpoints"]

# === 🔄 Get access token ===
def get_access_token():
    url = "https://api.dropboxapi.com/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": APP_KEY,
        "client_secret": APP_SECRET
    }
    r = requests.post(url, data=data)
    r.raise_for_status()
    return r.json()["access_token"]

# === 🔐 Initialize Dropbox client ===
ACCESS_TOKEN = get_access_token()
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# === 🧠 Load or initialize cache ===
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
else:
    cache = {}

# === 📤 Upload files recursively ===
def file_hash(path):
    with open(path, "rb") as f:
        return md5(f.read()).hexdigest()

def should_exclude(path):
    return any(pattern in path for pattern in EXCLUDE_PATTERNS)

def upload_folder(local_folder, dropbox_folder):
    for root, _, files in os.walk(local_folder):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), local_folder)
            if should_exclude(rel_path):
                continue

            local_path = os.path.join(root, file)
            dropbox_path = f"{dropbox_folder}/{rel_path}".replace("\\", "/")
            file_md5 = file_hash(local_path)

            if rel_path in cache and cache[rel_path] == file_md5:
                print(f"⏩ Skipped (unchanged): {rel_path}")
                continue

            with open(local_path, "rb") as f:
                dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
                cache[rel_path] = file_md5
                print(f"✅ Uploaded: {rel_path}")

# === 🚀 Run upload ===
upload_folder(LOCAL_ROOT, DROPBOX_ROOT)

# === 💾 Save updated cache ===
with open(CACHE_FILE, "w") as f:
    json.dump(cache, f, indent=2)
