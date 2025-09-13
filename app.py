import streamlit as st
from openai import OpenAI

# Load API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="🤖 Allan AI Chat", layout="centered")
st.title("🤖 Allan AI Chat")

# --- Store chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a highly intelligent, friendly AI assistant. "
                                      "You explain things clearly, give detailed answers, and "
                                      "can adapt your tone depending on the user. "
                                      "Always try to be helpful and engaging."},
        {"role": "assistant", "content": "Hello! 👋 I'm your AI assistant. How can I help you today?"}
    ]

# --- Show chat history ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"🤖 **AI:** {msg['content']}")

# --- Input box ---
prompt = st.chat_input("Type your message...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Query OpenAI with smarter model
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o",  # upgraded from gpt-4o-mini
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content

    # Add AI reply
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Refresh page to show new messages
    st.rerun()
