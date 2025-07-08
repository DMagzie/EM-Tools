
import os
import sys
import dropbox

def upload_file(dbx, local_path, dropbox_path):
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
    print(f"Uploaded: {local_path} -> {dropbox_path}")

def upload_folder(dbx, folder="outputs"):
    for root, _, files in os.walk(folder):
        for file in files:
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, folder)
            dropbox_path = f"/EM_Explorer/{rel_path}"
            upload_file(dbx, local_path, dropbox_path)

def main():
    token = os.getenv("DROPBOX_TOKEN")
    if not token:
        print("❌ DROPBOX_TOKEN not found in environment. Set it manually.")
        sys.exit(1)

    dbx = dropbox.Dropbox(token)

    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            if os.path.isfile(path):
                upload_file(dbx, path, f"/EM_Explorer/{os.path.basename(path)}")
            elif os.path.isdir(path):
                upload_folder(dbx, folder=path)
            else:
                print(f"⚠️ Skipped: {path} (not found)")
    else:
        upload_folder(dbx)  # default to outputs folder

if __name__ == "__main__":
    main()
