import pyttsx3

# Taking text as input:

a = input("Enter text here:\n")

# Text to audio:

engine = pyttsx3.init()
engine.say(a)
engine.runAndWait()
