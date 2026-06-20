# phishing_keywords.py

def detect_keywords(text):

    text = text.lower()

    score = 0

    tactics = []

    if "urgent" in text:
        score += 15
        tactics.append("Urgency")

    if "verify" in text:
        score += 15
        tactics.append("Credential Theft")

    if "password" in text:
        score += 15
        tactics.append("Password Harvesting")

    if "click here" in text:
        score += 15
        tactics.append("Click Bait")

    if "suspended" in text:
        score += 15
        tactics.append("Fear")

    return score, tactics