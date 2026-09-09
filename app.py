import streamlit as st
import requests

st.title(":rainbow[Welcome to Language Translation APP]")

text = st.text_area("Enter your text here:")

webhook_url = "https://shaik5195522.app.n8n.cloud/webhook/daefa7c5-372a-4a0b-a69f-2f37b5396ff6"

if st.button("Hindi", key="Hindi_btn"):
    if text:
        response = requests.post(
            webhook_url,
            json={"input": text, "language": "Hindi"}
        )

        if response.status_code == 200:
    st.write("Response from n8n:")
    st.write(response.json())
else:
    st.error(f"Translation failed: {response.status_code}")
    st.write(response.text)
elif st.button("Telugu", key="Telugu_btn"):
    if text:
        response = requests.post(
            webhook_url,
            json={"input": text, "language": "Telugu"}
        )

        if response.status_code == 200:
    st.write("Response from n8n:")
    st.write(response.json())
else:
    st.error(f"Translation failed: {response.status_code}")
    st.write(response.text)