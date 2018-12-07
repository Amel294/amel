import cv2 as cv
img1=cv.imread('/home/ai31/Desktop/common/ML/Day10/ml.png')
img2=cv.imread('/home/ai31/Desktop/common/ML/Day10/opencv-logo.png')
print(img1.shape)
print(img2.shape)
dst=cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destrAllWindows()
