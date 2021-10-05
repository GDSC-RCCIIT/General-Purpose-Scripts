import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile, askdirectory
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("Word to PDF Converter")


def openfile():
    file = askopenfile(filetypes=[("Word Files", "*.docx")])
    convert(file.name)
    showinfo("Done", "File Sucessfully Converted")


def openfolder():
    folder = askdirectory()
    convert(folder)
    showinfo("Done", "Folder Files Sucessfully Converted")


label = tk.Label(win, text="Choose File/Folder : ")
label.grid(row=0, column=0, padx=5, pady=5)

button1 = ttk.Button(win, text="Select File", width=30, command=openfile)
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = ttk.Button(win, text="Select Folder", width=30, command=openfolder)
button2.grid(row=2, column=0, padx=5, pady=5)

helpText = """
    How to Use -
    Use the application to either convert single file or a folder containing multiple doc files!
    Simply select your file/folder and the app will take care of the rest!
"""

helpLabel = tk.Label(win, text=helpText)
helpLabel.grid(row=3, column=0, padx=5, pady=5)

win.mainloop()
