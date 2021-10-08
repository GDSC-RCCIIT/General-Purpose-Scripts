# Run this script as root

import csv
from datetime import datetime as dt
import platform

# change hosts path according to your OS
if "Linux" in platform.platform():
    print("System Detected: ", platform.platform())
    hosts_path = "/etc/hosts"
elif "Darwin" in platform.platform():
    print("System Detected: ", platform.platform())
    hosts_path = "/etc/hosts"
elif "Window" in platform.platform():
    print("System Detected: ", platform.platform())
    hosts_path = "C:\\Windows\\System32\\drivers\\etc"

# localhost's IP
redirect = "127.0.0.1"

# websites That you want to block
website_list = []
with open("websites.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        website_list.append(row)


# time of your work
inp = input("""You want to WORK or have FUN [work(W)/fun[F]]:""")
if inp == "W" or inp == "w":
    print("Working hours...")
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                # mapping hostnames to your localhost IP address
                file.write(redirect + " " + website + "\n")
elif inp == "F" or inp == "f":
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)

        # removing hostnmes from host file
        file.truncate()

    print("Fun hours...")
else:
    print("Sorry, Couldn't understand what you want")
