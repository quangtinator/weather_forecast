import requests
import pandas as pd

BASE_URL = "http://api.weatherapi.com/v1/forecast.json?"
API_KEY = "bea853d469e0444dbe7152331220507"
DAYS = 3

city = input("Enter city name: ")

response = requests.get(BASE_URL + "key="+ API_KEY + "&q=" + city + "&days=" + str(DAYS))

if response.status_code != 200:
    print("API request failed with status code:", response.status_code)
else:
    weather_forecast = response.json()['forecast']['forecastday']

    timestamps = []
    windspeed = []
    temp = []
    cloud = []

    for day in weather_forecast:
        for hour in day['hour']:
            timestamps.append(hour['time'])
            windspeed.append(hour['wind_kph'])
            temp.append(hour['temp_c'])
            cloud.append(hour['cloud'])
    
    df = pd.DataFrame(list(zip(timestamps, windspeed, temp, cloud)),
               columns =['Timestamps', 'Wind Speed(kmph)', 'Temperature(°C)', 'Cloud(%)'])
    
    df['Timestamps'] = pd.to_datetime(df['Timestamps'])
    df.to_csv("weather_forecast.csv", index=False)