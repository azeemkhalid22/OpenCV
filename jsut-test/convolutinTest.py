# import cv2 as cv
# import cv2
# import numpy as np
# image = cv.imread('cat.jpg',cv.IMREAD_GRAYSCALE)
# cv.imshow("image",image)
# cv.waitKey(0)   
# cv.destroyAllWindows()



#import modules
import cv2 as cv
import numpy as np
#read image
image = cv.imread('nature.jpg')

#make filter

kernal_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernal_3x3 = np.ones((3,3), dtype=np.float32)/ 9.0
kernal_15x15 = np.ones((15,15), dtype=np.float32)/225.0

#Apply filter

input1 = cv.filter2D(image,-1, kernal_identity)
input2 = cv.filter2D(image, -1, kernal_3x3)
input3 = cv.filter2D(image, -1, kernal_15x15)


#show the output image
cv.imshow('original image',image)
cv.imshow('identity image',input1)
cv.imshow('3x3_blur',input2)
cv.imshow('15x15_blur',input3)
cv.waitKey(0)   
cv.destroyAllWindows()



