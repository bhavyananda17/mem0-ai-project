import streamlit as st
from stt import transcribe_audio
from intent import detect_intent
from tools import handle_intent
from utils import save_uploaded_file
import os
from dotenv import load_dotenv

load_dotenv()

st.title("Voice AI Agent")

api_key = os.getenv("GEMINI_API_KEY")
if api_key and api_key != "your_api_key_here":
    with st.sidebar:
        st.success("✓ API Key loaded")
else:
    with st.sidebar:
        st.error("✗ API Key not configured")

if "transcription" not in st.session_state:
    st.session_state.transcription = None
if "intent_result" not in st.session_state:
    st.session_state.intent_result = None
if "action_result" not in st.session_state:
    st.session_state.action_result = None

uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file)
    temp_path = save_uploaded_file(uploaded_file)

st.subheader("Transcription")

if uploaded_file is not None:
    try:
        st.session_state.transcription = transcribe_audio(temp_path)
        st.write(st.session_state.transcription)
    except Exception as e:
        st.error(f"Transcription error: {str(e)}")
else:
    st.write("...")

st.subheader("Intent")

if st.session_state.transcription:
    try:
        st.session_state.intent_result = detect_intent(st.session_state.transcription)
        st.write(f"**Detected:** {st.session_state.intent_result}")
    except Exception as e:
        st.error(f"Intent detection error: {str(e)}")
else:
    st.write("...")

st.subheader("Action")

if st.session_state.intent_result:
    try:
        st.session_state.action_result = handle_intent(st.session_state.intent_result, st.session_state.transcription)
        st.success(st.session_state.action_result)
    except Exception as e:
        st.error(f"Action error: {str(e)}")
else:
    st.write("...")

st.subheader("Output")
st.write("...")
