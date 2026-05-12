import streamlit as st
import pandas as pd
import numpy as np
import time
import random
import plotly.express as px  # Advanced charts ke liye
from datetime import datetime

# Page Config
st.set_page_config(page_title="Pro AI Health Monitor", layout="wide")

# Sidebar for Device Status
with st.sidebar:
    st.header("🛰️ Hardware Sync")
    st.success("Connected: Kanan's SmartWatch")
    st.write(f"Battery: {random.randint(60, 95)}%")
    st.divider()
    st.markdown("### AI Engine Status: **Active**")

st.title("🛡️ Advanced AI Health Guardian")

# --- DATA GENERATION (Simulating Real-time sensors) ---
hr = random.randint(68, 92)
sys = random.randint(115, 140)
dia = random.randint(75, 90)
spo2 = random.randint(94, 99)
stress_level = random.randint(20, 80)

# --- ADVANCED LOGIC: HEALTH SCORE CALCULATION ---
def calculate_health_score(h, s, o2):
    score = 100
    if h > 90 or h < 60: score -= 15
    if s > 130: score -= 20
    if o2 < 95: score -= 25
    return max(score, 10)

health_score = calculate_health_score(hr, sys, spo2)

# --- TOP ROW: METRICS ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Heart Rate", f"{hr} BPM", "Normal" if hr < 90 else "High")
c2.metric("Blood Pressure", f"{sys}/{dia}", "-5% vs yesterday")
c3.metric("SpO2 Level", f"{spo2}%", "Stable")
c4.metric("Overall Health Score", f"{health_score}/100")

st.divider()

# --- MIDDLE ROW: ANALYTICS & PREDICTION ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📈 Real-time Vital Trends")
    # Generating 24 hours of dummy data
    chart_data = pd.DataFrame({
        'Hour': list(range(24)),
        'Heart Rate': np.random.randint(65, 95, 24),
        'Stress': np.random.randint(10, 70, 24)
    })
    fig = px.line(chart_data, x='Hour', y=['Heart Rate', 'Stress'], 
                  template="plotly_white", markers=True)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("🔮 Predictive Insights")
    if sys > 135:
        st.error("🚨 **High Risk Detected:** Potential Hypertension. Recommendation: Lower sodium intake and consult a specialist.")
    elif health_score < 80:
        st.warning("⚠️ **Fatigue Warning:** Your stress levels are rising. Take a 15-minute break.")
    else:
        st.success("✅ **Optimal State:** Your vitals are consistent with athletic recovery patterns.")

# --- BOTTOM SECTION: WEARABLE DATA LOG ---
with st.expander("📄 View Full Diagnostic Data Logs"):
    log_data = pd.DataFrame({
        'Timestamp': [datetime.now().strftime("%H:%M:%S") for _ in range(5)],
        'Event': ['Syncing...', 'Anomaly Check', 'Calibrating SpO2', 'Data Upload', 'Report Ready'],
        'Status': ['Done', 'Cleared', 'Done', 'Success', 'Live']
    })
    st.table(log_data)

st.markdown("---")
st.caption("Powered by Gemini AI & Real-time Wearable Integration Simulation")
