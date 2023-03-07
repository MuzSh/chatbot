import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you doing today?", "Hi %1, nice to meet you!"]
    ],
    [
        r"what is your name?",
        ["My name is Gene, the greatest bot ever!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No worries", "Don't apologize"]
    ],
    [
        r"hi|hello|hey",
        ["Hey there, how can I help you?", "Hi, what's on your mind?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye, have a great day!", "Bye for now"]
    ]
]
chatbot = Chat(pairs, reflections)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form.get("text", "")
    response = chatbot.respond(message)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
