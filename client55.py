#!/usr/bin/python3
import socket
import sys
import os
#import tqdm
from ics226 import *
import struct

BUF_SIZE = 1024
HOST = '127.0.0.1'
PORT = 12345
SPACER = "<SPACE PLEASE>"

filename = sys.argv[1] #"test.txt" #sys.argv[1]
#filesize = os.path.getsize(filename)
#path = "Images/"
#filename = path + filename

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
sock.connect((HOST, PORT)) # Initiates 3-way handshake
print('Client:', sock.getsockname()) # Source IP and source port

sock.send(f"{filename}\n".encode('utf-8'))
#progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
try:
    with open(filename, 'wb') as f:
        print(filename)
        bytes_read = receiveData(sock)
        #print(bytes_read)
        f.write(bytes_read)
        #print(bytes_read)
except Exception as details:
    print(details)
    

        #progress.update(len(bytes_read))
sock.close()
#data = (sys.argv[1]+'\n').encode('utf-8')
#data = ("test\n").encode('utf-8')
#sock.sendall(data) # Destination IP and port implicit due to connect call
#reply = sock.recv(BUF_SIZE) # recvfrom not needed since address is known
#print('Reply:', reply)
#sock.close() # Termination
