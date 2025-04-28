import pandas as pd

# Load all three datasets
wearable = pd.read_csv('wearable_data.csv')
text_emotion = pd.read_csv('text_emotion_output.csv')
voice_emotion = pd.read_csv('voice_emotion_output.csv')

# Make sure all three datasets have the same number of rows
min_len = min(len(wearable), len(text_emotion), len(voice_emotion))
wearable = wearable.iloc[:min_len]
text_emotion = text_emotion.iloc[:min_len]
voice_emotion = voice_emotion.iloc[:min_len]

# Optional: rename columns to distinguish text and voice emotion
text_emotion.rename(columns={'Detected Emotion': 'Text Emotion'}, inplace=True)
voice_emotion.rename(columns={'Detected Emotion': 'Voice Emotion'}, inplace=True)

# Merge all three into one DataFrame
combined = pd.concat([wearable, text_emotion, voice_emotion], axis=1)

# Save to CSV
combined.to_csv('combined_health_data.csv', index=False)

print("combined_health_data.csv created successfully.")
print(combined.head())