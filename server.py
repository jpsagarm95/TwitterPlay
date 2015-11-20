import socket
import sys
import ftplib
import os.path

HOST, PORT = "localhost", 9999
count = 0
USERNAME = "tejaswini"
PASSWORD = "svkvr1"
# Create a socket (SOCK_STREAM means a TCP socket)
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server and send data
#sock.connect((HOST, PORT))
session = ftplib.FTP(HOST,USERNAME,PASSWORD)
#session.connect(HOST,PORT,USERNAME,PASSWORD)
print "entered try"
while True:
	filename = "sentiment_"+str(count) + ".txt"
	while not os.path.isfile("sentiment_"+str(count+1)+'.txt'):
		continue
	print "Found file"		
	infile = open(filename,'rb')  
	session.storlines('STOR ' +filename+'w' , infile)                
	infile.close()                                    
	print "Sent file "+ filename	
	count += 1
	
session.quit()
# Receive data from the server and shut down
# received = sock.recv(1024)
	
    #sock.close()

#print "Sent:     {}".format(data)
#print "Received: {}".format(received)
    
    
    
