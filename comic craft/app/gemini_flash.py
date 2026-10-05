import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_story(prompt: str) -> str:
    """
    Generate a comic story using Gemini Flash.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    result = generate_story(
        "Create a short comic story about a young hero who discovers a magical forest."
    )

    print("\n--- Generated Comic Story ---\n")
    print(result)