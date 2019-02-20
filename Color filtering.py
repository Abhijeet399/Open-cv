import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #hsv is hue sat value
    lower_green=np.array([60,20,90])
    upper_green=np.array([120,250,255])

    mask = cv2.inRange(hsv,lower_green,upper_green)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    kernal1=np.ones((5,5),np.uint8)
    errosion=cv2.erode(mask,kernal1,iterations=1)
    dialation=cv2.dilate(mask,kernal1,iterations=1)
    #res1=cv2.bitwise_and(frame,frame,mask=errosion)
    #res2=cv2.bitwise_and(frame,frame,mask=dialation)

    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal1)
    #opening removes false positives & noise from background
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal1)  
    #closing removes false negatives & noise from object
    
    kernel = np.ones((5,5),np.float32)/25
    smooth= cv2.filter2D(res, -1,kernel)

    blur = cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)

    #cv2.imshow('blur',blur)
    cv2.imshow('open',opening)
    cv2.imshow('close',closing)
    #cv2.imshow('frame',frame)
    #cv2.imshow('res1',res1)
    #cv2.imshow('res2',res2)
    cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    cv2.imshow('errosion',errosion)
    cv2.imshow('dialate',dialation)
    #cv2.imshow('smooth',smooth) 
    #cv2.imshow('m',median)    
       

    k=cv2.waitKey(5) & 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()
cap.release()
