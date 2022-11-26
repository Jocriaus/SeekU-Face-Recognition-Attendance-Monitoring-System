import cv2
import numpy as np
import face_recognition
import os

# path for training images
path = "./Face Recognition/data_set"
images = []
classNames = []
# os.listdir is a reserve word to list all the folder inside path
myList = os.listdir(path)
print(myList)

# for loop to run through all subfolders of the root folders
for root, dirs, files in os.walk(path):
    # for loop in every files on folders
    for f in files:
        # reads the images on root/files
        currentImage = cv2.imread(f"{root}/{f}")
        # appends currentImage through images array
        images.append(currentImage)
        # get the className by appending the name of file and removes extension
        classNames.append(os.path.splitext(f)[0])

print(classNames)

# function to encode images
def findEncodings(images):
    encodeList = []
    # for loop for every images in the folder
    for img in images:
        # converts the color of img to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # face_recognition.face_encodings is a reserve word to encode the images
        encode = face_recognition.face_encodings(img)[0]
        # appends encodeList array
        encodeList.append(encode)
    return encodeList


# after defining the functions we need to provide images by using images variable to findEncodings function and declares it to encodeListKnownFaces variable
encodeListKnownFaces = findEncodings(images)

print("Encode Complete")
# cv2.VideoCaption is a reservice word of cv2 in order to use webcam
cap = cv2.VideoCapture(0)
# an infinite loop in order to capture every frames of the camera
while True:
    success, img = cap.read()
    # cv2.resize is reserve word to resize the image or camera display
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    # converts the image into RGB
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
    # the next step is to find the location of the face in order to do that we need to use a reserved word
    # face_recognition.face_location is a reserve word to find the location of the face
    facesCurrentFrame = face_recognition.face_locations(imgSmall)
    # after that we need to encode the current frame of the camera
    encodesCurrentFrame = face_recognition.face_encodings(imgSmall, facesCurrentFrame)

    # for loop in order to encode every frame of the camera
    for encodeFace, faceLocation in zip(encodesCurrentFrame, facesCurrentFrame):
        # in order to compare the detected face to the training images we need to use face_recognition.compare_faces reserved word
        matches = face_recognition.compare_faces(encodeListKnownFaces, encodeFace)
        # in order to find the distance of face we need to use face_recognition.face_distance reserved word
        faceDistance = face_recognition.face_distance(encodeListKnownFaces, encodeFace)
        print(faceDistance)
        # it returns the minimum values along axis of matchIndex
        matchIndex = np.argmin(faceDistance)

        # an if statement in order to draw rectangle to the detected face and also to write the name of detected face
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            # x and y axis to draw rectangle
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # draws the rectangle to the detected face
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                img,
                name,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                2,
            )
    # to show the camera when running the system we need to use cv2.imshow
    cv2.imshow("Webcam", img)
    # in order to close the webcam press esc
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cap.release()

# Algorithm used in face_recognition library
# HOG(Histogram of Gradients) - for detecting the face
# Face landmark estimation - for Posing and Projecting Images
# Deep Convolutional Neural Networks - used to identify patterns on images and videos.
# SVM classifier(machine learning classification algorithm) - used to find the persons name from the encoding

# if you want to know the full details of algorithms that use in face_recognition library kindly read the article of Adam Gietgey
# https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
