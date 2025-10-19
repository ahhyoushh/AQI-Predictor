"""import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# -----------------------------
API_KEY = 'd176a71a02d55f8e6b7fd7dc9fd4863d'
LAT, LON = 18.62563042095768, 73.82133096390638   # Pune coordinates
# -----------------------------
# Use timezone-aware datetime
end = int(datetime.now(timezone.utc).timestamp())
start = int((datetime.now(timezone.utc) - timedelta(days=7)).timestamp())

url_history = f"https://api.openweathermap.org/data/2.5/air_pollution/history?lat={LAT}&lon={LON}&start={start}&end={end}&appid={API_KEY}"
resp_hist = requests.get(url_history).json()
print(resp_hist)
hourly_list = resp_hist.get('list', [])

if not hourly_list:
    print(resp_hist)
else:
    hist_data = []
    for item in hourly_list:
        dt = datetime.fromtimestamp(item['dt'], tz=timezone.utc)
        comp = item['components']
        hist_data.append({
            'Date': dt.date(),
            'PM2.5': comp.get('pm2_5'),
            'PM10': comp.get('pm10'),
            'CO': comp.get('co'),
            'SO2': comp.get('so2'),
            'NO2': comp.get('no2'),
            'OZONE': comp.get('o3')
        })

    df_last = pd.DataFrame(hist_data)
    df_last = df_last.groupby('Date').mean().reset_index()

    print("🕒 Past Days AQI (Daily Averages):")
    print(df_last)"""