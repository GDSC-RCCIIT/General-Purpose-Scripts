import pyttsx3
import PyPDF2

print("WELCOME TO AUDIOBOOK")
import tkinter as tk
from tkinter import filedialog
import os
print("Please select a file:")
root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilename()

files2=files.split("/")
filename=files2[len(files2)-1]
"""Removing filename from path"""
removing_file=[]
for i in range(len(files2)):
    if i!=len(files2)-1:
        removing_file.append(files2[i]+"/")
"""Assigning path"""
path=""
for a in removing_file:
    path+=a

os.chdir(path)
book = open(filename, "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)  # prints number of pages

speaker = pyttsx3.init()  # Initialize the speaker
rate = speaker.getProperty("rate")
speaker.setProperty("rate", 170)
# rate=170 is normal speed, you can increase and decrease as per your convenience

speaker = pyttsx3.init()
user_input = int(input("Enter the starting page:"))
for i in range(user_input, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
print("Thank you")
