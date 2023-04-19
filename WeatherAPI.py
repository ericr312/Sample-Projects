import datetime as dt
import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"
API_key = open('APIkey', 'r').read()

def kelvin_to_cel_fahr(kelvin):
    cel = kelvin - 273.15
    fahr = cel * (9/5) + 32
    return cel, fahr


def wind_direction(speed, degs):
    directions = ["North", "North-NorthEast", "NorthEast", "East-NorthEast", "East", "East-SouthEast", "SouthEast",
                  "South-SouthEast", "South", "South-SouthWest", "SouthWest", "West-SouthWest", "West",
                  "West-NorthWest", "NorthWest", "North-NorthWest"]
    index = round(((degs + 11.25) % 360) / 22.5)
    direction = directions[index]

    if speed == 0:
        direction = "North"

    return speed, direction


def weather_data(place):
    url = base_url + "appid=" + API_key + "&q=" + place
    response = requests.get(url).json()                         #creates a dictionary of the data
    description = response['weather'][0]['description']
    wind_speed = response['wind']['speed']
    wind_dir = response['wind']['deg']
    wind_stat = wind_direction(wind_speed, wind_dir)
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_cel_fahr(temp_kelvin)
    return temp_celsius, description, wind_stat


def display_weather(temp, desc, winds):
    print(f'Temperature: {round(temp, 2)}°C')
    print(f'Conditions: {desc}')
    print(f'Winds: {winds[0]} m/s, from the {winds[1]}')

city = input("Enter City: ")

temp, desc, wind = weather_data(city)
display_weather(temp, desc, wind)

