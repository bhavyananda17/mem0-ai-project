import streamlit as st

st.title("Voice AI Agent")

uploaded_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file)

st.subheader("Transcription")
st.write("...")

st.subheader("Intent")
st.write("...")

st.subheader("Action")
st.write("...")

st.subheader("Output")
st.write("...")
