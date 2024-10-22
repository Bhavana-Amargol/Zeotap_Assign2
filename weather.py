import requests
import time
from datetime import datetime

API_KEY = "your_api_key"  # Replace with your OpenWeatherMap API key
CITY_IDS = {
    'Delhi': 1273294,
    'Mumbai': 1275339,
    'Chennai': 1264527,
    'Bangalore': 1277333,
    'Kolkata': 1275004,
    'Hyderabad': 1269843
}
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def fetch_weather_data(city_id):
    url = f"{BASE_URL}?id={city_id}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {
        'city': data['name'],
        'temperature': kelvin_to_celsius(data['main']['temp']),
        'feels_like': kelvin_to_celsius(data['main']['feels_like']),
        'condition': data['weather'][0]['main'],
        'timestamp': data['dt']
    }

def fetch_weather_for_metros():
    weather_data = []
    for city_name, city_id in CITY_IDS.items():
        city_weather = fetch_weather_data(city_id)
        weather_data.append(city_weather)
    return weather_data
