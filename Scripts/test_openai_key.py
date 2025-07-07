import openai
import os

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test if the API key works by making a simple request using the old API format
try:
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Switch to gpt-3.5-turbo (instead of deprecated text-davinci-003)
        prompt="Hello, OpenAI! Test my API key.",
        max_tokens=50
    )
    print("API Key is working. Response:", response.choices[0].text.strip())
except Exception as e:
    print("Error with the API key:", e)
