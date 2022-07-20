import cv2 as cv
import os
import numpy as np
faceCascade = cv.CascadeClassifier('D:\open cv\.env\OPENCV-PYTHON-Zero-to-One-Course-Resources-master\OPENCV-PYTHON-Zero-to-One-Course-Resources-master\OpenCV\jsut-test\haarcascade_frontalface_default.xml')
VideoCapture =cv.VideoCapture(0)
while True:
 # Capture frame-by-frame
    ret, frames = VideoCapture.read()
    gray = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv.imshow('Video', frames)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

