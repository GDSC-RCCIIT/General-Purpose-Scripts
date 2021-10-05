

'''

from gtts import gTTS
from playsound import playsound
import os
filename="welcome"
# The text that you want to convert to audio
mytext = "Welcome to our Voice Based Email. Login with your email account in order to continue. "
  
myobj = gTTS(text=mytext, lang='en', slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(filename+".mp3")
  
# Playing the converted file
playsound(filename+".mp3")
os.remove(filename+".mp3")



'''



import imaplib,email
from gtts import gTTS
import os
from playsound import playsound

import speech_recognition as sr



import re

file = "good"
i="0"
passwrd = ""
addr = ""
item =""


def texttospeech(text, filename):
    filename = filename + '.mp3'
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return

def speechtotext(duration):
    global i, addr, passwrd
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        playsound('speak.mp3')
        audio = r.listen(source, phrase_time_limit=duration)
    try:
        response = r.recognize_google(audio)
    except:
        response = 'N'
    return response

def convert_special_char(text):
    temp=text
    special_chars = ['attherate','dot','underscore','dollar','hash','star','plus','minus','space','dash']
    for character in special_chars:
        while(True):
            pos=temp.find(character)
            if pos == -1:
                break
            else :
                if character == 'attherate':
                    temp=temp.replace('attherate','@')
                elif character == 'dot':
                    temp=temp.replace('dot','.')
                elif character == 'underscore':
                    temp=temp.replace('underscore','_')
                elif character == 'dollar':
                    temp=temp.replace('dollar','$')
                elif character == 'hash':
                    temp=temp.replace('hash','#')
                elif character == 'star':
                    temp=temp.replace('star','*')
                elif character == 'plus':
                    temp=temp.replace('plus','+')
                elif character == 'minus':
                    temp=temp.replace('minus','-')
                elif character == 'space':
                    temp = temp.replace('space', '')
                elif character == 'dash':
                    temp=temp.replace('dash','-')
    return temp



def login_view():
    global i,passwrd,addr

    text1 = "Welcome to our Voice Based Email. Login with your email account in order to continue. "
    texttospeech(text1, file + i)
    i = i + str(1)

    flag = True
    while (flag):
        texttospeech("Enter your Email", file + i)
        i = i + str(1)
        addr = speechtotext(10)
        
        if addr != 'N':
            texttospeech("You meant " + addr + " say yes to confirm or no to enter again", file + i)
            i = i + str(1)
            say = speechtotext(10)
            if say == 'yes' or say == 'Yes':
                flag = False
        else:
            texttospeech("could not understand what you meant:", file + i)
            i = i + str(1)
    addr = addr.strip()
    addr = addr.replace(' ', '')
    addr = addr.lower()
    addr = convert_special_char(addr)
    
    

    flag = True
    while (flag):
        texttospeech("Enter your password", file + i)
        i = i + str(1)
        passwrd = speechtotext(10)
        
        if addr != 'N':
            texttospeech("You meant " + passwrd + " say yes to confirm or no to enter again", file + i)
            i = i + str(1)
            say = speechtotext(3)
            if say == 'yes' or say == 'Yes':
                flag = False
        else:
            texttospeech("could not understand what you meant:", file + i)
            i = i + str(1)
    passwrd = passwrd.strip()
    passwrd = passwrd.replace(' ', '')
    passwrd = passwrd.lower()
    passwrd = convert_special_char(passwrd)
    print("--------------------------------------------------------------\n")
    print("Enter your email : " + addr + "\n")
    print("Enter your password : " + passwrd + "\n")
    print("--------------------------------------------------------------\n")
   

    return addr,passwrd

