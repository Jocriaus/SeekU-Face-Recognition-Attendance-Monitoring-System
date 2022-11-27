#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import snapshot as ss
import main_function as mf



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
        self.fr_vid = mf.facerecogApp()
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
        
        self.camera_canvas = tk.Canvas(self.right_frame, width = self.fr_vid.width, height = self.fr_vid.height)
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
        ss.snapApp()


if __name__ == "__main__":
    app = FaceRecognitionUI()
    app.run()
