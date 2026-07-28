from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Read Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def generate_document(user_request):
    """
    Generates a business document using Gemini AI.
    """

    prompt = f"""
    You are a professional business document writer.

    Create a well-structured business document based on the user's request.

    User Request:
    {user_request}

    Include:
    - Title
    - Introduction
    - Main Content
    - Conclusion

    Make the document professional and well formatted.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error while generating document: {str(e)}"