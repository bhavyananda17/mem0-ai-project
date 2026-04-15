import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment. Please set it in .env file")

genai.configure(api_key=api_key)

def detect_intent(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Classify the intent of this text into ONE of: create_file, write_code, summarize, chat. Respond with only the word.\n\nText: {text}")
    return response.text.strip().lower()
