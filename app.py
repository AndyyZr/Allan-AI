import streamlit as st
from openai import OpenAI

# Load your API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🤖 My AI App")

# Input box
prompt = st.text_input("Ask me something:")

# Button to send
if st.button("Submit") and prompt:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast + cheap model
            messages=[{"role": "user", "content": prompt}]
        )
        st.write(response.choices[0].message.content)
