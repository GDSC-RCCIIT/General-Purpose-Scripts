# importing packages
import time
from datetime import datetime
from plyer import notification
from playsound import playsound

# import pyobjus

msg = "Wake Up!"  # your default remainder/alarm message
audio_path = "./alarm-songs/ncs_high.mp3"  # your default remainder/alarm audio


def show_notification(title_msg, message):
    """shows notification if proper permissions given and modules installed"""
    print("notification displayed")


#    notification.notify(
#        title=title_msg,
#        message=msg,
#        # app_icon = "<path of the icon-image>",
#        timeout=0,
#    )


def set_timer():
    """function to set Timer"""
    timer_time = input("Enter the time after which you want a remainder:\nHH:MM:SS\n")
    timer_hour = int(timer_time[0:2])
    timer_minute = int(timer_time[3:5])
    timer_seconds = int(timer_time[6:8])
    print("Setting up timer...")
    #    print(timer_hour * 3600 + timer_minute * 60 + timer_seconds)
    time.sleep(timer_hour * 3600 + timer_minute * 60 + timer_seconds)
    print(msg)
    show_notification("Remainder", msg)
    playsound(audio_path)


def set_alarm():
    """function to set Alarm"""
    alarm_time = input("Enter the time of alarm to be set:\nHH:MM:SS [AM/PM]\n")
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_seconds = alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    print("Setting up alarm...")

    while True:
        now = datetime.now()
        print(now)
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")
        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_minute == current_minute:
                    if alarm_seconds == current_seconds:
                        print(msg)
                        show_notification("Alarm", msg)
                        playsound(audio_path)
                        break


if __name__ == "__main__":
    isDefaultAudio = True
    isDefault = input(
        f"Do you want to change default audio from {audio_path}? (N/y) : "
    )
    if isDefault == "y":
        audio_path = input("Provide audio path : ")
    while True:
        print("Menu : ")
        print("\t[1.] Set Timer")
        print("\t[2.] Set Alarm")
        print("\t[3.] Change audio path")
        print("\t[4.] Change message")
        print("\t[5.] Exit")
        choice = int(input(("Enter choice : ")))
        if choice == 1:
            set_timer()
        elif choice == 2:
            set_alarm()
        elif choice == 3:
            audio_path = input("Enter audio path : ")
        elif choice == 4:
            msg = input("Enter new message : ")
        elif choice == 5:
            print("Thank you :)")
            break
        else:
            print("Invalid choice !")
