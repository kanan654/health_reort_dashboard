import streamlit as st
import pandas as pd
import numpy as np
import time
import random
import plotly.express as px
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Health Guardian Pro",
    page_icon="🛡️",
    layout="wide"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    div[data-testid="stExpander"] { background-color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: DEVICE SYNC ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3843/3843547.png", width=100)
    st.header("🛰️ Hardware Status")
    
    # Auto-detection simulation
    with st.spinner("Scanning for Wearables..."):
        time.sleep(1.5)
    
    st.success("✅ SmartWatch v2.0 Connected")
    st.info(f"User: Kanan Kathuria\n\nLast Sync: {datetime.now().strftime('%H:%M:%S')}")
    st.progress(random.randint(70, 90), text="Battery Life")
    
    st.divider()
    if st.button("🔄 Refresh Data"):
        st.rerun()

# --- HEADER ---
st.title("🛡️ AI-Powered Health Monitoring & Diagnostic System")
st.caption("Advanced Real-time Analytics with Predictive Emergency Response")

# --- CORE LOGIC: DATA SIMULATION ---
# No manual inputs - automatically generates realistic health data
hr = random.randint(65, 105)
sys = random.randint(110, 145)
dia = random.randint(70, 95)
spo2 = random.randint(93, 99)
sleep_quality = random.randint(50, 95)

# --- ADVANCED LOGIC: HEALTH SCORE & RISK ---
def analyze_health(h, s, d, o2):
    score = 100
    risks = []
    
    if h > 95: 
        score -= 15
        risks.append("Elevated Heart Rate")
    if s > 135: 
        score -= 20
        risks.append("Hypertension Risk (High BP)")
    if o2 < 95: 
        score -= 25
        risks.append("Low Oxygen Saturation")
        
    status = "Optimal" if score > 85 else "Caution" if score > 65 else "High Risk"
    return score, status, risks

health_score, health_status, risk_list = analyze_health(hr, sys, dia, spo2)

# --- ROW 1: KEY METRICS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Heart Rate", f"{hr} BPM", delta="Normal" if hr < 90 else "High", delta_color="inverse" if hr > 90 else "normal")
m2.metric("Blood Pressure", f"{sys}/{dia}", delta="Elevated" if sys > 130 else "Stable", delta_color="inverse" if sys > 130 else "normal")
m3.metric("SpO2 (Oxygen)", f"{spo2}%", delta="Critical" if spo2 < 95 else "Good", delta_color="inverse" if spo2 < 95 else "normal")
m4.metric("Health Score", f"{health_score}/100", delta=health_status)

st.divider()

# --- ROW 2: VISUAL TRENDS & AI PREDICTIONS ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📈 24-Hour Vital Activity")
    df = pd.DataFrame({
        'Hour': list(range(24)),
        'Heart Rate': np.random.randint(60, 100, 24),
        'Stress Level': np.random.randint(10, 80, 24)
    })
    fig = px.area(df, x='Hour', y=['Heart Rate', 'Stress Level'], 
                  color_discrete_map={"Heart Rate": "#ff4b4b", "Stress Level": "#1f77b4"},
                  template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("👨‍⚕️ AI Physician's Insights")
    
    if health_status == "High Risk":
        st.error(f"🚨 **Warning:** {', '.join(risk_list)}")
    elif health_status == "Caution":
        st.warning(f"⚠️ **Notice:** {', '.join(risk_list)}")
    else:
        st.success("✅ Vitals are within the healthy range.")

    # Smart Recommendations Logic
    st.markdown("### **Recommendations:**")
    if sys > 130:
        st.info("🔹 **Diet:** Reduce salt intake. Drink 2L water.\n\n🔹 **Action:** Avoid heavy workouts for 4 hours.")
    elif hr > 95:
        st.info("🔹 **Relaxation:** Try 5-min Box Breathing.\n\n🔹 **Action:** Check for caffeine over-consumption.")
    else:
        st.info("🔹 **Activity:** You are fit for high-intensity training today.")

# --- ROW 3: EMERGENCY SOS & LOGS ---
st.divider()
row3_c1, row3_c2 = st.columns(2)

with row3_c1:
    st.subheader("🚨 Emergency Intervention")
    if health_status != "Optimal":
        st.write("Anomalies detected. Would you like to trigger an alert?")
        if st.button("Trigger Emergency SOS", type="primary"):
            with st.spinner("Broadcasting location to Emergency Contacts..."):
                time.sleep(2)
                st.error("🚨 SOS Alert Sent! Doctor & Family notified.")
    else:
        st.write("Emergency systems on standby. No action needed.")

with row3_c2:
    st.subheader("🎯 Daily Goals")
    steps = random.randint(3000, 9000)
    st.write(f"Steps: {steps} / 10000")
    st.progress(steps/10000)
    st.write("Calories Burned: **450 kcal**")

# --- DATA LOGS ---
with st.expander("📂 View Technical System Logs"):
    log_df = pd.DataFrame({
        'Timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(5)],
        'Module': ['Sensor_Sync', 'AI_Engine', 'Risk_Analyzer', 'Cloud_Upload', 'UI_Renderer'],
        'Status': ['OK', 'Active', 'Monitoring', 'Encrypted', 'Ready']
    })
    st.table(log_df)

st.markdown("---")
st.caption("Built for Placement Portfolio | Integration: Gemini AI & IoT Wearables Simulation")
