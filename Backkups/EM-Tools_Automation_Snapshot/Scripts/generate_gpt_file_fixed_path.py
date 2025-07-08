import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/DavidM/Dropbox/EM-Tools/.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_PATH = "/Users/DavidM/Dropbox/EM-Tools"
project_track = "LCCA"
version = "v0.02"
filename = f"{version}_{project_track}_ChangeLog.txt"
output_path = os.path.join(BASE_PATH, "Deliverables", project_track, filename)

prompt = f"Create a changelog for version {version} of the {project_track} Tool."

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)

output_text = response.choices[0].message.content.strip()
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w") as f:
    f.write(output_text)

print(f"✅ File generated: {output_path}")
