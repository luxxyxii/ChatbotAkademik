from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import Chatbot
import os

app = Flask(__name__)
CORS(app)

bot = Chatbot()

@app.route("/", methods=["GET"])
def home():
    return "Chatbot Asisten Deadline API is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    response = bot.get_response(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
