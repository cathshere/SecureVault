import requests
import time

API_KEY = "YOUR_API_KEY"


def check_url(url):

    # Simulation mode for testing
    if "phishing-demo.local" in url:
        return {
            "malicious": 8,
            "suspicious": 2
        }

    headers = {
        "x-apikey": API_KEY
    }

    submit_url = "https://www.virustotal.com/api/v3/urls"

    try:
        # Submit URL
        response = requests.post(
            submit_url,
            headers=headers,
            data={"url": url}
        )

        data = response.json()

        analysis_id = data["data"]["id"]

        # Wait for analysis
        time.sleep(3)

        report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

        report_response = requests.get(
            report_url,
            headers=headers
        )

        report = report_response.json()

        stats = report["data"]["attributes"]["stats"]

        return {
            "malicious": stats["malicious"],
            "suspicious": stats["suspicious"]
        }

    except:
        return {
            "malicious": "Unknown",
            "suspicious": "Unknown"
        }