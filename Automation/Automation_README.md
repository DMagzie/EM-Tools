# Automation Scripts – EM Tools

This folder contains utility scripts used to automate deployment, syncing, and repository tasks
for the EM Tools project.

## Scripts

- `automated_file_push.py`  
  Commits all current changes in the project and pushes to the connected GitHub repo.

- `create_github_repo.py`  
  Initializes a new GitHub repository using the GitHub API. Uses the `GITHUB_PAT` from `.env`.

- `upload_file_to_github.py`  
  Uploads one or more individual files to an existing GitHub repo and path via API.

- `upload_to_dropbox.py`  
  Uploads local files or the entire `outputs/` folder to Dropbox under `/EM_Explorer/`.
  Requires `DROPBOX_TOKEN` in `.env`.

---

> ⚠️ These scripts depend on your manually managed `.env` file for secrets.
> Do not commit `.env` or sensitive files to GitHub.
