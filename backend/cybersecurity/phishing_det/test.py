from email_analyzer import analyze_email, save_report

text = input("Paste suspicious email:\n\n")

report = analyze_email(text)



print("Risk Score:", report["risk_score"])

print("Threat Level:", report["threat_level"])

print("\nURLs Found:")

for item in report["url_details"]:
    print("-", item["url"])

print("\nDetected Tactics:")

for tactic in report["tactics"]:
    print("-", tactic)

save_report(report)

print("\nVirusTotal Results:")

for item in report["url_details"]:
    print(item["url"])
    print("Malicious:", item["malicious_engines"])
    print("Suspicious:", item["suspicious_engines"])