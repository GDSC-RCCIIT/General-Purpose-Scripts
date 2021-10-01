import threading
from queue import Queue
import time
import socket

print_lock = threading.Lock()


target = input("Target IP address: ")


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = s.connect((target, port))
        with print_lock:

            print("port: ", port)
        connection.close()
    except:
        pass


def threader():
    while True:
        worker = que.get()
        portscan(worker)

        que.task_done()


# Createing the queue and threader
que = Queue()

for x in range(30):
    thred = threading.Thread(target=threader)
    thred.daemon = True
    thred.start()


start = time.time()

for worker in range(1, 100):
    que.put(worker)

que.join()
