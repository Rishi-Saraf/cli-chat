# Author : Rishi Saraf
# Github Repo : Github.com/Rishi-Saraf

# import section
import socket
import threading
import sys

class Server:
	"""The class for the server"""
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # initialization of the server socket
	connections = [] # A list of all the clients connected to the server
	def __init__(self):
		self.sock.bind(("127.0.0.1",6000)) # Binding the socket with the IP address and Port numbers
		self.sock.listen() # Listening for new connections
		print("[SERVER STARTED] Starting server...")

	def handler(self,c,a):
		while True:
				data = c.recv(2048).decode("utf-8") # Decoding the data as bytes
				data = f"{data}"
				print(data)
				conns = []
				for conn in self.connections:
					if not(conn == c):
						conns.append(conn)
				for connection in conns:
						connection.send(bytes(data,"utf-8"))	
	
	def run(self):
		while True:
			conn,addr = self.sock.accept()
			print(f"[{addr} CONNECTED] Connected new client...")
			connThread = threading.Thread(target=self.handler,args=(conn,addr))
			connThread.daemon = True # Creating the handler function as a daemon
			connThread.start()
			self.connections.append(conn) # Adding the new connection to the connections list


class Client:
	'''The class for a client'''
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	def sendMsg(self):
		'''
		The function for sending message to the server 
		which eventually sends it to other clients
		'''
		while True:
			data = input("")
			data = f"[Message from {self.name}] {data}"
			data = bytes(data,"utf-8")
			self.sock.send(data)

	def recvMsg(self):
		'''
		The function for recieving messages from the server
		'''
		while True:
			data = self.sock.recv(2048).decode("utf-8")
			data = f"\n{data}"
			if data:
				print(str(data))

	def __init__(self,address):
		self.sock.connect((address,6000))
		self.name = input("Please enter your name : ")
		clientThread = threading.Thread(target=self.sendMsg) 
		clientThread.daemon = True # Initializing the sendMsg function as a daemon
		recvThread = threading.Thread(target=self.recvMsg)
		recvThread.daemon = True # Initializing the recvMsg function as a daemon
		recvThread.start() # Starting the daemon
		clientThread.start() # Starting the daemon
		recvThread.join()
		clientThread.join()
		while True:
			pass # An infinite loop that just keeps the two daemons running


if __name__ == "__main__":

	# The address of the Server should be provided as an argument in order to run the client 
	if len(sys.argv)>1: 
		client = None
		try:
			client = Client(sys.argv[1])
		except Exception as e:
			print("Some Error Occured")
		finally:
			if not(client==None):
				client.sock.close()
	else:
		server=None
		try:
			server = Server()
			server.run()
		except Exception as e:
			print("Some Error Occured")
		finally:
			if not(server==None):
				server.sock.close()
		
