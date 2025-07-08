from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv(dotenv_path="/Users/DavidM/Dropbox/EM-Tools/.env")

openai.api_key = os.getenv("OPENAI_API_KEY")

# Parameters
project_track = "LCCA"
version = "v0.02"
filename = f"{version}_{project_track}_ChangeLog.txt"
output_path = os.path.join("Deliverables", project_track, filename)

# Prompt for GPT
prompt = f"Create a changelog for version {version} of the {project_track} Tool."

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)

# Extract response text
output_text = response.choices[0].message.content.strip()

# Ensure output folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write to file
with open(output_path, "w") as f:
    f.write(output_text)

print(f"✅ File generated: {output_path}")
