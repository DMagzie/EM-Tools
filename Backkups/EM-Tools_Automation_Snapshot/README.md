# EM-Tools Automation Snapshot

This snapshot contains all necessary Python scripts, .env setup, and instructions to create an end-to-end automation loop for:

- Generating deliverables with OpenAI
- Storing in Dropbox-organized folders
- Uploading to GitHub via REST API

## Folder Structure

EM-Tools/
├── Scripts/
│   ├── envTest.py
│   ├── generate_gpt_file_fixed_path.py
│   └── upload_file_to_github.py
├── .env.template
├── .gitignore
└── README.md

## Setup Instructions

1. **Install Requirements**
```bash
pip install openai python-dotenv requests
```

2. **Create `.env` from Template**
Duplicate `.env.template` and fill in your actual keys:
```bash
cp .env.template .env
```

3. **Run Environment Check**
```bash
python3 Scripts/envTest.py
```

4. **Generate Deliverable**
```bash
python3 Scripts/generate_gpt_file_fixed_path.py
```

5. **Upload to GitHub**
```bash
python3 Scripts/upload_file_to_github.py
```

## Diagram

```
[ OpenAI ] ---> [ Local Script ] ---> [ Dropbox/EM-Tools/Deliverables/ ]
                                   |
                                   v
                              [ GitHub Repo ]
```

Make sure `.env` is excluded from Git with `.gitignore`.
