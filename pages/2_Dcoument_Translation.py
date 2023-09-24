import streamlit as st

st.title("Document Translation")

# Language selection
source_lang = st.selectbox("Select source language", ("English", "Spanish", "French", "German"))
target_lang = st.selectbox("Select target language", ("English", "Spanish", "French", "German"))

# Document upload
uploaded_file = st.file_uploader("Upload document", type=["txt", "docx", "pdf"])

# Translate button
if st.button("Translate"):
    if uploaded_file is not None:
        st.success(f"Original document ({source_lang}):")
        content = uploaded_file.read()
        st.code(content)
        st.success(f"Translated document ({target_lang}):")
        st.code("Translation output")
    else:
        st.warning("Please upload a document to translate.")
