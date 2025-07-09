import os
import json
import dropbox
from dropbox.oauth import DropboxOAuth2FlowNoRedirect

# Load environment variables
REFRESH_TOKEN = os.getenv("DROPBOX_REFRESH_TOKEN")
APP_KEY = os.getenv("DROPBOX_APP_KEY")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET")

if not all([REFRESH_TOKEN, APP_KEY, APP_SECRET]):
    raise EnvironmentError("Missing Dropbox OAuth environment variables.")

# Create Dropbox client using refresh token
dbx = dropbox.Dropbox(
    oauth2_refresh_token=REFRESH_TOKEN,
    app_key=APP_KEY,
    app_secret=APP_SECRET
)

def upload_file_to_dropbox(local_path, dropbox_path):
    """Upload a file to Dropbox."""
    with open(local_path, "rb") as f:
        print(f"Uploading: {local_path} → {dropbox_path}")
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def process_manifest(manifest_path):
    """Load and process a dropbox_upload_manifest.json file."""
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    for item in manifest.get("deliverables", []):
        local = item["local_path"]
        dropbox_target = item["dropbox_path"]

        if os.path.exists(local):
            upload_file_to_dropbox(local, dropbox_target)
        else:
            print(f"⚠️ Skipped missing file: {local}")

def scan_for_manifests(base_folder="."):
    """Recursively search for dropbox_upload_manifest.json files."""
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file == "dropbox_upload_manifest.json":
                manifest_path = os.path.join(root, file)
                print(f"🔍 Found manifest: {manifest_path}")
                process_manifest(manifest_path)

if __name__ == "__main__":
    scan_for_manifests("EM_Explorer_Track")
