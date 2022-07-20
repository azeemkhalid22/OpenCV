import cv2
import numpy as np

img = cv2.imread('nature.jpg')

#kernal for horizoltal motion side
# size = 15
# kernel = np.zeros((size,size))
# kernel[int((size-1)/2),:] = np.ones(size)
# kernel = kernel/size


#Outline Edge Detection on an image
# kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])

#for sharpening the image (kernal)
# kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])

# Using Emboss Filter
# kernel = np.array([[-2, -1, 0],[-1, 1, 1],[0, 1, 2]])

#Sobel filter
kernel = np.array([[-1, 0, 1],[-2, 0, 2],  [-1, 0, 1]])


output  = cv2.filter2D(img, -1, kernel)
cv2.imshow('winname', output)
cv2.imshow('winnam1e', img)
cv2.waitKey(0)