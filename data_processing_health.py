import pandas as pd

def preprocess_health_data(file_path):
    df = pd.read_csv(file_path)
    print("Shape of data:", df.shape)
    df.dropna(inplace=True)
    df.to_csv("clean_health_data.csv", index=False)
    return df

if __name__ == "__main__":
    df = preprocess_health_data("wearable_data.csv")
    print(df.head())