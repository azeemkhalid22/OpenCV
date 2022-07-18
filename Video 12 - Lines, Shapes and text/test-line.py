import cv2 as cv
import numpy as np

image = cv.imread('cat.jpg')
cv.imshow("display window", image)
cv.waitKey(0)
cv.destroyAllWindows()