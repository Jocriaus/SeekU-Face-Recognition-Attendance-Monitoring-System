#!/usr/bin/python3
import tkinter as tk
import query_mod as qry
import tkinter.messagebox as messbx
import PIL.Image, PIL.ImageTk
import os
import sys
import re


class RegisterVisitorApp:
    def __init__(self, home_mod, cam_app, file_path):
        # build ui
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.client_cam_app = cam_app
        self.home_window = home_mod
        self.img_path = file_path
        self.sql_query = qry.dbQueries()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.register_visitor_app = tk.Toplevel()
        self.register_visitor_app.configure(background="#F7FAE9", height=200, width=200)
        width = self.register_visitor_app.winfo_screenwidth()
        height = self.register_visitor_app.winfo_screenheight()
        self.register_visitor_app.geometry("%dx%d" % (width, height))
        self.register_visitor_app.resizable(False, False)
        self.register_visitor_app.title("SeekU - Admin Register Visitor")
        self.register_visitor_app.iconbitmap(".\SeekU\SeekU.ico")
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        self.register_visitor_frame4 = tk.Frame(self.register_visitor_app)
        self.register_visitor_frame4.configure(
            background="#0072bc", height=200, width=200
        )
        self.camera_canvas = tk.Canvas(self.register_visitor_frame4)
        self.camera_canvas.configure(
            background="#0072bc", highlightbackground="#0072bc"
        )
        self.camera_canvas.place(
            anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, x=0, y=0
        )
        self.camera_canvas.bind("<1>", self.change_pic, add="")
        self.register_visitor_frame4.place(
            anchor="center", relheight=0.50, relwidth=0.50, relx=0.65, rely=0.47
        )
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        self.register_visitor_frame3 = tk.Frame(self.register_visitor_app)
        self.register_visitor_frame3.configure(
            background="#F7FAE9", height=200, width=200
        )
        self.app_name_logo = tk.Label(self.register_visitor_frame3)
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
        self.app_logo_label = tk.Label(self.register_visitor_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9", image=self.img_SeekUlarge, text="label1"
        )
        self.app_logo_label.place(anchor="center", relx=0.32, rely=0.5)
        self.return_button = tk.Button(self.register_visitor_frame3)
        self.return_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Return",
        )
        self.return_button.place(anchor="center", relx=0.935, rely=0.85, x=0, y=0)
        self.return_button.bind("<1>", self.return_func, add="")
        self.register_visitor_frame3.place(
            anchor="center", relheight=0.25, relwidth=0.61, relx=0.65, rely=0.85
        )
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        self.register_visitor_frame2 = tk.Frame(self.register_visitor_app)
        self.register_visitor_frame2.configure(
            background="#F7FAE9", height=200, width=200
        )
        self.register_visitor_label = tk.Label(self.register_visitor_frame2)
        self.register_visitor_label.configure(
            background="#F7FAE9", font="{arial} 28 {bold}", text="Register Visitor"
        )
        self.register_visitor_label.place(
            anchor="center", relx=0.5, rely=0.05, x=0, y=0
        )
        self.first_name_label = tk.Label(self.register_visitor_frame2)
        self.first_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="First Name",
        )
        self.first_name_label.place(anchor="center", relx=0.32, rely=0.125, x=0, y=0)
        self.first_name_entry = tk.Entry(self.register_visitor_frame2)
        self.first_name_entry.configure(font="{arial} 20 {}")
        self.first_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.165, x=0, y=0
        )
        self.last_name_label = tk.Label(self.register_visitor_frame2)
        self.last_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Last Name",
        )
        self.last_name_label.place(anchor="center", relx=0.32, rely=0.22, x=0, y=0)
        self.last_name_entry = tk.Entry(self.register_visitor_frame2)
        self.last_name_entry.configure(font="{arial} 20 {}")
        self.last_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.26, x=0, y=0
        )

        self.contact_num_label = tk.Label(self.register_visitor_frame2)
        self.contact_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Contact No.",
        )
        self.contact_num_label.place(anchor="center", relx=0.33, rely=0.315, x=0, y=0)
        self.contact_num_entry = tk.Entry(self.register_visitor_frame2)
        self.contact_num_entry.configure(font="{arial} 20 {}")
        self.contact_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.355, x=0, y=0
        )
        self.address_label = tk.Label(self.register_visitor_frame2)
        self.address_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Address",
        )
        self.address_label.place(anchor="center", relx=0.295, rely=0.41, x=0, y=0)
        self.address_entry = tk.Entry(self.register_visitor_frame2)
        self.address_entry.configure(font="{arial} 20 {}")
        self.address_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.45, x=0, y=0
        )
        self.register_button = tk.Button(self.register_visitor_frame2)
        self.register_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Register",
        )
        self.register_button.place(anchor="center", relx=0.5, rely=0.92, x=0, y=0)
        self.register_button.bind("<1>", self.register_visitor, add="")
        self.register_visitor_frame2.place(
            anchor="center", relheight=0.86, relwidth=0.35, relx=0.18, rely=0.565
        )
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.register_visitor_frame1 = tk.Frame(self.register_visitor_app)
        self.register_visitor_frame1.configure(
            background="#fff000", height=200, width=200
        )
        self.school_logo_label = tk.Label(self.register_visitor_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text="label1",
        )
        self.school_logo_label.place(anchor="center", relx=0.25, rely=0.5)
        self.register_visitor_frame1.place(
            anchor="center", relheight=0.13, relwidth=1.0, relx=0.5, rely=0.065
        )
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        # see the function for description
        self.disp_pic()
        # Main widget
        self.mainwindow = self.register_visitor_app
        self.mainwindow.wm_attributes("-fullscreen", "True")
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)

    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    # this function will destroy the current window and return to camera app
    def back_cam_app_window(self):
        self.client_cam_app.deiconify()
        self.register_visitor_app.destroy()

    def register_visitor_function(self):
        # putting the values into variables to save into the database.
        # create a data for the user then get the PK for the name of the image
        # save the PK to a variable then use it for the  saving of image
        """
        Database Connection
        """

        last_name_var = self.last_name_entry.get()
        first_name_var = self.first_name_entry.get()
        contact_num_var = self.contact_num_entry.get()
        address_var = self.address_entry.get()
        if (
            len(last_name_var) != 0
            and len(first_name_var) != 0
            and len(contact_num_var) != 0
            and len(address_var) != 0
        ):
            input_values = [
                first_name_var,
                last_name_var,
                contact_num_var,
                address_var,
            ]
            concatenated_inputs = "".join(input_values)
            pattern = re.compile("[^a-zA-Z0-9 \-@.,]")

            if not pattern.search(concatenated_inputs):
                self.sql_query.register_visitor(
                    first_name_var,
                    last_name_var,
                    contact_num_var,
                    address_var,
                )
                img_name = self.sql_query.capture_visitor_image(
                    first_name_var, last_name_var, contact_num_var, address_var
                )
                os.rename(
                    self.img_path + "/000000000.jpg",
                    self.img_path + "/" + str(img_name[0]) + ".jpg",
                )
                messbx.showinfo(
                    "Success",
                    "The visitor record has been registered successfully.",
                )
            else:
                messbx.showwarning("Warning", "The input contains special characters.")
        else:
            messbx.showwarning(
                "Warning", "Kindly ensure all fields are filled by entering a value."
            )

        """
        Save to database
        Get the primary key
        rename img to primary key use os.rename()
        """

        # this function will display the image into the canvas

    def disp_pic(self):
        self.load_image = PIL.Image.open(self.img_path + "/000000000.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)

    def register_visitor(self, event=None):
        self.register_visitor_function()

    # this command will open the camera app
    def change_pic(self, event=None):
        self.back_cam_app_window()

    def return_func(self, event=None):
        self.back_cam_app_window()
        if os.path.exists(self.img_path + "/000000000.jpg"):
            os.remove(self.img_path + "/000000000.jpg")
