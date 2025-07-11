import os
import json
import dropbox
import requests
from hashlib import md5

# === 🔐 Dropbox App (SkunkET) credentials ===
APP_KEY = "ywb1x3c744ot17c"
APP_SECRET = "1wzcm1xituufgox"
REFRESH_TOKEN = "jWaRcQHUpm4AAAAAAAAAAVd4r7om_M8BqjsgMsPFWzjpu5tJ7rwFEkIweuwAXRTL"

# === 📁 Local/Dropbox paths ===
LOCAL_ROOT = "EM-Tools"
DROPBOX_ROOT = "/EM_Explorer/EM-Tools"
CACHE_FILE = ".last_uploaded_em_tools.json"

# === 🔄 Get access token from refresh token ===
def get_access_token():
    url = "https://api.dropboxapi.com/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": APP_KEY,
        "client_secret": APP_SECRET
    }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        return r.json()["access_token"]
    else:
        raise Exception(f"❌ Failed to get access token: {r.text}")

# === 🔐 Initialize Dropbox client ===
ACCESS_TOKEN = get_access_token()
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# ✅ Validate token
try:
    account = dbx.users_get_current_account()
    print(f"🔐 Connected to Dropbox as: {account.name.display_name} ({account.email})")
except dropbox.exceptions.AuthError:
    raise ValueError("❌ Dropbox token invalid or expired.")

# === 🔍 Hashing and sync logic ===
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
else:
    cache = {}

def file_hash(path):
    with open(path, "rb") as f:
        return md5(f.read()).hexdigest()

def should_upload(local_path, rel_path):
    return cache.get(rel_path) != file_hash(local_path)

def upload_file(local_path, rel_path):
    dropbox_path = f"{DROPBOX_ROOT}/{rel_path.replace(os.sep, '/')}"
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    print(f"✅ Uploaded: {rel_path}")
    cache[rel_path] = file_hash(local_path)

def main():
    print(f"📁 Scanning {LOCAL_ROOT}/ for changes...")
    for root, _, files in os.walk(LOCAL_ROOT):
        for file in files:
            if file.startswith(".") or file.endswith(".DS_Store") or file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, LOCAL_ROOT)
            if should_upload(full_path, rel_path):
                upload_file(full_path, rel_path)

    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)
    print("\n✅ Sync complete.")

if __name__ == "__main__":
    main()
