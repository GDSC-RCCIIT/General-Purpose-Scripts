from os import close
from tkinter import *
from datetime import date, datetime
import threading
import time
from typing import Counter
import pygame
from PIL import ImageTk,Image
gui= Tk()
Show=Text(gui,height=7,width=20, pady=10)
def stop():
    pygame.mixer.init()
    pygame.mixer.music.stop()
def play(hh,mm,ss):
    gui2=Toplevel(gui)
    wake=Label(gui2,text="It's Time Buddy",fg="red",font=("Arial",20)).place(x=0,y=50)
    exit_button=Button(gui2,text="STOP",command=lambda: (stop(),gui2.destroy())).place(x=70,y=100)
    h=str(hh)
    m=str(mm+5)
    s=str(ss)
    snooze=Button(gui2,text="SNOOZE",command=lambda: (thread_run(h,m,s),stop(),gui2.destroy())).place(x=70,y=150)
    pygame.mixer.init()
    pygame.mixer.music.load("resources/alarm_beep.mp3")
    pygame.mixer.music.play(-1)
def alarm(h,m,s):
    hh=int(h)
    mm=int(m)
    ss=int(s)
    hours=[]
    minute=[]
    second=[]
    hours.append(hh)
    minute.append(mm)
    second.append(ss)
    show=h+":"+m+":"+s
    Show.insert(END,show+'\n')
    count=len(hours)
    for i in range(len(hours)):
        while True:
            if(hours[i]==datetime.now().hour and minute[i]== datetime.now().minute and second[i]== datetime.now().second):
                play(hh,mm,ss)
                break
def thread_run(h,m,s):
    t=threading.Thread(target=alarm, args=(h,m,s,))
    t.start()
gui.title("Alarm")
gui.geometry("520x500")
gui.configure(bg="#2F2D2D")
canvas= Canvas(gui, width= 70, height= 70,bd=0, bg="#2F2D2D")
img= (Image.open("resources/clock.jpg"))
resized_image= img.resize((70,70), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0,anchor=NW,image=new_image)
text = Label(gui,text="Set Your Alarm:", bg="#2F2D2D", fg="white",font=("Arial",16,"bold"))
text1=Label(gui,bg="#2F2D2D", fg="white",font=("Arial",16,"bold"))
text2 = Label(gui,text="Saved Alarms:", bg="#2F2D2D", fg="white",font=("Arial",16,"bold"))
hour = StringVar()
min = StringVar()
sec = StringVar()
addTime = Label(gui,text = "Hours       Mins        Secs",fg="white",bg="#2F2D2D",font=("Arial",16)).place(x = 120,y=190)
hourTime= Entry(gui,textvariable = hour,bg = "white",width = 8)
minTime= Entry(gui,textvariable = min,bg = "white",width = 8)
secTime = Entry(gui,textvariable = sec,bg = "white",width = 8)
def clearTxt():
    hourTime.delete(0,END)
    minTime.delete(0,END)
    secTime.delete(0,END)
submit = Button(gui,text = "Set Alarm",command=lambda: (thread_run(hourTime.get(),minTime.get(),secTime.get()),clearTxt())).place(x =220,y=260)
def Close():
    gui.destroy()
def tick():
    time2=time.strftime("%H:%M:%S")
    text1.config(text=time2)
    text1.after(200,tick)
text1.place(x=420,y=0)
canvas.place(x=220,y=40)
text2.place(x=160,y=300)
text.place(x=160,y=150)
hourTime.place(x=122,y=220)
minTime.place(x=220,y=220)
secTime.place(x=310,y=220)
Show.place(x=160,y=340)
gui.protocol("WM_DELETE_WINDOW",Close)
gui.resizable(False, False)
tick()
gui.mainloop() 