import os
import base64
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path="/Users/DavidM/Dropbox/EM-Tools/.env")

# Get GitHub environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH")
COMMIT_MESSAGE = "Add .docx version of project README"

# Set local and GitHub paths
local_path = "/Users/DavidM/Dropbox/EM-Tools/docs/EM-Tools_ReadMe_Snapshot.docx"
github_path = "EM-Tools/docs/EM-Tools_ReadMe_Snapshot.docx"
api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{github_path}"

# Read file and encode as base64
with open(local_path, "rb") as file:
    encoded_content = base64.b64encode(file.read()).decode("utf-8")

# Set request headers
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# Check if file exists to get SHA
response = requests.get(api_url, headers=headers)
sha = response.json().get("sha") if response.status_code == 200 else None

# Prepare data payload
data = {
    "message": COMMIT_MESSAGE,
    "content": encoded_content,
    "branch": GITHUB_BRANCH,
}
if sha:
    data["sha"] = sha

# Upload the file
upload_response = requests.put(api_url, headers=headers, json=data)

# Output the result
if upload_response.status_code in [200, 201]:
    print("✅ Upload successful!")
else:
    print(f"❌ Upload failed: {upload_response.status_code}")
    print(upload_response.json())
