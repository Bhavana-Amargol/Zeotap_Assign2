THRESHOLDS = {
    'temperature': 35  # Trigger alert if temp exceeds 35 degrees Celsius for two consecutive updates
}

alerts_triggered = []

def check_alerts(weather_data):
    if weather_data['temperature'] > THRESHOLDS['temperature']:
        alerts_triggered.append(f"Alert: {weather_data['city']} temperature exceeded {THRESHOLDS['temperature']}°C at {weather_data['temperature']}°C")

def monitor_weather_conditions():
    weather_data = fetch_weather_for_metros()
    for city_weather in weather_data:
        aggregate_daily_data(city_weather)
        check_alerts(city_weather)
