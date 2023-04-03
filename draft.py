from email.mime import image
import cv2
from cv2 import contourArea 
import numpy as np

video = cv2.VideoCapture("video.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

if(video.isOpened()==False):
    print("ERROR OCCURED")
    
    
    
    
while video.isOpened():
    ret, frame = video.read()
    h,w, _ = frame.shape
    #print("height =", h, "weight =", w) 
    
    #region = frame[120:360 , 64:576]
    
    
    
    
    
    mask = object_detector.apply(frame)
    _, mask = cv2.threshold(mask, 254,255, cv2.THRESH_BINARY)
    countors, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    
    
            
            
            
    upperBound = int(h/10)
    lowerBound = int(h*(9/10))
    leftBound = int(w/4)
    rightBound = int(w*3/4)
    cood1 = (leftBound, upperBound)
    cood2 = (rightBound, lowerBound)
    t=10
    region=[cood1,cood2]
    
    

    frame1 = cv2.rectangle(frame, cood1, cood2, (0,0,255),t)
    
    
    
    
    for i in countors:
        area = cv2.contourArea(i)
        
           
            
            
        if area >100:
            cv2.drawContours(frame, [i], -1, (255,0,0), 2)
            x,y,wi,hi = cv2.boundingRect(i)
            if y+int(hi/2) in range(cood1[1],cood2[1]):
                
                cv2.rectangle(frame,(x,y), ((x+wi),(y+hi)),(0,255,0),1)
                print("Frame'i %", (hi/h)*100,"yatayda ve %", (wi/w)*100 ,"dikeyde kapsayan hedef, hedef vuruş alanında")


    #cv2.rectangle(frame, (120,64))
    #cv2.imshow("region", region)
    cv2.imshow("Frame",frame)
    #cv2.imshow("MASK",mask)   
    
    
  
    if cv2.waitKey(25) & 0xFF== ord("q"):
        break
    


video.release()

cv2.destroyAllWindows()

