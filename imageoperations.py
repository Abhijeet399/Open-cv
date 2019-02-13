import numpy as np
import cv2

img=cv2.imread('watch.jpg.jpg',1)

px=img[525,255]

#print(px)    #colour of pixel

img[525,255]=[255,255,255]
#print(px)

watch_face=img[90:200,20:250]
img[0:110,0:230]=watch_face

#roi = img[200:700,200:700]
#print(roi)
img[200:300,200:300]=[255,255,255]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
