from tkinter import *
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder

t = Tk()
t.title("TRUECALLER")
t.geometry("350x165")


# get details function
def get_Details():
    gett = enter.get()
    opt_var = variable.get()

    # if entry empty throw error else show op
    if not gett:
        messagebox.showerror("Data error", "Can't keep empty")
    else:
        code_no = opt_var + gett
        phone_number1 = phonenumbers.parse(code_no, "en")

        real_phone_number = phonenumbers.format_number(phone_number1, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        geo_location = geocoder.description_for_number(phone_number1, "en")
        sim = carrier.name_for_number(phone_number1, "en")

        messagebox.showinfo(real_phone_number, sim + "\n" + geo_location)
        t.geometry("350x200")


# LABEL1
L1 = Label(t, text="Enter your Phone number:", font=("poppins", 9), bg="#fff761", fg="#000000", width='50')
L1.place(x=0, y=13)

# PHONE CODE OPTIONS (you can add more)
phone_code = ["+91",
              "+93",
              "+32"
              ]

variable = StringVar(t)
variable.set(phone_code[0])

code_opt = OptionMenu(t, variable, *phone_code)
code_opt.place(x=46, y=50)

# ENTRY BOX
enter = Entry(t, width="20", font=("poppins", 13))
enter.place(x=118, y=53)

# BUTTON
but = Button(t, text="Get Details", font=("poppins", 10, "bold"), fg="#fffc3b", bg="#454543", width=25, relief="raised",
             command=get_Details)
but.place(x=66, y=90)

# TANCODES Label
L2 = Label(t, text=">_TanCodes", font=("poppins", 7), bg="#c5dae8", border="2")
L2.place(x=140, y=140)

t.resizable(0, 0)
t.configure(background='#f2fcff')
t.mainloop()
