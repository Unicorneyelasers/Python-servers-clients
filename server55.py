#!/usr/bin/python3

import os
import socket
import sys
from ics226 import *
import struct

#import tqdm

BUF_SIZE = 1024
HOST = '127.0.0.1' #causes server to listen on all interfaces
PORT = 12345
SPACER = "<SPACE PLEASE>"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(5)
print('Server:', sock.getsockname())

while True:
    client_sock, address = sock.accept()
    print('Client:', client_sock.getpeername())
    received =  get_socket_line(client_sock)
    filename = "Images/" + received.decode('utf-8')
    #filename = os.path.basename(filename)
    print(filename)
    #filesize = int(filesize)
        #progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    try:
        with open(filename, 'rb') as f:
            
                bytes_read =f.read()
                #print(bytes_read)
                sendData(client_sock, bytes_read)
                
    except Exception as details:
        print(details)

            #progress.update(len(bytes_read))
    client_sock.close()
    #sock.close()
        
        
    
    #data = get_socket_line(sc)
    #data =sc.recv(BUF_SIZE)
    #data = "Hello " + data.decode('utf-8') + "\n" 
    #data = read_file(data)
    #print(data)
    #sc.sendall(data.decode('utf-8'))
    #sc.close()
