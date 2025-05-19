# 🇮🇳 CulturVista – Explore India's Hidden Cultural Treasures

CulturVista is an interactive, AI-powered web application that showcases India's diverse cultural heritage, promotes responsible tourism, and helps travelers plan unforgettable journeys using modern technologies like **Snowflake**, **Streamlit**, and **OpenAI GPT**.

![Banner](https://upload.wikimedia.org/wikipedia/commons/5/54/India_Gate_in_New_Delhi_03-2016_img3.jpg) <!-- Replace with your own image if needed -->

---

## 🌟 Features

- 🗺️ **Interactive Cultural Explorer** — Browse cultural destinations by state  
- 📈 **Tourism Trends Dashboard** — Visualize domestic & foreign tourist trends  
- 📍 **Hidden Gems Map** — Explore lesser-known sites using an interactive map  
- 🌿 **Responsible Tourism Guide** — Travel tips + region-specific recommendations  
- 🤖 **AI Cultural Assistant** — Ask GPT questions about travel, seasons, and history  
- 🧳 **AI-Powered Trip Planner** — Get a full itinerary based on interest & location  
- 🎥 **Lottie Animations + Typing Effects** — Enhanced user experience  
- ⚙️ **Snowflake Integration** — Pull live cultural data from Snowflake database

---

## 🚀 Tech Stack

| Tech | Usage |
|------|-------|
| Streamlit | App UI and interaction |
| OpenAI GPT-3.5 | Cultural assistant and trip planner |
| Snowflake | Data warehousing for cultural/tourism data |
| Folium | Interactive maps |
| Lottie | Web animations |
| Dotenv | Secure API key handling |

---

## 📦 Installation

1. **Clone the repo**
   ```
   git clone https://github.com/yourusername/culturvista.git
   cd culturvista
   ```

2. **Create and activate virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Set your OpenAI key**

   Create a `.env` file:
   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. **Run the app**
   ```
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
culturvista/
├── app.py                     # Main Streamlit application
├── .env                       # OpenAI API key (ignored by Git)
├── requirements.txt           # All dependencies
├── data/                      # Contains tourism/cultural CSVs
├── scripts/
│   └── snowflake_connection.py # Snowflake connector setup
├── README.md
```

---

## 🧠 Sample Questions for the AI Assistant

- What's the best time to visit Meghalaya for cultural tourism?  
- Give me a 5-day heritage itinerary for Telangana.  
- How can I travel responsibly in Northeast India?

---

## 🌐 Deployment

You can deploy this app on:
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Vercel](https://vercel.com/) (via Streamlit sharing)

---

## ✨ Acknowledgements

- Ministry of Tourism – [India Tourism Statistics](https://www.tourism.gov.in/)  
- [OpenAI](https://openai.com) — for GPT APIs  
- [Snowflake](https://snowflake.com) — for secure scalable data  
- [LottieFiles](https://lottiefiles.com) — for beautiful animations  
- All cultural and tourism data used is for educational, non-commercial purposes.

---

## 💬 Contact

Made with ❤️ by [Your Name]  
Email: yourname@email.com  
GitHub: [@rickyrick23](https://github.com/rickyrick23)
