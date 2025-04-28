import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# Sample text emotion data
emotion_data = [
    "Happy", "Happy", "Neutral", "Sad", "Angry", "Happy", "Sad", "Happy",
    "Happy", "Happy", "Happy", "Sad", "Happy", "Angry", "Fear", "Happy"
]

# Creating a DataFrame
df = pd.DataFrame({'Emotion': emotion_data})

# Convert emotion labels to numeric values
le = LabelEncoder()
df['Emotion_Encoded'] = le.fit_transform(df['Emotion'])

# Using Isolation Forest to detect anomalies
model = IsolationForest(contamination=0.15, random_state=42)
df['Anomaly'] = model.fit_predict(df[['Emotion_Encoded']])

# Converting anomaly result: -1 means anomaly, 1 means normal
df['Anomaly_Label'] = df['Anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')

# Saving data to CSV
df.to_csv('text_emotion_anomalies.csv', index=False)

# Display result
print(df)