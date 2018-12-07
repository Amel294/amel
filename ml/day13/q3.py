import cv2 as cv
import numpy as np

img = cv.imread('/home/ai31/Desktop/common/ML/Day13/girl.jpg',0)
kernel = np.ones((2,2),np.uint8)
open1 = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(open1, cv.MORPH_CLOSE, kernel)
img2=np.hstack((img,closing))
cv.imshow('dst',img2)
cv.waitKey(0)

