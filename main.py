import requests
import datetime
import pytz

api_key = "Put your API key here"

#Prompt user for location
user_city = input("Please enter city: ")
user_state = input("Please enter state: ")
user_country_code = input("Please enter country code: ")

#Get location lat and lon from geo api
location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_city},"
                        f"{user_state},{user_country_code}&limit={5}&appid={api_key}")
if location.status_code == 200:
    lat = location.json()[0]['lat']
    lon = location.json()[0]['lon']
else:
    "Error getting location"
    lat = 1
    lon = 1

#Get weather from weather api
weather_results = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial')
if weather_results.status_code == 200:
    print(f"Current temperature in {user_city} is {weather_results.json()['main']['temp']}")
else:
    print("Error getting weather data")

five_day_forecast = requests.get(f"http://api.openweathermap.org/data/2.5/"
                                 f"forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial")
if five_day_forecast.status_code == 200:
    count = 0
    print("---Five day forecast---")
    for i in five_day_forecast.json()['list']:
        count += 1
        date_info = i['dt_txt']
        date_parsed = datetime.datetime.strptime(date_info, '%Y-%m-%d %H:%M:%S')
        date_formatted = datetime.datetime.strftime(date_parsed, '%m-%d-%y %H:%M:%S')
        print(f"{date_formatted}: {five_day_forecast.json()['city']['timezone']} {i['main']['temp']}")
else:
    print("Error getting weather data")