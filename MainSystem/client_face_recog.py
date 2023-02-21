import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
import face_recog as mf

class ClientFaceRecogApp:
    def __init__(self,vid_source, login_mod, sel_cam, home_mod, file_path):

        #assignment for passed parameters
        self.login_window = login_mod
        self.select_cam_window = sel_cam
        self.home_window = home_mod

        # build ui
        self.face_recog_app = tk.Toplevel()
        self.face_recog_app.configure(
            background="#0072bc", height=200, width=200)
        width= self.face_recog_app.winfo_screenwidth()               
        height= self.face_recog_app.winfo_screenheight()               
        self.face_recog_app.geometry("%dx%d" % (width, height))
        self.face_recog_app.resizable(False, False)

        
#-----------------------------------------------------------------------------------------
        self.face_recog_frame3 = tk.Frame(self.face_recog_app)
        self.face_recog_frame3.configure(
            background="#0072bc", height=200, width=200)
        self.face_recog_frame3.place(
            anchor="center",
            relheight=0.83,
            relwidth=.83,
            relx=0.42,
            rely=0.42)

        self.camera_canvas = tk.Canvas(self.face_recog_frame3)
        self.camera_canvas.configure(
            background="#0072bc",
            highlightbackground="#0072bc")
        self.camera_canvas.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=.5,
            rely=.5,
            x=0,
            y=0)

        print(self.camera_canvas.winfo_width())
        print(self.camera_canvas.winfo_height())
        self.fr_vid = mf.FaceRecognition(vid_source,file_path, 1280, 720 )
        # self.fr_vid = mf.FaceRecognition(vid_source,file_path, 1592, 896 )
        # self.fr_vid = mf.FaceRecognition(vid_source,file_path, 640, 480 )
        


#-----------------------------------------------------------------------------------------        
        self.face_recog_frame2 = tk.Frame(self.face_recog_app)
        self.face_recog_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.stud_name_label = tk.Label(self.face_recog_frame2)
        self.stud_name_label.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial} 54 {}",
            foreground="#0072bc",
            justify="left",
            text='Jose Crisanto Austria')
        self.stud_name_label.place(anchor="center", relx=0.5, rely=0.3)
        self.attendance_label = tk.Label(self.face_recog_frame2)
        self.attendance_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 40 {}",
            foreground="#0072bc",
            justify="left",
            text='19/23/2023 - 07:30:30')
        self.attendance_label.place(anchor="center", relx=0.5, rely=0.75)
        self.school_logo_label = tk.Label(self.face_recog_frame2)
        self.img_STICollegeBalagtasLogo = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png")
        self.school_logo_label.configure(
            background="#F7FAE9",
            image=self.img_STICollegeBalagtasLogo,
            text='label1')
        self.school_logo_label.place(anchor="center", relx=0.07, rely=0.5)
        self.face_recog_frame2.place(
            anchor="center",
            relheight=0.16,
            relwidth=1.0,
            relx=0.50,
            rely=0.92)



