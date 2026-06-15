import streamlit as st
import pandas as pd
import plotly.express as px

import random
import folium
from streamlit_folium import st_folium

# Page Settings
st.set_page_config(
    page_title="Citizen Safety Intelligence Platform",
    page_icon="🛡️",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("safety_data.csv")

# Sidebar
st.sidebar.title("🛡️ Citizen Safety Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Location Dashboard",
        "Safety Prediction",
        "Risk Analytics",
        "Safety Hotspots",
        "Community Alerts",
        "Emergency Assistance",
        "Daily Safety Tips",
        "About"
    ]
)

# ---------------- HOME ----------------

if page == "Home":

    st.title("🛡️ Citizen Safety Intelligence Platform")

    st.info(
    "🤖 AI-powered platform helping citizens make safer travel decisions across India."
    )

    st.markdown("""
    ### Travel Smarter. Stay Safer.

   Analyze locations before travelling and receive:

   - Safety Insights
   - Risk Assessment
   - Community Alerts
   - Travel Recommendations
   - Safety Analytics
   """)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("States Covered", len(df["State"].unique()))
    c2.metric("Cities Covered", len(df["City"].unique()))
    c3.metric("Safety Records", len(df))
    c4.metric("Alerts", "Active")

    st.subheader("📈 Platform Highlights")

    col1, col2, col3 = st.columns(3)

    col1.success("🟢 20 States Covered")
    col2.info("🏙️ 60 Cities Covered")
    col3.warning("🚨 Active Monitoring")
    st.markdown("---")

    st.subheader("🌟 Why Use This Platform?")

    col1, col2 = st.columns(2)

    with col1:
         
         st.info("📍 Analyze locations before travel")
         st.info("🔮 Predict safety risks")
         st.info("🚨 Receive community alerts")

    with col2:
         st.info("🗺 Discover safer alternatives")
         st.info("🆘 Access emergency assistance")
         st.info("🤖 Get AI-powered recommendations")

    st.markdown("---")

    st.subheader("🚨 Latest Alerts")

    st.warning("⚠ Heavy crowd reported near Bus Stand")
    st.warning("⚠ Poor lighting reported in Market Area")
    st.warning("⚠ Road maintenance near Railway Station")


# ---------------- LOCATION DASHBOARD ----------------

elif page == "Location Dashboard":

    st.title("📍 Location Dashboard")

    state = st.selectbox(
        "Select State",
        sorted(df["State"].unique())
    )

    state_df = df[df["State"] == state]

    city = st.selectbox(
        "Select City",
        sorted(state_df["City"].unique())
    )

    selected = state_df[state_df["City"] == city].iloc[0]

    st.subheader(f"📍 {city}, {state}")

    col1, col2, col3 = st.columns(3)

    col1.metric("Safety Index", selected["SafetyIndex"])
    col2.metric("Crime Rate", selected["CrimeRate"])
    col3.metric("Crowd Density", selected["CrowdDensity"])

    st.write("### Area Information")
    st.write("Weather:", selected["Weather"])
    st.write("Lighting:", selected["Lighting"])
    st.write("Location Type:", selected["LocationType"])

# ---------------- SAFETY PREDICTION ----------------

elif page == "Safety Prediction":

    st.title("🔮 Safety Prediction")

    weather = st.selectbox(
        "Weather",
        ["Clear", "Rainy", "Foggy", "Stormy", "Sunny"]
    )

    crowd = st.selectbox(
        "Crowd Density",
        ["Low", "Medium", "High"]
    )

    crime = st.selectbox(
        "Crime Rate",
        ["Low", "Medium", "High"]
    )

    lighting = st.selectbox(
        "Lighting",
        ["Good", "Poor"]
    )

    if st.button("Analyze Safety"):

        if crime == "High" or lighting == "Poor":

            st.error("🚨 HIGH RISK DETECTED")
            st.info("📍 Visit Safety Hotspots page for safer alternatives.")

            st.subheader("🚨 Recommendations")

            st.write("✓ Avoid isolated roads")
            st.write("✓ Share live location")
            st.write("✓ Travel with companions")
            st.write("✓ Stay in well-lit areas")
            st.write("✓ Enable SOS")

        elif crime == "Medium":

            st.warning("⚡ TRAVEL WITH CAUTION")

            st.subheader("⚠ Recommendations")

            st.write("✓ Stay alert")
            st.write("✓ Use public routes")
            st.write("✓ Inform family about travel")

        else:

            st.success("🏆 GREEN ZONE DETECTED")
            st.progress(92)

            st.subheader("✅ Recommendations")

            st.write("✓ Normal travel conditions")
            st.write("✓ Follow standard precautions")

