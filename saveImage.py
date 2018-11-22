from picamera import PiCamera
from time import sleep

def save_image(path):    
    #set camera
    camera = PiCamera()
    #print("start!")
    camera.start_preview()

    #save image
    camera.capture(path)
    
    sleep(1)
    #print("stop!")
    camera.stop_preview()
    
    camera.close()
