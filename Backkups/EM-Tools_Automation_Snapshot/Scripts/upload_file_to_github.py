import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/DavidM/Dropbox/EM-Tools/.env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH")
COMMIT_MESSAGE = os.getenv("COMMIT_MESSAGE")
GITHUB_FILE_PATH_LCCA = os.getenv("GITHUB_FILE_PATH_LCCA")

project_track = "LCCA"
version = "v0.02"
filename = f"{version}_{project_track}_ChangeLog.txt"
local_path = f"/Users/DavidM/Dropbox/EM-Tools/Deliverables/{project_track}/{filename}"
github_path = f"{GITHUB_FILE_PATH_LCCA}{filename}"

api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{github_path}"

with open(local_path, "rb") as f:
    content = base64.b64encode(f.read()).decode("utf-8")

headers = {"Authorization": f"token {GITHUB_TOKEN}"}
response = requests.get(api_url, headers=headers)
sha = response.json().get("sha") if response.status_code == 200 else None

data = {
    "message": COMMIT_MESSAGE.replace("${PROJECT_TRACK}", project_track),
    "content": content,
    "branch": GITHUB_BRANCH,
}
if sha:
    data["sha"] = sha

response = requests.put(api_url, headers=headers, json=data)

if response.status_code in [200, 201]:
    print(f"✅ File uploaded to GitHub: {github_path}")
else:
    print(f"❌ Upload failed with status {response.status_code}")
    print(response.json())
