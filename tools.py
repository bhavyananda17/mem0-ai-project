import google.generativeai as genai
import os
from dotenv import load_dotenv
from utils import ensure_output_folder, get_timestamped_filename

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment. Please set it in .env file")

genai.configure(api_key=api_key)

def handle_intent(intent, text):
    try:
        ensure_output_folder()
        model = genai.GenerativeModel("gemini-pro")
        
        if intent == "create_file":
            filename = get_timestamped_filename("generated_file.txt")
            with open(filename, "w") as f:
                f.write(text)
            return f"✓ File created: {filename}"
        
        elif intent == "write_code":
            response = model.generate_content(f"Generate Python code based on this request: {text}\n\nRespond with only the code, no explanation.")
            code = response.text
            filename = get_timestamped_filename("generated_code.py")
            with open(filename, "w") as f:
                f.write(code)
            return f"✓ Code generated and saved to {filename}"
        
        elif intent == "summarize":
            response = model.generate_content(f"Summarize this text concisely: {text}")
            summary = response.text
            return f"Summary:\n{summary}"
        
        elif intent == "chat":
            response = model.generate_content(text)
            return response.text
        
        return "Unknown intent"
    except Exception as e:
        raise Exception(f"Action handler failed: {str(e)}")
