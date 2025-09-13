import streamlit as st
from openai import OpenAI


st.title("🤖 My AI Assistant")

# ✅ This pulls the key you stored in secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

user_input = st.text_input("Ask me anything:")

if st.button("Send") and user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
    )
    st.write(response.choices[0].message.content)
