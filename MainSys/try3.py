import tkinter as tk
from tkinter import filedialog
import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import os

class CameraApp:
    def __init__(self, master=None):
        # build ui
        self.snapshot_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.snapshot_app.configure(
            background="#F7FAE9", height=200, width=200)
        width= self.snapshot_app.winfo_screenwidth()               
        height= self.snapshot_app.winfo_screenheight()               
        self.snapshot_app.geometry("%dx%d" % (width, height))
        self.snapshot_app.resizable(False, False)
        self.snapshot_frame4 = tk.Frame(self.snapshot_app)
        self.snapshot_frame4.configure(
            background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.snapshot_frame4)
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
        self.snapshot_frame4.place(
            anchor="center",
            relheight=0.50,
            relwidth=0.50,
            relx=0.5,
            rely=0.575)
        self.snapshot_frame3 = tk.Frame(self.snapshot_app)
        self.snapshot_frame3.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.snapshot_frame3)
        self.img_SeekULogotypesmall = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype large.png")
        self.app_name_logo.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#0072bc",
            image=self.img_SeekULogotypesmall,
            justify="left",
            text='SEEK')
        self.app_name_logo.place(anchor="center", relx=0.575, rely=.5)
        self.app_logo_label = tk.Label(self.snapshot_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUlarge,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.35, rely=0.5)
        self.snapshot_frame3.place(
            anchor="center",
            relheight=0.16,
            relwidth=1.0,
            relx=0.50,
            rely=0.21)
        self.snapshot_frame2 = tk.Frame(self.snapshot_app)
        self.snapshot_frame2.configure(
            background="#fff000", height=200, width=200)
        self.school_logo_label = tk.Label(self.snapshot_frame2)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png")
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text='label1')
        self.school_logo_label.place(anchor="center", relx=.25, rely=0.5)
        self.snapshot_frame2.place(
            anchor="center",
            relheight=0.13,
            relwidth=1.0,
            relx=0.5,
            rely=0.065)
        self.snapshot_frame1 = tk.Frame(self.snapshot_app)
        self.snapshot_frame1.configure(
            background="#F7FAE9", height=200, width=200)
        self.snapshot_button = tk.Button(self.snapshot_frame1)
        self.snapshot_button.configure(
            background="#0072bc",
            font="{arial black} 36 {}",
            foreground="#F7FAE9",
            text='Snapshot')
        self.snapshot_button.place(
            anchor="center",
            relheight=0.6,
            relwidth=0.2,
            relx=.5,
            rely=0.5)
        self.snapshot_button.bind("<ButtonPress>", self.take_picture, add="")
        self.snapshot_frame1.place(
            anchor="center",
            relheight=0.15,
            relwidth=1.0,
            relx=0.5,
            rely=0.925)

        # Main widget
        self.mainwindow = self.snapshot_app
        self.mainwindow.wm_attributes('-fullscreen', 'True')

    def run(self):
        self.mainwindow.mainloop()

    def take_picture(self, event=None):

        ret, frame = self.vid.get_frame()
        resized = cv2.resize(frame, (self.camera_canvas.winfo_width(), self.camera_canvas.winfo_height()), interpolation=cv2.INTER_AREA)
        if ret:
            cv2.imwrite(os.path.join(self.folder_selected ,(contact_num + ".jpg")), cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))

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


if __name__ == "__main__":
    app = CameraApp()
    app.run()
