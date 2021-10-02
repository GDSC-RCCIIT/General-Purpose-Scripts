import smtplib                                      # Simple Mail Transfer Protocol
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3                                      # Python Text to Speech version 3
import getpass                                      # Take Hidden Password Input
import pyperclip                                    # Copy text to clipboard


# Talk function which uses pyttsx3
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Speech to text which uses Speech Recognition with google api
def getSpeech():
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source, phrase_time_limit=3)
        try:
            info = listener.recognize_google(voice)
            return info
        except:
            return None


# Get email subject info
def subject():
    talk("What is Subject of your Email?")
    em_subject = getSpeech()

    while em_subject == None:
        talk("Can't understand, Speak Again!")
        em_subject = getSpeech()

    return em_subject


# Get email body info
def body():
    talk("What is body of your Email?")
    em_body = getSpeech()
    while em_body == None:
        talk("Can't understand, Speak Again!")
        em_body = getSpeech()

    return em_body


# Get sender's info
def sender():
    talk("What is the name of sender?")
    em_sender = getSpeech()

    while em_sender == None:
        talk("Can't understand, Speak Again!")
        em_sender = getSpeech()

    if em_sender.lower() in email_dict:
        emailid = email_dict[em_sender.lower()]

    else:
        emailid = "Email ID Not Available"

    return em_sender.title(), emailid


# Get receiver's info
def reciever():
    talk("What is the name of reciever?")
    em_reciever = getSpeech()

    while em_reciever == None:
        talk("Can't understand, Speak Again")
        em_reciever = getSpeech()

    if em_reciever.lower() in email_dict:
        emailid = email_dict[em_reciever.lower()]

    else:
        emailid = "Email ID Not Available"

    return em_reciever.title(), emailid


# Send Email using smtplib
def sendEmail(reciever, sender, subject, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)

    email = EmailMessage()
    email['From'] = sender
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(message)

    server.send_message(email)


# Reading usernames and emails from text file
def readFile():
    f = open("userEmails.txt", "r")
    data = (f.read())
    ls = []
    x = ''
    for i in data:
        if i == '\n':
            ls.append(x)
            x = ''
        else:
            x = x+i
    ls.append(x)

    for i in ls:
        name, email = i.split()
        email_dict[name] = email


# Adding more usernames and emails to text file
def writeFile(name, email):
    f = open("userEmails.txt", "a")
    f.write(f"\n{name.lower()} {email.lower()}")


if __name__ == '__main__':
    print("Email Sender launched\n")
    email_dict = {}
    readFile()
    engine = pyttsx3.init()
    listener = sr.Recognizer()

    ans = 'yes'
    while 'yes' in ans:

        subject = subject()
        body = body()
        sender, s_email = sender()
        reciever, r_email = reciever()

        if s_email == "Email ID Not Available":
            talk("Unable to fetch Email I D for the given sender, please type down sender's email")
            s_email = input('>>')
            writeFile(sender, s_email)
        if r_email == "Email ID Not Available":
            talk("Unable to fetch Email I D for the given reciever, please type down reciever's email")
            r_email = input('>>')
            writeFile(reciever, r_email)

        print(f"\nTo: {reciever}({r_email})")
        print("\nSubject:", subject)
        print("\nBody:", body)
        print("\nBest Regards,")
        print(sender, "\n")

        talk("Preview your Email, Do you want to send it?")
        
        send = getSpeech()
        while send == None:
            talk("Can't understand, Speak Again")
            send = getSpeech()
        if 'yes' in send:
            talk("Type down sender's password to send email.")
            # password = getpass.getpass(prompt="Password: ")
            password = input(">>")
            try:
                sendEmail(r_email, s_email, subject, password, body)
            except:
                talk("Invalid Credentials, your email have been copied to clipboard.")
                pyperclip.copy(f"To: {reciever}({r_email})\nSubject: {subject}\nBody: {body}\n\nBest Regards,\n{sender}")

        else:
            talk("Do you want to copy this email to clipboard?")
            copy = getSpeech()
            while copy == None:
                talk("Can't understand, Speak Again")
                copy = getSpeech()
            if 'yes' in copy:
                pyperclip.copy(f"To: {reciever}({r_email})\nSubject: {subject}\nBody: {body}\n\nBest Regards,\n{sender}")
            talk("Your Email have been successfully copied to clipboard")

        talk("Do you want to send another Email?")
        ans = getSpeech()
        while ans == None:
            talk("Can't understand, Speak Again")
            ans = getSpeech()
        ans = ans.lower()
