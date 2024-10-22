# Zeotap_Assign2

# Prerequisites
Before setting up the application, ensure you have the following tools installed:

 Docker or Podman for container management.
 Python 3.8+ for backend processing.
 PostgreSQL or MySQL as the database to store weather data.
 OpenWeatherMap API Key for accessing weather data.
 Email SMTP Server: For sending email alerts (e.g., Gmail SMTP server).
 Git: For version control and pushing code to GitHub.
 To install libraries , 
```
pip install requests
pip install schedule
pip install matplotlib
python weather_processor.py
python visuals.py
```

# Installation
Clone the project repository from GitHub to your local machine:
```bash
git clone https://github.com/Bhavana-Amargol/Zeotap_Assign2
cd weather-monitoring-app
```


# Step 2: Set up Containers
Database: Use Docker or Podman to spin up a PostgreSQL/MySQL database container.
PostgreSQL (via Docker):

```bash
docker run --name weather-db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=adminpass -e POSTGRES_DB=weather_data -p 5432:5432 -d postgres

```
MySQL (via Docker):
```bash
docker run --name weather-db -e MYSQL_ROOT_PASSWORD=adminpass -e MYSQL_DATABASE=weather_data -p 3306:3306 -d mysql

```

```bash
podman run --name weather-db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=adminpass -e POSTGRES_DB=weather_data -p 5432:5432 -d postgres
```

# Step 3: Install Python Dependencies
Create a virtual environment and install the required Python packages.

```bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

requests
psycopg2-binary  # for PostgreSQL
mysql-connector-python  # for MySQL
matplotlib  # for visualizations
flask  # for web server (if using Flask for web UI)

# 3. Setting Up the Environment
Step 1: Configure Environment Variables
Create a .env file to store sensitive information like the API key, database connection details, and other configurable parameters:

```bash

OPENWEATHERMAP_API_KEY=your_api_key
DATABASE_URL=postgresql://admin:adminpass@localhost:5432/weather_data
If using MySQL, modify the DATABASE_URL:
DATABASE_URL=mysql://root:adminpass@localhost:3306/weather_data
Step 2: Migrate Database
Set up the database schema for storing weather data.
python manage.py migrate
```
 # 4. Running the Application
Step 1: Start the Application
You can run the application with:
```
python app.py
```
This will start fetching data from OpenWeatherMap and processing it in real-time.

# Step 2: Accessing the Application
If you’re using a web server (like Flask), access the application at:

```
http://localhost:5000
```
# 5. Tools and Technologies Used
Python: Backend processing and API calls.
PostgreSQL / MySQL: Database for storing weather summaries and historical data.
Docker / Podman: Container management for running the database.
OpenWeatherMap API: Data source for real-time and forecasted weather.
Flask (optional): Web framework for the UI.
Matplotlib: Visualization of weather trends.

# 6. Testing
Test Cases:
API Connection Test:
Ensure the system can successfully connect to the OpenWeatherMap API using a valid API key.
Test by running the following command and checking the logs:
```
python app.py
```
Data Retrieval:

Simulate API calls by adjusting the interval and ensure the system is retrieving data from the specified cities.
Use sample data to test whether the parsing of weather data is correct.
Temperature Conversion:

Test the conversion of temperatures from Kelvin to Celsius based on user preferences.
Daily Summary Calculations:

Simulate a sequence of weather updates and verify that daily summaries (average, min, max temperatures) are calculated correctly.
Alert Testing:

Define user thresholds for alerts (e.g., temperature exceeding 35°C) and ensure the system triggers alerts when the threshold is breached.

# Bonus Features
Extended Weather Parameters:
The system now includes additional parameters such as humidity and wind speed in the rollups and aggregates. The same thresholds can be applied to these parameters, and forecasts are retrieved to alert users ahead of time.
Additional Weather Parameters: The system now tracks and aggregates humidity and wind speed data.

Forecast Support:
Weather forecasts for the next 5 days are fetched and processed to provide insights on upcoming weather conditions. Forecast-based alerts trigger notifications if predicted weather exceeds the defined thresholds.
Weather Forecasting: Weather forecasts for the next 5 days are fetched and processed to generate summaries and forecast-based alerts.
