import streamlit as st
import pandas as pd
import numpy as np
import time
import random
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="AI Health Dashboard", layout="wide")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 AI-Powered Health Monitoring System")
st.write("Real-time automated health tracking & diagnostic engine.")

# --- AUTOMATION LOGIC: Wearable Device Auto-Detection ---
with st.sidebar:
    st.header("Connection Status")
    # Yahan humne manual select hata kar auto-detect simulate kiya hai
    with st.spinner("Searching for devices..."):
        time.sleep(1) # Fake loading time
    
    st.success("✅ SmartWatch v2.0 Connected")
    st.info(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")
    
    st.divider()
    st.button("Force Re-sync")

# --- DATA SIMULATION (Manual Inputs Removed) ---
# Ab user ko set nahi karna padega, code khud random logic se data uthayega
heart_rate = random.randint(70, 95)
systolic_bp = random.randint(110, 135)
diastolic_bp = random.randint(70, 85)
sleep_hours = round(random.uniform(5.5, 8.5), 1)
spo2 = random.randint(95, 99)

# --- DASHBOARD LAYOUT ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="❤️ Heart Rate", value=f"{heart_rate} bpm", delta="Normal")

with col2:
    st.metric(label="🩸 Blood Pressure", value=f"{systolic_bp}/{diastolic_bp}", delta="-2 mmHg")

with col3:
    st.metric(label="😴 Sleep", value=f"{sleep_hours} hrs", delta="Good")

with col4:
    st.metric(label="🌬️ SpO2", value=f"{spo2}%", delta="Stable")

# --- AI DIAGNOSTIC ENGINE (Logic) ---
st.subheader("🤖 AI Health Insights")

def generate_ai_report(hr, s_bp, slp):
    tips = []
    if hr > 90:
        tips.append("⚠️ Your Heart Rate is slightly high. Try deep breathing exercises.")
    if s_bp > 130:
        tips.append("⚠️ Elevated BP detected. Reduce salt intake and stay hydrated.")
    if slp < 6:
        tips.append("⚠️ Sleep deprivation noticed. Aim for at least 7 hours tonight.")
    
    if not tips:
        return "✅ Everything looks perfect! You are in great health today."
    return "\n".join(tips)

report = generate_ai_report(heart_rate, systolic_bp, sleep_hours)
st.info(report)

# --- CHART (Real-time Simulation) ---
st.subheader("Activity Trend (Last 24 Hours)")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Heart Rate', 'Activity', 'Stress']
)
st.line_chart(chart_data)

st.success("Report generated successfully and ready for download.")
