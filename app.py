# app.py (Streamlit Frontend)
import streamlit as st
import main
import sqlite3

st.set_page_config(page_title="Email Parser", layout="wide")
st.title("📨 Email Parser Dashboard")

uploaded_file = st.file_uploader("Upload email file (.eml)", type="eml")

if uploaded_file:
    with open("temp.eml", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    email_id = main.parse_email("temp.eml")
    st.success(f"Email parsed successfully! ID: {email_id}")

st.subheader("Parsed Emails")
emails = main.get_parsed_emails()

if emails:
    st.dataframe(
        data=emails,
        column_config={
            "id": "ID",
            "subject": "Subject",
            "sender": "From",
            "receiver": "To",
            "timestamp": "Date",
            "attachments": "Attachments"
        },
        use_container_width=True
    )
else:
    st.info("No emails parsed yet")
