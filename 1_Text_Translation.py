import streamlit as st

st.title("Translation App")

# Language selection
source_lang = st.selectbox("Select source language", ("English", "Spanish", "French", "German"))
target_lang = st.selectbox("Select target language", ("English", "Spanish", "French", "German"))

# Text input
text = st.text_area("Enter text to translate")

# Translate button
if st.button("Translate"):
    if text:
        st.success(f"Original text ({source_lang}): {text}")
        st.success(f"Translated text ({target_lang}): Translation output")
    else:
        st.warning("Please enter some text to translate.")
