# Script to automate Email Sending
import smtplib

to = input("Enter the Email of recipent:\n")
content = input("Enter the Content for E-Mail:\n")

sender_email = "youremail@mail.com"
sender_password = "yourpassword"


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", "587")
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, content)
    server.close()
    print("Email Successfully send\n")


sendEmail(to, content)
