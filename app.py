import streamlit as st

st.write("Test audio app")

with open("chopin-valse.ogg", "rb") as f:
    audio_bytes = f.read()

st.audio(audio_bytes, format="audio/ogg")
