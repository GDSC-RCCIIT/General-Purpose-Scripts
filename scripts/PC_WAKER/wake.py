import pyautogui
import time
import argparse
import sys

pyautogui.FAILSAFE = False

count = 0

def wake(args):
    global count
    while True:
        time.sleep(args.time)
        for i in range(0, 100):
            pyautogui.moveTo(0, i * 5)
        for i in range(0, 3):
            pyautogui.press('shift')
        if args.v == 2:
            count += 1
            print(count)
        else:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-time','-t', type=float, default=30.0, help="Time(seconds) to wait before moving the mouse to keep the computer wake. Default is 30 seconds")

    parser.add_argument('-v', type=int, default=1, help="This defines verbosity level. This is for to see how many times the wake function has run. Default is 1 and maximum is 2")

    args = parser.parse_args()

    sys.stdout.write(str(wake(args)))