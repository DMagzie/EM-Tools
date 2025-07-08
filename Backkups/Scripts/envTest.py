from dotenv import load_dotenv
import os

# Explicitly point to the .env file in the EM-Tools root
load_dotenv(dotenv_path="/Users/DavidM/Dropbox/EM-Tools/.env")

openai_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")

print("OPENAI_API_KEY:", "Loaded ✅" if openai_key else "Missing ❌")
print("GITHUB_TOKEN:", "Loaded ✅" if github_token else "Missing ❌")
print("DEBUG: OPENAI_API_KEY =", repr(openai_key))  # For debugging hidden characters
