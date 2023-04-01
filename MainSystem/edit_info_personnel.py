#!/usr/bin/python3
import tkinter as tk
import Treeview_table as tbl
import query as qry
import admin_camera_app as aCA
import PIL.Image, PIL.ImageTk
import sys
import os

class EditPersonnelApp:
    def __init__(self, pn, pfn, pln, pm, pcn, pad, pt, vid_source, admin_win, img_path):

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.video_source = vid_source
        self.admin_home_window = admin_win
        self.img_path = img_path
        self.personnel_num = pn
        self.personnel_firstname = pfn
        self.personnel_lastname = pln
        self.personnel_middlename = pm
        self.personnel_contact_num = pcn
        self.personnel_address = pad
        self.personnel_type = pt
        self.treeview = tbl.TreeviewGUI()
        self.sql_query = qry.dbQueries()
        self.edit_bool = True
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        # build ui
        self.edit_personnel_app = tk.Toplevel()
        self.edit_personnel_app.configure(
            background="#F7FAE9", height=200, width=200
        )
        width = self.edit_personnel_app.winfo_screenwidth()
        height = self.edit_personnel_app.winfo_screenheight()
        self.edit_personnel_app.geometry("%dx%d" % (width, height))
        self.edit_personnel_app.resizable(False, False)
        self.edit_personnel_app.title("SeekU - Admin Edit Personnel Info")
        self.edit_personnel_app.iconbitmap(".\SeekU\SeekU.ico")
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        self.edit_pers_frame4 = tk.Frame(self.edit_personnel_app)
        self.edit_pers_frame4.configure(background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.edit_pers_frame4)
        self.camera_canvas.configure(
            background="#0072bc", highlightbackground="#0072bc"
        )
        self.camera_canvas.place(
            anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, x=0, y=0
        )
        self.edit_pers_frame4.place(
            anchor="center", relheight=0.50, relwidth=0.50, relx=0.65, rely=0.47
        )
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        self.edit_pers_frame3 = tk.Frame(self.edit_personnel_app)
        self.edit_pers_frame3.configure(background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.edit_pers_frame3)
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
        self.app_logo_label = tk.Label(self.edit_pers_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9", image=self.img_SeekUlarge, text="label1"
        )
        self.app_logo_label.place(anchor="center", relx=0.32, rely=0.5)
        self.return_button = tk.Button(self.edit_pers_frame3)
        self.return_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Return",
        )
        self.return_button.place(anchor="center", relx=0.935, rely=0.85, x=0, y=0)
        self.return_button.bind("<1>", self.return_func, add="")
        self.edit_pers_frame3.place(
            anchor="center", relheight=0.25, relwidth=0.61, relx=0.65, rely=0.85
        )
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        self.edit_pers_frame2 = tk.Frame(self.edit_personnel_app)
        self.edit_pers_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.register_pers_label = tk.Label(self.edit_pers_frame2)
        self.register_pers_label.configure(
            background="#F7FAE9", font="{arial} 28 {bold}", text="Edit Personnel"
        )
        self.register_pers_label.place(anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.personnel_num_label = tk.Label(self.edit_pers_frame2)
        self.personnel_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Personnel No.",
        )
        self.personnel_num_label.place(anchor="center", relx=0.36, rely=0.125, x=0, y=0)
        self.personnel_num_entry = tk.Entry(self.edit_pers_frame2)
        self.personnel_num_entry.configure(font="{arial} 20 {}")
        self.personnel_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.165, x=0, y=0
        )
        self.first_name_label = tk.Label(self.edit_pers_frame2)
        self.first_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="First Name",
        )
        self.first_name_label.place(anchor="center", relx=0.32, rely=0.22, x=0, y=0)
        self.first_name_entry = tk.Entry(self.edit_pers_frame2)
        self.first_name_entry.configure(font="{arial} 20 {}")
        self.first_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.26, x=0, y=0
        )
        self.mid_name_label = tk.Label(self.edit_pers_frame2)
        self.mid_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Middle Name",
        )
        self.mid_name_label.place(anchor="center", relx=0.345, rely=0.315, x=0, y=0)
        self.mid_name_entry = tk.Entry(self.edit_pers_frame2)
        self.mid_name_entry.configure(font="{arial} 20 {}")
        self.mid_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.355, x=0, y=0
        )
        self.last_name_label = tk.Label(self.edit_pers_frame2)
        self.last_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Last Name",
        )
        self.last_name_label.place(anchor="center", relx=0.32, rely=0.41, x=0, y=0)
        self.last_name_entry = tk.Entry(self.edit_pers_frame2)
        self.last_name_entry.configure(font="{arial} 20 {}")
        self.last_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.45, x=0, y=0
        )
        self.personnel_type_label = tk.Label(self.edit_pers_frame2)
        self.personnel_type_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Personnel Type",
        )
        self.personnel_type_label.place(
            anchor="center", relx=0.38, rely=0.505, x=0, y=0
        )

        self.contact_num_label = tk.Label(self.edit_pers_frame2)
        self.contact_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Contact No.",
        )
        self.contact_num_label.place(anchor="center", relx=0.33, rely=0.6, x=0, y=0)

        # option menu
        self.personnel_type_var = tk.StringVar(value="Choose Personnel Type")
        __values = ["Professor", "Non-Teaching Personnel"]
        self.personnel_optionmenu = tk.OptionMenu(
            self.edit_pers_frame2, self.personnel_type_var, *__values
        )
        self.personnel_optionmenu.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.555, x=0, y=0
        )
        self.personnel_optionmenu.configure(font="{arial} 16", justify="left")
        self.personnel_options = self.edit_personnel_app.nametowidget(
            self.personnel_optionmenu.menuname
        )
        self.personnel_options.config(font="{arial} 16")

        self.contact_num_entry = tk.Entry(self.edit_pers_frame2)
        self.contact_num_entry.configure(font="{arial} 20 {}")
        self.contact_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.64, x=0, y=0
        )
        self.address_label = tk.Label(self.edit_pers_frame2)
        self.address_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Address",
        )
        self.address_label.place(anchor="center", relx=0.295, rely=0.695, x=0, y=0)
        self.address_entry = tk.Entry(self.edit_pers_frame2)
        self.address_entry.configure(font="{arial} 20 {}")
        self.address_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.735, x=0, y=0
        )
        self.save_changes_button = tk.Button(self.edit_pers_frame2)
        self.save_changes_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Save",
        )
        self.save_changes_button.place(anchor="center", relx=0.70, rely=0.92, x=0, y=0)
        self.save_changes_button.bind("<1>", self.save_personnel, add="")
        self.edit_changes_button = tk.Button(self.edit_pers_frame2)
        self.edit_changes_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Edit",
        )
        self.edit_changes_button.place(anchor="center", relx=0.30, rely=0.92, x=0, y=0)
        self.edit_changes_button.bind("<1>", self.edit_personnel, add="")
        self.edit_pers_frame2.place(
            anchor="center", relheight=0.86, relwidth=0.35, relx=0.18, rely=0.565
        )
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.edit_pers_frame1 = tk.Frame(self.edit_personnel_app)
        self.edit_pers_frame1.configure(background="#fff000", height=200, width=200)
        self.school_logo_label = tk.Label(self.edit_pers_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text="label1",
        )
        self.school_logo_label.place(anchor="center", relx=0.25, rely=0.5)
        self.edit_pers_frame1.place(
            anchor="center", relheight=0.13, relwidth=1.0, relx=0.5, rely=0.065
        )
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.disp_pic()
        self.put_info()
        self.disable_entry()
        # Main widget
        self.mainwindow = self.edit_personnel_app
        # will set the window to fullscreen
        self.mainwindow.attributes("-topmost", True)
        # this protocol will do a function after pressing the close button.
        self.mainwindow.wm_attributes("-fullscreen", "True")
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)


    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit() 

    # this will return to the camera app
    def show_home_win(self):
        self.admin_home_window.deiconify()
        self.edit_personnel_app.destroy()

    def hide_this_window(self):
        self.edit_personnel_app.withdraw()

    # this function will destroy the current window and return to camera app
    def show_cam_app_window(self):
        self.hide_this_window()
        aCA.CameraEditApp(self.disp_temp_pic,self.video_source,self.edit_personnel_app, self.img_path)


    # enables entry widgets
    def disable_entry(self):
        self.address_entry.configure(state="disabled")
        self.mid_name_entry.configure(state="disabled")
        self.last_name_entry.configure(state="disabled")
        self.first_name_entry.configure(state="disabled")
        self.contact_num_entry.configure(state="disabled")
        self.personnel_num_entry.configure(state="disabled")
        self.personnel_optionmenu.configure(state="disabled")

    # enables entry widgets
    def enable_entry(self):
        self.address_entry.configure(state="normal")
        self.mid_name_entry.configure(state="normal")
        self.last_name_entry.configure(state="normal")
        self.first_name_entry.configure(state="normal")
        self.contact_num_entry.configure(state="normal")
        self.personnel_num_entry.configure(state="normal")
        self.personnel_optionmenu.configure(state="normal")

    def put_info(self):
        self.select_personnel()
        # set the content of the entry as the users information


    def select_personnel(self):
        self.personnel_num_entry.insert(0, self.personnel_num)
        self.first_name_entry.insert(0, self.personnel_firstname)
        self.last_name_entry.insert(0, self.personnel_lastname)
        self.mid_name_entry.insert(0, self.personnel_middlename)
        self.contact_num_entry.insert(0, self.personnel_contact_num)
        self.address_entry.insert(0, self.personnel_address)
        self.personnel_type_var.set(value=self.personnel_type)

    def save_personnel_function(self):
        self.personnel_num_var = self.personnel_num_entry.get()
        self.personnel_firstname_var = self.first_name_entry.get()
        self.personnel_lastname_var = self.last_name_entry.get()
        self.personnel_middlename_var = self.mid_name_entry.get()
        self.personnel_contact_num_var = self.contact_num_entry.get()
        self.personnel_address_var = self.address_entry.get()
        self.personnel_type_variable = self.personnel_type_var.get()

        self.sql_query.update_personnel(
            self.personnel_num_var,
            self.personnel_firstname_var,
            self.personnel_lastname_var,
            self.personnel_middlename_var,
            self.personnel_contact_num_var,
            self.personnel_address_var,
            self.personnel_type_variable,
        )

        if os.path.exists(self.img_path + "/temp.jpg"):
            img_name = self.personnel_num
            os.rename(self.img_path+"/" +img_name+ ".jpg",self.img_path + "/temp.jpg")

    # this function will display the image into the canvas
    def disp_pic(self):
        self.load_image = PIL.Image.open(self.img_path +"/" + self.personnel_num +".jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)
    
    def disp_temp_pic(self):
        self.load_image = PIL.Image.open(self.img_path +"/temp.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)

    def save_personnel(self, event=None):
        self.save_personnel_function()
        # save infos

    def edit_personnel(self, event=None):
        # enables and disables the entry and optionmenu
        if self.edit_bool == True:
            self.enable_entry()
            self.edit_bool = False
        elif self.edit_bool == False:
            self.disable_entry()
            self.edit_bool = True

    # this command will open the camera app
    def change_pic(self, event=None):
        self.show_cam_app_window()

    def return_func(self, event=None):
        self.show_home_win()
        if os.path.exists(self.img_path + "/temp.jpg"):
            os.remove(self.img_path + "/temp.jpg")

