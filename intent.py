from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_intent(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Classify the intent of this text into ONE of: create_file, write_code, summarize, chat. Respond with only the word.\n\nText: {text}"
            }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip().lower()
