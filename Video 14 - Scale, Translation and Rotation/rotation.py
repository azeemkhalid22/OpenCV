import cv2 
import numpy 


#Loading image from memory
image = cv2.imread('cat.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width,channel = image.shape

#Translation matrix
matrix = cv2.getRotationMatrix2D((width/2,height/2), 10, 1)

#Applying the matrix to the image 
translated = cv2.warpAffine(image, matrix, (width, height))

#Showing the image
cv2.imshow('translation', translated)
print(channel)
cv2.waitKey()




#another code eg
# img = cv.imread('nature.png')
# rows,cols,ch = img.shape
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv.getAffineTransform(pts1,pts2)
# dst = cv.warpAffine(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()




#3rd eg code//   capture video from webcam and show by apply projective transform 
# import cv2
# import numpy as np
 
# # Turn on Laptop's webcam
# cap = cv2.VideoCapture(0)
 
# while True:
     
#     ret, frame = cap.read()
 
#     # Locate points of the documents
#     # or object which you want to transform
#     pts1 = np.float32([[0, 260], [640, 260],
#                        [0, 400], [640, 400]])
#     pts2 = np.float32([[0, 0], [400, 0],
#                        [0, 640], [400, 640]])
     
#     # Apply Perspective Transform Algorithm
#     matrix = cv2.getPerspectiveTransform(pts1, pts2)
#     result = cv2.warpPerspective(frame, matrix, (500, 600))
     
#     # Wrap the transformed image
#     cv2.imshow('frame', frame) # Initial Capture
#     cv2.imshow('frame1', result) # Transformed Capture
 
#     if cv2.waitKey(24) == 27:
#         break
 
# cap.release()
# cv2.destroyAllWindows()