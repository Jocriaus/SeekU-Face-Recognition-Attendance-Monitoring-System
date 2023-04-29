import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
import face_recog_mod as mf
import query_mod as qry
import sys


class ClientFaceRecogApp:
    def __init__(self, login_mod, sel_cam, home_mod,detection,splashs, fr_vid_mod):

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.splash = splashs
        self.login_window = login_mod
        self.select_cam_window = sel_cam
        self.home_window = home_mod
        self.detection_time = detection *1000
        self.call_cam = False
        self.sql_query = qry.dbQueries()
        self.fr_vid = fr_vid_mod

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        # build ui
        self.face_recog_app = tk.Toplevel()
        self.face_recog_app.configure(background="#0072bc", height=200, width=200)
        width = self.face_recog_app.winfo_screenwidth()
        height = self.face_recog_app.winfo_screenheight()
        self.face_recog_app.geometry("%dx%d" % (width, height))
        self.face_recog_app.resizable(False, False)
        self.face_recog_app.title("SeekU - Client Face Recognition Attendance")
        self.face_recog_app.iconbitmap(".\SeekU\SeekU.ico")

        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        # this sets the camera size
        
        self.face_recog_frame3 = tk.Frame(self.face_recog_app)
        self.face_recog_frame3.configure(background="#0072bc", height=200, width=200)
        self.face_recog_frame3.place(
            anchor="center", relheight=0.83, relwidth=0.83, relx=0.42, rely=0.42
        )

        self.camera_canvas = tk.Canvas(self.face_recog_frame3)
        self.camera_canvas.configure(
            background="#0072bc", highlightbackground="#0072bc"
        )
        self.camera_canvas.place(
            anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, x=0, y=0
        )

        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------

        # Contains-the-sti-logo-attendance-and-student-name---------------------------------------------------------------------------------------------------------

        self.face_recog_frame2 = tk.Frame(self.face_recog_app)
        self.face_recog_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.client_name_label = tk.Label(self.face_recog_frame2)
        self.client_name_label.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial} 54 {}",
            foreground="#0072bc",
            justify="left",
            text="Client Name",
        )
        self.client_name_label.place(anchor="center", relx=0.5, rely=0.3)
        self.attendance_label = tk.Label(self.face_recog_frame2)
        self.attendance_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 40 {}",
            foreground="#0072bc",
            justify="left",
            text="Attendance",
        )
        self.attendance_label.place(anchor="center", relx=0.5, rely=0.75)
        self.school_logo_label = tk.Label(self.face_recog_frame2)
        self.img_STICollegeBalagtasLogo = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background="#F7FAE9", image=self.img_STICollegeBalagtasLogo, text="label1"
        )
        self.school_logo_label.place(anchor="center", relx=0.07, rely=0.5)
        self.face_recog_frame2.place(
            anchor="center", relheight=0.16, relwidth=1.0, relx=0.50, rely=0.92
        )

        # Contains-the-sti-logo-attendance-and-student-name---------------------------------------------------------------------------------------------------------
        # Contains-the-signout-and-cancel-buttons-app-logo-and-logotype---------------------------------------------------------------------------------------------------------

        self.face_recog_frame = tk.Frame(self.face_recog_app)
        self.face_recog_frame.configure(background="#F7FAE9", height=200, width=200)
        self.app_logo_label = tk.Label(self.face_recog_frame)
        self.img_SeekUmedium = tk.PhotoImage(file=".\SeekU\SeekU medium.png")
        self.app_logo_label.configure(
            background="#F7FAE9", image=self.img_SeekUmedium, text="label1"
        )
        self.app_logo_label.place(
            anchor="center", relheight=0.13, relwidth=0.85, relx=0.50, rely=0.17
        )
        self.app_name_logo = tk.Label(self.face_recog_frame)
        self.img_SeekULogotypeextralarge = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype extra large.png"
        )
        self.app_name_logo.configure(
            background="#F7FAE9",
            foreground="#0072bc",
            image=self.img_SeekULogotypeextralarge,
            relief="flat",
            text="E",
        )
        self.app_name_logo.place(anchor="center", relx=0.5, rely=0.51)
        self.return_button = tk.Button(self.face_recog_frame)
        self.return_button.configure(
            font="{arial black} 20 {}", foreground="#0072bc", text="Log out"
        )
        self.return_button.place(
            anchor="center", relheight=0.05, relwidth=0.55, relx=0.5, rely=0.06
        )
        self.return_button.bind("<ButtonPress>", self.return_func, add="")
        self.cancel_button = tk.Button(self.face_recog_frame)
        self.cancel_button.configure(
            font="{arial black} 30 {}", foreground="#0072bc", text="Cancel"
        )
        self.cancel_button.place(
            anchor="center", relheight=0.08, relwidth=0.69, relx=0.5, rely=0.925
        )
        self.cancel_button.bind("<ButtonPress>", self.cancel_attendance, add="")
        self.face_recog_frame.place(
            anchor="center", relheight=1.0, relwidth=0.16, relx=0.92, rely=0.5
        )
        # Contains-the-signout-button-app-logo-and-logotype---------------------------------------------------------------------------------------------------------
        # see function description
        self.cam_update()
        # see function descritption
        self.hide_name()
        
        # Main widget
        self.mainwindow = self.face_recog_app

        # will set the window to fullscreen
        self.mainwindow.wm_attributes("-fullscreen", "True")
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)
        self.splash()
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)
        

    # -----------------------------------------------------------------------------------------
    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    # this will show the home window and destroy this window
    def show_home_window(self):
        self.home_window.deiconify()
        self.face_recog_app.destroy()

    # this function will hide the name and the attendance widgets
    def hide_name(self):
        self.client_name_label.place_forget()
        self.attendance_label.place_forget()

    # this function will show the name and the attendance widgets
    def show_name(self):
        self.client_name_label.place(anchor="center", relx=0.5, rely=0.3)
        self.attendance_label.place(anchor="center", relx=0.5, rely=0.75)

    # this function updates the canvas content - shows the camera
    def cam_update(self):
        if self.fr_vid.cont:
            return
        # Get a frame from the video source
        ret, frame = self.fr_vid.get_frame()
        # if it return a frame and if there are still no face detected
        if ret & (not self.fr_vid.face_detected):
            if not self.fr_vid.cont:
                self.hide_name()
                # consistently getting the time and date
                self.current_time = time.strftime("%H:%M:%S", time.localtime())
                current_date = datetime.date.today().strftime("%Y/%m/%d")
                self.current_date_n_time = current_date + " " + self.current_time
                self.fr_vid.box_and_dot(frame)
                # saving the frame from the array unto the photo variable as an "image"
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                # putting of image(frame) into the canvas

                self.camera_canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
                # self.detect_face()
                print("cont2")
                self.fr_vid.face_in_box(self.recognize_face)
                # call again the same method after 15 millisecond
        self.face_recog_app.after(15, self.cam_update)

    # this function will save the attendance of the students
    def attendance(self):
        print("detected")
        self.show_name()
        # use the self.fr_vid.name to get the name in the database
        client_num = self.fr_vid.name
        print(client_num)
        if self.sql_query.check_student_no(client_num):
            full_name = self.sql_query.get_student_name(client_num)
        elif self.sql_query.check_personnel_no(client_num):
            full_name = self.sql_query.get_personnel_name(client_num)
        elif self.sql_query.check_visitor_no(client_num):      
            full_name = self.sql_query.get_visitor_name(client_num) 
        
        self.client_name_label.config(text=full_name)
        self.attendance_label.config(text=self.current_date_n_time)
        # the system will open the image of the client using the array
        # of paths of the image with the index of the image.
        self.load_image = Image.open(self.fr_vid.paths_array[self.fr_vid.image_index])
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((1280, 720), Image.ANTIALIAS)

        self.student_image = ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)

    # this function will check the images if there are similar faces
    def recognize_face(self):
        self.fr_vid.face_recognition_func()
        print(self.fr_vid.face_detected)
        print("recognize face before not")
        # if a face is detected it will stop detecting and
        # will display the image of the owner of the face
        if self.fr_vid.face_detected:
            print("run")
            self.attendance()
            # this will call the next person function
            self.face_recog_app.after(self.detection_time, self.next_person)
            self.save_attendance_func()
        elif not self.fr_vid.face_detected:
            print ("no face")
            # this will call the next person function if there is no face detected
            self.face_recog_app.after(1000, self.next_person)

    # this function will reset the conditions that enables the face detection
    # and camera display, will call the cam_update function to resume cam display
    def next_person(self):
        self.fr_vid.cont = False
        self.fr_vid.face_detected = False
        self.fr_vid.recognized = False
        self.cam_update()

    # this will save the attendance of the student
    def save_attendance_func(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        date_int = int(datetime.datetime.now().strftime("%y%m%d"))
        custom_no = date_int * 100000

        if self.sql_query.check_student_no(int(self.fr_vid.name)):
            self.sql_query.student_attendance_record(custom_no, str(self.fr_vid.name), current_date, self.current_time)
        elif self.sql_query.check_personnel_no(self.fr_vid.name):
            self.sql_query.personnel_attendance_record(custom_no, str(self.fr_vid.name), current_date, self.current_time)
        elif self.sql_query.check_visitor_no(self.fr_vid.name):
            self.sql_query.visitor_attendance_record(custom_no, str(self.fr_vid.name), current_date, self.current_time)
        
    # this command will return to the home window
    def return_func(self, event=None):
        self.show_home_window()
        self.fr_vid.cam_release()
        self.face_recog_app.destroy()

    # this will cancel the saving the current attendance of the person detected
    def cancel_attendance(self, event=None):
        pass
