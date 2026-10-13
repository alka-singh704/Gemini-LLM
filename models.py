#GEMINI API FUNCTION
from google import genai
import os

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

def generate_content(text):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=text
    )
    return response.text