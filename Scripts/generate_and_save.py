import openai
import os

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate content with ChatGPT (simulate file generation)
def generate_file_content():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can change this to "gpt-4" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, OpenAI! Test my API key."}
        ]
    )
    return response['choices'][0]['message']['content']

# Save the generated content to a file in the Dropbox folder
def save_to_dropbox(content, file_name):
    # Define the path to the Dropbox folder
    dropbox_folder = '/Users/DavidM/Dropbox/EM-Tools/Deliverables/'
    
    # Ensure the folder exists
    if not os.path.exists(dropbox_folder):
        os.makedirs(dropbox_folder)

    # Define the full file path
    file_path = os.path.join(dropbox_folder, file_name)

    # Write the content to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"File saved to Dropbox: {file_path}")

# Main function to generate and save the file
if __name__ == "__main__":
    content = generate_file_content()
    save_to_dropbox(content, "test_file.txt")
