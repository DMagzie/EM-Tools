import os
import json
import dropbox

# 🔐 Paste your fresh values here for testing
REFRESH_TOKEN = "sl.u.AF2tQkNqqqb_3ILulOBayoE6Q8OTjM9dtpgTbIHeLjUVFNwjk-MqPs8cMlFJHXxAxrKFLLBnRA-eGMZmZfHjadzSACqdhZDK_2I8D4FgSTg3zyJBHfirsxPlwKaC5lIN3q7TOqwscVGS88AtCPT3BE-OZQUweBnTv8XZi63Aj-NuDYhdOhSE0oD446F54q35cmbyBs7WSgGKFlLDsGWNX8F_zjJe5Pyep-i5YX95fB9BVfbJKVSnQNhkCSBFmjUfXs2jQR7s8tjMI54A_YXrB48btVJEZnVfC3qhDRIhVlSfbOxewyDVxXjFnhy7f0XQ3UYamNZHPbt0oHDwzRSEQ_OiFmSSegIhvs-w2A00wvl8E25ZogRVTzRxrMjQZyxo1pc-7Qfpa5gobb4t5EPPDr8rbIiOqhPBqkTO2QElRrsfrc3bPTp1zw7jxUagWKAkQ1hHo4E3Ywewx-fftcACSmKOtdRlhriZI4ZAq1P0OYJJ1elWOKQ6FPGegp_qIHhsvcwKsEkDQ82mum1wTnm3XhsZ9q6X9SWlT1Onkf-gLsyAip_34xY5zt3AMUfwZbB_EQj9TAktXZL6JvpcHIozlgKOYby0H4LnereeJZ1j_JcrWJqydMtT9te8w5v6A605IJ77BKznA3KijL8HRgUqZHALeMynXiEl6wzt4a2nYbqa9SOAGBuwVrBjg4l6-0vM7a-DEas5BXQl3N5JcE5XHT4ZNX5KYxebCcckw-7qMLfOEGwywOvzCNWVxxEWde3rWRbvfPZ2uh4E9d9KIL0nhqOXdCk0gEGvkowrLnd4GKHm75f6PmzFB4UrEBfuYjmdqEYUNfw9I0ZWmDFiyWJGxxFR-nQ-drJkbo7_SCwWCTw5QAeS4YDTGXUDUDWs2GrzlUFf6YITPd4NYzAdH135oQQBSgfAC3I4SyE1DFzLuDKUNPteY7U9B5Tx3yBZjV6M82v7iC86wrb6-kp2zkPlJ_e63-mwWX1TfHxVII1lOx4p3bUIKyFPAs-vggmQBzvFsMrvxOkkp1_YaFamneykiOvm7mVZmmx9sGGegdRD6zW4NGNay-l7zDDTYG2231FdKFEPm3IyWLscrunkJyOSbwUoDXZRD4XSecRkAlRV0CeIt1_wXINhsjV3wf8efRzmndCdfrV4QhZ3lIM3-3Y-gGx3HoxWWcjjpHMCIN5bOgo9EsVDC6fWEstYQwE7NVjndpOAh5fccUJFMIhnx3WYjMyv2HNu_yEgqYt93bzfIxYKLc0dq_jKAqDcMLVJpkCtd5sDg8FA3MQYLStMKkNLPc5s"
APP_KEY = "upat648kujqnjlb"
APP_SECRET = "49cpul9npdx0kgf"


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
