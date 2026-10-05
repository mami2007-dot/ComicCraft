import os
import base64
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


def generate_image(prompt: str, output_path: str) -> str:
    """
    Generate a comic image using Gemini Flash Image.
    """

    interaction = client.interactions.create(
        model="gemini-3.1-flash-image",
        input=prompt,
        response_format={
            "type": "image",
            "aspect_ratio": "1:1",
            "image_size": "1K"
        }
    )

    if not interaction.output_image:
        raise RuntimeError("Gemini did not return an image")

    image_data = base64.b64decode(interaction.output_image.data)

    with open(output_path, "wb") as f:
        f.write(image_data)

    return output_path


if __name__ == "__main__":
    output_file = "static/panels/test_panel.png"

    os.makedirs("static/panels", exist_ok=True)

    result = generate_image(
        "Create a colorful comic book panel showing a young hero "
        "discovering a magical forest for the first time. "
        "Dynamic comic-book artwork, expressive character, "
        "detailed background, vibrant lighting.",
        output_file
    )

    print("\n--- Comic Image Generated Successfully ---")
    print(f"Image saved to: {result}")