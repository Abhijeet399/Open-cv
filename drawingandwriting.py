import cv2
import numpy as np

img=cv2.imread('watch.jpg.jpg',1)

cv2.line(img,(0,400),(150,400),(255,2,255),4)
cv2.rectangle(img,(15,25),(500,500),(143,28,65),10)
cv2.circle(img,(200,100),55,(0,0,255),0)

pts=np.array([[10,10],[50,84],[132,100],[400,20],[500,500]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,70,33),3)
#                        to
#                        join
 #                       first
  #                      & last
   #                     point

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv tuts',(0,130),font,1,(10,2,152),1,cv2.LINE_AA)
                            #start point                                                    
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
