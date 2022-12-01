#python file for face recognition and data training 
import cv2
import numpy as np
import face_recognition
import os

class facerecogApp:
    def __init__(self, video_source=0):    

        self.face_detected = True
        # path for training images
        self.path = ".\\FaceRecognition\\data_set"
        #array for images, image location, and image names
        self.images = []
        self.paths_array = []
        self.classNames = []
        # os.listdir is a reserve word to list all the folder inside path
        self.myList = os.listdir(self.path)

        print(self.myList)

        # for loop to run through all subfolders of the root folders
        for root, dirs, files in os.walk(self.path):
            # for loop in every files on folders
            for f in files:
                # reads the images on root/files
                currentImage = cv2.imread(f"{root}/{f}")
                # appends currentImage through images array
                self.images.append(currentImage)
                file_path = os.path.join(root ,(f))
                self.paths_array.append(file_path)
                # get the className by appending the name of file and removes extension
                self.classNames.append(os.path.splitext(f)[0])
            

        print(self.paths_array)
        print(self.classNames)

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
        self.encodeListKnownFaces = findEncodings(self.images)

        print("Encode Complete")

        #ENCODING FINISHES 

        # Open the video source
        self.live_feed = cv2.VideoCapture(0)
        if not self.live_feed.isOpened():
            raise ValueError("Unable to open video source", video_source)

        #setting the height and width of the camera
        self.live_feed.set(cv2.CAP_PROP_FRAME_WIDTH,700)
        self.live_feed.set(cv2.CAP_PROP_FRAME_HEIGHT,700)

        # Get video source width and height
        self.width = self.live_feed.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.live_feed.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.live_feed.isOpened():
            ret, self.frame = self.live_feed.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    def face_recognition_func(self):
        #function to detect faces and match on the encoded images
        success, self.frame = self.get_frame()
        
        # cv2.resize is reserve word to resize the image or camera display
        self.img_small = cv2.resize(self.frame, (0, 0), None, 0.25, 0.25)
        # converts the image into RGB
        self.img_small = cv2.cvtColor(self.img_small, cv2.COLOR_BGR2RGB)
        
        # the next step is to find the location of the face in order to do that we need to use a reserved word
        # face_recognition.face_location is a reserve word to find the location of the face
        facesCurrentFrame = face_recognition.face_locations(self.img_small)
        # after that we need to encode the current frame of the camera
        encodesCurrentFrame = face_recognition.face_encodings(self.img_small, facesCurrentFrame)

        # for loop in order to encode every frame of the camera
        for encodeFace, faceLocation in zip(encodesCurrentFrame, facesCurrentFrame):
            if self.face_detected:
                # in order to compare the detected face to the training images we need to use face_recognition.compare_faces reserved word
                matches = face_recognition.compare_faces(self.encodeListKnownFaces, encodeFace)
                # in order to find the distance of face we need to use face_recognition.face_distance reserved word
                faceDistance = face_recognition.face_distance(self.encodeListKnownFaces, encodeFace)
                # it returns the minimum values along axis of matchIndex
                matchIndex = np.argmin(faceDistance)

                # an if statement in order to draw rectangle to the detected face and also to write the name of detected face
                # if statement that tells it detected the image
                if matches[matchIndex]:
                    
                    #change the content - make it appear the original image to the person detected
                    self.name = self.classNames[matchIndex].upper()
                    #getting the image of the index for referencing
                    self.image_index = matchIndex
                    #this boolean will be the key for stopping the face recognition and the cam_update function
                    self.face_detected = False
                    break
                    
"""
Class facerecogApp
    def __init__ = will encode the images 
        def findEncodings = will encode the images
    def get_frame = will get the frame if the camera is open
    def face_recognition_func = will detect the images
"""

# Algorithm used in face_recognition library
# HOG(Histogram of Gradients) - for detecting the face
# Face landmark estimation - for Posing and Projecting Images
# Deep Convolutional Neural Networks - used to identify patterns on images and videos.
# SVM classifier(machine learning classification algorithm) - used to find the persons name from the encoding
