import time
import pyobjus
from plyer import notification

title_msg = input("Enter title: ")
msg = input("Enter the reminder message: ")
sleep_time = int(input("Enter time after which you want to be remineded: "))
timer = int(input("Enter the interval time: "))

while True:
    notification.notify(
        title=title_msg,
        message=msg,
        # app_icon = "<path of the icon-image>",
        timeout=timer,
    )
    time.sleep(sleep_time)  # time is seconds
