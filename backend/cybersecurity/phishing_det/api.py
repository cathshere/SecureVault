from flask import Flask, request, jsonify, render_template
from email_analyzer import analyze_email

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

    return render_template(
        "reports.html",
        active_page="reports"
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

    data = request.get_json()

    if not data or "email" not in data:
        return jsonify({
            "error": "No email content provided."
        }), 400

    report = analyze_email(data["email"])

    return jsonify(report)


# ======================================================
# Run Server
# ======================================================
if __name__ == "__main__":
    app.run(debug=True)
