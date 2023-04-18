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

#def wind_direction(speed, degs):
#    dir_dict = {}
#    c_p = ['North', 'North-NorthEast', 'NorthEast', 'East-NorthEast', 'East', 'East-SouthEast', 'SouthEast', 'South-SouthEast',
#           'South', 'South-SouthWest', 'SouthWest', 'West-SouthWest', 'West', 'West-NorthWest', 'NorthWest', 'North-NorthWest']
#    split = 36000//32
    #for i in range(0, 36000, 100):
    #    if i < split:
    #        dir_dict[i] = c_p[0]
    #    if split < i < split*3:
    #        dir_dict[i] = c_p[1]
    #    if split*3 < i < split*5:
    #        dir_dict[i] = c_p[2]
    #    if split*5 < i < split*7:
    #        dir_dict[i] = c_p[3]
    #    if split*7 < i < split*9:
    #        dir_dict[i] = c_p[4]
    #    if split*9 < i < split*11:
    #        dir_dict[i] = c_p[5]
    #    if split*11 < i < split*13:
    #        dir_dict[i] = c_p[6]
    #    if split*13 < i < split*15:
    #        dir_dict[i] = c_p[7]
    #    if split*15 < i < split*17:
    #        dir_dict[i] = c_p[8]
    #    if split*17 < i < split*19:
    #        dir_dict[i] = c_p[9]
    #    if split*19 < i < split*21:
    #        dir_dict[i] = c_p[10]
    #    if split*21 < i < split*23:
    #        dir_dict[i] = c_p[11]
    #    if split*23 < i < split*25:
    #        dir_dict[i] = c_p[12]
    #    if split*25 < i < split*27:
    #        dir_dict[i] = c_p[13]
    #    if split*27 < i < split*29:
    #        dir_dict[i] = c_p[14]
    #    if split*29 < i < split*31:
    #        dir_dict[i] = c_p[15]
    #    if split*31 < i <= split*33:
    #        dir_dict[i] = c_p[0]
    #amped_degs = degs * 100
    #direc = dir_dict[amped_degs]
    #if speed == 0:
    #    direc = 'North'
    #return speed, direc


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
#print(temp, desc, wind)
display_weather(temp, desc, wind)
#display_weather(weather_data(city))

