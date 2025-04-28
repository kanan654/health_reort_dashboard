import pandas as pd
import numpy as np

def generate_emotion_data():
    emotions = ['Happy', 'Stressed', 'Sad', 'Relaxed']
    emotion_labels = np.random.choice(emotions, 80)
    emotion_score = [np.random.uniform(0, 1) for _ in range(80)]

    df = pd.DataFrame({
        'Emotion': emotion_labels,
        'Stress Score': emotion_score
    })
    df.to_csv("emotion_data.csv", index=False)
    return df


if __name__ == "__main__": 
    df = generate_emotion_data()
    print(df.head())