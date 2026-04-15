from openai import OpenAI
import os
from dotenv import load_dotenv
from utils import ensure_output_folder

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from openai import OpenAI
import os
from dotenv import load_dotenv
from utils import ensure_output_folder, get_timestamped_filename

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_intent(intent, text):
    try:
        ensure_output_folder()
        
        if intent == "create_file":
            filename = get_timestamped_filename("generated_file.txt")
            with open(filename, "w") as f:
                f.write(text)
            return f"✓ File created: {filename}"
        
        elif intent == "write_code":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"Generate Python code based on this request: {text}"
                    }
                ]
            )
            code = response.choices[0].message.content
            filename = get_timestamped_filename("generated_code.py")
            with open(filename, "w") as f:
                f.write(code)
            return f"✓ Code generated and saved to {filename}"
        
        elif intent == "summarize":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize this text concisely: {text}"
                    }
                ]
            )
            summary = response.choices[0].message.content
            return f"Summary:\n{summary}"
        
        elif intent == "chat":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": text
                    }
                ]
            )
            return response.choices[0].message.content
        
        return "Unknown intent"
    except Exception as e:
        raise Exception(f"Action handler failed: {str(e)}")
