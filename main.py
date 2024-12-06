import requests
import datetime

api_key = "Put your API key here"

#Prompt user for location
user_city = input("Please enter city: ")
user_state = input("Please enter state: ")
user_country_code = input("Please enter country code: ")
curr_or_five_day = input("Would you like current weather, or 5 day forecast? Enter \"current\" or \"5 day\" : ")

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

if curr_or_five_day == "current":
    #Get current weather from weather api
    weather_results = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial')
    if weather_results.status_code == 200:
        print(f"Current temperature in {user_city} is {weather_results.json()['main']['temp']}")
    else:
        print("Error getting weather data")

elif curr_or_five_day == "5 day":
    #Get five-day forecast from weather api
    five_day_forecast = requests.get(f"http://api.openweathermap.org/data/2.5/"
                                     f"forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial")
    if five_day_forecast.status_code == 200:
        count = 0
        print("---Five day forecast---")
        for i in five_day_forecast.json()['list']:
            count += 1
            utc_offset = datetime.timedelta(seconds=five_day_forecast.json()['city']['timezone'])
            curr_time = datetime.datetime.fromisoformat(i['dt_txt'])
            local_time = curr_time + utc_offset
            local_time = local_time.strftime('%m-%d-%y %I:%M')



            print(f"{local_time}: {i['main']['temp']}")
    else:
        print("Error getting weather data")
else:
    print("Didn't enter current or 5 day")