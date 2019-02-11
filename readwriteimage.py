import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('watch.jpg.jpg',0)
##cv2.imshow('watch',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
plt.imshow(img,cmap= 'gray',interpolation='lanczos')
##plt.plot([500,10],[500,100],'k',linewidth=1)
plt.show()
##cv2.imwrite('watchgray.png',img)
