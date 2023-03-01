import tkinter as tk
from tkinter import filedialog
import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import os


class AddVisitorApp:
    def __init__(self, vid_source, login_mod, sel_cam, home_mod, cam_app, file_path):

        #assignment for passed parameters
        self.client_cam_app = cam_app
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.home_window = home_mod
        self.img_path = file_path
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
            rely=.5,)
        self.camera_canvas.bind("<ButtonPress>", self.change_pic, add="")
        self.add_visitor_frame3.place(
            anchor="center",
            relx=0.68,
            rely=0.36,
            height=480,
            width=854)

#-----------------------------------------------------------------------------------------
        self.add_visitor_frame2 = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.add_visitor_frame2)
        self.img_SeekULogotypesmall = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype medium.png")
        self.app_name_logo.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#0072bc",
            image=self.img_SeekULogotypesmall,
            justify="left",
            text='SEEK')
        self.app_name_logo.place(anchor="center", relx=0.70, rely=.5)
        self.app_logo_label = tk.Label(self.add_visitor_frame2)
        self.img_SeekUmedium = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUmedium,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.47, rely=0.50)
        self.log_out_button = tk.Button(self.add_visitor_frame2)
        self.log_out_button.configure(
            font="{arial black} 20 {}",
            foreground="#0072bc",
            text='Return')
        self.log_out_button.place(
            anchor="center",
            relheight=0.15,
            relwidth=0.1,
            relx=0.93,
            rely=0.85)
        self.log_out_button.bind("<ButtonPress>", self.log_out_func, add="")
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
        self.save_info_button = tk.Button(self.add_visitor_frame)
        self.save_info_button.configure(
            font="{arial black} 30 {}",
            foreground="#0072bc",
            text='Save')
        self.save_info_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.50,
            relx=.5,
            rely=.90)
        self.save_info_button.bind("<ButtonPress>", self.save_func, add="")
        self.school_logo_label = tk.Label(self.add_visitor_frame)
        self.img_STICollegeBalagtasLogo = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo large.png")
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

        self.disp_pic()
        # Main widget
        self.mainwindow = self.add_visitor_app
        self.mainwindow.attributes('-topmost', True)
        self.mainwindow.wm_attributes('-fullscreen', 'True', )

#-----------------------------------------------------------------------------------------
    def show_cam_app_win(self):
        self.client_cam_app.deiconify()
        self.add_visitor_app.destroy()

    def show_home_window(self):
        self.home_window.deiconify()
        self.add_visitor_app.destroy()


    def disp_pic(self):
        self.load_image = PIL.Image.open(self.img_path + "/temp.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image. ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image = self.student_image, anchor = tk.NW)
    
    def save_info(self):
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
        """
        Save to database
        Get the primary key
        rename img to primary key use os.rename()
        """
    

    def change_pic(self, event=None):
        self.show_cam_app_win()
        self.add_visitor_app.destroy()

    def log_out_func(self, event=None):
        self.show_cam_app_win()
        self.add_visitor_app.destroy()


    def save_func(self, event=None):
        self.save_info()