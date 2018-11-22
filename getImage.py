from picamera import PiCamera
#from time import sleep

#set camera
camera = PiCamera()

def saveImage(path):
    
    #print("start!")
    camera.start_preview()

    #save image
    camera.capture(path)
        
    #print("stop!")
    camera.stop_preview()
