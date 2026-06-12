import os
import requests
from datetime import datetime

def fetch_weather(city="London"):
    print(f"📡 Connecting to weather servers for {city}...")
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✅ Weather data successfully retrieved!")
            return response.text.strip()
        else:
            return f"⚠️ Weather updates temporarily unavailable (Status: {response.status_code})"
    except Exception as e:
        return f"❌ Failed to reach weather API: {e}"

def fetch_quote():
    print("📡 Connecting to ZenQuotes API servers...")
    try:
        url = "https://zenquotes.io/api/today"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            print("✅ Inspirational quote successfully retrieved!")
            return f'"{quote}" — {author}'
        else:
            return "⚠️ 'Make today count!' — Anonymous (Live API unavailable)"
    except Exception as e:
        return f"❌ Failed to reach quote API: {e}"

def generate_daily_report():
    print("\n🚀 --- STARTING BUILD PULSE ENGINE ---")
    weather_summary = fetch_weather("New York")
    daily_inspiration = fetch_quote()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    markdown_report = f"""# ⚡ BUILD PULSE DAILY BRIEFING
> *Generated completely automatically on autopilot via GitHub Actions.*

## 📅 Execution Details
- **Timestamp:** `{current_time}`
- **System Status:** 🟢 Operational / Healthy

## 🌤️ Live Weather Overview
- **Current Conditions:** {weather_summary}

## 💡 Daily Inspiration
{daily_inspiration}

---
*Build Pulse Bot — Project completed successfully from scratch.*
"""
    
    filename = "daily_summary.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(markdown_report)
        print(f"💾 Report compiled cleanly and saved locally as: '{filename}'")
    except Exception as e:
        print(f"❌ Critical error saving report file: {e}")

if __name__ == "__main__":
    generate_daily_report()
    print("🏁 Engine run sequence complete. Ready for deployment.\n")