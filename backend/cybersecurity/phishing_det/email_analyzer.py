from phishing_keywords import detect_keywords
from url_checker import extract_urls

import re
import socket
import requests
import json
import os
from urllib.parse import urlparse

from virustotal_api import check_url





# Extract domain from URL
def extract_domain(url):
    return urlparse(url).netloc


# Convert domain to IP address
def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "Unknown"


# Get geolocation details from IP address
def get_location(ip):

    if ip == "Unknown":
        return {
            "country": "Unknown",
            "city": "Unknown",
            "isp": "Unknown"
        }

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")

        data = response.json()

        return {
            "country": data.get("country"),
            "city": data.get("city"),
            "isp": data.get("isp")
        }

    except:
        return {
            "country": "Unknown",
            "city": "Unknown",
            "isp": "Unknown"
        }


# Calculate phishing score and threat level
def calculate_score(text):
    text = text.replace("hxxps://", "https://")
    text = text.replace("hxxp://", "http://")
    text = text.replace("[.]", ".")
    score = 0
    
    urls = extract_urls(text)

    if len(urls) > 0:
        score += 20

    keyword_score, tactics = detect_keywords(text)

    score += keyword_score
    score = min(score, 100)

    if score < 30:
        level = "LOW"

    elif score < 60:
        level = "MEDIUM"

    else:
        level = "HIGH"

    return score, level, tactics


# Main email analysis function
# Main email analysis function
def analyze_email(text):

    text = text.replace("hxxps://", "https://")
    text = text.replace("hxxp://", "http://")
    text = text.replace("[.]", ".")

    score, level, tactics = calculate_score(text)

    urls = extract_urls(text)

    url_details = []

    for url in urls:
        domain = extract_domain(url)
        ip = get_ip(domain)
        location = get_location(ip)
        vt_result = check_url(url)

        url_details.append({
            "url": url,
            "domain": domain,
            "ip": ip,
            "country": location["country"],
            "city": location["city"],
            "isp": location["isp"],
            "malicious_engines": vt_result["malicious"],
            "suspicious_engines": vt_result["suspicious"]
        })

    # moved outside the loop — now this always runs
    report = {
        "risk_score": score,
        "threat_level": level,
        "tactics": tactics,
        "url_details": url_details
    }

    return report

# Save report to JSON file
import uuid
from datetime import datetime, timezone

def save_report(report, email_text="", report_type="phishguard"):
    os.makedirs("reports", exist_ok=True)
    filename = "reports/report_history.json"

    # Load existing history (or start fresh)
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []
    else:
        history = []

    # Build a record matching what reports.html expects
    record = {
        "id": f"rpt_{uuid.uuid4().hex[:8]}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "type": report_type,
        "subject": (email_text[:80] + "...") if len(email_text) > 80 else email_text,
        "risk_score": report["risk_score"],
        "threat_level": report["threat_level"],
        "tactics": report["tactics"],
        "reported_by": "Catherine A.",
        "status": "blocked" if report["threat_level"] == "HIGH"
                  else "flagged" if report["threat_level"] == "MEDIUM"
                  else "clean"
    }

    history.insert(0, record)  # newest first

    with open(filename, "w") as file:
        json.dump(history, file, indent=4)

    print("\nReport saved to history!")
    return record
