# !/usr/bin/env python3
# system-usage.py
"""Checking Disk and CPU usage."""

import shutil
import psutil
import string
from ctypes import windll


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)

        bitmask >>= 1

    return drives


def check_disk_usage(disk):
    du = shutil.disk_usage(disk + ":\\")
    free = du.free / du.total * 100
    return free


def check_cpu_usage(time):
    cu = psutil.cpu_percent(time)
    return cu


if __name__ == "__main__":
    disks = get_drives()
    time = 5
    for disk in disks:
        print(f"Free space on disk {disk}: {check_disk_usage(disk):.3f} %")

    print(f"Average CPU Usage for {time} sec: {check_cpu_usage(time):.3f} %")
