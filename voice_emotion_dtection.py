
import librosa
import numpy as np
import pandas as pd  

def extract_voice_features(file_path):
    try:
        y, sr = librosa.load(file_path)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mean_mfccs = np.mean(mfccs.T, axis=0)
        return mean_mfccs
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None

def predict_emotion(features):
    
    if features is not None:
        if features[0] > -200:
            return "Happy"
        else:
            return "Sad"
    return "Unknown"

if __name__ == "__main__": 
    file_path = "sample_voice.wav"  # Use any 5–10 second wav file
    features = extract_voice_features(file_path)
    emotion = predict_emotion(features)
    
    print("Detected Emotion:", emotion)

    # Save to CSV
    data = {'File Path': [file_path], 'Detected Emotion': [emotion]}
    df = pd.DataFrame(data)
    df.to_csv("voice_emotion_output.csv", index=False)