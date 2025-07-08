
import openai
import os
import git
from datetime import datetime

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define the folder path for Deliverables
GITHUB_REPO_PATH = "/Users/DavidM/Dropbox/EM-Tools"  # Path to your local GitHub repo
DELIVERABLES_PATH = os.path.join(GITHUB_REPO_PATH, 'Deliverables')  # Save in the Deliverables folder

# Initialize the git repository
repo = git.Repo(GITHUB_REPO_PATH)
origin = repo.remotes.origin

# Function to generate text using OpenAI
def generate_file(prompt, file_name):
    try:
        # Generate content with OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or use another engine like "gpt-3.5-turbo"
            prompt=prompt,
            max_tokens=500
        )

        # Get the generated text
        generated_text = response.choices[0].text.strip()

        # Save the file in the Deliverables directory
        file_path = os.path.join(DELIVERABLES_PATH, file_name)
        with open(file_path, 'w') as file:
            file.write(generated_text)
        
        print(f"File generated and saved as {file_name}")
        return file_path
    except Exception as e:
        print(f"Error generating file: {e}")
        return None

# Function to commit and push the file to GitHub
def commit_and_push(file_path):
    try:
        # Add the file to git
        repo.git.add(file_path)
        
        # Commit the file
        commit_msg = f"Automated commit for {os.path.basename(file_path)}"
        repo.index.commit(commit_msg)
        
        # Push to GitHub
        origin.push()
        print(f"File {file_path} committed and pushed to GitHub.")
    except Exception as e:
        print(f"Error committing and pushing: {e}")

# Main function
def main():
    # Example prompt for the file generation
    prompt = "Please generate a summary for the LCCA tool v0.01"
    file_name = f"v0.01_LCCA_Tool_Summary_{datetime.now().strftime('%Y-%m-%d')}.txt"  # Example file name
    
    # Generate the file with OpenAI
    file_path = generate_file(prompt, file_name)

    # If the file was generated successfully, commit and push it
    if file_path:
        commit_and_push(file_path)

if __name__ == "__main__":
    main()
