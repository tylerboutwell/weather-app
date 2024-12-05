import requests
api_key = "Enter Your API Key"

#Prompt user for location
user_city = input("Please enter city: ")
user_state = input("Please enter state: ")
user_country_code = input("Please enter country code: ")

#Get location lat and lon from geo api
location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_city},"
                        f"{user_state},{user_country_code}&limit={5}&appid={api_key}")
lat = location.json()[0]['lat']
lon = location.json()[0]['lon']

#Get weather from weather api
weather_results = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial')
print(f"Temperature in {user_city} is {weather_results.json()['main']['temp']}")

#print(requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial").json())