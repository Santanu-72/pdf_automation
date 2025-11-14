import streamlit as st
import requests

st.title("PDF Upload → Email Sender")

# ✅ USE YOUR PRODUCTION N8N WEBHOOK URL HERE
WEBHOOK_URL = "http://localhost:5678/webhook/send-pdf-email"

email = st.text_input("Enter your Email")
pdf_file = st.file_uploader("Upload PDF", type="pdf")

if st.button("Send Email"):
    if not email:
        st.error("Please enter your email.")
    elif not pdf_file:
        st.error("Please upload a PDF file.")
    else:
        files = {
            "file": (pdf_file.name, pdf_file.getbuffer(), "application/pdf")
        }
        data = {
            "email": email
        }

        try:
            response = requests.post(WEBHOOK_URL, data=data, files=files)
            st.success(f"Response: {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")

