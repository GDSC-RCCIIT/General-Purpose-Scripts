from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

""" ask user to input the instagram post url """
link = input("Enter Instagram Image URL: ")

""" 
create a webdriver chrome object by passing the path of "chromedriver.exe" file.(do not include .exe in the path).
"""
driver = webdriver.Chrome("chromedriver")

""" Open the instagram post on your chrome browser"""
driver.get(link)

""" Fetch the source file of the html page using BeautifulSoup"""
soup = BeautifulSoup(driver.page_source, "lxml")

""" Extract the url of the image from the source code"""
img = soup.find("img", class_="FFVAD")
img_url = img["src"]


"""Download the image via the url using the requests library"""
r = requests.get(img_url)

with open("instagram" + str(time.time()) + ".png", "wb") as f:
    f.write(r.content)

print("success")
