# pip install psutil
import psutil,time
number=int(input("Enter Percentage you want to get Notified:"))
while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if percent <= number:
        # pip install py-notifier
        # pip install win10toast
        from pynotifier import Notification

        Notification(
            title=f"Battery reached to {number}",
            description=str(percent) + "% Battery remain!!",
            duration=5,  # Duration in seconds

        ).send()
        break

    time.sleep(60)
    continue
