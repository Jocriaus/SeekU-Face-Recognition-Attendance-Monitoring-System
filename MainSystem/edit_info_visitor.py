#!/usr/bin/python3
import tkinter as tk
import query as qry
import PIL.Image, PIL.ImageTk
import os
import sys

class EditVisitorApp:
    def __init__(self,vn,vfn,vln,vcn,vad,vs, videosource, admin_app, file_path):
        # build ui
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.video_source = videosource
        self.admin_home_window = admin_app
        self.img_path = file_path
        self.visitor_number = vn
        self.visitor_firstname = vfn
        self.visitor_lastname = vln
        self.visitor_contact_number = vcn
        self.visitor_address = vad
        self.visitor_status = vs
        self.sql_query = qry.dbQueries()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.edit_visitor_app = tk.Toplevel()
        self.edit_visitor_app.configure(
            background="#F7FAE9", height=200, width=200
        )
        width = self.edit_visitor_app.winfo_screenwidth()
        height = self.edit_visitor_app.winfo_screenheight()
        self.edit_visitor_app.geometry("%dx%d" % (width, height))
        self.edit_visitor_app.resizable(False, False)
        self.edit_visitor_app.title("SeekU - Admin Edit Visitor")
        self.edit_visitor_app.iconbitmap(".\SeekU\SeekU.ico")
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        self.edit_visitor_frame4 = tk.Frame(self.edit_visitor_app)
        self.edit_visitor_frame4.configure(background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.edit_visitor_frame4)
        self.camera_canvas.configure(
            background="#0072bc", highlightbackground="#0072bc"
        )
        self.camera_canvas.place(
            anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, x=0, y=0
        )
        self.camera_canvas.bind("<1>", self.change_pic, add="")
        self.edit_visitor_frame4.place(
            anchor="center", relheight=0.50, relwidth=0.50, relx=0.65, rely=0.47
        )
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        self.edit_visitor_frame3 = tk.Frame(self.edit_visitor_app)
        self.edit_visitor_frame3.configure(background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.edit_visitor_frame3)
        self.img_SeekULogotypesmall = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype small.png"
        )
        self.app_name_logo.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#0072bc",
            image=self.img_SeekULogotypesmall,
            justify="left",
            text="SEEK",
        )
        self.app_name_logo.place(anchor="center", relx=0.60, rely=0.5)
        self.app_logo_label = tk.Label(self.edit_visitor_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9", image=self.img_SeekUlarge, text="label1"
        )
        self.app_logo_label.place(anchor="center", relx=0.32, rely=0.5)
        self.return_button = tk.Button(self.edit_visitor_frame3)
        self.return_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Return",
        )
        self.return_button.place(anchor="center", relx=0.935, rely=0.85, x=0, y=0)
        self.return_button.bind("<1>", self.return_func, add="")
        self.edit_visitor_frame3.place(
            anchor="center", relheight=0.25, relwidth=0.61, relx=0.65, rely=0.85
        )
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        # Contains-edit-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        self.edit_visitor_frame2 = tk.Frame(self.edit_visitor_app)
        self.edit_visitor_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.edit_visitor_label = tk.Label(self.edit_visitor_frame2)
        self.edit_visitor_label.configure(
            background="#F7FAE9", font="{arial} 28 {bold}", text="Edit Visitor"
        )
        self.edit_visitor_label.place(anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.first_name_label = tk.Label(self.edit_visitor_frame2)
        self.first_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="First Name",
        )
        self.first_name_label.place(anchor="center", relx=0.32, rely=0.125, x=0, y=0)
        self.first_name_entry = tk.Entry(self.edit_visitor_frame2)
        self.first_name_entry.configure(font="{arial} 20 {}")
        self.first_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.165, x=0, y=0
        )
        self.last_name_label = tk.Label(self.edit_visitor_frame2)
        self.last_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Last Name",
        )
        self.last_name_label.place(anchor="center", relx=0.32, rely=0.22, x=0, y=0)
        self.last_name_entry = tk.Entry(self.edit_visitor_frame2)
        self.last_name_entry.configure(font="{arial} 20 {}")
        self.last_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.26, x=0, y=0
        )

        self.contact_num_label = tk.Label(self.edit_visitor_frame2)
        self.contact_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Contact No.",
        )
        self.contact_num_label.place(anchor="center", relx=0.33, rely=0.315, x=0, y=0)
        self.contact_num_entry = tk.Entry(self.edit_visitor_frame2)
        self.contact_num_entry.configure(font="{arial} 20 {}")
        self.contact_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.355, x=0, y=0
        )
        self.address_label = tk.Label(self.edit_visitor_frame2)
        self.address_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Address",
        )
        self.address_label.place(anchor="center", relx=0.295, rely=0.41, x=0, y=0)
        self.address_entry = tk.Entry(self.edit_visitor_frame2)
        self.address_entry.configure(font="{arial} 20 {}")
        self.address_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.45, x=0, y=0
        )
        self.user_status_label = tk.Label(self.edit_visitor_frame2)
        self.user_status_label.configure(
            background="#F7FAE9", font="{arial} 20 {bold}", text="Visitor Status"
        )
        self.user_status_label.place(anchor="center", relx=0.370, rely=0.49, x=0, y=0)
                # variable for the radiobuttons, to connect them
        self.stat_var = tk.StringVar()
        self.stat_var.set(self.visitor_status)
        self.active_radiobutton = tk.Radiobutton(self.edit_visitor_frame2)
        self.active_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 18 {}",
            text="Active",
            variable=self.stat_var,
            value="IsActive",
        )
        self.active_radiobutton.place(anchor="center", relx=0.4, rely=0.535, x=0, y=0)
        self.inactive_radiobutton = tk.Radiobutton(self.edit_visitor_frame2)
        self.inactive_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 18 {}",
            text="Archive",
            variable=self.stat_var,
            value="IsArchived",
        )
        self.inactive_radiobutton.place(anchor="center", relx=0.6, rely=0.575, x=0, y=0)
        self.save_changes_button = tk.Button(self.edit_visitor_frame2)
        self.save_changes_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Save",
        )
        self.save_changes_button.place(anchor="center", relx=0.70, rely=0.92, x=0, y=0)
        self.save_changes_button.bind("<1>", self.save_visitor, add="")
        self.edit_changes_button = tk.Button(self.edit_visitor_frame2)
        self.edit_changes_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Edit",
        )
        self.edit_changes_button.place(anchor="center", relx=0.30, rely=0.92, x=0, y=0)
        self.edit_changes_button.bind("<1>", self.edit_visitor, add="")
        self.edit_visitor_frame2.place(
            anchor="center", relheight=0.86, relwidth=0.35, relx=0.18, rely=0.565
        )
        # Contains-edit-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.edit_visitor_frame1 = tk.Frame(self.edit_visitor_app)
        self.edit_visitor_frame1.configure(background="#fff000", height=200, width=200)
        self.school_logo_label = tk.Label(self.edit_visitor_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text="label1",
        )
        self.school_logo_label.place(anchor="center", relx=0.25, rely=0.5)
        self.edit_visitor_frame1.place(
            anchor="center", relheight=0.13, relwidth=1.0, relx=0.5, rely=0.065
        )
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        # see the function for description
        self.disp_pic()
        # Main widget
        self.mainwindow = self.edit_visitor_app
        self.mainwindow.attributes("-topmost", True)
        # this protocol will do a function after pressing the close button.
        self.mainwindow.wm_attributes("-fullscreen", "True")
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)


    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit() 

    # this function will destroy the current window and return to camera app
    def back_cam_app_window(self):
        self.admin_home_window.deiconify()
        self.edit_visitor_app.destroy()

    # enables entry widgets
    def disable_entry(self):
        self.address_entry.configure(state="disabled")
        self.last_name_entry.configure(state="disabled")
        self.first_name_entry.configure(state="disabled")
        self.contact_num_entry.configure(state="disabled")


    # enables entry widgets
    def enable_entry(self):
        self.address_entry.configure(state="normal")
        self.last_name_entry.configure(state="normal")
        self.first_name_entry.configure(state="normal")
        self.contact_num_entry.configure(state="normal")

    def select_student(self):
        self.first_name_entry.insert(0, self.visitor_firstname)
        self.last_name_entry.insert(0, self.visitor_lastname)
        self.contact_num_entry.insert(0, self.visitor_contact_number)
        self.address_entry.insert(0, self.visitor_address)


    def save_visitor_function(self):
        # putting the values into variables to save into the database.
        # create a data for the user then get the PK for the name of the image
        # save the PK to a variable then use it for the  saving of image
        """
        Database Connection
        """
        self.last_name_var = self.last_name_entry.get()
        self.first_name_var = self.first_name_entry.get()
        self.contact_num_var = self.contact_num_entry.get()
        self.address_var = self.address_entry.get()
        self.visitor_status_var = self.stat_var

        self.sql_query.update_visitor(
            self.first_name_var, 
            self.last_name_var,
            self.contact_num_var, 
            self.address_var,
            self.visitor_status_var,
            self.visitor_number,
        )

        if os.path.exists(self.img_path + "/temp.jpg"):
            img_name = self.visitor_number
            os.rename(self.img_path+"/" +img_name+ ".jpg",self.img_path + "/temp.jpg")
        """
        Save to database
        Get the primary key
        rename img to primary key use os.rename()
        """

        # this function will display the image into the canvas
    def disp_pic(self):
        self.load_image = PIL.Image.open(self.img_path + "/temp.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.visitor_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.visitor_image, anchor=tk.NW)

    def disp_temp_pic(self):
        self.load_image = PIL.Image.open(self.img_path +"/temp.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.visitor_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.visitor_image, anchor=tk.NW)



    def edit_visitor(self, event=None):
        # enables and disables the entry and optionmenu
        if self.edit_bool == True:
            self.enable_entry()
            self.edit_bool = False
        elif self.edit_bool == False:
            self.disable_entry()
            self.edit_bool = True


    def save_visitor(self, event=None):
        self.save_visitor_function()
        # save infos

    # this command will open the camera app
    def change_pic(self, event=None):
        self.back_cam_app_window()

    def return_func(self, event=None):
        self.back_cam_app_window()
        if os.path.exists(self.img_path + "/temp.jpg"):
            os.remove(self.img_path + "/temp.jpg")

