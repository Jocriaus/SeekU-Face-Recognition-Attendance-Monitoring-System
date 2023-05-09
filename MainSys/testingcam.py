
import cv2
import tkinter as tk

class CameraSelector:
    def __init__(self, master):
        self.master = master
        self.cam_var = tk.IntVar()
        
        # Get all accessible cameras on the system
        self.cams = []
        index = 0
        while True:
            cam = cv2.VideoCapture(index)
            if not cam.isOpened():
                break
            self.cams.append(cam)
            index += 1
        
        # Create radio buttons for each camera
        for i, cam in enumerate(self.cams):
            cam_name = f"Camera {i+1}"
            cam_radiobutton = tk.Radiobutton(self.master)
            cam_radiobutton.configure(
                background="#0072bc",
                font="Arial 24",
                foreground="#F7FAE9",
                text=cam_name,
                selectcolor="black",
                variable=self.cam_var,
                value=i,
                command=self.check_selection)
            cam_radiobutton.place(anchor="center", relx=.5, rely=.42 + i*.1)
    
    def check_selection(self):
        cam_index = self.cam_var.get()
        cam = self.cams[cam_index]
        
        # Add canvas and video feed to display selected camera
        canvas = tk.Canvas(self.master, width=640, height=480)
        canvas.place(relx=0.5, rely=0.5, anchor="center")
        
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = cv2.createBitmap(frame)
            canvas.create_image(0, 0, image=photo, anchor="nw")
            self.master.update()
    
    def run(self):
        self.master.mainloop()

root = tk.Tk()
app = CameraSelector(root)
app.run()