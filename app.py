import streamlit as st
from openai import OpenAI

st.title("🤖 My AI Assistant")

# Connect to OpenAI with your secret key (from Streamlit Secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Chat input
user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=400,
    )
    st.write(response.choices[0].message.content)
