import os
from tkinter import *
from tkinter import messagebox
Window=Tk()
Window.geometry("1920x1080")
Window.title("MAIL OTP")
def verify():
    cmd=str(a.get())
    temp='python sendmail.py'+' '+cmd
    os.system(temp)
label1=Label(Window,text="One Time Password",relief="solid",font=("arial",26,"bold"),fg='blue').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="EMAIL ID",font=("arial",22,"bold")).place(x=0,y=50)
w=Entry(Window,width=20,validate="key",textvariable=a)
w.place(x=900,y=50)
log = Button(Window, text="Proceed",relief="raised", bg='yellow', font=("arial", 26, "bold"), fg='black',command=verify).place(x=900,y=150)
Window.mainloop()