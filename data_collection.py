import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_wearable_data():
    timestamps = [datetime.now() + timedelta(minutes=i) for i in range(80)]
    heart_rate = [np.random.randint(60, 100) for _ in range(80)]
    steps = [np.random.randint(0, 500) for _ in range(80)]
    sleep_quality = [np.random.choice(['Best', 'Good', 'Fair']) for _ in range(80)]

    data = pd.DataFrame({
        'Timestamp': timestamps,
        'Heart Rate': heart_rate,
        'Steps': steps,
        'Sleep Quality': sleep_quality
    })
    print(data.head())  # Show top 5 rows
    return data

if __name__ == "__main__":
    data = generate_wearable_data()
    print(data.head())  # Show top 5 rows
    data.to_csv("wearable_data.csv", index=True)  #Save as CSV file