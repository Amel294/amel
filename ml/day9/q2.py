import numpy as np
import cv2 as cv
img=np.zeros((512,512,3),np.uint8)
cv.rectangle(img,(10,1),(500,100),(0,255,0),3)
cv.line(img,(10,1),(500,100),(0,255,0),3)
#img[50:100,50:100]=(0,225,0)i
#print img
cv.imshow("image",img)
cv.waitKey(0)              
