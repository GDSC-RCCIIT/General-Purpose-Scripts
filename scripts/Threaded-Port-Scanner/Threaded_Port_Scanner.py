import threading
from queue import Queue
import time
import socket
from termcolor import colored

"""
A 'print_lock' is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.

"""

print_lock = threading.Lock()

print(
    colored(
        "              ****  Welcome to Threaded Port Scanner by 'MrRobot3301' **** \n",
        "red",
    )
)

print(
    colored(
        " reach me >>>>>> ' anonymouslegion00@protonmail.com' & ' https://github.com/MrRobot3301/' <<<<<< \n",
        "red",
    )
)

# target = socket.gethostname() #Enable this line to scan localhost
target = input(
    colored("[+] Enter Host/IP Address to scan open ports :  ", "blue")
)  # Disable this line to scan localhost
ip = socket.gethostbyname(target)

print(f"[+] Hostname : {target}")
print(f"[+] Ip Address : {ip}")


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    try:
        con = s.connect((ip, port))
        with print_lock:
            print(colored(f"[+] Port {port} is open", "green"))
        con.close()
    except:
        pass


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()


# Create the queue and threader
q = Queue()

# how many threads are we going to allow for
for x in range(20000):
    t = threading.Thread(target=threader)

    # classifying as a daemon, so they will die when the main dies
    t.daemon = True

    # begins, must come after daemon definition
    t.start()


start = time.time()

# Range of ports to scan
for worker in range(1, 65536):
    q.put(worker)

# wait until the thread terminates.
q.join()
