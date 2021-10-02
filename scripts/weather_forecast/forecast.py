"""
usage:

run python forecast.py <city_name>


"""


from geopy.exc import GeocoderTimedOut as gt
from geopy.geocoders import Nominatim
import requests
import sys


def find_lat_long(city):
    try:
        locator = Nominatim(user_agent="myGeocoder")
        code = locator.geocode(city)
        if code is not None:
            return code.latitude, code.longitude
        else:
            return None, None
    except gt:
        return find_lat_long(city)


def find_forcast(city):
    lat, long = find_lat_long(city)
    if lat is not None and long is not None:
        # print(lat,long)
        url = "https://fcc-weather-api.glitch.me/api/current"
        params = {"lat": lat, "lon": long}
        res = requests.get(url=url, params=params)
        data = res.json()
        print(
            "weather forcast: {} \ntemperature: {} \nmaximum tempreature {} c \nminimum temperature  {} c \nhumidity {} %".format(
                data["weather"][0]["main"],
                data["main"]["temp"],
                data["main"]["temp_max"],
                data["main"]["temp_min"],
                data["main"]["humidity"],
            )
        )
    else:
        print("invalid city name")


if len(sys.argv) == 2:
    city = sys.argv[1]
    find_forcast(city)
else:
    print("too less arguement or too many ... please give a valid city name as cli")
