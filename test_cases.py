# System Setup
def test_api_key():
    try:
        response = fetch_weather_data(CITY_IDS['Delhi'])
        assert response is not None
        print("API key is valid, and connection successful.")
    except:
        print("Invalid API key or connection error.")
      
#Temperature Conversion
def test_temperature_conversion():
    assert kelvin_to_celsius(300) == 26.85
    assert kelvin_to_celsius(273.15) == 0
  
#Daily Weather Summary Calculation
def test_daily_summary():
    weather_data = [
        {'temperature': 30, 'condition': 'Clear', 'timestamp': 1609459200},
        {'temperature': 32, 'condition': 'Clear', 'timestamp': 1609459500},
        {'temperature': 29, 'condition': 'Rain', 'timestamp': 1609459800},
    ]
    for data in weather_data:
        aggregate_daily_data(data)
    
    summary = calculate_daily_summary('2021-01-01')
    assert summary['avg_temp'] == 30.33
    assert summary['max_temp'] == 32
    assert summary['min_temp'] == 29
    assert summary['dominant_condition'] == 'Clear'

#Alert Triggering
def test_alert_triggering():
    weather_data = {'city': 'Delhi', 'temperature': 36, 'timestamp': 1609459200}
    check_alerts(weather_data)
    assert len(alerts_triggered) == 1
    assert "exceeded" in alerts_triggered[0]
