import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder

# Load the detected emotions CSV file
df = pd.read_csv("voice_emotion_output.csv")

# One-hot encode the emotion labels (e.g., Happy, Sad, etc.)
encoder = OneHotEncoder(sparse_output=False)
encoded_emotions = encoder.fit_transform(df[['Detected Emotion']])

# Fit Isolation Forest on encoded emotions
model = IsolationForest(contamination=0.2, random_state=42)
df['Anomaly'] = model.fit_predict(encoded_emotions)

# Map -1 to "Anomalous", 1 to "Normal"
df['Anomaly Label'] = df['Anomaly'].map({-1: 'Anomalous', 1: 'Normal'})

# Save the results to a new CSV
df.to_csv("voice_emotion_anomalies.csv", index=False)

print("Anomaly detection completed. Output saved to 'voice_emotion_anomalies.csv'")
print(df[['voice', 'Detected Emotion', 'Anomaly Label']].head())