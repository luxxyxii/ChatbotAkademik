import gradio as gr
import pickle
import json
import random

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

def chatbot_response(message):
    vector = vectorizer.transform([message])
    tag = model.predict(vector)[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "Maaf, saya belum memahami pertanyaan tersebut."

iface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Tanya soal akademik..."),
    outputs="text",
    title="Chatbot Akademik",
    description="Asisten akademik berbasis Machine Learning"
)

iface.launch()
