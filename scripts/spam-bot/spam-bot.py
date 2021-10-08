# import packages
import pyautogui as auto
import time

# Put cursor where you want to type in this time
msg = input("Enter the message: ")
n = input("How many times ? [-1 for infinite times]: ")

print("Put cursor in the text-field")
time.sleep(5)  # Here 5 seconds selected for that.

if int(n) != -1:
    for i in range(0, int(n)):
        auto.typewrite(msg + "\n")

else:
    while True:
        auto.write(msg)
        auto.press("enter")  # 'Enter' key is pressed
        auto.sleep(1)  # Time Gap of 1 second b/w two messages
    # stop the program execution when you want to stop spamming
