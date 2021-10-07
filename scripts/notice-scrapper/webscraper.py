import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

print(
    "HEY YOU ,JUST RUN THE PROGRAM.THIS WILL CREATE A NOTICE.CSV FILE WHERE YOU FIND ALL OF IT\n\n\n"
)
my_url = "http://www.rcciit.org/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
contents = page_soup.findAll("div", {"class": "contentBox"})
filename = "notice.csv"
f = open(filename, "w")
headers = "NOTICE:\n"
f.write(headers)
for content in contents:
    notice = content.findAll("td", {"colspan": "2"})[0].text

    f.write(notice.replace(",", " ") + "\n\n")
f.close()
print("\n\n")
a = int(input("HUMAN TEST:  CAPTCHA: 2+2="))
if a == 4:
    print("human")
else:
    print("robot uprising")
c = input(
    " OPEN THE NOTICE.CSV FILE.\n DONOT FORGET TO DELETE THE notice.csv FILE AFTER USE"
)
