import tempfile
import os
from datetime import datetime

def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name

def ensure_output_folder():
    if not os.path.exists("output"):
        os.makedirs("output")

def get_timestamped_filename(base_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = os.path.splitext(base_name)
    return f"output/{name}_{timestamp}{ext}"
