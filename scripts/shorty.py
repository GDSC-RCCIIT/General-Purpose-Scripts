import requests, os, sys

print("Enter URL: ", end="")
url = input()
short = "http://tinyurl.com/api-create.php?url=" + url
final = requests.get(short)  # direct link is passed and shortened is returned here
if final.text == "Error":
    print("The provided Link is Not valid! Retry")
else:
    # print (short)
    print("Shortened Link: " + final.text)
