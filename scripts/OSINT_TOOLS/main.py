import requests
import json
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier


def ip_location(ip):
    # ip=input("enter=")
    r = requests.get(f"https://geolocation-db.com/json/{ip}&position=true")
    res = r.json()
    data = f"""
    Country name -> {res['country_name']} ({res['country_code']})
    State -> {res['state']}
    City -> {res['city']}
    latitude -> {res['latitude']} longitude -> {res['longitude']}
    Postal Code -> {res['postal']}
    IPv4 -> {res['IPv4']}
    """
    print(data)


def phone_num(number):
    ch_number = phonenumbers.parse(number, "CH")
    ro_number = phonenumbers.parse(number, "RO")
    gb_number = phonenumbers.parse(number, "GB")
    country = geocoder.description_for_number(ch_number, "en")
    provider = carrier.name_for_number(ro_number, "en")
    timez = timezone.time_zones_for_number(gb_number)
    more_info = f"https://www.truecaller.com/search/in/{number}"
    data = f"""
    Country -> {country}
    Provider -> {provider}
    time -> {timez}
    for more info visit {more_info}"""
    print(data)


help = """
1. IP lookup
2. Phone number lookup
Press `Ctrl+C` to exit"""
print(help)
try:
    while True:
        user = input("Enter>> ")
        # address = input("enter IP address >>> ")
        # ip_location(address)
        # phone_num("+916291170644")
        if user == "1":
            user_ip = input("Enter IP address >> ")
            ip_location(user_ip)
        elif user == "2":
            user_number = input("Enter phone number >> ")
            phone_num(user_number)
        elif user == "help":
            print(help)
        else:
            print("Wrong input")
            print(help)
except:
    print()
    pass
