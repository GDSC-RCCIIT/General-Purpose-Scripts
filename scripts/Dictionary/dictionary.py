import urllib.request
import time
import sys

from bs4 import *

print("                Welcome to My Dictionary")
print("                ------------------------")
print("\n ")
c = "A"
import webbrowser


def webpage(u):
    webbrowser.open(u)


def dic():
    try:
        p = n = 0
        search = input("Enter the word=")
        url = "https://www.vocabulary.com/dictionary/" + search
        s = urllib.request.urlopen(url).read()
        s = s.decode("utf-8")
        soupm = BeautifulSoup(s, "html.parser")
        soup = soupm.body.p
        r = str(soup)
        if "Whether you're a student, an educator, " in r:
            soup2 = soupm.body.tr
            soup = soup2
        if soup == None:
            soup1 = BeautifulSoup(s, "html.parser")
            soup1 = soup1.body.h3
            soup = soup1
        soup = str(soup)
        # print(soup.gettext())
        if "For Everyone" in soup or "Whether you're a student, an educator, " in soup:
            print(
                "Sorry Please check the word or else the word is not in the dictionary"
            )
            return url
        for i in soup:
            if i == "<":
                p = p + 1
            elif i == ">":
                p = 0
            elif i == "\t":
                continue
            elif i == "\n":
                n += 1
                if n > 3:
                    continue
            elif p == 0:
                print(i, end="")
                time.sleep(0.04)
    except:
        print(
            "Sorry!!enter a valid word \n Make sure you have an active internet connection \n"
        )
        webpage(url)
        print("\n")
    return url


while c != "E" or c != "e":
    url = dic()
    c = input("\n Enter R to read more C to continue E to exit=")
    if c == "r" or c == "R":
        webpage(url)
        counter = 0
        for i in range(0, 9, 1):
            if counter == 0:
                counter = counter + 1
                print("Wait a minute untill we fetch your word", end="")
            print("..", end="")
            time.sleep(1)
        c = input("\n Enter R to read more C to continue E to exit=")
    if c == "c" or c == "C":
        pass
    elif c == "E" or c == "e":
        break
print("\n ")
print("         THANK YOU FOR USING MY DICTIONARY")
