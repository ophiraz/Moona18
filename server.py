import socket
import threading
import sys

LISTEN_PORT = 1234

def func(client_soc):
    try:
        # Receiving data from the client
        client_msg = client_soc.recv(1024)
        print(client_msg.decode())
        #client_msg = #jpg
    except socket.error as errorMsg:
        print("CONECTION ERROR!!!\n")
        return -1
    client_soc.close()


def main():
    # Create a TCP/IP socket
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding to local port 1234
    server_address = ('', LISTEN_PORT)
    try:
        listening_sock.bind(server_address)
    except socket.error as errorMsg:
        print ('Bind failed. Error Code :(')
        sys.exit(1)
    # Listen for incoming connections
    listening_sock.listen(5)
    while True:
        client_sock, client_address = listening_sock.accept()   # Create a new conversation socket
        ip = client_address[0]
        threading.Thread(target = func, args = (client_sock, )).start()
    # Closing the listening socket
    listening_sock.close()

if __name__ == "__main__":
    main()

