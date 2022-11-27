#!/usr/bin/python3
import cv2
import numpy as np
import face_recognition
import tkinter as tk
import tkinter.ttk as ttk
import snapshot as ss
from PIL import Image, ImageTk
import os

     
cont = None
add_client_win = None
class FaceRecognitionUI:
    def __init__(self, master=None):
        # build ui
        self.system_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.system_app.configure(
            background="#0072bc",
            height=200,
            relief="flat",
            takefocus=True,
            width=200)
        self.fr_vid = facerecogApp()
        self.system_app.geometry("1280x720")
        self.system_app.resizable(True, True)
        self.system_app.title("SeekU - Face Recognition Attendance System")
        
        #main frame that consistst two frames (left and right)
        self.main_frame = ttk.Frame(self.system_app)
        self.main_frame.configure(height=200, width=200)

        #left frame (Includes System Name, Sti Logo etc)
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.configure(background="#0072bc", height=200, width=200)
        self.system_name_label = tk.Label(self.left_frame)
        self.system_name_label.configure(
            background="#0072bc",
            font="{Arial Black} 40 {}",
            foreground="#fff200",
            justify="center",
            takefocus=False,
            text='SEEK U')
        self.system_name_label.grid(
            column=1, padx=10, pady=35, row=0, sticky="n")
        self.year_label = tk.Label(self.left_frame)
        self.year_label.configure(
            background="#0072bc",
            cursor="arrow",
            font="{arial black} 14 {}",
            foreground="#ffffff",
            justify="center",
            takefocus=False,
            text='BSCS - 4A S.Y. 2022-2023')
        self.year_label.grid(column=1, padx=10, row=0)
        self.client_name_label = tk.Label(self.left_frame)
        self.client_name_label.configure(
            background="#fff200",
            font="{Arial Black} 25 {}",
            foreground="#0072bc",
            height=2,
            justify="center",
            text='Detecting...',
            width=20)
        self.client_name_label.grid(
            column=0, columnspan=2, ipadx=30, padx=5, row=1)
        self.attendance_label = tk.Label(self.left_frame)
        self.attendance_label.configure(
            background="#fff200",
            font="{Arial Black} 13 {}",
            foreground="#0072bc",
            height=2,
            justify="center",
            relief="flat",
            text='Attendance:',
            width=35)
        self.attendance_label.grid(
            column=0,
            columnspan=2,
            ipadx=20,
            ipady=10,
            padx=5,
            row=2)
        self.next_button = tk.Button(self.left_frame)
        self.next_button.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            takefocus=False,
            text='Next',
            width=15)
        self.next_button.grid(
            column=0,
            columnspan=2,
            ipady=1,
            padx=90,
            pady=20,
            row=4,
            sticky="w")
        self.next_button.bind("<ButtonPress>", self.next_student, add="+")
        self.label5 = tk.Label(self.left_frame)
        self.img_STICollegeBalagtasLogos = tk.PhotoImage(
            file="SeekU/STI College Balagtas Logo-s.png")
        self.label5.configure(
            background="#0072bc",
            image=self.img_STICollegeBalagtasLogos,
            text='label3')
        self.label5.grid(
            column=0,
            padx=20,
            pady=20,
            row=0,
            rowspan=2,
            sticky="nw")
        self.reset_button = tk.Button(self.left_frame)
        self.reset_button.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            text='Reset',
            width=10)
        self.reset_button.grid(
            column=0,
            columnspan=2,
            padx=90,
            pady=20,
            row=4,
            sticky="e")
        self.reset_button.bind("<ButtonPress>", self.reset_attendance, add="+")
        self.left_frame.pack(expand="true", fill="both", side="left")
        self.left_frame.grid_anchor("center")
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure("all", weight=1)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.columnconfigure("all", weight=1)

        #right Frame(includes camera and add button)
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.configure(background="#0072bc", height=400, width=400)
        self.add_button = tk.Button(self.right_frame)
        self.add_button.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            text='Add',
            width=20)
        self.add_button.grid(column=0, padx=5, pady=60, row=0, sticky="s")
        self.add_button.bind("<ButtonPress>", self.add_client, add="+")
        #camera 
        
        self.camera_canvas = tk.Canvas(self.right_frame, 
            width = self.fr_vid.width, 
            height = self.fr_vid.height
            )
        #self.camera_canvas.configure(
        #    borderwidth=0,
        #    height=500,
        #    insertborderwidth=0,
        #    relief="flat",
        #    width=500,
        #    image=mf.facerecogApp.display_cam()
        #    )
        self.camera_canvas.grid(column=0, padx=5, pady=10, row=0)
        #self.camera_canvas.after(25,)
        #self.canvas.create_image(image= self.final_img)
        self.right_frame.pack(expand="true", fill="both", side="right")
        self.right_frame.grid_anchor("center")
        self.right_frame.rowconfigure(0, weight=1)
        self.right_frame.columnconfigure(0, weight=1)
        self.main_frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")

        #calling camera update for camera display
        self.cam_update()

        # Main widget
        self.mainwindow = self.system_app

    #def put_into_image(self, event=None):
        #self.img_from_feed = Image.fromarray(mf.img_small)
        # Convert image to PhotoImage
        #self.final_img = ImageTk.PhotoImage(image = self.img_from_feed)

    def run(self):
        self.mainwindow.mainloop()  

    def next_student(self, event=None):
        pass

    def reset_attendance(self, event=None):
        pass

    def add_client(self, event=None):
        #shut down update function on main window
        global cont
        cont = True
        ss.snapApp(self.restart)
        #self.system_app.destroy()
        #self.use_camera()

    def restart(self):
        global cont
        cont = False
        self.system_app.destroy() 
        FaceRecognitionUI().run()

    #def use_camera(self):
    #    global cont
    #    cont = True

    def cam_update(self):
        global cont
        if cont:
            return
        # Get a frame from the video source
        ret, frame = self.fr_vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.camera_canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
            # cv2.resize is reserve word to resize the image or camera display
            self.img_small = cv2.resize(frame , (0, 0), None, 0.25, 0.25)
            # converts the image into RGB
            self.img_small = cv2.cvtColor(self.img_small, cv2.COLOR_BGR2RGB)
            
            # the next step is to find the location of the face in order to do that we need to use a reserved word
            # face_recognition.face_location is a reserve word to find the location of the face
            facesCurrentFrame = face_recognition.face_locations(self.img_small)
            # after that we need to encode the current frame of the camera
            encodesCurrentFrame = face_recognition.face_encodings(self.img_small, facesCurrentFrame)

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
                # if statement that tells it detected the image
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    print(name)
                    # x and y axis to draw rectangle
                    y1, x2, y2, x1 = faceLocation
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    # draws the rectangle to the detected face
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(
                        frame,
                        name,
                        (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        2,
                    )
        #call again the same method after 5 millisecond
        self.system_app.after(5, self.cam_update)
        cont = False
        #print(cont)

        
#in comment
        


# path for training images
path = "./FaceRecognition/data_set"
#array for images and names
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



class facerecogApp:
    def __init__(self, video_source=0):    
        # Open the video source
        self.live_feed = cv2.VideoCapture(0)
        if not self.live_feed.isOpened():
            raise ValueError("Unable to open video source", video_source)

        #setting the height and width of the camera
        self.live_feed.set(cv2.CAP_PROP_FRAME_WIDTH,500)
        self.live_feed.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

        # Get video source width and height
        self.width = self.live_feed.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.live_feed.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def reopen_cam(self):
        self.live_feed.open(0)
        print("jc")

    def get_frame(self):
        if self.live_feed.isOpened():
            ret, frame = self.live_feed.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    def face_recognition_func(self):
        # an infinite loop in order to capture every frames of the camera
        while True:
            success, self.img = self.live_feed.read()

            # cv2.resize is reserve word to resize the image or camera display
            self.img_small = cv2.resize(self.img, (0, 0), None, 0.25, 0.25)
            # converts the image into RGB
            self.img_small = cv2.cvtColor(self.img_small, cv2.COLOR_BGR2RGB)
            
            # the next step is to find the location of the face in order to do that we need to use a reserved word
            # face_recognition.face_location is a reserve word to find the location of the face
            facesCurrentFrame = face_recognition.face_locations(self.img_small)
            # after that we need to encode the current frame of the camera
            encodesCurrentFrame = face_recognition.face_encodings(self.img_small, facesCurrentFrame)

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
                # if statement that tells it detected the image
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    print(name)
                    # x and y axis to draw rectangle
                    y1, x2, y2, x1 = faceLocation
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    # draws the rectangle to the detected face
                    cv2.rectangle(self.img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(self.img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(
                        self.img,
                        name,
                        (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        2,
                    )

    
            # to show the camera when running the system we need to use cv2.imshow
            #cv2.imshow("Webcam", self.img)

            # in order to close the webcam press esc
            #k = cv2.waitKey(30) & 0xFF
            #if k == 27:
            #    break
        
            
    def __del__(self):
        if self.live_feed.isOpened():
            self.live_feed.release()




if __name__ == "__main__":
    
    app = FaceRecognitionUI()
    app.run()