#-----------------------------------------------------------------------------------------

        self.face_recog_frame = tk.Frame(self.face_recog_app)
        self.face_recog_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_logo_label = tk.Label(self.face_recog_frame)
        self.img_SeekUmedium = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUmedium,
            text='label1')
        self.app_logo_label.place(
            anchor="center",
            relheight=0.13,
            relwidth=0.85,
            relx=0.50,
            rely=0.17)
        self.app_name_labels = tk.Label(self.face_recog_frame)
        self.app_name_labels.configure(
            background="#F7FAE9",
            font="{arial black} 80 {}",
            foreground="#0072bc",
            relief="flat",
            text='S')
        self.app_name_labels.place(
            anchor="center",
            relheight=0.10,
            relwidth=.32,
            relx=.5,
            rely=0.29)
        self.app_name_labele = tk.Label(self.face_recog_frame)
        self.app_name_labele.configure(
            background="#F7FAE9",
            font="{arial black} 80 {}",
            foreground="#0072bc",
            relief="flat",
            text='E')
        self.app_name_labele.place(
            anchor="center",
            relheight=0.12,
            relwidth=.32,
            relx=.5,
            rely=0.4)
        self.app_name_labele2 = tk.Label(self.face_recog_frame)
        self.app_name_labele2.configure(
            background="#F7FAE9",
            font="{arial black} 80 {}",
            foreground="#0072bc",
            relief="flat",
            text='E')
        self.app_name_labele2.place(
            anchor="center",
            relheight=.12,
            relwidth=.32,
            relx=.5,
            rely=0.51)
        self.app_name_labelk = tk.Label(self.face_recog_frame)
        self.app_name_labelk.configure(
            background="#F7FAE9",
            font="{arial black} 80 {}",
            foreground="#0072bc",
            relief="flat",
            text='K')
        self.app_name_labelk.place(
            anchor="center",
            relheight=.12,
            relwidth=.32,
            relx=.5,
            rely=0.62)
        self.app_name_labelu = tk.Label(self.face_recog_frame)
        self.app_name_labelu.configure(
            background="#F7FAE9",
            font="{arial black} 80 {}",
            foreground="#fff200",
            relief="flat",
            text='U')
        self.app_name_labelu.place(
            anchor="center",
            relheight=0.11,
            relwidth=0.32,
            relx=.5,
            rely=0.75)
        self.sign_out_button = tk.Button(self.face_recog_frame)
        self.sign_out_button.configure(
            font="{arial black} 20 {}",
            foreground="#0072bc",
            text='Sign Out')
        self.sign_out_button.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.55,
            relx=0.5,
            rely=0.06)
        self.sign_out_button.bind("<ButtonPress>", self.sign_out_func, add="")
        self.cancel_button = tk.Button(self.face_recog_frame)
        self.cancel_button.configure(
            font="{arial black} 30 {}",
            foreground="#0072bc",
            text='Cancel')
        self.cancel_button.place(
            anchor="center",
            relheight=0.08,
            relwidth=0.69,
            relx=.5,
            rely=.925)
        self.cancel_button.bind(
            "<ButtonPress>",
            self.cancel_attendance,
            add="")
        self.face_recog_frame.place(
            anchor="center",
            relheight=1.0,
            relwidth=0.16,
            relx=0.92,
            rely=0.5)
        
        self.cam_update()
        self.hide_name()
        # Main widget
        self.mainwindow = self.face_recog_app
        self.mainwindow.wm_attributes('-fullscreen', 'True')


#-----------------------------------------------------------------------------------------

    def show_home_window(self):
        self.home_window.deiconify()
        self.face_recog_app.destroy()
        # add additional function for destroying camera


        # will update the canvas content
    def cam_update(self):
        # Get a frame from the video source
        ret, frame = self.fr_vid.get_frame()
        # if it return a frame and if there are still no face detected
        if ret & self.fr_vid.face_detected:
            # consistently getting the time and date 
            self.current_time = time.strftime('%H:%M:%S', time.localtime())
            self.current_date = datetime.date.today().strftime("%m/%d/%y")
            self.current_date_n_time = 'Attendance: ' + self.current_date +' '+self.current_time  
            self.fr_vid.box_and_dot(frame)
            # saving the frame from the array unto the photo variable as an "image"
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            # putting of image(frame) into the canvas
            
            self.camera_canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
            # self.detect_face()
            self.fr_vid.face_in_box(self.recognize_face)

            # call again the same method after 15 millisecond
        self.face_recog_app.after(15, self.cam_update)  

    def attendance(self):
        print("detected")

        self.show_name()
        # use the self.fr_vid.name to get the name in the database
        self.stud_name_label.config(text = self.fr_vid.name)
        self.attendance_label.config(text = self.current_date_n_time)
        """
        system connection to the database
        """
        # the system will open the image of the client using the array
        # of paths of the image with the index of the image.
        self.load_image = Image.open(self.fr_vid.paths_array[self.fr_vid.image_index])
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((1280, 720), Image. ANTIALIAS)

        self.student_image = ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image = self.student_image, anchor = tk.NW)


    def hide_name(self):
        self.stud_name_label.place_forget()
        self.attendance_label.place_forget()

    def show_name(self):
        self.stud_name_label.place(anchor="center", relx=0.5, rely=0.3)
        self.attendance_label.place(anchor="center", relx=0.5, rely=0.75)

    def recognize_face(self):

        self.fr_vid.face_recognition_func()
        # if a face is detected it will stop detecting and
        # will display the image of the owner of the face
        if not self.fr_vid.face_detected :
            print('run')
            self.attendance()
        

        # add delay then add call cam_update

    def sign_out_func(self, event=None):
        self.show_home_window()
        self.face_recog_app.destroy()

    def cancel_attendance(self, event=None):
        pass



