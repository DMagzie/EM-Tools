from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="/Users/DavidM/Dropbox/EM-Tools/.env")

openai_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")

print("OPENAI_API_KEY:", "Loaded ✅" if openai_key else "Missing ❌")
print("GITHUB_TOKEN:", "Loaded ✅" if github_token else "Missing ❌")
