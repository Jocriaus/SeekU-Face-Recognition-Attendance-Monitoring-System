import cv2 as cv
import numpy as np

#load cascade classifier training file for haarcascade
haar_face_cascade = cv.CascadeClassifier(
    "FaceDetection/data/haarcascade_frontalface_alt.xml"
)

cap = cv.VideoCapture(0)
while True:

    #img as video 
    _,  img = cap.read()
    #img set img as graye color
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    
    faces = haar_face_cascade.detectMultiScale(gray, 1.1, 6)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 250), 2)

    cv.imshow("Detect Face Image", img)
    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
