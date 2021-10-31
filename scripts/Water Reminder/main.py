import time
from plyer import notification

print("Welcome to Water Reminder application!")
print("You will be reminded to drink water every 2 hours")

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Time to drink water!",
            message="It's time to hydrate your body again",
            app_icon="icon.ico",
            timeout=10,
        )
        time.sleep(120 * 60)
