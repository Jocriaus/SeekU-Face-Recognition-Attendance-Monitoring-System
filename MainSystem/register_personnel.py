#!/usr/bin/python3
import tkinter as tk
import query_mod as qry
import tkinter.messagebox as messbx
import PIL.Image, PIL.ImageTk
import face_recognition
import os
import sys
import re


class RegisterPersonnelApp:
    def __init__(self, cam_app, admin_hom, file_path, saveonly, refresh, condition):
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.select_cam_window = cam_app
        self.admin_home_window = admin_hom
        self.img_path = file_path
        self.sql_query = qry.dbQueries()
        self.saveonly = saveonly
        self.refresh_func =refresh
        self.window_will_open= condition
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.register_personnel_app = tk.Toplevel()
        self.register_personnel_app.configure(
            background="#F7FAE9", height=200, width=200
        )
        width = self.register_personnel_app.winfo_screenwidth()
        height = self.register_personnel_app.winfo_screenheight()
        self.register_personnel_app.geometry("%dx%d" % (width, height))
        self.register_personnel_app.resizable(False, False)
        self.register_personnel_app.title("SeekU - Admin Register Personnel")
        self.register_personnel_app.iconbitmap(".\SeekU\SeekU.ico")
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        self.register_pers_frame4 = tk.Frame(self.register_personnel_app)
        self.register_pers_frame4.configure(background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.register_pers_frame4)
        self.camera_canvas.configure(
            background="#0072bc", highlightbackground="#0072bc"
        )
        self.camera_canvas.place(
            anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, x=0, y=0
        )
        self.camera_canvas.bind("<1>", self.change_pic, add="")
        self.register_pers_frame4.place(
            anchor="center", relheight=0.50, relwidth=0.50, relx=0.65, rely=0.47
        )
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        self.register_pers_frame3 = tk.Frame(self.register_personnel_app)
        self.register_pers_frame3.configure(background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.register_pers_frame3)
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
        self.app_logo_label = tk.Label(self.register_pers_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9", image=self.img_SeekUlarge, text="label1"
        )
        self.app_logo_label.place(anchor="center", relx=0.32, rely=0.5)
        self.return_button = tk.Button(self.register_pers_frame3)
        self.return_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Return",
        )
        self.return_button.place(anchor="center", relx=0.935, rely=0.85, x=0, y=0)
        self.return_button.bind("<1>", self.return_func, add="")
        self.register_pers_frame3.place(
            anchor="center", relheight=0.25, relwidth=0.61, relx=0.65, rely=0.85
        )
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        self.register_pers_frame2 = tk.Frame(self.register_personnel_app)
        self.register_pers_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.register_pers_label = tk.Label(self.register_pers_frame2)
        self.register_pers_label.configure(
            background="#F7FAE9", font="{arial} 28 {bold}", text="Register Personnel"
        )
        self.register_pers_label.place(anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.personnel_num_label = tk.Label(self.register_pers_frame2)
        self.personnel_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Personnel No.",
        )
        self.personnel_num_label.place(anchor="center", relx=0.36, rely=0.125, x=0, y=0)
        self.personnel_num_entry = tk.Entry(self.register_pers_frame2)
        self.personnel_num_entry.configure(font="{arial} 20 {}")
        self.personnel_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.165, x=0, y=0
        )
        self.first_name_label = tk.Label(self.register_pers_frame2)
        self.first_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="First Name",
        )
        self.first_name_label.place(anchor="center", relx=0.32, rely=0.22, x=0, y=0)
        self.first_name_entry = tk.Entry(self.register_pers_frame2)
        self.first_name_entry.configure(font="{arial} 20 {}")
        self.first_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.26, x=0, y=0
        )
        self.mid_name_label = tk.Label(self.register_pers_frame2)
        self.mid_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Middle Name",
        )
        self.mid_name_label.place(anchor="center", relx=0.345, rely=0.315, x=0, y=0)
        self.mid_name_entry = tk.Entry(self.register_pers_frame2)
        self.mid_name_entry.configure(font="{arial} 20 {}")
        self.mid_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.355, x=0, y=0
        )
        self.last_name_label = tk.Label(self.register_pers_frame2)
        self.last_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Last Name",
        )
        self.last_name_label.place(anchor="center", relx=0.32, rely=0.41, x=0, y=0)
        self.last_name_entry = tk.Entry(self.register_pers_frame2)
        self.last_name_entry.configure(font="{arial} 20 {}")
        self.last_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.45, x=0, y=0
        )
        self.personnel_type_label = tk.Label(self.register_pers_frame2)
        self.personnel_type_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Personnel Type",
        )
        self.personnel_type_label.place(
            anchor="center", relx=0.38, rely=0.505, x=0, y=0
        )

        self.contact_num_label = tk.Label(self.register_pers_frame2)
        self.contact_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Contact No.",
        )
        self.contact_num_label.place(anchor="center", relx=0.33, rely=0.6, x=0, y=0)

        # option menu
        self.personnel_type_entry = tk.StringVar(value="Professor")
        __values = ["Professor", "Non-Teaching Personnel"]
        self.personnel_optionmenu = tk.OptionMenu(
            self.register_pers_frame2, self.personnel_type_entry, *__values
        )
        self.personnel_optionmenu.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.555, x=0, y=0
        )
        self.personnel_optionmenu.configure(font="{arial} 16", justify="left")
        self.personnel_options = self.register_personnel_app.nametowidget(
            self.personnel_optionmenu.menuname
        )
        self.personnel_options.config(font="{arial} 16")

        self.contact_num_entry = tk.Entry(self.register_pers_frame2)
        self.contact_num_entry.configure(font="{arial} 20 {}")
        self.contact_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.64, x=0, y=0
        )
        self.address_label = tk.Label(self.register_pers_frame2)
        self.address_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Address",
        )
        self.address_label.place(anchor="center", relx=0.295, rely=0.695, x=0, y=0)
        self.address_entry = tk.Entry(self.register_pers_frame2)
        self.address_entry.configure(font="{arial} 20 {}")
        self.address_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.735, x=0, y=0
        )
        self.register_button = tk.Button(self.register_pers_frame2)
        self.register_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Register",
        )
        self.register_button.place(anchor="center", relx=0.5, rely=0.92, x=0, y=0)
        self.register_button.bind("<1>", self.register_personnel, add="")
        self.register_pers_frame2.place(
            anchor="center", relheight=0.86, relwidth=0.35, relx=0.18, rely=0.565
        )
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.register_pers_frame1 = tk.Frame(self.register_personnel_app)
        self.register_pers_frame1.configure(background="#FFF875", height=200, width=200)
        self.school_logo_label = tk.Label(self.register_pers_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background="#FFF875",
            image=self.img_STICollegeBalagtasLogomedium,
            text="label1",
        )
        self.school_logo_label.place(anchor="center", relx=0.25, rely=0.5)
        self.register_pers_frame1.place(
            anchor="center", relheight=0.13, relwidth=1.0, relx=0.5, rely=0.065
        )
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        # see the function for description
        if not self.saveonly:
            self.disp_pic()
        # Main widget
        self.mainwindow = self.register_personnel_app
        self.mainwindow.wm_attributes("-fullscreen", "True")
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)

    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    # this function will destroy the current window and return to camera app
    def back_cam_app_window(self):
        if self.saveonly:
            self.refresh_func(self.window_will_open, "IsActive" )
            self.admin_home_window.deiconify()
            self.select_cam_window.deiconify()
            self.select_cam_window.grab_set()
            self.register_personnel_app.destroy()
        else:
            self.select_cam_window.deiconify()
            self.register_personnel_app.destroy()

    def register_personnel_function(self):
        register = True
        personnel_num_var = self.personnel_num_entry.get()
        register = self.client_no_check(personnel_num_var)
        first_name_var = self.first_name_entry.get()
        mid_name_var = self.mid_name_entry.get()
        last_name_var = self.last_name_entry.get()
        contact_num_var = self.contact_num_entry.get()
        personnel_type_var = self.personnel_type_entry.get()
        address_var = self.address_entry.get()

        if self.sql_query.check_student_no(personnel_num_var) == True:
            messbx.showwarning("Warning", "Personnel number already exists.")
        else:
            if (
                len(personnel_num_var) != 0
                and len(first_name_var) != 0
                and len(last_name_var) != 0
                and len(contact_num_var) != 0
                and len(personnel_type_var) != 0
                and len(address_var) != 0
            ):
                input_values = [
                    personnel_num_var,
                    first_name_var,
                    last_name_var,
                    mid_name_var,
                    contact_num_var,
                    address_var,
                ]
                concatenated_inputs = "".join(input_values)
                pattern = re.compile("[^a-zA-Z0-9 ñÑ]")

                if not pattern.search(concatenated_inputs):
                    if personnel_num_var.isdigit() or (
                        personnel_num_var.startswith("-")
                        and personnel_num_var[1:].isdigit()
                    ):
                        if ((contact_num_var.isdigit() or
                            contact_num_var.startswith("-")
                            and contact_num_var[1:].isdigit())
                            and len(contact_num_var) == 11
                        ):
                            if (
                                first_name_var.replace(" ", "").isalpha()
                                and ((not mid_name_var.isdigit()) or (mid_name_var.startswith("-") )
                                     and mid_name_var[1:].isdigit()) 
                                and last_name_var.replace(" ", "").isalpha()
                            ):
                                if register == True:
                                    img_name = personnel_num_var
                                    path_check = self.img_path + "/000000000.jpg"
                                    if self.saveonly and (not os.path.exists(path_check)):
                                        path_check = self.img_path + "/" + img_name + ".jpg"
                                        if os.path.exists(path_check):
                                            result = messbx.askokcancel(
                                                "Confirm Action",
                                                "Please review all the details you have inputted. Are you sure everything is final and correct?",
                                            )
                                            if result:
                                                path_check = self.img_path + "/" + img_name + ".jpg"
                                                image = face_recognition.load_image_file(path_check)
                                                face_locations = (
                                                    face_recognition.face_locations(image))

                                                if face_locations:
                                                    # User clicked OK
                                                    self.sql_query.register_personnel(
                                                        personnel_num_var,
                                                        first_name_var,
                                                        last_name_var,
                                                        mid_name_var,
                                                        contact_num_var,
                                                        address_var,
                                                        personnel_type_var,
                                                        
                                                    )
                                                    self.register_button.configure(state="disabled")
                                                    messbx.showinfo(
                                                        "Success",
                                                        "The personnel's record has been registered successfully.",
                                                    )
                                                else:
                                                    messbx.showerror(
                                                        "Error",
                                                        "Face detection failed. There are no face detected on the image.",
                                                    )
                                        else:
                                            messbx.showwarning(
                                            "Warning",
                                            "No image was found in the directory matching the entered client number.")
                                    elif (not self.saveonly) and (
                                        os.path.exists(path_check)
                                    ):
                                        result = messbx.askokcancel(
                                            "Confirm Action",
                                            "Please review all the details you have inputted. Are you sure everything is final and correct?",
                                        )
                                        if result:
                                            os.rename(path_check, self.img_path + "/" + img_name + ".jpg")
                                            self.sql_query.register_personnel(
                                                personnel_num_var,
                                                first_name_var,
                                                last_name_var,
                                                mid_name_var,
                                                contact_num_var,
                                                address_var,
                                                personnel_type_var,
                                            )
                                            messbx.showinfo(
                                                "Success",
                                                "The personnel's record has been registered successfully.",
                                            )
                                            self.register_button.configure(state="disabled")
                                    else:
                                        messbx.showwarning(
                                            "Warning",
                                            "No image was found in the directory matching the entered client number.",
                                        )
                            else:
                                messbx.showwarning(
                                    "Warning",
                                    "There is an invalid character in the input for the name of the personnel.",
                                )
                        else:
                            messbx.showwarning(
                                "Warning",
                                "The provided input for the contact number is "
                                + "invalid and does not correspond to a valid number.",
                            )
                    else:
                        messbx.showwarning(
                            "Warning",
                            "The provided input for the personnel number is "
                            + "invalid and does not correspond to a valid number.",
                        )
                else:
                    messbx.showwarning(
                        "Warning", "The input contains special characters."
                    )
            else:
                messbx.showwarning(
                    "Warning",
                    "Kindly ensure all fields are filled by entering a value.",
                )

    def client_no_check(self, client_no):
        if self.sql_query.check_username(client_no):
            messbx.showwarning(
                "Warning",
                "The personnel number "
                + client_no
                + " has already been assigned/taken.",
            )
            register = False
            return register
        else:
            register = True
            return register

        # this function will display the image into the canvas

    def disp_pic(self):
        self.load_image = PIL.Image.open(self.img_path + "/000000000.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)

    def register_personnel(self, event=None):
        self.register_personnel_function()

    # this command will open the camera app
    def change_pic(self, event=None):
        self.back_cam_app_window()

    def return_func(self, event=None):
        self.back_cam_app_window()
        if os.path.exists(self.img_path + "/000000000.jpg"):
            os.remove(self.img_path + "/000000000.jpg")
