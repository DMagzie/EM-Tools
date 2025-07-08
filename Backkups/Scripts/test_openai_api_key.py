import openai
import os

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test if API key works with a basic ChatGPT call
def test_api_key():
    try:
        # Correct API endpoint for chat models (v1/chat/completions)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # This should be a valid model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, OpenAI! Test my API key."}
            ]
        )
        print("API Key is working. Response:", response['choices'][0]['message']['content'])
    except Exception as e:
        print("Error with the API key:", e)

# Run the test
if __name__ == "__main__":
    test_api_key()
