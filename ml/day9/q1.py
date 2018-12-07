import numpy as np
import cv2 as cv
img=np.zeros((512,512,3),np.uint8)
#cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
img[50:100,50:100]=(0,225,0)
#print img
cv.imshow("image",img)
cv.waitKey(0)
