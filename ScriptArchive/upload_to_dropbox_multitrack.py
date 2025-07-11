import os
import json
import dropbox
from hashlib import md5

# ===🔐 Dropbox credentials ===
DROPBOX_TOKEN = "Rpx0Br2IFXIAAAAAAAAUlL1lHFNfVmTr_xTx0z21shY"
dbx = dropbox.Dropbox(DROPBOX_TOKEN)

# ===📁 Sync targets: key = local path, value = dropbox destination ===
FOLDER_MAP = {
    "EM-Tools-Assets/Test_Resources/CBECC_Models": "/EM_Explorer/Test_Resources/CBECC_Models",
    "Docs": "/Docs"
}

# ===🧠 Cache file to store previously uploaded hashes ===
CACHE_FILE = ".last_uploaded_multi_folder.json"

# ===🔍 File extensions to include (add others as needed) ===
VALID_EXTENSIONS = [".xml", ".idf", ".py", ".csv", ".json", ".md", ".xlsm"]

# ===✅ Connect to Dropbox ===
try:
    user = dbx.users_get_current_account()
    print(f"🔐 Connected to Dropbox as: {user.name.display_name} ({user.email})")
except dropbox.exceptions.AuthError:
    raise ValueError("❌ Dropbox token is invalid or expired.")

# ===📂 Load hash cache ===
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
else:
    cache = {}

def file_hash(path):
    with open(path, "rb") as f:
        return md5(f.read()).hexdigest()

def should_upload(path, rel_key):
    return cache.get(rel_key) != file_hash(path)

def upload_file(local_path, rel_key, dropbox_path):
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    print(f"✅ Uploaded: {dropbox_path}")
    cache[rel_key] = file_hash(local_path)

def sync_folder(local_root, dropbox_root):
    print(f"\n📁 Scanning {local_root} → {dropbox_root}")
    for root, _, files in os.walk(local_root):
        for file in files:
            if file.startswith(".") or file.endswith(".DS_Store"):
                continue
            ext = os.path.splitext(file)[1].lower()
            if ext not in VALID_EXTENSIONS:
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, local_root)
            rel_key = f"{local_root}/{rel_path}"
            dropbox_path = f"{dropbox_root}/{rel_path.replace(os.sep, '/')}"

            if should_upload(full_path, rel_key):
                upload_file(full_path, rel_key, dropbox_path)

def main():
    for local_folder, dropbox_folder in FOLDER_MAP.items():
        if os.path.exists(local_folder):
            sync_folder(local_folder, dropbox_folder)
        else:
            print(f"⚠️ Local folder not found: {local_folder}")

    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

    print("\n✅ Multi-folder sync complete.")

if __name__ == "__main__":
    main()
