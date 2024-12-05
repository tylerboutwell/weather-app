import requests

api_key = "ENTER YOUR API KEY"

user_city = input("Please enter city: ")
user_state = input("Please enter state: ")
user_country_code = input("Please enter country code: ")

location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_city},"
                        f"{user_state},{user_country_code}&limit={1}&appid={api_key}")


weather_results = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={33}&lon={55}&appid={api_key}&units=imperial')
print(f"Temperature in {user_city} is {weather_results.json()['main']['temp']}")
print(weather_results.json())