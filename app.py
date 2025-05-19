import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_lottie import st_lottie
import requests
import openai
import os
import time
from dotenv import load_dotenv
from scripts.snowflake_connection import get_snowflake_connection

# Load env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Optional CSS animation
st.markdown("""
    <style>
    .fade-in {
        animation: fadeIn 1.2s ease-in;
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Load Lottie animation from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Typing effect for AI output
def type_out(text):
    placeholder = st.empty()
    full = ""
    for char in text:
        full += char
        placeholder.markdown(full)
        time.sleep(0.01)

# Navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Cultural Explorer", "Tourism Trends", "Hidden Gems Map", "Responsible Tourism", "Cultural AI Assistant", "Trip Planner"]
)

# --------------------------
# HOME PAGE
# --------------------------
if page == "Home":
    st.title("🇮🇳 CulturVista")

    lottie_json = load_lottie_url("https://lottie.host/0dc3272b-083f-49a4-a54b-9d1d3fc4cda0/vW0Gcq7u2H.json")
    if lottie_json:
        st_lottie(lottie_json, speed=1, height=200, key="culturvista")

    st.markdown("<div class='fade-in'>Welcome to <b>CulturVista</b> – your AI-powered travel companion to explore India's hidden cultural treasures and travel responsibly.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("🌐 States Covered", 10)
        st.metric("📍 Hidden Destinations", 10)
        st.metric("🧭 Avg. Untouched Score", "8.1/10")
    with col2:
        st.metric("📊 Total Visitors in Data", "1.2M+")
        st.metric("⚙️ Powered by", "Snowflake + OpenAI")
        st.metric("🚀 Status", "Prototype Ready")

    st.markdown("### 🚀 Quick Explore")
    st.page_link("app.py", label="🖼️ Cultural Explorer")
    st.page_link("app.py", label="📈 Tourism Trends")
    st.page_link("app.py", label="🧳 AI Trip Planner")
    st.page_link("app.py", label="🤖 Ask the AI Guide")

# --------------------------
# CULTURAL EXPLORER
# --------------------------
elif page == "Cultural Explorer":
    st.title("🖼️ Cultural Explorer")
    st.markdown("Discover India's rich cultural heritage by state.")

    try:
        conn = get_snowflake_connection()
        df = pd.read_sql("SELECT * FROM CULTURAL_SITES", conn)
        df.columns = ['category', 'state', 'destination', 'highlight']
        states = df['state'].unique()
        selected_state = st.selectbox("Select a State/UT", sorted(states))
        filtered_df = df[df['state'] == selected_state]

        st.subheader(f"Cultural Highlights in {selected_state}")
        for _, row in filtered_df.iterrows():
            with st.expander(f"{row['destination']} ({row['category']})"):
                st.write(f"**Highlight:** {row['highlight']}")
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")

# --------------------------
# TOURISM TRENDS
# --------------------------
elif page == "Tourism Trends":
    st.title("📈 Tourism Trends Dashboard")

    try:
        tourism_df = pd.read_csv("data/tourism_trends_2023.csv")

        st.subheader("Top States by Domestic Tourist Visits")
        st.bar_chart(tourism_df.sort_values("Domestic_Visits", ascending=False).set_index("State")["Domestic_Visits"])

        st.subheader("Top States by Foreign Tourist Visits")
        st.bar_chart(tourism_df.sort_values("Foreign_Visits", ascending=False).set_index("State")["Foreign_Visits"])

        st.subheader("📊 Full Tourism Data")
        st.dataframe(tourism_df)

    except Exception as e:
        st.error(f"❌ Error loading tourism data: {e}")

# --------------------------
# HIDDEN GEMS MAP
# --------------------------
elif page == "Hidden Gems Map":
    st.title("🗺️ Hidden Cultural Gems – Story Map")

    try:
        gems_df = pd.read_csv("data/enhanced_hidden_cultural_gems_with_images.csv")
        m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)

        for _, row in gems_df.iterrows():
            untouched = int(row['Untouched_Score'])
            color = 'darkgreen' if untouched >= 9 else 'orange' if untouched >= 7 else 'blue'

            popup_html = f"""
            <div style="font-family: sans-serif; font-size: 13px;">
                <b>📍 {row['Destination']}, {row['State']}</b><br>
                🏛️ {row['Highlight']}<br>
                🌤️ {row['Seasonality']} | 👥 {row['Annual_Visitors']:,} visitors<br>
                🧭 Untouched Score: {row['Untouched_Score']}/10<br>
                <hr>
                <i>{row['Cultural_Story']}</i><br>
                📈 <b>Trend:</b> {row['Trend_Info']}
            </div>
            """
            iframe = folium.IFrame(popup_html, width=270, height=180)
            popup = folium.Popup(iframe, max_width=270)

            folium.Marker(
                location=[row["Latitude"], row["Longitude"]],
                popup=popup,
                tooltip=row["Destination"],
                icon=folium.Icon(color=color, icon="info-sign")
            ).add_to(m)

        st_folium(m, width=750, height=550)

    except Exception as e:
        st.error(f"❌ Error displaying map: {e}")

# --------------------------
# RESPONSIBLE TOURISM
# --------------------------
elif page == "Responsible Tourism":
    st.title("🌿 Responsible Tourism Recommendations")

    st.markdown("### ✅ General Guidelines")
    st.markdown("""
    - 🧘 Respect local customs  
    - 🛍️ Support local artisans  
    - 🚫 Avoid plastic  
    - 🏨 Choose eco-stays  
    - 📸 Ask before photographing  
    - 🗑️ Leave no trace
    """)

    st.markdown("### 📍 Region-Specific Tips")
    tips = {
        "Manipur": "Langthabal and Moirang offer a deep look into Meitei heritage.",
        "Meghalaya": "In Mawphlang’s sacred groves, avoid removing even fallen leaves.",
        "Uttar Pradesh": "Sites like Mahoba and Kalinjar are rich in Chandela history.",
        "Telangana": "Support rural tourism by staying in heritage homes.",
        "Assam": "Watch weavers in Sualkuchi; avoid aggressive bargaining."
    }
    for state, desc in tips.items():
        with st.expander(f"🌍 {state}"):
            st.markdown(desc)

    st.success("“Take only memories, leave only footprints.” — Chief Seattle")

# --------------------------
# CULTURAL AI ASSISTANT
# --------------------------
elif page == "Cultural AI Assistant":
    st.title("🤖 Cultural AI Assistant")
    user_input = st.text_area("Ask anything about travel, destinations, or responsible tourism")

    if st.button("Ask AI"):
        if user_input.strip():
            with st.spinner("Thinking..."):
                try:
                    from openai import OpenAI
                    client = OpenAI()
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful, kind, and professional Indian cultural tourism assistant."},
                            {"role": "user", "content": user_input}
                        ]
                    )
                    st.markdown("🧠 **AI Says:**")
                    type_out(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question.")

# --------------------------
# TRIP PLANNER
# --------------------------
elif page == "Trip Planner":
    st.title("🧳 AI Trip Planner")
    place = st.text_input("Which destination or state?", placeholder="e.g., Assam, Gujarat")
    days = st.slider("Trip Duration", 2, 15, 5)
    interest = st.selectbox("Focus area", ["Heritage", "Wildlife", "Spiritual", "Handicrafts", "Mixed"])

    if st.button("Generate Itinerary"):
        if place:
            with st.spinner("Crafting your journey..."):
                try:
                    from openai import OpenAI
                    client = OpenAI()
                    prompt = f"Plan a {days}-day itinerary in {place}, India with a focus on {interest.lower()} tourism. Include cultural sites, reasons to visit, and local tips."

                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a knowledgeable Indian cultural travel guide."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    st.markdown("📋 **Your Itinerary:**")
                    type_out(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a destination.")
