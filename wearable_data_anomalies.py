import pandas as pd
from sklearn.ensemble import IsolationForest
import os  # Import os to check the working directory

# Load data from wearable_data.csv
df = pd.read_csv('wearable_data.csv')

# Check for missing values
print(df.isnull().sum())

# Optionally handle missing values
df = df.dropna()  # Drop rows with missing values

# Convert 'Sleep Quality' to numeric
sleep_map = {'Good': 2, 'Okay': 1, 'Bad': 0}
df['Sleep Score'] = df['Sleep Quality'].map(sleep_map)

# Ensure features are numeric
df['Heart Rate'] = pd.to_numeric(df['Heart Rate'], errors='coerce')
df['Steps'] = pd.to_numeric(df['Steps'], errors='coerce')

# Features used for anomaly detection
features = ['Heart Rate', 'Steps', 'Sleep Score']

# Isolation Forest Model
model = IsolationForest(contamination=0.1, random_state=42)
df['Anomaly'] = model.fit_predict(df[features])

# Label anomalies: -1 = Anomaly
print(df[['Heart Rate', 'Steps', 'Sleep Score', 'Anomaly']])

# Check current working directory
print("Current Working Directory:", os.getcwd())

# Save the DataFrame with anomalies to a new CSV file
print("Saving DataFrame to CSV...")
df.to_csv('wearable_data_with_anomalies.csv', index=False)
print("CSV file saved successfully.")
    # Save to CSV
data = {'voice': [sample_voice], 'Detected Emotion': [emotion]}
df = pd.DataFrame(data)
df.to_csv("voice_emotion_output.csv", index=False)
