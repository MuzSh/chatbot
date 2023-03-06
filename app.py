import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, render_template

app = Flask(__name__)

pairs = [
    r"my name i s(.*)",
    ["hello%1, how are you today?. hey %1 how's it going?"]
],
[
    r"what is your name?",
    ["My name is gene, the greatest bot, nice to meet you"]
],
[
    r"sorry(.*)",
    ["It's alright", "It's okay", "never give up"]
],
[
    r"hey",
    ["hey what's up?"]
],
[
    r"quit",
    ["goodbye", "thank you, come again", "nice to meet you", "have a great day"]   
]

chatbot = Chat(pairs, reflections)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/chat",methods = ["POST"])

def chat():
    message = request.form["text"]
    response = chatbot.respond(message)
    return response

if __name__ == '__main__':
    app.run()