# Doc To PDF Converter
![python](https://img.shields.io/badge/language-Python-orange?style=for-the-badge)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=plasitc)](https://github.com/psf/black)

## About
&emsp;A Tkinter GUI Application that converts docx files to pdf files using docx2pdf python module.

![window preview](./Images/window_preview.png)

## Dependencies
- **Python 3.9.1**

| Module    | Version   |
| --------- | --------- |
| [tkinter](https://docs.python.org/3/library/tkinter.html)   | 8.6       |
| [docx2pdf](https://pypi.org/project/docx2pdf/)  | 0.1.7     |

### Installation
- `tkinter` comes installed with Python upon installation.
- To install `docx2pdf` use pip command:
    ```
    pip install docx2pdf
    ```

## How to use GUI
- Select any docx file from your PC by clicking 'Select File' button.
<br>**OR**
<br>Select any folder containing docx files in your PC by clicking 'Select Folder' button.
- The Application will convert the desired file(s) to pdf format.
- The files will be saved with the same name in the same folder from where they're uploaded.

## How to script works
- The GUI is rendered by the help of `tkinter` module. Precisely the `ttk.Button` and `ttk.Label` classes have been used to create the buttons and labels for the GUI.
    ```python
    label = tk.Label(win,text = "Choose File/Folder : ")
    label.grid(row=0,column=0,padx=5,pady=5)

    button1 = ttk.Button(win,text = "Select File",width=30,command=openfile)
    button1.grid(row=1,column=0,padx=5,pady=5)

    button2 = ttk.Button(win,text = "Select Folder",width=30,command=openfolder)
    button2.grid(row=2,column=0,padx=5,pady=5)

    helpLabel = tk.Label(win,text = helpText)
    helpLabel.grid(row=3,column=0,padx=5,pady=5)
    ```
- `showinfo()` method from have been used to display sucessful conversion message.
    ```python
    showinfo("Done","File Sucessfully Converted")
    ```
- `askopenfile()` and `askopendirectory()` methods have been used to ask user to select files from their PC.
    ```python
    file = askopenfile(filetypes =[('Word Files','*.docx')])
    ```
    **OR**

    ```python
    folder = askdirectory()
    ```
- `convert()` method from `docx2pdf` module method have been used to convert the respective file(s).
    ```python
    convert(file.name)
    ```
    **OR**

    ```python
    convert(folder)
    ```
