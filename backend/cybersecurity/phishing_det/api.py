from flask import Flask, request, jsonify, render_template
from email_analyzer import analyze_email
import json
import os

app = Flask(__name__)


# ======================================================
# Dashboard
# ======================================================
@app.route("/")
def dashboard():

    stats = {
        "high_risk": 3,
        "caution": 7,
        "clean": 41,
        "urls_scanned": 58
    }

    return render_template(
        "dashboard.html",
        active_page="dashboard",
        stats=stats
    )


# ======================================================
# PhishGuard
# ======================================================
@app.route("/phishguard")
def phishguard():

    return render_template(
        "phishguard.html",
        active_page="phishguard"
    )


# ======================================================
# URL Scanner
# ======================================================
@app.route("/urlscanner")
def urlscanner():

    return render_template(
        "urlscanner.html",
        active_page="urlscanner"
    )


# ======================================================
# Reports
# ======================================================
@app.route("/reports")
def reports():
    filepath = "reports/report_history.json"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            try:
                report_list = json.load(file)
            except json.JSONDecodeError:
                report_list = []
    else:
        report_list = []

    return render_template(
        "reports.html",
        active_page="reports",
        reports=report_list
    )


# ======================================================
# Settings
# ======================================================
@app.route("/settings")
def settings():

    return render_template(
        "settings.html",
        active_page="settings"
    )


# ======================================================
# Audit Log
# ======================================================
@app.route("/auditlog")
def auditlog():

    return render_template(
        "auditlog.html",
        active_page="auditlog"
    )


# ======================================================
# Email Analyzer API
# ======================================================
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        if not data or "email" not in data:
            return jsonify({"error": "No email content provided."}), 400

        report = analyze_email(data["email"])

        if not report:
            return jsonify({"error": "Analysis failed to produce a report."}), 500

        print("REPORT:", report)
        return jsonify(report)

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# ======================================================
# Run Server
# ======================================================
if __name__ == "__main__":
    app.run(debug=True)
