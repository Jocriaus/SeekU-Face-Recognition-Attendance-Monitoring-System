#python file for the main UI
import tkinter as tk
import tkinter.ttk as ttk
import snapshot as ss
import face_recog as mf
from PIL import Image, ImageTk
import datetime
import time

class FaceRecognitionUI:
    def __init__(self, master=None):
        #variable for catching the unknon error
        #when adding client
        self.cont = False
        # build ui (main window)
        self.system_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.system_app.configure(
            background="#0072bc",
            height=200,
            relief="flat",
            takefocus=True,
            width=200)
        self.system_app.geometry("1280x720")
        self.system_app.resizable(True, True)
        self.system_app.title("SeekU - Face Recognition Attendance System")
        #instantiating the object
        self.fr_vid = mf.facerecogApp()
        #main frame that consistst two frames (left and right)
        self.main_frame = ttk.Frame(self.system_app)
        self.main_frame.configure(height=200, width=200)
        #left frame (Includes System Name, Sti Logo etc)
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.configure(background="#0072bc", height=200, width=200)

        #label for the name of the system displayed
        self.system_name_label = tk.Label(self.left_frame)
        self.system_name_label.configure(
            background="#0072bc",
            font="{Arial Black} 40 {}",
            foreground="#fff200",
            justify="center",
            takefocus=False,
            text='SEEK U')
        self.system_name_label.grid(
            column=1, padx=10, pady=25, row=0, sticky="n")

        #label for the display of the year level
        self.year_label = tk.Label(self.left_frame)
        self.year_label.configure(
            background="#0072bc",
            cursor="arrow",
            font="{arial black} 14 {}",
            foreground="#ffffff",
            justify="center",
            takefocus=False,
            text='BSCS - 4A S.Y. 2022-2023')
        self.year_label.grid(column=1, padx=10, pady=50, row=0, sticky="s")

        #label for displaying the name of the detected person
        self.client_name_label = tk.Label(self.left_frame)
        self.client_name_label.configure(
            background="#fff200",
            font="{Arial Black} 25 {}",
            foreground="#0072bc",
            height=3,
            justify="center",
            text='Detecting...',
            width=25)
        self.client_name_label.grid(
            column=0, columnspan=2, ipadx=30, padx=5, row=1)

        #label for displaying the time of attendance
        self.attendance_label = tk.Label(self.left_frame)
        self.attendance_label.configure(
            background="#fff200",
            font="{Arial Black} 18 {}",
            foreground="#0072bc",
            height=2,
            justify="center",
            relief="flat",
            text='Attendance:                              ',
            width=25)
        self.attendance_label.grid(
            column=0,
            columnspan=2,
            ipadx=20,
            ipady=10,
            padx=5,
            row=2)

        #button for next person attendance
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

        #label for the logo of the sti image
        self.label5 = tk.Label(self.left_frame)
        self.img_STICollegeBalagtasLogos = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo-s.png")
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

        #button for resetting the wrong detection
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
        #setting up left frame
        self.left_frame.pack(expand="true", fill="both", side="left")
        self.left_frame.grid_anchor("center")
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure("all", weight=1)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.columnconfigure("all", weight=1)

        #right Frame(includes camera and add button)
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.configure(background="#0072bc", height=400, width=400)

        #button for adding new client
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

        #camera display on the Window
        self.camera_canvas = tk.Canvas(
            self.right_frame, 
            width = self.fr_vid.width, 
            height = self.fr_vid.height)
        self.camera_canvas.grid(column=0, padx=5, pady=10, row=0)

        #setting up right frame
        self.right_frame.pack(expand="true", fill="both", side="right")
        self.right_frame.grid_anchor("center")
        self.right_frame.rowconfigure(0, weight=1)
        self.right_frame.columnconfigure(0, weight=1)
        self.main_frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")

        self.cam_update()
        # Main widget
        self.mainwindow = self.system_app

    #this function will restart the main system.
    def restart(self):
        self.cont = False
        self.system_app.destroy() 
        FaceRecognitionUI().run()

    # will update the canvas content
    def cam_update(self):
        if self.cont:
            pass
        # Get a frame from the video source
        ret, frame = self.fr_vid.get_frame()
        # if it return a frame and if there are still no face detected
        if ret & self.fr_vid.face_detected:
            #consistently getting the time and date 
            self.current_time = time.strftime('%H:%M:%S', time.localtime())
            self.current_date = datetime.date.today().strftime("%m/%d/%y")
            self.current_date_n_time = 'Attendance: ' + self.current_date +' '+self.current_time    
            #saving the frame from the array unto the photo variable as an "image"
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            #putting of image(frame) into the canvas
            self.camera_canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
            #continuous face detection
            self.fr_vid.face_recognition_func()
            #if a face is detected it will stop detecting and
            # will display the image of the owner of the face
            if not self.fr_vid.face_detected :
                print('run')
                self.attendance()
        #call again the same method after 15 millisecond
        self.system_app.after(15, self.cam_update)
        self.cont = False

    # check attendance 
    # this will be used for the database. 
    # retrieving data and displaying necessary details on screen.
    def attendance(self):
        print("detected")
        self.client_name_label.config(text = self.fr_vid.name)
        self.attendance_label.config(text = self.current_date_n_time)
        """
        system connection to the database
        """
        # the system will open the image of the client using the array
        # of paths of the image with the index of the image.
        load_image = Image.open(self.fr_vid.paths_array[self.fr_vid.image_index])
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.student_image = ImageTk.PhotoImage(load_image)
        #will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image = self.student_image, anchor = tk.NW)
        
    def run(self):
        self.mainwindow.mainloop()  

    #command for pressing the next button
    #will return to the initial display of the screen
    def next_student(self, event=None):
        self.fr_vid.face_detected = True
        self.client_name_label.config(text = 'Detecting...')
        self.attendance_label.config(
        text = 'Attendance:                              ')
        self.cam_update

    #command for pressing the reset button
    #will not save the attendance if the detection is incorrect
    def reset_attendance(self, event=None):
        self.fr_vid.face_detected = True
        self.cam_update

    #command for pressing the add button
    #will call the snapshot file to add a new client
    def add_client(self, event=None):
        self.cont = True
        ss.snapApp(self.restart)


if __name__ == "__main__":
    app = FaceRecognitionUI()
    app.run()



"""
Class FaceRecognitionUI
    def __init__ = initialization of window and widgets 
    def restart = will restart the main system
    def cam_update = will display the camera/image of the detected face into the canvas
    def attendance = will set the image and details of the client
    def run = will run the system
    def next_student = will save the information of the student and reopen the camera
    def reset_student = will not save the info
    def add_client = will add new client to the system.
"""