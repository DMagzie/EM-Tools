import openai
import os

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test if the API key works by making a simple request using the new API format
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Can you confirm my OpenAI API key is working?"}
        ]
    )
    print("API Key is working. Response:", response['choices'][0]['message']['content'])
except Exception as e:
    print("Error with the API key:", e)
