from flask import Flask, request, jsonify
from email_analyzer import analyze_email

app = Flask(__name__)

@app.route("/")
def home():
    return "PhishMind API is running!"

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    email_text = data["email"]

    report = analyze_email(email_text)

    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)