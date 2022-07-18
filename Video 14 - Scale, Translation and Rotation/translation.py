import cv2 as cv
import numpy as np

#Loading image from memory
image = cv.imread('cat.jpg')

#Translation matrix
# matrix = numpy.float32([[1,0,100],[0,1,100]])
matrix = np.float32([[1,0,100],[0,1,100]])

#Applying the matrix to the image 
# cv.warpAffine(image,matrix,())
translated = cv.warpAffine(image, matrix, (image.shape[1]+100,image.shape[0]+100))

#Showing the image
cv.imshow('translation', translated)
cv.waitKey(4000)