# ---------------- COMMUNITY ALERTS ----------------

elif page == "Community Alerts":

    st.title("🚨 Community Alerts")

    st.warning("⚠ Heavy crowd reported near Bus Stand")
    st.warning("⚠ Poor lighting reported near Market Area")
    st.warning("⚠ Road maintenance near Railway Station")



elif page == "Safety Hotspots":

    st.title("🗺 Safety Hotspots")

    city = st.selectbox(
        "Select City",
        ["Hubli", "Bengaluru", "Mumbai", "Pune", "Hyderabad", "Chennai"]
    )

    city_coords = {
        "Hubli": [15.3647, 75.1240],
        "Bengaluru": [12.9716, 77.5946],
        "Mumbai": [19.0760, 72.8777],
        "Pune": [18.5204, 73.8567],
        "Hyderabad": [17.3850, 78.4867],
        "Chennai": [13.0827, 80.2707]
    }

    m = folium.Map(
        location=city_coords[city],
        zoom_start=12
    )

    folium.Marker(
        city_coords[city],
        popup="🟢 Safe Zone",
        icon=folium.Icon(color="green")
    ).add_to(m)

    folium.Marker(
        [city_coords[city][0] + 0.02, city_coords[city][1] + 0.02],
        popup="🟡 Moderate Zone",
        icon=folium.Icon(color="orange")
    ).add_to(m)

    folium.Marker(
        [city_coords[city][0] - 0.02, city_coords[city][1] - 0.02],
        popup="🔴 High Risk Zone",
        icon=folium.Icon(color="red")
    ).add_to(m)

    st_folium(m, width=1000, height=500)

    st.success("🟢 Safe | 🟡 Moderate | 🔴 High Risk")



elif page == "Emergency Assistance":

    st.title("🆘 Emergency Assistance")

    st.error("🚓 Police : 100")
    st.error("🚑 Ambulance : 108")
    st.error("🔥 Fire : 101")

    st.info("📱 Keep emergency contacts accessible during travel.")


elif page == "Daily Safety Tips":

    st.title("💡 Daily Safety Tips")

    tips = [
        "Share live location during night travel.",
        "Avoid isolated roads after dark.",
        "Keep emergency contacts ready.",
        "Use well-lit routes whenever possible.",
        "Stay alert in crowded places.",
        "Prefer trusted public transport services."
    ]

    if st.button("🎲 Generate Safety Tip"):
        st.success(random.choice(tips))


   # ---------------- RISK ANALYTICS ----------------

elif page == "Risk Analytics":

    st.title("📊 Risk Analytics Dashboard")

    st.info("AI-powered visualization of safety factors across locations")

    col1, col2 = st.columns(2)

    with col1:
        crime_chart = px.histogram(
            df,
            x="CrimeRate",
            title="Crime Rate Distribution"
        )
        st.plotly_chart(crime_chart, use_container_width=True)

    with col2:
        crowd_chart = px.histogram(
            df,
            x="CrowdDensity",
            title="Crowd Density Distribution"
        )
        st.plotly_chart(crowd_chart, use_container_width=True)

    weather_chart = px.histogram(
        df,
        x="Weather",
        title="Weather Conditions Distribution"
    )
    st.plotly_chart(weather_chart, use_container_width=True)

    st.subheader("📈 Platform Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric("States", len(df["State"].unique()))
    c2.metric("Cities", len(df["City"].unique()))
    c3.metric("Records", len(df))

# ---------------- ABOUT ----------------

elif page == "About":

    st.title("ℹ️ About")

    st.write("""
    AI Powered Citizen Safety Intelligence Platform

    Features:
    - Location Safety Analysis
    - Risk Prediction
    - Community Alerts
    - Safety Recommendations
    - Travel Guidance
    """)
