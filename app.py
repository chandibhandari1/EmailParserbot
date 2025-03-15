import streamlit as st
import main
import os

st.set_page_config(page_title="Email Parser", layout="wide")
st.title("📨 Email Parser Dashboard")

# Initialize database
main.init_db()

# File uploader
uploaded_file = st.file_uploader("Upload email file (.eml)", type="eml")

if uploaded_file:
    # Save uploaded file temporarily
    with open("temp.eml", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Add a "Parse Email" button
    if st.button("Parse Email"):
        # Parse the email
        email_id = main.parse_email("temp.eml")
        st.success(f"Email parsed successfully! ID: {email_id}")
        
        # Remove temporary file
        os.remove("temp.eml")

# Display parsed emails
st.subheader("Parsed Emails")
emails = main.get_parsed_emails()

if emails:
    st.dataframe(
        data=emails,
        columns=["ID", "Subject", "From", "To", "Date", "Attachments"],
        use_container_width=True
    )
else:
    st.info("No emails parsed yet")

