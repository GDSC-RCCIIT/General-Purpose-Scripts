import psutil
from plyer import notification
import time


threshold = int(input("Enter the threshold: "))
battery = psutil.sensors_battery()
percent = battery.percent
# print(percent)

while True:
    battery = psutil.sensors_battery()
    cur_per = battery.percent
    change = cur_per - percent
    diff = abs(change)
    # print(diff)
    if diff >= threshold:
        notification.notify(
            title="Battery Percentage",
            message=str(cur_per) + "% Battery Remaining",
            timeout=5,
        )
        percent = cur_per
    continue
