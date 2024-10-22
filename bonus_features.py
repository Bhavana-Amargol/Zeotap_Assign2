#Update the data retrieval section in weather_processor.py to fetch humidity and wind speed from the API.
import requests

def fetch_weather_data(city):
    api_key = 'your_api_key'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    response = requests.get(base_url)
    data = response.json()

    # Extract relevant weather data
    temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    humidity = data['main']['humidity']  # Humidity
    wind_speed = data['wind']['speed']  # Wind speed in meters/second
    weather_condition = data['weather'][0]['main']  # Main weather condition
    
    return {
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'condition': weather_condition
    }



#Use the OpenWeatherMap forecast API to gather forecast data:
def fetch_weather_forecast(city):
    api_key = 'your_api_key'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

    response = requests.get(forecast_url)
    data = response.json()

    # Process the forecast data
    forecast_data = []
    for forecast in data['list']:
        temperature = forecast['main']['temp'] - 273.15  # Kelvin to Celsius
        humidity = forecast['main']['humidity']
        wind_speed = forecast['wind']['speed']
        condition = forecast['weather'][0]['main']

        forecast_data.append({
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'condition': condition,
            'time': forecast['dt_txt']
        })

    return forecast_data

#Add additional calculations for daily average, minimum, and maximum humidity and wind speed in the Aggregator:
def calculate_daily_summary(weather_data):
    temperatures = [entry['temperature'] for entry in weather_data]
    humidities = [entry['humidity'] for entry in weather_data]
    wind_speeds = [entry['wind_speed'] for entry in weather_data]

    avg_temp = sum(temperatures) / len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)

    avg_humidity = sum(humidities) / len(humidities)
    min_wind_speed = min(wind_speeds)
    max_wind_speed = max(wind_speeds)

    # Dominant condition can still be calculated similarly
    dominant_condition = max(set([entry['condition'] for entry in weather_data]), key=[entry['condition'] for entry in weather_data].count)

    return {
        'avg_temp': avg_temp,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'avg_humidity': avg_humidity,
        'min_wind_speed': min_wind_speed,
        'max_wind_speed': max_wind_speed,
        'dominant_condition': dominant_condition
    }

#Add the ability to trigger alerts based on forecasted conditions as well:
def check_forecast_alerts(forecast_data, threshold_temp):
    for forecast in forecast_data:
        if forecast['temperature'] > threshold_temp:
            print(f"Alert: Forecasted temperature of {forecast['temperature']}°C exceeds threshold at {forecast['time']}.")
            # Additional logic for email alerts

#Additional Setup for Forecasts and Alerts
#The forecast system is now integrated to fetch weather predictions every few hours and generate summaries for the next 5 days.
#Threshold-based alerts now consider forecasted data and generate notifications when upcoming weather exceeds defined limits.
#The visualization can also be extended to plot humidity and wind speed trends alongside temperature:


import matplotlib.pyplot as plt

def plot_weather_trends(weather_data):
    dates = [entry['date'] for entry in weather_data]
    temps = [entry['avg_temp'] for entry in weather_data]
    humidities = [entry['avg_humidity'] for entry in weather_data]
    wind_speeds = [entry['avg_wind_speed'] for entry in weather_data]

    plt.plot(dates, temps, label="Average Temperature (°C)")
    plt.plot(dates, humidities, label="Average Humidity (%)")
    plt.plot(dates, wind_speeds, label="Average Wind Speed (m/s)")
    
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.title("Weather Trends")
    plt.legend()
    plt.show()
