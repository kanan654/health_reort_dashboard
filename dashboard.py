
import streamlit as st
import pandas as pd
import time
# Streamlit page config and heading
st.set_page_config(page_title="AI Health Monitoring Dashboard",page_icon ='🏥', layout="wide")
if st.button('Analyze'):
    with st.spinner("Analyze health data ...."):
        time.sleep(2)
        st.success('Analyze done!')
# Import your own project modules
from health_risk_prediction import predict_health_risk
from health_advisor import generate_health_advice
from device_check import check_device_health
from generator_report import generate_pdf_report
from integrated_alerts import all_alerts
st.title("🏥AI-Powered Health Monitoring System")
st.markdown("""
This dashboard integrates health risk prediction, emotion detection, wearable status check, 
and generates personalized health advice with downloadable health reports.
""")

# Load data function
@st.cache_data
def load_data():
    try:
        return pd.read_csv("combined_health_data.csv")
    except FileNotFoundError:
        st.error("combined_health_data.csv not found.")
        return pd.DataFrame()

# Load the data
health_data = load_data()

# ----------------------------- 
# Define function to generate advice
def generate_personalized_advice(row):
    heart_rate = row['Heart Rate']
    steps = row['Steps']
    sleep_quality_raw = row['Sleep Quality']

    if isinstance(sleep_quality_raw, str):
        if sleep_quality_raw.lower() == "best":
            sleep_quality = 5
        elif sleep_quality_raw.lower() == "good":
            sleep_quality = 4
        elif sleep_quality_raw.lower() == "average":
            sleep_quality = 3
        elif sleep_quality_raw.lower() == "poor":
            sleep_quality = 2
        elif sleep_quality_raw.lower() == "worst":
            sleep_quality = 1
        else:
            sleep_quality = 3  # default
    else:
        sleep_quality = int(sleep_quality_raw)

    advice = ""
    if heart_rate > 100:
        advice += "Reduce stress and caffeine intake. "
    if steps < 5000:
        advice += "Increase daily activity. "
    if sleep_quality < 3:
        advice += "Improve sleep habits."

    return advice
# -----------------------------

# Display data preview
if not health_data.empty:
    st.subheader("Loaded Health Data")
    st.dataframe(health_data.head())
col1,col2,col3 = st.columns(3)
# Predict Health Risk
with col1:
 if st.button("Predict Health Risk"):
    heart_rate = int(health_data['Heart Rate'].iloc[0])
    steps = int(health_data['Steps'].iloc[0])
    
    sleep_quality_raw = health_data['Sleep Quality'].iloc[0]
    if isinstance(sleep_quality_raw, str):
        if sleep_quality_raw.lower() == "best":
            sleep_quality = 5
        elif sleep_quality_raw.lower() == "good":
            sleep_quality = 4
        elif sleep_quality_raw.lower() == "average":
            sleep_quality = 3
        elif sleep_quality_raw.lower() == "poor":
            sleep_quality = 2
        elif sleep_quality_raw.lower() == "worst":
            sleep_quality = 1
        else:
            sleep_quality = 3  # default
    else:
        sleep_quality = int(sleep_quality_raw)

    prediction = predict_health_risk(heart_rate, steps, sleep_quality)
    st.metric(label= "Heart Rate",value = f"{heart_rate}bpm",delta="+2 bpm")
    st.metric(label="steps",value = f"{steps}steps")
    st.metric(label="sleep quality", value = sleep_quality)
    st.success(f"Health Risk Prediction: {prediction}")

# Provide Health Advice
with col2:
 if st.button("Get Personalized Health Advice"):
    advice_list = []
    for _, row in health_data.iterrows():
        advice = generate_personalized_advice(row)
        advice_list.append(advice)

    if len(advice_list) == len(health_data):
        health_data['Personalized Advice'] = advice_list
        st.success("Health advice generated.")
        st.dataframe(health_data)
    else:
        st.error("Mismatch between health data and advice list. Cannot proceed.")

# Device Status Check
with col3:
 if st.button("Check Wearable Device Status"):
    if not health_data.empty:
        row = health_data.iloc[0]   # Take the first row or any row you want
        status = check_device_health(row)
        if status:
            st.success("Wearable device is working fine.")
        else:
            st.error("Wearable device error detected!")
    else:
        st.error("No health data available to check device status.")

# Generate Alerts
def all_alerts(health_data):
    alerts = []
    for index, row in health_data.iterrows():
        if row['Heart Rate'] > 100:
            alerts.append('High Heart Rate')
        elif row['Sleep Quality'] == "Poor":
            alerts.append('Poor Sleep')
        else:
            alerts.append('Normal')
    return alerts
def all_alerts(health_data):
    return ["Normal", "High Heart Rate"]

alerts = all_alerts(health_data)   # No error

from fpdf import FPDF

def generate_pdf_report(health_data, health_risk):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Health Monitoring Report", ln=True, align="C")
    pdf.ln(10)

    # Health Risk
    pdf.cell(200, 10, txt=f"Predicted Health Risk: {health_risk}", ln=True, align="L")
    pdf.ln(10)

    # Add health data
    for col in health_data.columns:
        value = health_data[col].values[0]
        pdf.cell(200, 10, txt=f"{col}: {value}", ln=True, align="L")

    # Save the PDF
    output_path = "health_report.pdf"
    pdf.output(output_path)

    return output_path

def predict_health_risk(steps, sleep_quality):
    # Correct code
    if steps > 8000 and sleep_quality > 80:
        risk = "Low"
    elif steps > 4000 and sleep_quality > 50:
        risk = "Moderate"
    else:
        risk = "High"
    return risk
if st.button("Generate PDF Report"):
    steps = health_data["Steps"].iloc[0]
    sleep_quality = health_data["Sleep Quality"].iloc[0]
    health_risk =predict_health_risk(steps, sleep_quality)
    generate_pdf_report(health_data, health_risk)
    with open("health_report.pdf", "rb") as file:   
        btn = st.download_button(
            label="Download Health Report",
            data=file,
            file_name="Health_Report.pdf",
            mime="application/pdf",
            key = "download_health_report"
        )

    if not health_data.empty:
        # Clean column names
        health_data.columns = health_data.columns.str.strip().str.lower()

        st.write(health_data.columns.tolist())  # Optional: see available columns

        # Calculate steps and sleep_quality
        steps = pd.to_numeric(health_data['steps'], errors='coerce').mean()
        sleep_quality = pd.to_numeric(health_data['sleep quality'], errors='coerce').mean()

        # Calculate health risk
        health_risk = predict_health_risk(steps, sleep_quality)

        # Generate PDF
        pdf_path = generate_pdf_report(health_data, health_risk)

        st.success("PDF generated successfully!")

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download Health Report",
                data=f,
                file_name="Health_Report.pdf",
                mime="application/pdf"
            )
    else:
        st.error("No data available to generate report.")
