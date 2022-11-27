#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import cv2
import PIL.Image, PIL.ImageTk
import os


class FaceRecognitionUI:
    def __init__(self, master=None):
        # build ui
        self.system_app = tk.Tk() 
        self.system_app.configure(
            background="#0072bc",
            height=200,
            relief="flat",
            takefocus=True,
            width=200)
        self.system_app.geometry("1280x720")
        self.system_app.resizable(True, True)
        self.system_app.title("SeekU - Face Recognition Attendance System")
        self.main_frame = ttk.Frame(self.system_app)
        self.main_frame.configure(height=200, width=200)
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
            width=20)
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
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.configure(background="#0072bc", height=400, width=400)
        self.add_button = tk.Button(self.right_frame,)
        self.add_button.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            text='Add',
            width=20)
        self.add_button.grid(column=0, padx=5, pady=60, row=0, sticky="s")
        self.add_button.bind("<ButtonPress>", self.add_client, add="+")
        self.camera_canvas = tk.Canvas(self.right_frame)
        self.camera_canvas.configure(
            background="#0072bc",
            borderwidth=0,
            height=500,
            insertborderwidth=0,
            relief="flat",
            width=500)
        self.camera_canvas.grid(column=0, padx=5, pady=10, row=0)
        self.right_frame.pack(expand="true", fill="both", side="right")
        self.right_frame.grid_anchor("center")
        self.right_frame.rowconfigure(0, weight=1)
        self.right_frame.columnconfigure(0, weight=1)
        self.main_frame.pack(
            anchor="center",
            expand="true",
            fill="both",
            side="top")

        # Main widget
        self.mainwindow = self.system_app

    def run(self):
        self.mainwindow.mainloop()  

    def next_student(self, event=None):
        pass

    def reset_attendance(self, event=None):
        pass

    def add_client(self, event=None):
        snapApp()


class snapApp:
    def __init__(self, video_source=0):
        self.snapshot_app = tk.Toplevel()
        self.snapshot_app.title("Add Client")
        self.video_source = video_source

        # open video source
        self.vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(self.snapshot_app, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        
        #will be the file name
        self.input_text = tk.Text(self.snapshot_app,height = 2)
        self.input_text.pack()

        self.folder_selection_button=tk.Button(self.snapshot_app, text="Select Folder", width=50, command=self.select_folder)
        self.folder_selection_button.pack(anchor=tk.S, expand=True)

        # Button that lets the user take a snapshot
        self.snapshot_button=tk.Button(self.snapshot_app, text="Snap", width=50, command=self.snapshot)
        self.snapshot_button.pack(anchor=tk.S, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()


    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

        self.snapshot_app.after(self.delay, self.update)

    def select_folder(self):
        self.folder_selected = filedialog.askdirectory()

    def snapshot(self):
        # Get a frame from the video source
        student_number = self.input_text.get("1.0", "end-1c")
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite(os.path.join(self.folder_selected ,(student_number + ".jpg")), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        #setting the height and width of the camera
        #self.vid.set(cv2.CAP_PROP_FRAME_WIDTH,700)
        #self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
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
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)


if __name__ == "__main__":
    app = FaceRecognitionUI()
    app.run()
