import cv2 as cv
from cv2 import cvtColor
import numpy as np
image = cv.imread('cat.jpg',cv.IMREAD_GRAYSCALE)



cv.imshow("image",image)
cv.waitKey(0)   
cv.destroyAllWindows()
