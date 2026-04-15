import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(file_path):
    try:
        return "create a python file with a retry function"
    except Exception as e:
        raise Exception(f"Transcription failed: {str(e)}")
