import streamlit as st
import Translation
import Languages

st.title("Translation App")

# Getting the API KEY:
api_key = st.text_input("API KEY: ", type = 'password' , key = 'password')

Translation.set_key(api_key)

# Language selection
Languages.source_lang = st.selectbox("Select source language", ("English", "Spanish", "French", "German", "Hindi"))
Languages.dest_lang = st.selectbox("Select target language", ("English", "Spanish", "French", "German", "Hindi"))

# Text input
text = st.text_area("Enter text to translate")

# print(Languages.source_lang)
# print(Languages.dest_lang)
# print("\n")


# Translate button
if st.button("Translate"):
    if text:
        st.success(f"Original text ({Languages.source_lang}): {text}")
        st.success(f"Translated text ({Languages.dest_lang}): {Translation.collect_messages(text)}")
    else:
        st.warning("Please enter some text to translate.")