import socket
import getImage

SERVER_IP = "192.168.43.24" #"192.168.200.76"
SERVER_PORT = 1234

def getImege(path):
    #get imege
    img = open(path, "r")
    
    print(img.read())
    return img.read()

def sendData(msg):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connecting to remote computer 1234
        sock.connect((SERVER_IP, SERVER_PORT))
        # Sending data to server
        sock.sendall(msg.encode())
    except socket.error as errorMsg:
        print("ERROR!!! meage not sent. server is probiboly down\n")
        # Closing the socket
        sock.close()
        return False
    # Closing the socket
    sock.close()

def main():
    msg2 = "Gboy\n"
    
    #msg = getImege()
    sendData(msg2)

if __name__ == "__main__":
    main()

