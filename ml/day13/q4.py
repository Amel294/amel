import  cv2 as cv
import numpy as np

img=cv.imread('/home/ai31/Desktop/common/ML/Day13/building.png',0)
sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=1)
sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=1)
low=cv.pyrDown(sobelx)
cv.imshow('dst',low)
cv.waitKey(0)

