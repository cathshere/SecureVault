def detect_keywords(text):

    text = text.lower()

    score = 0
    tactics = []

    # Urgency
    urgency_words = [
        "urgent",
        "immediately",
        "24 hours",
        "within 24 hours",
        "as soon as possible",
        "expires today"
    ]

    if any(word in text for word in urgency_words):
        score += 20
        tactics.append("Urgency")

    # Credential Theft
    credential_words = [
        "verify",
        "confirm",
        "login",
        "sign in",
        "account",
        "credentials"
    ]

    if any(word in text for word in credential_words):
        score += 20
        tactics.append("Credential Theft")

    # Password Harvesting
    password_words = [
        "password",
        "reset password",
        "update password",
        "change password"
    ]

    if any(word in text for word in password_words):
        score += 20
        tactics.append("Password Harvesting")

    # Click Bait
    click_words = [
        "click here",
        "click below",
        "open link",
        "follow this link"
    ]

    if any(word in text for word in click_words):
        score += 15
        tactics.append("Click Bait")

    # Fear / Threat
    fear_words = [
        "suspended",
        "disabled",
        "locked",
        "failure",
        "terminated",
        "blocked"
    ]

    if any(word in text for word in fear_words):
        score += 15
        tactics.append("Fear")

    # Brand Impersonation
    brand_words = [
        "microsoft",
        "office 365",
        "google",
        "paypal",
        "amazon",
        "bank"
    ]

    if any(word in text for word in brand_words):
        score += 15
        tactics.append("Brand Impersonation")

    return min(score, 100), list(set(tactics))
