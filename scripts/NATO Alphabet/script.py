import sys
from gtts import gTTS
from playsound import playsound

txt = ""
nato_alphabet = {
    "a": "alpha",
    "b": "bravo",
    "c": "charlie",
    "d": "delta",
    "e": "echo",
    "f": "foxtrot",
    "g": "golf",
    "h": "hotel",
    "i": "india",
    "j": "juliet",
    "k": "kilo",
    "l": "lima",
    "m": "mike",
    "n": "november",
    "o": "oscar",
    "p": "papa",
    "q": "quebec",
    "r": "romeo",
    "s": "sierra",
    "t": "tango",
    "u": "uniform",
    "v": "victor",
    "w": "whiskey",
    "x": "x-ray",
    "y": "yankee",
    "z": "zulu",
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "niner",
    ".": "decimal",
}

try:
    sys.argv[1]
except:
    print("Usage: script.py <word>")
    exit(1)

for letter in sys.argv[1]:
    if letter.lower() not in nato_alphabet:
        print(letter)

    else:
        print(nato_alphabet[letter.lower()])
        txt += nato_alphabet[letter.lower()] + " "

# Language to be converted into
language = "en"

# Passing the text and language to the engine, here we have marked slow=False.
# Which tells the module that the converted audio should have a high speed.
myobj = gTTS(text=txt, lang=language, slow=False)

# Saving the converted audio in a mp3 file named nato
myobj.save("nato.mp3")

# Playing the converted file
playsound("nato.mp3")
