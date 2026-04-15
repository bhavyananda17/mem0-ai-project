from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(file_path):
    try:
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        text = transcript.text.strip()
        if not text:
            raise ValueError("Transcription returned empty text")
        return text
    except Exception as e:
        raise Exception(f"Transcription failed: {str(e)}")
