# Python program to implement server side of chat room.
import socket
import select
import sys
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])

server.bind((IP_address, Port))

server.listen(100)

list_of_clients = []

def clientthread(conn, addr):

	# sends a message to the client whose user object is conn
	conn.send("Welcome to this chatroom!")

	while True:
			try:
				message = conn.recv(2048)
				if message:

					
					print ("<" + addr[0] + "> " + message)

					# Calls broadcast function to send message to all
					message_to_send = "<" + addr[0] + "> " + message
					broadcast(message_to_send, conn)

				else:
					
					remove(conn)

			except:
				continue

def broadcast(message, connection):
	for clients in list_of_clients:
		if clients!=connection:
			try:
				clients.send(message)
			except:
				clients.close()

				# if the link is broken, we remove the client
				remove(clients)

def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

while True:

	
	conn, addr = server.accept()

	
	list_of_clients.append(conn)

	# prints the address of the user that just connected
	print (addr[0] + " connected")

	# creates and individual thread for every user
	# that connects
	start_new_thread(clientthread,(conn,addr))	

conn.close()
server.close()
