from pdf2docx import parse
import tkinter as tk
from tkinter import filedialog
import os,time


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
pdf_file = filename
filename2=filename.split(".")
docxfile=filename2[0]
word_file = f"{docxfile}.docx"
parse(filename, word_file, start=0, end=None)
time.sleep(2)
print(f"{pdf_file} converted into {word_file}")
