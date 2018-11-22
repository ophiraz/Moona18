import socket
from saveImage import save_image
from time import sleep

SERVER_IP = "192.168.43.24"
SERVER_PORT = 4321
PATH = "/home/pi/Documents/moona/image.jpg"

def getImage(path):
    #save image from the camera
    save_image(path)
    
    #get imege
    imageFile= open(path, "rb")
    
    return imageFile

def sendData(imageFile):
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connecting to remote computer 1234
        sock.connect((SERVER_IP, SERVER_PORT))
        l = imageFile.read()
        # Sending data to server 
        sock.sendall(l)
        
    except socket.error as errorMsg:
        print("ERROR!!! meage not sent. server is probiboly down\n")
        # Closing the socket
        sock.close()
        return False
    # Closing the socket
    sock.close()

def main():
    #msg2 = "Gboy\n"
    while (True):        
        #get the data
        imageFile = getImage(PATH)
        
        #send the msg to the server
        sendData(imageFile)

       
if __name__ == "__main__":
    main()
