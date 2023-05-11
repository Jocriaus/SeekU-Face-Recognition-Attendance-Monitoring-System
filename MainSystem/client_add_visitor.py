import tkinter as tk
import tkinter.messagebox as messbx
import tkinter as tk
import query_mod as qry
import PIL.Image, PIL.ImageTk
import os
import sys
import re


class AddVisitorApp:
    def __init__(self, home_mod, cam_app, file_path):

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.client_cam_app = cam_app
        self.home_window = home_mod
        self.img_path = file_path
        self.sql_query = qry.dbQueries()
        self.register = False
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        # build ui
        self.add_visitor_app = tk.Toplevel()
        self.add_visitor_app.configure(background="#F7FAE9", height=200, width=200)
        width = self.add_visitor_app.winfo_screenwidth()
        height = self.add_visitor_app.winfo_screenheight()
        self.add_visitor_app.geometry("%dx%d" % (width, height))
        self.add_visitor_app.resizable(False, False)
        self.add_visitor_app.title("SeekU - Client Add Visitor")
        self.add_visitor_app.iconbitmap(".\SeekU\SeekU.ico")

        # Contains-Camera-Canvas---------------------------------------------------------------------------------------------------
        self.add_visitor_frame3 = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame3.configure(background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.add_visitor_frame3)
        self.camera_canvas.configure(
            background="#0072bc", highlightbackground="#0072bc"
        )
        self.camera_canvas.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=0.5,
            rely=0.5,
        )
        self.camera_canvas.bind("<ButtonPress>", self.change_pic, add="")
        self.add_visitor_frame3.place(
            anchor="center", relx=0.68, rely=0.36, height=480, width=854
        )
        # Contains-Camera-Canvas---------------------------------------------------------------------------------------------------
        # Contains-the-returnbutton-logo-and-logotype---------------------------------------------------------------------------------------------------------
        self.add_visitor_frame2 = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.add_visitor_frame2)
        self.img_SeekULogotypesmall = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype medium.png"
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
        self.app_name_logo.place(anchor="center", relx=0.70, rely=0.5)
        self.app_logo_label = tk.Label(self.add_visitor_frame2)
        self.img_SeekUmedium = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9", image=self.img_SeekUmedium, text="label1"
        )
        self.app_logo_label.place(anchor="center", relx=0.47, rely=0.50)
        self.return_button = tk.Button(self.add_visitor_frame2)
        self.return_button.configure(
            font="{arial black} 20 {}", foreground="#0072bc", text="Return"
        )
        self.return_button.place(
            anchor="center", relheight=0.15, relwidth=0.1, relx=0.93, rely=0.85
        )
        self.return_button.bind("<ButtonPress>", self.return_func, add="")
        self.add_visitor_frame2.place(
            anchor="center", relheight=0.3, relwidth=1.0, relx=0.50, rely=0.85
        )
        # Contains-the-logo-and-logotype---------------------------------------------------------------------------------------------------------
        # Contains-save-info-button-and-diff-entry--------------------------------------------------------------------------------------------------------

        self.add_visitor_frame = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame.configure(background="#F7FAE9", height=200, width=200)
        self.save_info_button = tk.Button(self.add_visitor_frame)
        self.save_info_button.configure(
            font="{arial black} 30 {}",background="#0072bc", foreground="#F7FAE9", text="Register"
        )
        self.save_info_button.place(
            anchor="center", relheight=0.1, relwidth=0.50, relx=0.5, rely=0.90
        )
        self.save_info_button.bind("<ButtonPress>", self.save_func, add="")
        self.school_logo_label = tk.Label(self.add_visitor_frame)
        self.img_STICollegeBalagtasLogo = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo large.png"
        )
        self.school_logo_label.configure(
            background="#F7FAE9", image=self.img_STICollegeBalagtasLogo, text="label1"
        )
        self.school_logo_label.place(anchor="center", relx=0.5, rely=0.12)
        self.last_name_label = tk.Label(self.add_visitor_frame)
        self.last_name_label.configure(
            background="#F7FAE9", font="{arial} 36 {}", text="Last Name"
        )
        self.last_name_label.place(anchor="center", relx=0.34, rely=0.25, x=0, y=0)
        self.last_name_entry = tk.Entry(self.add_visitor_frame)
        self.last_name_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.last_name_entry.place(anchor="center", relx=0.55, rely=0.31, x=0, y=0)
        self.first_name_label = tk.Label(self.add_visitor_frame)
        self.first_name_label.configure(
            background="#F7FAE9", font="{arial} 36 {}", text="First Name"
        )
        self.first_name_label.place(anchor="center", relx=0.34, rely=0.40, x=0, y=0)
        self.first_name_entry = tk.Entry(self.add_visitor_frame)
        self.first_name_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.first_name_entry.place(anchor="center", relx=0.55, rely=0.46, x=0, y=0)
        self.contact_no_label = tk.Label(self.add_visitor_frame)
        self.contact_no_label.configure(
            background="#F7FAE9", font="{arial} 36 {}", text="Contact No."
        )
        self.contact_no_label.place(anchor="center", relx=0.36, rely=0.55, x=0, y=0)
        self.contact_no_entry = tk.Entry(self.add_visitor_frame)
        self.contact_no_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.contact_no_entry.place(anchor="center", relx=0.55, rely=0.61, x=0, y=0)
        self.address_label = tk.Label(self.add_visitor_frame)
        self.address_label.configure(
            background="#F7FAE9", font="{arial} 36 {}", text="Address"
        )
        self.address_label.place(anchor="center", relx=0.29, rely=0.70, x=0, y=0)
        self.address_entry = tk.Entry(self.add_visitor_frame)
        self.address_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.address_entry.place(anchor="center", relx=0.55, rely=0.76, x=0, y=0)
        self.add_visitor_frame.place(
            anchor="center", relheight=1.0, relwidth=0.35, relx=0.17, rely=0.5
        )
        # Contains-save-info-button-and-diff-entry--------------------------------------------------------------------------------------------------------
        # see the function for description
        self.disp_pic()
        # Main widget
        self.mainwindow = self.add_visitor_app
        # will set the window to fullscreen
        self.mainwindow.wm_attributes("-fullscreen", "True")
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)

    # -----------------------------------------------------------------------------------------
    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    # this will return to the camera app
    def show_cam_app_win(self):
        self.client_cam_app.deiconify()
        self.add_visitor_app.destroy()

    # this function will display the image into the canvas
    def disp_pic(self):
        self.load_image = PIL.Image.open(self.img_path + "/000000000.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)

    # this function will save the info to the database and rename the temp image
    def save_info(self):
        # putting the values into variables to save into the database.
        # create a data for the user then get the PK for the name of the image
        # save the PK to a variable then use it for the  saving of image
        """
        Database Connection
        """
        last_name_var = self.last_name_entry.get()
        first_name_var = self.first_name_entry.get()
        contact_num_var = self.contact_no_entry.get()
        address_var = self.address_entry.get()
        if not self.register:
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
                pattern = re.compile("[^a-zA-Z0-9 .,]")

                if not pattern.search(concatenated_inputs):
                    if  ((contact_num_var.isdigit() or 
                        contact_num_var.startswith("-") and contact_num_var[1:].isdigit() )and len(contact_num_var) == 11
                        ):
                        if (first_name_var.replace(" ", "").isalpha() and 
                            last_name_var.replace(" ", "").isalpha()
                            ):
                            result = messbx.askokcancel("Confirm Action", "Please review all the details you have inputted. Are you sure everything is final and correct?")
                            if result:
                                self.sql_query.register_visitor(
                                    first_name_var,
                                    last_name_var,
                                    contact_num_var,
                                    address_var,
                                )
                                img_name = self.sql_query.capture_visitor_image(
                                    first_name_var,
                                    last_name_var,
                                    contact_num_var,
                                    address_var,
                                )
                                os.rename(
                                    self.img_path + "/000000000.jpg",
                                    self.img_path + "/" + str(img_name[0]) + ".jpg",
                                )
                                self.register = True
                                messbx.showinfo(
                                    "Success",
                                    "The visitor's record has been successfully updated.",
                                )
                        else:
                            messbx.showwarning(
                                "Warning",
                                "There is an invalid character in the input for the name the visitor.",
                            )
                    else:
                        messbx.showwarning(
                            "Warning",
                            "The provided input for the contact number is "+
                            "invalid and does not correspond to a valid number.",
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

    # this command will open the camera app
    def change_pic(self, event=None):
        self.show_cam_app_win()
        self.add_visitor_app.destroy()

    # this command will return to the camera app
    def return_func(self, event=None):
        self.show_cam_app_win()
        self.add_visitor_app.destroy()

    # this command will save the info of the visitor
    def save_func(self, event=None):
        self.save_info()
