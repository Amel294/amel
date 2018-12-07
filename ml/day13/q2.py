
import cv2 as cv
import numpy as np

img = cv.imread('/home/ai31/Desktop/common/ML/Day13/man.jpg',0)
kernel = np.ones((2,2),np.uint8)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
open1 = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
img=np.hstack((img,closing))
img2=np.hstack((img,open1))
cv.imshow('dst',img)
cv.imshow('dst',img2)
cv.waitKey(0)
