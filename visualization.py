import matplotlib.pyplot as plt

def plot_temperature_trends():
    for date_str, day_data in daily_data.items():
        temps = [data['temperature'] for data in day_data]
        timestamps = [data['timestamp'] for data in day_data]
        plt.plot(timestamps, temps, label=date_str)

    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.show()
