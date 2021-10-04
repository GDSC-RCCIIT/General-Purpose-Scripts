from tkinter import *

from tkinter import Tk

import base64
import random

root = Tk()

root.geometry("1200x6000")

root.title("Message Encyption and Decyption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)

# UI BUILDING

lblInfo = Label(Tops, font=('helvitica', 50, 'bold'),
                text="Secured Chat Machine with \n End-to_End Encryption",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

# INTIALISING VARIABLES
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

lblMsg = Label(f1, font=('arial', 16, 'bold'),
               text=" MESSAGE ", bd=16, anchor="w")
lblInfo.grid(row=1, column=0)

txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="Powder blue", justify='center')
txtMsg.grid(row=1, column=1)

lblkey = Label(f1, font=('arial', 16, 'bold'),
               text="Key (only interger)", bd=16, anchor="w")
lblkey.grid(row=2, column=0)

txtkey = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='center')
txtkey.grid(row=2, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=10, anchor="w")
lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4, bg="Powder blue",
                justify='center')
txtmode.grid(row=3, column=1)

lblResult = Label(f1, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, justify='center')
lblResult.grid(row=2, column=2)

txtResult = Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="white", justify='center')

txtResult.grid(row=2, column=3)


# VIFGENERE CIPHER
# FUNCTION TO ENCODE

def encode(key, msg):
    enc = []

    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# FNCTION TO DECODE
def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def qExit():
    root.destroy()


def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


def Results():
    print("Message= ", (Msg.get()))

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))


# SHOW MESSAGE BTN
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="powder blue",
                  command=Results).grid(row=7, column=1)

# RESET BTN
btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)

# Exit BTN
btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black",
                 font=('arial', 16, 'bold'), width=10,
                 text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)
root.mainloop()
