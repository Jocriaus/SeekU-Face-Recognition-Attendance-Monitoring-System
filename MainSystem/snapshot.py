# python file for taking pictures
from tkinter import filedialog
import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import os

class snapApp:
    def __init__(self,restart,video_source=0 ):
        # build ui (second window)
        self.snapshot_app = tk.Toplevel()
        self.snapshot_app.title("SeekU - Add Client")
        self.snapshot_app.configure(
            background="#0072bc")
        self.snapshot_app.geometry("1280x720")
        self.snapshot_app.iconbitmap(".\SeekU\SeekU.ico")
        self.snapshot_app.attributes('-topmost', True)
        self.restart_var = restart
        # open video source
        self.vid = MyVideoCapture(video_source)
        # Create a canvas that can fit the above video source size
        self.snap_camera_canvas = tk.Canvas(self.snapshot_app, width = self.vid.width, height = self.vid.height)
        self.snap_camera_canvas.pack(anchor="e",padx=10, expand="false", side="left")
        
        # snapshot! title label
        self.snapshot_lbl = tk.Label(self.snapshot_app)
        self.snapshot_lbl.configure(
            background="#0072bc",
            font="{Arial Black} 30 {}",
            foreground="#fff200",
            text='Snapshot!')
        self.snapshot_lbl.pack(anchor="center", padx=10, pady=25, side="top")

        # student num label
        self.student_num_lbl = tk.Label(self.snapshot_app)
        self.student_num_lbl.configure(
            background="#0072bc",
            font="{Arial Black} 20 {}",
            foreground="#fff200",
            text='Client Number:')
        self.student_num_lbl.pack(anchor="center", padx=30, pady=5, side="top")
        # will be the file name of the client's image
        self.student_num_entry = tk.Entry(self.snapshot_app)
        self.student_num_entry.configure(font="{Arial Baltic} 14 {}", width=35)
        self.student_num_entry.pack(anchor="center", side="top")

        # Last Name Label
        self.last_name_lbl = tk.Label(self.snapshot_app)
        self.last_name_lbl.configure(
            background="#0072bc",
            font="{Arial Black} 20 {}",
            foreground="#fff200",
            text='Last Name:')
        self.last_name_lbl.pack(anchor="center", pady=5, side="top")
        # last name entry of the client
        self.last_name_entry = tk.Entry(self.snapshot_app)
        self.last_name_entry.configure(font="{Arial Baltic} 14 {}", width=35)
        self.last_name_entry.pack(anchor="center", side="top")

        # First Name Label
        self.first_name_lbl = tk.Label(self.snapshot_app)
        self.first_name_lbl.configure(
            background="#0072bc",
            font="{Arial Black} 20 {}",
            foreground="#fff200",
            text='First Name:')
        self.first_name_lbl.pack(anchor="center", pady=5, side="top")
        # First name entry of the client
        self.first_name_entry = tk.Entry(self.snapshot_app)
        self.first_name_entry.configure(font="{Arial Baltic} 14 {}", width=35)
        self.first_name_entry.pack(anchor="center", side="top")

        # guest checker Will ask if the client is a guest
        self.guest_checked_var = tk.IntVar()
        self.guest_check = tk.Checkbutton(self.snapshot_app, variable = self.guest_checked_var ,command= self.isguest)
        self.guest_check.configure(
            background="#0072bc",
            font="{Arial Black} 16 {}",
            foreground="#fff200",
            text='Guest?')
        self.guest_check.pack(anchor="center", side="top")

        # mobile number Label
        self.mob_num_lbl = tk.Label(self.snapshot_app)
        self.mob_num_lbl.configure(
            background="#0072bc",
            font="{Arial Black} 20 {}",
            foreground="#fff200",
            text='Mobile Number:')
        # self.mob_num_lbl.pack(anchor="center", pady=5, side="top")
    
        # mobile entry of the client/guest
        self.mob_num_entry = tk.Entry(self.snapshot_app)
        self.mob_num_entry.configure(font="{Arial Baltic} 14 {}", width=35)
        # self.mob_num_entry.pack(anchor="center", expand="true", side="top")

        # button for the folder selection
        self.folder_selection_button=tk.Button(self.snapshot_app, command=self.select_folder)
        self.folder_selection_button.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            text='Select Folder',
            width=20)
        self.folder_selection_button.pack(anchor=tk.S,pady=20, expand=True)

        # Button that lets the user take a snapshot
        self.snapshot_btn = tk.Button(self.snapshot_app, command=self.snapshot_func)
        self.snapshot_btn.configure(
            background="#fff200",
            font="{Arial Black} 20 {}",
            foreground="#0072bc",
            text='Take a Picture!',
            width=20)
        self.snapshot_btn.pack(anchor="s", padx=10, pady=5, side="bottom")
        # self.snapshot_btn.bind("<ButtonPress>", self.snapshot_func)

        # setting up haar cascade
        self.haar_face_cascade = cv2.CascadeClassifier(
        "MainSystem\Face Detection Data\haarcascade_frontalface_alt.xml"
        )
        self.cont = False

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15       
        self.cam_update()

        self.snapshot_app.protocol("WM_DELETE_WINDOW", self.restart_system )
        

    def cam_update(self):
        if self.cont:
            return
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            # turning the image into gray for the haar cascade to be read
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detecting the face
            faces = self.haar_face_cascade.detectMultiScale(gray, 1.1, 6)
            # placing a rectangle within the face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 114, 188), 2)
            # pu tthe image/frame into the canvas
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.snap_camera_canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

        self.snapshot_app.after(self.delay, self.cam_update)
        self.cont = False

    # will put a temporary image to the camera canvas
    def add_client_camera_error_fix(self):
        temp_image = PIL.Image.open(".\SeekU\Background.png")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.bg_image = PIL.ImageTk.PhotoImage(temp_image)
        # will display the image into the canvas
        self.snap_camera_canvas.create_image(0, 0, image = self.bg_image, anchor = tk.NW)

    def select_folder(self):
        self.snapshot_app.attributes('-topmost', False)
        self.folder_selected = filedialog.askdirectory()
        self.snapshot_app.attributes('-topmost', True)

    # Get a frame from the video source 
    def snapshot_func(self):
        # putting the values into variables to save into the database. 
        student_number = self.student_num_entry.get()
        """
        Database Connection
        """
        student_last_name = self.last_name_entry.get()
        student_first_name = self.first_name_entry.get()

        if not self.guest_checked_var.get() == 0:
            mobile_number = self.mob_num_entry.get()
        ret, frame = self.vid.get_frame()
        
        if ret:
            cv2.imwrite(os.path.join(self.folder_selected ,(student_number + ".jpg")), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    
    def isguest(self):
        if self.guest_checked_var.get() == 0:
            # self.mob_num_entry.configure(state='disabled')
            self.mob_num_lbl.pack_forget()
            self.mob_num_entry.pack_forget()            
        else:
            # self.mob_num_entry.configure(state='normal')
            self.mob_num_lbl.pack(anchor="center", pady=5, side="top")
            self.mob_num_entry.pack(anchor="center", expand="true", side="top")
            self.folder_selection_button.pack_forget()
            self.folder_selection_button.pack(anchor=tk.S,pady=20, expand=True)
            self.snapshot_btn.pack_forget()
            self.snapshot_btn.pack(anchor="s", padx=10, pady=5, side="bottom")

    def restart_system(self):
        self.cont = True
        self.add_client_camera_error_fix()
        self.restart_var()
        
    

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # setting the height and width of the camera
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            # flipping the image so it is not inverted
            frame = cv2.flip(frame, 1)
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)


"""
class snapApp
    def __init__ = will encode the images 
    def cam_update = will display the camera into the canvas
    def add_client_camera_error_fix = Will put a temporary image to the camera canvas
    def select_folder = will encode the images
    def snapshot_func = will take grab the image and save to the selected folder together of the information given
    def isGuest = this function will remove the mobile numeber label and entry
    def restart_system = will restart the system by calling the restart function in system_main.py

class MyVideoCapture
    def __init__ = will set up the camera
    def __del__ = will delete the camera/video source
    def get_frame = will get frame if the camera is open

"""