import gradio as gr
from transformers import pipeline

# Load an open-source chatbot model (Mistral-7B is strong and free to use)
chatbot = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    device_map="auto"
)

# Chat function with history
def chat(message, history):
    history = history or []
    prompt = "".join([f"User: {u}\nAI: {a}\n" for u, a in history])
    prompt += f"User: {message}\nAI:"

    response = chatbot(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )[0]["generated_text"]

    # Extract only AI's answer (strip out the prompt)
    answer = response.split("AI:")[-1].strip()
    history.append((message, answer))
    return answer, history

# Gradio Chat UI
demo = gr.ChatInterface(
    fn=chat,
    title="My AI Chatbot 🤖",
    description="An open-source chatbot powered by Mistral 7B. Works like ChatGPT!"
)

demo.launch()
