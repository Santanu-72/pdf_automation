import streamlit as st
import requests

st.title("PDF → Email via n8n")

# Replace with your n8n webhook URL
WEBHOOK_URL = st.secrets.get("N8N_WEBHOOK_URL", "https://REPLACE_WITH_WEBHOOK")

pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
to_email = st.text_input("Recipient Email")
message = st.text_area("Message (optional)")

if st.button("Send via n8n"):
    if not pdf_file:
        st.error("Please upload a PDF file.")
    elif not to_email:
        st.error("Enter recipient email.")
    else:
        with st.spinner("Sending..."):
            files = {"file": (pdf_file.name, pdf_file, "application/pdf")}
            data = {"to_email": to_email, "message": message}
            try:
                resp = requests.post(WEBHOOK_URL, files=files, data=data)
                if resp.status_code == 200:
                    st.success("PDF sent successfully!")
                else:
                    st.error(f"Error: {resp.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")

st.info("Configure your N8N_WEBHOOK_URL in Streamlit Secrets.")

