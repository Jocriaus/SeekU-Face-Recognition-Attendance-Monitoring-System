import tkinter as tk
from tkinter import filedialog
import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import os


class AddVisitorApp:
    def __init__(self, vid_source, login_mod, sel_cam, home_mod, ):

        #assignment for passed parameters
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.home_window = home_mod
        # open video source
        

        # build ui
        self.add_visitor_app = tk.Toplevel()
        self.add_visitor_app.configure(
            background="#F7FAE9", height=200, width=200)
        width= self.add_visitor_app.winfo_screenwidth()               
        height= self.add_visitor_app.winfo_screenheight() 
        self.add_visitor_app.geometry("%dx%d" % (width, height))
        self.add_visitor_app.resizable(False, False)


#-----------------------------------------------------------------------------------------
        self.add_visitor_frame3 = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame3.configure(
            background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.add_visitor_frame3)
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
        self.add_visitor_frame3.place(
            anchor="center",
            relheight=0.60,
            relwidth=0.60,
            relx=0.68,
            rely=0.36)

        self.vid = MyVideoCapture(self.video_source, 1280, 720)
#-----------------------------------------------------------------------------------------
        self.add_visitor_frame2 = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_name_labelS = tk.Label(self.add_visitor_frame2)
        self.app_name_labelS.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#0072bc",
            justify="left",
            text='SEEK')
        self.app_name_labelS.place(anchor="center", relx=0.70, rely=.5)
        self.app_name_labelU = tk.Label(self.add_visitor_frame2)
        self.app_name_labelU.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#FFF200",
            justify="left",
            text='U')
        self.app_name_labelU.place(anchor="center", relx=0.87, rely=0.5)
        self.app_logo_label = tk.Label(self.add_visitor_frame2)
        self.img_SeekUmedium = tk.PhotoImage(file=".\SeekU\SeekU medium.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUmedium,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.47, rely=0.50)
        self.sign_out_button = tk.Button(self.add_visitor_frame2)
        self.sign_out_button.configure(
            font="{arial black} 20 {}",
            foreground="#0072bc",
            text='Sign out')
        self.sign_out_button.place(
            anchor="center",
            relheight=0.15,
            relwidth=0.1,
            relx=0.93,
            rely=0.85)
        self.sign_out_button.bind("<ButtonPress>", self.sign_out, add="")
        self.add_visitor_frame2.place(
            anchor="center",
            relheight=0.3,
            relwidth=1.0,
            relx=0.50,
            rely=0.85)




#-----------------------------------------------------------------------------------------            
        self.add_visitor_frame = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.snapshot_button = tk.Button(self.add_visitor_frame)
        self.snapshot_button.configure(
            font="{arial black} 30 {}",
            foreground="#0072bc",
            text='Snapshot')
        self.snapshot_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.50,
            relx=.5,
            rely=.90)
        self.snapshot_button.bind("<ButtonPress>", self.save_info, add="")
        self.school_logo_label = tk.Label(self.add_visitor_frame)
        self.img_STICollegeBalagtasLogo = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo.png")
        self.school_logo_label.configure(
            background="#F7FAE9",
            image=self.img_STICollegeBalagtasLogo,
            text='label1')
        self.school_logo_label.place(
            anchor="center",
            relx=.5,
            rely=0.12)
        self.last_name_label = tk.Label(self.add_visitor_frame)
        self.last_name_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='Last Name')
        self.last_name_label.place(
            anchor="center", relx=0.34, rely=0.25, x=0, y=0)
        self.last_name_entry = tk.Entry(self.add_visitor_frame)
        self.last_name_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.last_name_entry.place(
            anchor="center", relx=0.55, rely=0.31, x=0, y=0)
        self.first_name_label = tk.Label(self.add_visitor_frame)
        self.first_name_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='First Name')
        self.first_name_label.place(
            anchor="center", relx=0.34, rely=0.40, x=0, y=0)
        self.first_name_entry = tk.Entry(self.add_visitor_frame)
        self.first_name_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.first_name_entry.place(
            anchor="center", relx=0.55, rely=0.46, x=0, y=0)
        self.contact_no_label = tk.Label(self.add_visitor_frame)
        self.contact_no_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='Contact No.')
        self.contact_no_label.place(
            anchor="center", relx=0.36, rely=0.55, x=0, y=0)
        self.contact_no_entry = tk.Entry(self.add_visitor_frame)
        self.contact_no_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.contact_no_entry.place(
            anchor="center", relx=0.55, rely=.61, x=0, y=0)
        self.address_label = tk.Label(self.add_visitor_frame)
        self.address_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='Address')
        self.address_label.place(
            anchor="center", relx=0.29, rely=0.70, x=0, y=0)
        self.address_entry = tk.Entry(self.add_visitor_frame)
        self.address_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.address_entry.place(
            anchor="center", relx=0.55, rely=0.76, x=0, y=0)
        self.add_visitor_frame.place(
            anchor="center",
            relheight=1.0,
            relwidth=0.35,
            relx=0.17,
            rely=0.5)

        self.haar_face_cascade = cv2.CascadeClassifier(
        "MainSystem\DetectionData\haarcascade_frontalface_alt.xml")

        self.cam_update()
        # Main widget
        self.mainwindow = self.add_visitor_app
        self.mainwindow.attributes('-topmost', True)
        self.mainwindow.wm_attributes('-fullscreen', 'True', )

#-----------------------------------------------------------------------------------------
    def show_home_window(self):
        self.home_window.deiconify()
        self.add_visitor_app.destroy()
        # add additional function for destroying camera

    def cam_update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            resized = cv2.resize(frame, (self.camera_canvas.winfo_width(), self.camera_canvas.winfo_height()), interpolation=cv2.INTER_AREA)
            # turning the image into gray for the haar cascade to be read
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            # detecting the face
            faces = self.haar_face_cascade.detectMultiScale(gray, 1.1, 6)
            # placing a rectangle within the face
            for (x, y, w, h) in faces:
                cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 114, 188), 2)
            # pu tthe image/frame into the canvas
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(resized))
            self.camera_canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

        self.add_visitor_app.after(15, self.cam_update)

    def select_folder(self):
        self.add_visitor_app.attributes('-topmost', False)
        self.folder_selected = filedialog.askdirectory()
        self.add_visitor_app.attributes('-topmost', True)
    
        # Get a frame from the video source 
    def snapshot_func(self):
        # putting the values into variables to save into the database. 
        # create a data for the user then get the PK for the name of the image
        # save the PK to a variable then use it for the  saving of image
        """
        Database Connection
        """
        last_name = self.last_name_entry.get()
        first_name = self.first_name_entry.get()
        contact_num = self.contact_no_entry.get()
        address = self.address_entry.get()
        self. select_folder()
        ret, frame = self.vid.get_frame()
        resized = cv2.resize(frame, (self.camera_canvas.winfo_width(), self.camera_canvas.winfo_height()), interpolation=cv2.INTER_AREA)
        if ret:
            cv2.imwrite(os.path.join(self.folder_selected ,(contact_num + ".jpg")), cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))
    


    def sign_out(self, event=None):
        self.show_home_window()
        self.add_visitor_app.destroy()

    def save_info(self, event=None):
        self.snapshot_func()

class MyVideoCapture:
    def __init__(self, video_source,  xsize,ysize):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # setting the height and width of the camera
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH,xsize)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT,ysize)
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
