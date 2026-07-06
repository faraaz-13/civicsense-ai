import streamlit as st

st.set_page_config(page_title="CivicSense AI", layout="wide")

st.title("🌍 CivicSense AI")
st.subheader("AI for Better Living and Smarter Communities")

st.write("Transforming fragmented community data into actionable insights using AI.")

menu = st.sidebar.selectbox("Choose Module", ["Dashboard", "AI Chat", "Analytics"])

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.header("📊 Community Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Weather", "Sunny ☀️")
    with col2:
        st.metric("Traffic", "Moderate 🚗")
    with col3:
        st.metric("Air Quality", "Good 😊")

    st.info("No active alerts in your area 🚨")

# ---------------- AI CHAT ----------------
elif menu == "AI Chat":
    st.header("🤖 AI Assistant")

    user_input = st.text_input("Ask about your city")

    if user_input:
        st.success("AI Response:")
        st.write("Based on current community data, conditions are stable and safe. No major risks detected.")

# ---------------- ANALYTICS ----------------
elif menu == "Analytics":
    st.header("📈 Analytics")

    st.write("• Risk Prediction: Low")
    st.write("• Trend: Stable Environment")
    st.write("• Recommendation: Normal daily activities are safe")
