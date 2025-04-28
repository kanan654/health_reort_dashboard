# device_check.py

import pandas as pd

def check_device_health(row):
    issues = []

    # Example rules to check if sensor/device is faulty
    if 'Heart Rate' in row and (row['Heart Rate'] <= 30 or row['Heart Rate'] >= 200):
        issues.append("Heart rate reading out of expected range.")
    if 'Steps' in row and row['Steps'] < 0:
        issues.append("Negative steps count detected.")
    if 'Sleep Quality' in row and row['Sleep Quality'] not in ['Good', 'Okay', 'Bad']:
        issues.append("Invalid sleep quality value.")

    if not issues:
        return "Device functioning normally"
    else:
        return " | ".join(issues)

# Load your health data (use combined_health_data.csv or wearable_data.csv)
try:
    df = pd.read_csv('combined_health_data.csv')  # Make sure this file exists
except FileNotFoundError:
    print("Error: combined_health_data.csv not found.")
    exit()

# Run device check for each row
df['Device Status'] = df.apply(check_device_health, axis=1)

# Save results
df.to_csv('device_health_status.csv', index=False)
print("Device check complete. Results saved to device_health_status.csv")

# Print sample output
print(df[['Heart Rate', 'Steps', 'Sleep Quality', 'Device Status']].head())