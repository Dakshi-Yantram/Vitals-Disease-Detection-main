def analyze_vitals(vitals):
    alerts = []
    risk = "LOW"

    if vitals.get("spo2", 100) < 90:
        alerts.append("Low SpO2")
        risk = "HIGH"

    if vitals.get("heart_rate", 70) > 120:
        alerts.append("High Heart Rate")
        risk = "HIGH"

    return {
        "risk_level": risk,
        "alerts": alerts,
        "stability": "UNSTABLE" if risk == "HIGH" else "STABLE"
    }
