import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')


retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscale,12,255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    #255 is max pixel value,then the type of threshold
retval2, otsu = cv2.threshold(grayscale,12,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('thres2',threshold2)
cv2.imshow('otsu',otsu)
cv2.imshow('org',img)
cv2.imshow('gaus',gaus)
cv2.imshow('thres',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
