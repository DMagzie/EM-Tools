import os
from github import Github
import git
from git.exc import GitCommandError

# Configuration: Replace these with your details
DROPBOX_FOLDER_PATH = '/Users/DavidM/Dropbox/EM-Tools'  # Path to your Dropbox folder
REPO_NAME = 'EM-Tools'  # Desired name for your GitHub repository

# Fetch GitHub token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Check if the GITHUB_TOKEN environment variable is set
if not GITHUB_TOKEN:
    raise ValueError("GitHub token is not set in the environment variables!")

# Step 1: Initialize the local Git repository in the Dropbox folder
def initialize_git_repo(folder_path):
    try:
        print(f"Initializing Git repository in {folder_path}...")
        repo = git.Repo.init(folder_path)
        print("Git repository initialized.")
        return repo
    except GitCommandError as e:
        print(f"Error initializing Git repo: {e}")
        return None

# Step 2: Create a new repository on GitHub
def create_github_repo(github_token, repo_name):
    try:
        g = Github(github_token)
        user = g.get_user()
        print(f"Creating repository '{repo_name}' on GitHub...")
        repo = user.create_repo(repo_name)
        print(f"GitHub repository '{repo_name}' created.")
        return repo
    except Exception as e:
        print(f"Error creating GitHub repository: {e}")
        return None

# Step 3: Link local repo to GitHub repo and push
def push_to_github(local_repo, github_repo_url, github_token):
    try:
        print(f"Using GitHub URL: {github_repo_url}")

        # Check if the remote 'origin' exists, and set the URL
        if 'origin' in local_repo.remotes:
            origin = local_repo.remotes.origin
            origin.set_url(f"https://{github_token}@github.com/{github_repo_url.split('github.com/')[1]}")
        else:
            origin = local_repo.create_remote('origin', github_repo_url)

        local_repo.git.add(A=True)
        local_repo.index.commit("Initial commit")
        
        print("Pushing to GitHub...")
        local_repo.git.push('--set-upstream', origin, 'main')
        print("Push successful!")
    except GitCommandError as e:
        print(f"Error pushing to GitHub: {e}")

def main():
    # Step 1: Initialize local Git repository
    repo = initialize_git_repo(DROPBOX_FOLDER_PATH)
    
    if repo is None:
        print("Failed to initialize Git repository. Exiting.")
        return
    
    # Step 2: Create GitHub repository
    github_repo = create_github_repo(GITHUB_TOKEN, REPO_NAME)
    
    if github_repo is None:
        print("Failed to create GitHub repository. Exiting.")
        return
    
    # Step 3: Link local repo to GitHub and push (Pass github_token to push_to_github)
    github_repo_url = f"https://github.com/{github_repo.owner.login}/{github_repo.name}.git"
    push_to_github(repo, github_repo_url, GITHUB_TOKEN)  # Passing the token here

if __name__ == "__main__":
    main()
