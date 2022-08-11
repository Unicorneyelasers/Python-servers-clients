#!/usr/bin/python3

import socket
import sys
import threading
from ics226 import *

######## SERVER ########

HOST = '127.0.0.1' 
PORT = 12345    
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))  
sock.listen(2)    
print('Server:', sock.getsockname()) 
print()

ROW = 5
COL = 5

board = [['-']*COL for _ in range(ROW)]
    
locks = []
for i in range(2):
    locks.append(threading.Semaphore())
    locks[-1].acquire()

def contactPlayer(player_id):

    if(player_id == 0):
        player_id_str = "X"
    if(player_id == 1):
        player_id_str = "O"
    sc, sockname = sock.accept()
    
    while True:
        locks[player_id].acquire()
        displayBoard(board)
        sc.sendall((str(board)+"\n").encode('utf-8'))
        print()
        print(player_id_str)

        if findWinner(board):
            print("Winner is " + player_id_str)
            displayBoard(board)
            sc.sendall(("Winner is " + player_id_str + "\n").encode('utf-8'))
            locks[(player_id + 1) % 2].release()
            #sc.close()
            sys.exit()
        try:
            sc.sendall((str("Row ")+"\n").encode('utf-8'))
            row_data = get_socket_line(sc).decode('utf-8')

            sc.sendall((str("Column ")+"\n").encode('utf-8'))
            col_data = get_socket_line(sc).decode('utf-8')


        except Exception as detail:
            print(detail)
        
        try:
            if (validateInput(col_data, row_data)):
                print("passed validateInput")
                if(checkBoard(board, row_data, col_data)):
                    print("passed checkBoard")
                    board[int(row_data)][int(col_data)] = player_id_str
                    #move this
                    if not findWinner(board):    
                        displayBoard(board)
                        sc.sendall(("nothing yet \n").encode('utf-8'))
                        locks[(player_id + 1) % 2].release()
                    else:
                        displayBoard(board)
                        sc.sendall(("nothing yet \n").encode('utf-8'))
                        locks[(player_id + 1) % 2].release()
                else:
                    displayBoard(board)
                    sc.sendall(("nothing yet \n").encode('utf-8'))
                    locks[(player_id + 1) % 2].release()
            else:
                displayBoard(board)
                sc.sendall(("nothing yet \n").encode('utf-8'))
                locks[(player_id + 1) % 2].release()
        except Exception as detail:
            print(detail)
num_players = 0
while num_players != 2:
    threading.Thread(target = contactPlayer, args = (num_players, )).start()
    num_players = num_players + 1

locks[0].release()