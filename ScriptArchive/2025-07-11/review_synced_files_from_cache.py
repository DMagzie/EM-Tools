import os
import shutil

# Define source (ChatGPT session cache) and target (local project folder)
SESSION_CACHE = "/mnt/data/session_cache"
LOCAL_PROJECT_ROOT = os.path.expanduser("~/Dropbox/EM-Tools")  # Adjust path if needed

def sync_files():
    if not os.path.exists(SESSION_CACHE):
        print(f"❌ Session cache not found at: {SESSION_CACHE}")
        return

    print(f"🔄 Syncing files from session cache to {LOCAL_PROJECT_ROOT}\n")

    for root, _, files in os.walk(SESSION_CACHE):
        for file in files:
            src_path = os.path.join(root, file)
            relative_path = os.path.relpath(src_path, SESSION_CACHE)
            dest_path = os.path.join(LOCAL_PROJECT_ROOT, relative_path)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            try:
                shutil.copy2(src_path, dest_path)
                print(f"✓ Synced: {relative_path}")
            except Exception as e:
                print(f"✗ Failed to sync {relative_path}: {e}")

if __name__ == "__main__":
    sync_files()
