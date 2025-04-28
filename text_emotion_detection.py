from transformers import pipeline
import pandas as pd
# Load emotion detection pipeline
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def detect_emotion_from_text(text):
    result = emotion_classifier(text)
    return result[0]['label']

if __name__ == "__main__":
    sample_text = "I'm feeling really stressed about this project"
    emotion = detect_emotion_from_text(sample_text)
    print("Detected Emotion:", emotion)

    data = {'Text': [sample_text], 'Detected Emotion': [emotion]}
    df = pd.DataFrame(data)
    df.to_csv("text_emotion_output.csv", index=False)
