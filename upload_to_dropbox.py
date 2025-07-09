import os
import json
import requests
import dropbox

# ===🔐 CONFIG: Paste your credentials here ===
REFRESH_TOKEN = "jWaRcQHUpm4AAAAAAAAAAVd4r7om_M8BqjsgMsPFWzjpu5tJ7rwFEkIweuwAXRTL"
APP_KEY = "ywb1x3c744ot17c"
APP_SECRET = "1wzcm1xituufgox"

# ===📦 Dropbox OAuth Manual Refresh ===
def get_access_token():
    url = "https://api.dropboxapi.com/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": APP_KEY,
        "client_secret": APP_SECRET
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"❌ Failed to refresh token: {response.text}")

# ===📁 Upload Logic ===
def upload_file_to_dropbox(dbx, local_path, dropbox_path):
    with open(local_path, "rb") as f:
        print(f"📤 Uploading: {local_path} → {dropbox_path}")
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def process_manifest(dbx, manifest_path):
    with open(manifest_path, "r") as f:
        manifest = json.load(f)
    for item in manifest.get("deliverables", []):
        local = item["local_path"]
        dropbox_target = item["dropbox_path"]
        if os.path.exists(local):
            upload_file_to_dropbox(dbx, local, dropbox_target)
        else:
            print(f"⚠️ Skipped missing file: {local}")

def scan_for_manifests(base_folder="."):
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file == "dropbox_upload_manifest.json":
                manifest_path = os.path.join(root, file)
                print(f"🔍 Found manifest: {manifest_path}")
                access_token = get_access_token()
                dbx = dropbox.Dropbox(oauth2_access_token=access_token)
                process_manifest(dbx, manifest_path)

if __name__ == "__main__":
    scan_for_manifests("EM_Explorer_Track")
