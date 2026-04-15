import streamlit as st
from stt import transcribe_audio
from intent import detect_intent
from tools import handle_intent

st.title("Voice AI Agent")

uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file)

st.subheader("Transcription")

transcription = None
intent_result = None
action_result = None

if uploaded_file is not None:
    import tempfile
    import os
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_path = tmp.name
    
    try:
        transcription = transcribe_audio(temp_path)
        st.write(transcription)
    except Exception as e:
        st.error(f"Transcription error: {str(e)}")
else:
    st.write("...")

st.subheader("Intent")

if transcription:
    try:
        intent_result = detect_intent(transcription)
        st.write(intent_result)
    except Exception as e:
        st.error(f"Intent detection error: {str(e)}")
else:
    st.write("...")

st.subheader("Action")

if intent_result:
    action_result = handle_intent(intent_result, transcription)
    st.write(action_result)
else:
    st.write("...")

st.subheader("Output")
st.write("...")
