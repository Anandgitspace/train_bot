from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"  # Make sure Rasa is running!

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.form["message"]
    
    response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
    
    messages = response.json()
    bot_reply = "Please reach out to customer care on 000-000-00 for further assistance."
    
    if messages:
        bot_reply = messages[0].get("text", bot_reply)
    
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, port=5500)
