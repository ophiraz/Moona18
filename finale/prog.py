import cv2

def checkImage(pathImage):
    ret = False

    bird1_cascade = cv2.CascadeClassifier('bird1-cascade.xml')
    bird2_cascade = cv2.CascadeClassifier('bird2-cascade.xml')

    img = cv2.imread(pathImage)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    birds1 = bird1_cascade.detectMultiScale(gray, 1.3, 5)
    birds2 = bird2_cascade.detectMultiScale(gray, 1.3, 5)

    if type(birds1) != tuple or type(birds2) != tuple:
        ret = True

    for (x,y,w,h) in birds1:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Bird', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)

    for (x,y,w,h) in birds2:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Bird', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)

    #cv2.imshow('img', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
   
    return ret
