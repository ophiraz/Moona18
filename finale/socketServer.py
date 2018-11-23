import socket
import threading
import sys
import prog

import numpy as np
import cv2
from time import sleep

LISTEN_PORT = 4321
    
PATH = "imageTest.jpg"
    
def func(client_soc, path_to_save): 
    isBird = False
    try:
        f = open(path_to_save, "wb")
        client_msg = client_soc.recv(1024)
        while(client_msg):
            # Receiving data from the client
            f.write(client_msg)
            client_msg = client_soc.recv(1024)
        print("File receaved and in: %s\n" % path_to_save)
        f.close()
        #client_msg = #jpg
    except socket.error as errorMsg:
        print("CONECTION ERROR!!!\n")
        return -1
        #chacke if there are birds
    isBird = prog.checkImage(path_to_save)
    if (isBird):
        img = cv2.imread("flights.jpg")
        print("OK\n")
    else:
        img = cv2.imread("dont_flights.jpg")
        print("Not SAFE!!!\a") 
    client_soc.close()

def server(path_to_save):
    # Create a TCP/IP socket
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding to local port 4321
    server_address = ('', LISTEN_PORT)
    try:
        listening_sock.bind(server_address)
    except socket.error as errorMsg:
        print ('Bind failed. Error Code :(')
        sys.exit(1)
    # Listen for incoming connections
    listening_sock.listen(5)
    while True:
        print("Whaiting for conection...\n")
        client_sock, client_address = listening_sock.accept()   # Create a new conversation socket
        ip = client_address[0]
        print("Conection astablesd with (%s)" % ip)
        threading.Thread(target = func, args = (client_sock, path_to_save, )).start()
    # Closing the listening socket
    listening_sock.close()
    
    
if __name__ == "__main__":
    server(PATH)
