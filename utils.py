import tempfile
import os

def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name

def ensure_output_folder():
    if not os.path.exists("output"):
        os.makedirs("output")
