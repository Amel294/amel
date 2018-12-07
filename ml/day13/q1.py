import cv2 as cv
import numpy as np

img=cv.imread('/home/ai31/Desktop/common/ML/Day13/man.jpg',0)
kernal=np.ones((2,2),np.uint8)
erosion=cv.erode(img,kernal,iterations = 1)
dilation=cv.dilate(erosion,kernal,iterations = 1)
img=np.hstack((img,dilation))
cv.imshow('dst',img)
cv.waitKey(0)

