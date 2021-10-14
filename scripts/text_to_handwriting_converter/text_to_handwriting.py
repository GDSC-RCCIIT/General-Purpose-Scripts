import pywhatkit
from tkinter import filedialog
from PIL import Image


def option():
    return input(
        """Press 1 or 2
    1. Type your own text
    2. Upload a file
    input--> """
    )


def save_handwriting():
    print("Processing....")
    pywhatkit.text_to_handwriting(text, "Handwriting.png", rgb=(0, 0, 225))


# -----User Input to whether he prefers manually typing or uploading a .txt file--------
option_input = option()


# ----------Loops until valid inputs have been given--------
while option_input != "1" and option_input != "2":
    print("You have pressed the wrong option please try again\n")
    option_input = option()


# ----------Checks if option 1 has been clicked--------
if option_input == "1":
    text = input(
        """Enter the text here:
    input--> """
    )
    save_handwriting()


# ----------Checks if option 2 has been clicked--------
if option_input == "2":
    try:
        filepath = filedialog.askopenfilename(
            initialdir="C:",
            title="Open file",
            filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        )
        file = open(filepath, "r")
        text = file.read()
        save_handwriting()
        file.close()

    except:
        print("You haven't selected a file\n")


# ----------To show the converted image to the user--------
img = Image.open("Handwriting.png")
img.show()
