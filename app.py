import streamlit as st
from openai import OpenAI

st.title("🤖 My AI Assistant")

# Connect to OpenAI with your secret key (from Streamlit Secrets)
client = OpenAI(api_key=st.secrets["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"])

# Chat input
user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=400,
    )
    st.write(response.choices[0].message.content)
