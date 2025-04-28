# health_advisor.py

import pandas as pd

def generate_health_advice(row):
    advice = []

    # Basic rules (you can modify or extend this logic)
    if 'Heart Rate' in row and row['Heart Rate'] > 100:
        advice.append("High heart rate detected. Consider relaxation or hydration.")
    if 'Steps' in row and row['Steps'] < 1000:
        advice.append("Low physical activity. Try to move more.")
    if 'Sleep Quality' in row and row['Sleep Quality'] == 'Bad':
        advice.append("Poor sleep quality. Maintain a consistent sleep schedule.")
    if 'Text Emotion' in row and row['Text Emotion'] in ['sadness', 'anger', 'fear']:
        advice.append(f"Detected negative emotion ({row['Text Emotion']}). Talk to someone or try calming activities.")
    if 'Voice Emotion' in row and row['Voice Emotion'] in ['sadness', 'anger', 'fear']:
        advice.append(f"Voice suggests stress ({row['Voice Emotion']}). Take a break or meditate.")

    if not advice:
        advice.append("All health metrics are within normal range.")

    return " | ".join(advice)

# Load the combined health data
try:
    df = pd.read_csv('combined_health_data.csv')
except FileNotFoundError:
    print("Error: combined_health_data.csv not found. Make sure the file is in the same folder.")
    exit()

# Generate advice for each row
df['Health Advice'] = df.apply(generate_health_advice, axis=1)

# Save to a new CSV
df.to_csv('combined_health_with_advice.csv', index=False)
print("Health advice generated and saved to combined_health_with_advice.csv")
print(df[['Heart Rate', 'Steps', 'Sleep Quality', 'Text Emotion', 'Voice Emotion', 'Health Advice']].head())