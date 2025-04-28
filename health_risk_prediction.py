def predict_health_risk(heart_rate, steps, sleep_quality):
    risk_score = 0

    # Heart rate condition
    if heart_rate > 100:
        risk_score += 2
    elif heart_rate < 60:
        risk_score += 1

    # Steps condition
    if steps < 3000:
        risk_score += 2

    # Sleep quality condition
    if sleep_quality < 5:
        risk_score += 2

    # Risk level
    if risk_score >= 5:
        return "High Risk"
    elif risk_score >= 3:
        return "Moderate Risk"
    else:
        return "Low Risk"

# Run the function when file is executed directly
if __name__ == "__main__":
    # Sample test values
    heart_rate = 105
    steps = 2500
    sleep_quality = 4

    risk = predict_health_risk(heart_rate, steps, sleep_quality)
    print("Heart Rate:", heart_rate)
    print("Steps:", steps)
    print("Sleep Quality:", sleep_quality)
    print("Predicted Health Risk Level:", risk)