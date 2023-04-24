# python file for face recognition and data training 
import cv2
import numpy as np
import face_recognition
import os
import math
import time
import mediapipe as mp

class FaceRecognition:
    def __init__(self, video_source, file_path, xsize,ysize):    
    
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.recognized = False
        self.enter = False

        # this is used for the detecting if the face is inside the box
        self.init_time = 0
        self.current_time = 0
        self.passed_time = 0

        # path for training images
        self.path = file_path

        self.cont = False
        self.face_detected = True

        # array for images, image location, and image names
        self.images = []
        self.paths_array = []
        self.classNames = []

        # os.listdir is a reserve word to list all the folder inside path
        self.myList = os.listdir(self.path)

        # classifier for face detection
        self.haar_face_cascade = cv2.CascadeClassifier(
        "MainSystem\DetectionData\haarcascade_frontalface_alt.xml"
        )

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(max_num_faces = 1)
        self.draw_spec = self.mp_draw.DrawingSpec(thickness = 1, circle_radius=2)

        print(self.myList)
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------



    #Getting-the-dataset-------------------------------------------------------------------------------------------
 
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

    #Getting-the-dataset-------------------------------------------------------------------------------------------

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

        # ENCODING FINISHES 

        # Open the video source
        self.live_feed = cv2.VideoCapture(video_source,cv2.CAP_DSHOW)
        if not self.live_feed.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # setting the height and width of the camera
        self.live_feed.set(cv2.CAP_PROP_FRAME_WIDTH,xsize)
        self.live_feed.set(cv2.CAP_PROP_FRAME_HEIGHT,ysize)

        # Get video source width and height
        self.width = self.live_feed.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.live_feed.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #---------------------------------------------------------------------------------------------------------


    def get_frame(self):
        if self.live_feed.isOpened():
            ret, self.frame = self.live_feed.read()
            self.frame = cv2.flip(self.frame, 1)
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # this function detects the faces and return the value of the detected face
    def face_recognition_func(self):
        # function to detect faces and match on the encoded images
        success, self.frame = self.get_frame()
        # cv2.resize is reserve word to resize the image or camera display
        self.img_small = cv2.resize(self.frame, (0, 0),None, 0.25, 0.25)
        # converts the image into RGB
        self.img_small = cv2.cvtColor(self.img_small, cv2.COLOR_BGR2RGB)
        
        # the next step is to find the location of the face in order to do that we need to use a reserved word
        # face_recognition.face_location is a reserve word to find the location of the face
        facesCurrentFrame = face_recognition.face_locations(self.img_small)
        # after that we need to encode the current frame of the camera
        encodesCurrentFrame = face_recognition.face_encodings(self.img_small, facesCurrentFrame)

        # for loop in order to encode every frame of the camera
        for encodeFace, faceLocation in zip(encodesCurrentFrame, facesCurrentFrame):
            print("entered face recognize")
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
                    # change the content - make it appear the original image to the person detected
                    self.name = self.classNames[matchIndex].upper()
                    # getting the image of the index for referencing
                    self.image_index = matchIndex
                    # this boolean will be the key for stopping the face recognition and the cam_update function
                    self.face_detected = False
                    print('face detected')
                    break


    def get_mesh_face(self, img, draw=True):    
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   
        results = self.face_mesh.process(img_rgb)    # drawing landmarks    
        faces = []    
        if results.multi_face_landmarks:        
            for face_landmarks in results.multi_face_landmarks:            
                if draw:                
                    self.mp_draw.draw_landmarks(img, face_landmarks, self.mp_face_mesh.FACEMESH_CONTOURS,self.draw_spec, self.draw_spec)            # getting the pixel coordinates            
                face = []            
                for index, landmark in enumerate(face_landmarks.landmark):                
                    ih, iw, ic = img.shape                
                    x, y = int(landmark.x * iw), int(landmark.y * ih)                
                    face.append((x, y))            
                    faces.append(face)    
        return img, faces                


    # this function puts a square shape of a frame and puts a circle
    # on the center of the face
    def box_and_dot(self, img):
        frame, faces = self.get_mesh_face(img, False)

        if faces :
            face = faces[0]
            self.center = face[1]
            cv2.circle(frame,self.center,5, (0, 114, 188),5)

        height, width, z = frame.shape
        self.TL = (math.floor(width/3), math.floor(height/4))
        self.TR = (self.TL[0]*2, self.TL[1])
        self.BL = (self.TL[0], self.TL[1]*3)
        self.BR = (self.TR[0], self.BL[1])

        cv2.line(frame, self.TL, self.TR, (0, 114, 188) , 5)
        cv2.line(frame, self.TL, self.BL, (0, 114, 188), 5)
        cv2.line(frame, self.TR, self.BR, (0, 114, 188), 5)
        cv2.line(frame, self.BL, self.BR, (0, 114, 188), 5)
    
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = self.haar_face_cascade.detectMultiScale(gray, 1.1, 6)
        for (x, y, w, h) in face:
            self.center = (math.floor(x+ w / 2), math.floor(y+ h / 2))
            cv2.circle(frame,self.center,5, (0, 114, 188),5)
        """
            
    # this function detects if the face is inside the square within the time set.
    def face_in_box(self, recognize_face):
        recognize_face_func = recognize_face
        if self.recognized:
            return
        if((self.TL[0] <= self.center[0]) and (self.TL[1]<= self.center[1] ) and (self.BR[0] >= self.center[0]) and (self.BR[1]>= self.center[1])):
            if not self.enter:
                self.init_time = time.time()
                self.enter = True

            self.current_time = time.time()
            self.passed_time = self.current_time - self.init_time
            print(self.passed_time)
            # three is the time set 
            if self.passed_time >= 3:
                self.init_time = 0
                self.current_time = 0
                self.recognized = True
                self.cont = True
                self.enter = False
                recognize_face_func()
        else:
            self.enter = False




"""
    def box(self, frame):
        height, width, z = frame.shape
        TL = (math.floor(width/3), math.floor(height/4))
        TR = (TL[0]*2, TL[1])
        BL = (TL[0], TL[1]*3)
        BR = (TR[0], BL[1])

        cv2.line(frame, TL, TR, (0, 114, 188) , 5)
        cv2.line(frame, TL, BL, (0, 114, 188), 5)
        cv2.line(frame, TR, BR, (0, 114, 188), 5)
        cv2.line(frame, BL, BR, (0, 114, 188), 5)
        
    def detect_eyes(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = self.haar_cascade_eyes.detectMultiScale(gray, 1.1, 6)
            # placing a rectangle within the face
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 114, 188), 2)
"""

                    
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
