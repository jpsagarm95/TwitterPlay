import socket
import sys

HOST, PORT = "localhost", 9999
filename = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
infile = open(filename)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    
    for line in infile:
    	sock.sendall(line + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

#print "Sent:     {}".format(data)
#print "Received: {}".format(received)
    
    
    
