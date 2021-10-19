from gtts import gTTS
from playsound import playsound
from os import remove
from requests import get


def rand_quotes():
    res = get("https://zenquotes.io/api/random").json()[0]
    return f'{res["q"]} by {res["a"]}'


def day_quotes():
    res = get("https://zenquotes.io/api/today").json()[0]
    return f'{res["q"]} by {res["a"]}'


def say(text):
    gTTS(text=text, lang="en", slow=False).save("temp.mp3")
    playsound("temp.mp3")
    remove("temp.mp3")


if __name__ == "__main__":
    print("type `help` for more information")
    while True:
        inp = input("==>")
        if inp == "?" or inp == "help":
            print(
                """ Commands: 
            random
            today
            exit
            """
            )
        if inp == "random":
            say(rand_quotes())
        if inp == "today":
            say(day_quotes())
        if inp == "exit":
            print("bye bye :) ")
            break

