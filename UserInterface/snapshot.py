from tkinter import filedialog
import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import os

class snapApp:
    def __init__(self, video_source=0):
        self.snapshot_app = tk.Toplevel()
        self.snapshot_app.title("Add Client")
        self.snapshot_app.configure(
            background="#0072bc")
        self.video_source = video_source

        # open video source
        self.vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(self.snapshot_app, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        
        #will be the file name
        self.input_text = tk.Text(self.snapshot_app)
        self.input_text.configure(
             bg = "#fff200",
             font="{Arial Black} 14 {}",
             height = 1, 
             width = 20
        )
        self.input_text.pack()

        #button for the folder selection
        self.folder_selection_button=tk.Button(self.snapshot_app, command=self.select_folder)
        self.folder_selection_button.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            text='Select Folder',
            width=20)
        self.folder_selection_button.pack(anchor=tk.S,pady=20, expand=True)

        # Button that lets the user take a snapshot
        self.snapshot_button=tk.Button(self.snapshot_app, command=self.snapshot)
        self.snapshot_button.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            text='Take a Picture',
            width=20)
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

