import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("/home/ai31/Desktop/common/ML/Day10/images/gradient.png")
ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

title=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOREZO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(title[i])
	plt.xticks([]),plt.yticks([])

plt.show()
