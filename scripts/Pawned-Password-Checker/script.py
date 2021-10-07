import requests
import hashlib

API_URL = "https://api.pwnedpasswords.com/range/"

password = input("Enter your password: ")
sha = hashlib.sha1(password.encode()).hexdigest()
first5, tail = sha[:5], sha[5:]

response = requests.get(API_URL + sha[0:5:])
found = False
for resp in response.text.splitlines():
    if(resp.find(tail.upper()) != -1):
        found = True
        break
print("You password is leaked online" if found else "You password is not leaked online")
