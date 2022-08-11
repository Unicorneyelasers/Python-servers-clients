#!/usr/bin/python3

####### CLIENT #######

import socket
import sys
from ics226 import *
import ast


BUF_SIZE = 1024
HOST = '127.0.0.1'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print('Client:', sock.getsockname())
print()


while True:
    data = get_socket_line(sock).decode('utf-8')
    if data.startswith("Winner"):
        #print("Congratulations")
        sock.close()
        sys.exit()
        break
        
    displayBoard(eval(data)) 

    row_prompt = get_socket_line(sock).decode('utf-8')
    print(row_prompt)             
    
    
    row_data = input()     
    sock.sendall((row_data + '\n').encode('utf-8'))         

    col_prompt = get_socket_line(sock).decode('utf-8')    
    print(col_prompt)
    
    col_data = input()         
    sock.sendall((col_data + '\n').encode('utf-8'))

    data = get_socket_line(sock).decode('utf-8')
    if data.startswith("Winner"):
        #print("Congratulations")
        sock.close()

sock.close()
sys.exit(0)