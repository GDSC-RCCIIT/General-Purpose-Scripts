import bs4 as Beautifulsoup
from requests_html import HTMLSession
from time import sleep
import smtplib


class scrap:
    def __init__(self, url, budget, email):

        self.url = url
        self.budget = int(budget)
        self.email = email
        self.session = HTMLSession()
        self.webpage = self.session.get(self.url).content
        self.parser = "lxml"
        self.soup = Beautifulsoup.BeautifulSoup(self.webpage, self.parser)

    def __str__(self):
        return self.soup.prettify()

    def get_title(self):
        self.product_title = self.soup.find(id="productTitle").text.strip()
        return self.product_title

    def get_price(self):

        price_raw = self.soup.find(id="priceblock_ourprice").text.strip()
        price_filtered = price_raw[1 : len(price_raw) - 3]
        self.product_price = int("".join([x for x in price_filtered if x != ","]))
        return self.product_price

    def checks(self):
        if self.product_price < self.budget:
            return True
        else:
            return False

    def run(self):
        self.get_price()
        self.get_title()
        if self.checks():
            self.send_mail()
            return False
        else:
            return True

    def send_mail(self):
        body = (
            """Your product <b>"""
            + str(self.product_title)
            + """</b> Found lower then your threshold value <b>"""
            + str(self.budget)
            + """</b>.\n This procuct is available is at  price of <b>"""
            + str(self.product_price)
            + """</b>"""
        )
        print(body)
        dev_email = "User's Email Address"
        dev_password = "User's Password"
        server = smtplib.SMTP("smtp.gmail.com", "587")
        server.ehlo()
        server.starttls()
        server.login(dev_email, dev_password)
        server.sendmail(dev_email, self.email, body)
        server.close()
        print("Email Successfully sent\n")


url = input("Enter Url of amazon webpage: ")
price = int(input("Enter Threshold price: "))
email = input("Enter your Email Address to send an alert: ")
recurrence = float(input("Enter time gap to check price (in Hrs): "))
main = scrap(url, price, email)
while main.run():
    sleep(recurrence * 60 * 60)
