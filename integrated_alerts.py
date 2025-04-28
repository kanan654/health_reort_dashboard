import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
from sklearn.mixture import GaussianMixture

# Load data from CSV
def load_user_data(filename):
    try:
        df = pd.read_csv(filename)
        df = df.sort_values(by='Timestamp') if 'Timestamp' in df.columns else df
        return df
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return pd.DataFrame()

# Calculate average and std deviation
def calculate_baseline(user_data, metrics=['Heart Rate', 'Steps']):
    baseline = {}
    for metric in metrics:
        if metric in user_data.columns:
            baseline[metric] = {
                'mean': user_data[metric].mean(),
                'std': user_data[metric].std()
            }
    return baseline

# Alert based on threshold
def check_for_health_issues_threshold(baseline, current_reading):
    alerts = []
    for metric, stats in baseline.items():
        if metric in current_reading:
            value = current_reading[metric]
            if value < stats['mean'] - 2 * stats['std'] or value > stats['mean'] + 2 * stats['std']:
                alerts.append(f"{metric} is abnormal: {value}")
    return alerts

# Alert using SVM
def check_for_health_issues_svm(user_data, current_reading, features=['Heart Rate', 'Steps']):
    alerts = []
    model = OneClassSVM(gamma='auto').fit(user_data[features])
    current_array = np.array([current_reading[feature] for feature in features]).reshape(1, -1)
    prediction = model.predict(current_array)
    if prediction[0] == -1:
        alerts.append(f"SVM Anomaly Alert: {current_reading}")
    return alerts

# Alert using LOF
def check_for_health_issues_lof(user_data, current_reading, features=['Heart Rate', 'Steps']):
    alerts = []
    model = LocalOutlierFactor(n_neighbors=20)
    X = user_data[features]
    model.fit(X)
    current_array = np.array([current_reading[feature] for feature in features]).reshape(1, -1)
    prediction = model.fit_predict(np.vstack([X, current_array]))
    if prediction[-1] == -1:
        alerts.append(f"LOF Anomaly Alert: {current_reading}")
    return alerts

# Alert using GMM
def check_for_health_issues_gmm(user_data, current_reading, features=['Heart Rate', 'Steps'], threshold_percentile=10):
    alerts = []
    gmm = GaussianMixture(n_components=1)
    X_train = user_data[features]
    gmm.fit(X_train)

    log_likelihood = gmm.score_samples(X_train)
    threshold = np.percentile(log_likelihood, threshold_percentile)

    current_array = np.array([[current_reading[feature] for feature in features]])
    current_score = gmm.score_samples(current_array)[0]

    if current_score < threshold:
        alerts.append(f"GMM Anomaly Alert: {current_reading}")
    return alerts

# Dummy text anomaly function (replace with actual logic)
def detect_text_anomaly(text="I'm tired and dizzy."):
    keywords = ['dizzy', 'tired', 'pain', 'weak']
    for word in keywords:
        if word in text.lower():
            return text
    return None

# Dummy voice anomaly function (replace with actual logic)
def detect_voice_anomaly(audio_path="sample_voice.wav"):
    # Placeholder for actual voice emotion detection
    return "Detected negative emotion from voice"

# ----------- Main execution starts here -------------

filename = "wearable_data.csv"
user_data = load_user_data(filename)

# Simulate current input
current_reading = {
    'Heart Rate': 92,
    'Steps': 2500
}

baseline = calculate_baseline(user_data)
health_alerts = []
health_alerts.extend(check_for_health_issues_threshold(baseline, current_reading))
health_alerts.extend(check_for_health_issues_svm(user_data, current_reading))
health_alerts.extend(check_for_health_issues_lof(user_data, current_reading))
health_alerts.extend(check_for_health_issues_gmm(user_data, current_reading))

# Emotion detection
text_alert = detect_text_anomaly()
voice_alert = detect_voice_anomaly()

# Combine and display alerts
all_alerts = []
all_alerts.extend(health_alerts)
if text_alert:
    all_alerts.append(f"Text Emotion Alert: {text_alert}")
if voice_alert:
    all_alerts.append(f"Voice Emotion Alert: {voice_alert}")

if all_alerts:
    print("\n--- ALERTS TRIGGERED ---")
    for alert in all_alerts:
        print(alert)

    # Save alerts to CSV
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert_entries = [{'Timestamp': timestamp, 'Alert': a} for a in all_alerts]
    alert_df = pd.DataFrame(alert_entries)
    
    # Append to CSV file
    try:
        existing_df = pd.read_csv("alert_logs.csv")
        updated_df = pd.concat([existing_df, alert_df], ignore_index=True)
        updated_df.to_csv("alert_logs.csv", index=False)
    except FileNotFoundError:
        alert_df.to_csv("alert_logs.csv", index=False)
else:
    print("No health or emotion anomalies detected.")
