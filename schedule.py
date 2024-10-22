import schedule

schedule.every(5).minutes.do(monitor_weather_conditions)
schedule.every().day.at("23:59").do(lambda: [print(calculate_daily_summary(date)) for date in daily_data])

while True:
    schedule.run_pending()
    time.sleep(1)
