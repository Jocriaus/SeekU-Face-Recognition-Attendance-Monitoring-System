import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messbx
import splash_screen as sS
import client_camera_app as cCA
import datetime
import query_mod as qry
import datetime as datetime
import sys
import os
import re
import face_recog_mod as fr
class HomeApp:
    def __init__(self,vid_source, login_mod, sel_cam):
        
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.sql_query = qry.dbQueries()
        self.on_settings = False
        self.set_data()
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        # build ui
        self.home_app = tk.Toplevel()
        self.home_app.configure(background="#0072bc", height=200, width=200)
        self.home_app.geometry("500x600")
        self.home_app.resizable(False, False)
        self.home_app.title("SeekU - Home")
        self.home_app.iconbitmap(".\SeekU\SeekU.ico")
    #0072bc
    #contains the settings --------------------------------------------------------------------------------------------
        self.home_app_frame4 = tk.Frame(self.home_app)
        self.home_app_frame4.configure(
            background="#0072bc", height=200, width=200)
        self.save_button = tk.Button(self.home_app_frame4)
        self.save_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 20 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Save',
            width=10)
        self.save_button.place(
            anchor="center",
            relheight=0.12,
            relwidth=0.34,
            relx=.31,
            rely=0.925)
        self.save_button.bind(
            "<ButtonPress>", self.save_settings, add="")
        
        self.reset_button = tk.Button(self.home_app_frame4)
        self.reset_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 12 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Reset',
            width=10)
        self.reset_button.place(
            anchor="center",
            relheight=0.09,
            relwidth=0.2,
            relx=.875,
            rely=0.85)
        self.reset_button.bind(
            "<ButtonPress>", self.reset_folder, add="")
        
        self.reencode_button = tk.Button(self.home_app_frame4)
        self.reencode_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 10 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Re-Encode',
            width=10)
        self.reencode_button.place(
            anchor="center",
            relheight=0.09,
            relwidth=0.2,
            relx=.875,
            rely=0.965)
        self.reencode_button.bind(
            "<ButtonPress>", self.reencode, add="")
        
        self.tolerance_lvl_label = tk.Label(self.home_app_frame4)
        self.tolerance_lvl_label.configure(
            background="#0072bc",
            font="{arial} 16 {bold}",
            foreground="#F7FAE9",
            text='Camera Tolerance')
        self.tolerance_lvl_label.place(anchor="center", relx=0.325, rely=0.15)
        self.tolerance_lvl_scale = tk.Scale(self.home_app_frame4)
        self.tolerance_lvl_scale.configure(
            background="#0072bc",
            borderwidth=0,
            digits=3,
            font="{arial } 12 {}",
            foreground="#F7FAE9",
            from_=0,
            highlightthickness=0,
            orient="horizontal",
            relief="sunken",
            resolution=.01,
            showvalue="true",
            to=1)
        self.tolerance_lvl_scale.place(
            anchor="center", relwidth=0.725, relx=0.5, rely=0.23)
        self.data_set_label = tk.Label(self.home_app_frame4)
        self.data_set_label.configure(
            background="#0072bc",
            font="{arial} 16 {bold}",
            foreground="#F7FAE9",
            text='Data Set Folder Name')
        self.data_set_label.place(anchor="center", relx=0.36, rely=0.35)
        self.data_set_entry = tk.Entry(self.home_app_frame4)
        self.data_set_entry.configure(font="{arial} 16 {}")
        self.data_set_entry.place(
            anchor="center",
            relheight=0.07,
            relwidth=0.4,
            relx=0.34,
            rely=0.425,
            x=0,
            y=0)
        self.detection_time_lbl = tk.Label(self.home_app_frame4)
        self.detection_time_lbl.configure(
            background="#0072bc",
            font="{arial} 16 {bold}",
            foreground="#F7FAE9",
            text='Detection Time (seconds)')
        self.detection_time_lbl.place(anchor="center", relx=0.4, rely=0.525)
        self.detection_time_entry = tk.Entry(self.home_app_frame4)
        self.detection_time_entry.configure(font="{arial} 16 {}")
        self.detection_time_entry.place(
            anchor="center",
            relheight=0.07,
            relwidth=0.4,
            relx=0.34,
            rely=0.6,
            x=0,
            y=0)
        self.default_time_out_lbl = tk.Label(self.home_app_frame4)
        self.default_time_out_lbl.configure(
            background="#0072bc",
            font="{arial} 16 {bold}",
            foreground="#F7FAE9",
            text='Default Time out (HH:MM:SS)')
        self.default_time_out_lbl.place(anchor="center", relx=0.425, rely=0.69)
        self.default_time_out_entry = tk.Entry(self.home_app_frame4)
        self.default_time_out_entry.configure(font="{arial} 16 {}")
        self.default_time_out_entry.place(
            anchor="center",
            relheight=0.07,
            relwidth=0.4,
            relx=0.34,
            rely=0.775,
            x=0,
            y=0)
        self.home_app_frame4.place(
            anchor="center",
            relheight=.7,
            relwidth=1,
            relx=0.5,
            rely=0.4)
        
    #Contains-the-buttons----------------------------------------------------------------------------------------------------- 
        self.home_app_frame2 = tk.Frame(self.home_app)
        self.home_app_frame2.configure(
            background="#0072bc", height=200, width=200)
        self.attendance_button = tk.Button(self.home_app_frame2)
        self.attendance_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 24 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Attendance',
            width=10)
        self.attendance_button.place(
            anchor="center",
            relheight=0.15,
            relwidth=0.5,
            relx=.5,
            rely=0.4)
        self.attendance_button.bind(
            "<ButtonPress>", self.attendance_press, add="")
        self.add_visitor = tk.Button(self.home_app_frame2)
        self.add_visitor.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 24 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Add Visitors',
            width=10)
        self.add_visitor.place(
            anchor="center",
            relheight=.15,
            relwidth=0.5,
            relx=.5,
            rely=0.6)
        self.add_visitor.bind("<ButtonPress>", self.add_visitors_press, add="")
        self.encode_button = tk.Button(self.home_app_frame2)
        self.encode_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Encode',
            width=10)
        self.encode_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.2,
            relx=.85,
            rely=0.9)
        self.encode_button.bind(
            "<ButtonPress>", self.encode, add="")
        
        self.home_app_frame2.place(
            anchor="center",
            relheight=.7,
            relwidth=1,
            relx=0.5,
            rely=0.6)
    #Contains-the-buttons----------------------------------------------------------------------------------------------------- 


    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
        self.home_app_frame = tk.Frame(self.home_app)
        self.home_app_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.seeku_logo = tk.Label(self.home_app_frame)
        self.img_SeekUsmall = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekUsmall,
            text='label1')
        self.seeku_logo.place(anchor="center", relx=0.3, rely=0.5)
        self.app_name_label = tk.Label(self.home_app_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png")
        self.app_name_label.configure(
            background="#F7FAE9",
            font="{arial black} 40 {}",
            foreground="#0072bc",
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text='SEEK')
        self.app_name_label.place(anchor="center", relx=0.65, rely=0.5)
        self.home_app_frame.place(
            anchor="center",
            relheight=0.25,
            relwidth=1,
            relx=.5,
            rely=.12)
        #Contains logout and settings --------------------------------------------
        self.home_app_frame3 = tk.Frame(self.home_app)
        self.home_app_frame3.configure(
            background="#F7FAE9", height=200, width=200)       
        self.return_label = tk.Label(self.home_app_frame3)
        self.return_label.config(            
            background="#F7FAE9",
            font="{arial} 12 {}",
            foreground="#0072bc",
            relief="flat",
            text='Return')
        self.return_label.place(anchor="center", relx=0.1, rely=0.5)
        self.return_label.bind("<1>", self.return_press, add="")
        self.return_label.bind("<Enter>", self.return_hover, add="")
        self.return_label.bind("<Leave>", self.return_hover_out, add="")

        self.logout_label = tk.Label(self.home_app_frame3)
        self.logout_label.config(            
            background="#F7FAE9",
            font="{arial} 12 {}",
            foreground="#0072bc",
            relief="flat",
            text='Log out')
        self.logout_label.place(anchor="center", relx=0.9, rely=0.5)
        self.logout_label.bind("<1>", self.logout_press, add="")
        self.logout_label.bind("<Enter>", self.logout_hover, add="")
        self.logout_label.bind("<Leave>", self.logout_hover_out, add="")

        self.settings_label = tk.Label(self.home_app_frame3)
        self.settings_label.config(            
            background="#F7FAE9",
            font="{arial} 12 {}",
            foreground="#0072bc",
            relief="flat",
            text='Settings')
        self.settings_label.place(anchor="center", relx=0.7, rely=0.5)
        self.settings_label.bind("<1>", self.setting_press, add="")
        self.settings_label.bind("<Enter>", self.setting_hover, add="")
        self.settings_label.bind("<Leave>", self.setting_hover_out, add="")
        
        self.home_app_frame3.place(
            anchor="center",
            relheight=0.05,
            relwidth=1,
            relx=.5,
            rely=.975)
        
        print("this is video source" + str(self.video_source) )
    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
        self.show_home_frame()
        self.set_settings_data()
        # this protocol will do a function after pressing the close button.
        self.home_app.protocol("WM_DELETE_WINDOW", self.exit_program )
        # Main widget
        self.mainwindow = self.home_app
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)
        # refer to the function's comments
        self.center(self.mainwindow)

    #-----------------------------------------------------------------------------------------
    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit() 

    # this function will hide the window after logging in.
    def hide_this_window(self):
        self.home_app.withdraw()

    def show_this_window(self):
        self.home_app.deiconify()

    # this function will return to the login window
    def show_log_window(self):
        self.login_window.deiconify()
        self.home_app.destroy()

    def show_select_cam(self):
        self.sel_cam_window.deiconify()
        self.home_app.destroy()
    

    def fix_path(self, path):
        newpath = ""
        for char in path:
            if char == "/":
                newpath += "\\"
            else:
                newpath += char
        return newpath
        
    

    # this function will center the window
    def center(self, win):
        win.update()
        w_req, h_req = win.winfo_width(), win.winfo_height()
        w_form = win.winfo_rootx() - win.winfo_x()
        w = w_req + w_form * 2
        h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry('{0}x{1}+{2}+{3}'.format(w_req, h_req, x, y))

    # this function will let the user choose the folder according to what is needed
    def select_folder(self):
        self.mainwindow.attributes("-topmost", False)
        dialog_parent = tk.Toplevel(self.mainwindow)
        dialog_parent.withdraw()
        dialog_parent.grab_set()
        folder_select = filedialog.askdirectory(title="Select Folder")
        if folder_select == "":
            folder_select = False
            dialog_parent.grab_release()
            dialog_parent.destroy()
            return folder_select
        else:
            dialog_parent.grab_release()
            dialog_parent.destroy()
            return folder_select

    # this command will open the attendance module
    def attendance_press(self, event=None):
        tolerance = self.sql_query.get_tolerance_lvl()
        self.hide_this_window()
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        setting = self.sql_query.get_fr_path_file_date().strip()
        print("cd "+ current_date)
        print("s "+ setting)
        # if else condition if date setting is similar to current date
        if setting == current_date:
            folder_selected = self.sql_query.get_face_recog_path()
        else:
            folder_selected = self.select_folder()
            if folder_selected:
                newpath = self.fix_path(folder_selected)
                self.sql_query.set_face_recog_path(newpath)
                self.sql_query.set_fr_path_file_date(current_date)
        # add for handling the select folder function if nothing is chosen.
        if folder_selected:
            if self.data_set_name == os.path.basename(folder_selected):
                sS.SplashScreenWin(
                    self.video_source,
                    self.login_window,
                    self.sel_cam_window, 
                    self.home_app,
                    self.detection_time,
                    tolerance, 
                    folder_selected
                    )
        else:
            self.show_this_window()
        
    # this command will open the add visitor module
    def add_visitors_press(self, event=None):
        folder_selected = ""
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        setting = self.sql_query.get_av_path_file_date().strip()
        self.hide_this_window()
        print("cd "+current_date)
        print("s "+setting)
        # if else condition if date setting is similar to current date
        if setting == current_date:
            folder_selected = self.sql_query.get_add_visitor_path()
        else:
            folder_selected = self.select_folder()
            if folder_selected:
                newpath = self.fix_path(folder_selected)
                self.sql_query.set_add_visitor_path(newpath)
                self.sql_query.set_av_path_file_date(current_date)
        if folder_selected:
            cCA.CameraApp(
                self.video_source,self.login_window,self.sel_cam_window, self.home_app, folder_selected )
        else:
            self.show_this_window()

    def show_setting_frame(self):
        self.home_app_frame2.place_forget()
        self.home_app_frame4.place(
            anchor="center",
            relheight=.7,
            relwidth=1,
            relx=0.5,
            rely=0.55)
    def show_home_frame(self):
        self.home_app_frame4.place_forget()
        self.home_app_frame2.place(
            anchor="center",
            relheight=.7,
            relwidth=1,
            relx=0.5,
            rely=0.6)
    def clear_entry(self):
        self.data_set_entry.delete(0, "end")
        self.default_time_out_entry.delete(0, "end")
        self.detection_time_entry.delete(0, "end")
    def set_data(self):
        self.tolerance = self.sql_query.get_tolerance_lvl()
        self.data_set_name = self.sql_query.get_data_set_fldr()
        timeout_w_micros = self.sql_query.get_time_out_time() 
        # Format the datetime object as a string without microseconds
        self.timeout = timeout_w_micros[0:8]
        self.detection_time = self.sql_query.get_detection_time()

    def set_settings_data(self):
        self.clear_entry()
        self.tolerance_lvl_scale.set(self.tolerance)
        self.data_set_entry.insert(0, self.data_set_name)
        self.default_time_out_entry.insert(0, self.timeout)
        self.detection_time_entry.insert(0, self.detection_time)

    def return_press(self, event=None):
        self.show_select_cam()

    def return_hover(self, event=None):
        self.return_label.configure(font="{arial} 12 {bold}")

    def return_hover_out(self, event=None):
        self.return_label.configure(font="{arial} 12 {}")

    # this command will open the log in window
    def logout_press(self, event=None):
        self.show_log_window()

    def logout_hover(self, event=None):
        self.logout_label.configure(font="{arial} 12 {bold}")

    def logout_hover_out(self, event=None):
        self.logout_label.configure(font="{arial} 12 {}")

    # this command will open the log in window
    def setting_press(self, event=None):

        if not self.on_settings:
            self.set_data()
            self.set_settings_data()
            self.show_setting_frame()
            self.on_settings = True
            self.settings_label.configure(text='Home')
        elif self.on_settings:
            timeout_w_micros = self.sql_query.get_time_out_time() 
            # Format the datetime object as a string without microseconds
            timeout = timeout_w_micros[0:8]
                  
            if  (str(self.tolerance_lvl_scale.get()) == str(self.sql_query.get_tolerance_lvl())
                and str(self.data_set_entry.get()) == str(self.sql_query.get_data_set_fldr())
                and str(self.default_time_out_entry.get()) == str(timeout)
                and str(self.detection_time_entry.get()) == str(self.sql_query.get_detection_time())
                ):
                self.show_home_frame()
                self.settings_label.configure(text='Settings')
                self.on_settings = False
            else:
                result = messbx.askokcancel("Confirm Action", "Do you wish to proceed without saving?")
                if result:
                    # User clicked OK
                    self.show_home_frame()
                    self.settings_label.configure(text='Settings')
                    self.on_settings = False                    

    def setting_hover(self, event=None):
        self.settings_label.configure(font="{arial} 12 {bold}")

    def setting_hover_out(self, event=None):
        self.settings_label.configure(font="{arial} 12 {}")

    def reset_folder(self, event=None):

        result = messbx.askokcancel("Confirm Action", "Do you wish to reset selected folders?")
        if result:
            reset_date = "2020-01-01"
            self.sql_query.set_av_path_file_date(reset_date)
            self.sql_query.set_fr_path_file_date(reset_date)

    def reencode(self, event=None):
        if os.path.exists("encodings.pickle"):
            result = messbx.askokcancel("Confirm Action", "Do you wish to reset all encoded images")
            if result:
                os.remove("encodings.pickle")
        else:
            messbx.showinfo("Not Encoded", "The data set is not currently encoded.")

    def encode(self, event=None):
        if os.path.exists("encodings.pickle"):
             messbx.showwarning("Warning", "The data set is already encoded. Delete the existing to proceed.")
        else:
            folder_selected = self.select_folder()
            fr.FaceEncoding(folder_selected)
            messbx.showinfo("Encoded", "The data set has been encoded.")

    def save_settings(self, event=None):
        tolerance = self.tolerance_lvl_scale.get()
        folder_name = self.data_set_entry.get()
        timeout_str = self.default_time_out_entry.get()
        time = self.detection_time_entry.get()

        if (len(self.data_set_entry.get()) != 0
            and len(self.default_time_out_entry.get()) != 0
            and len(self.detection_time_entry.get()) != 0
            ):
            input_values = [
                folder_name,
                time,
                self.default_time_out_entry.get()
            ]

            concatenated_inputs = "".join(input_values)
            pattern = re.compile("[^a-zA-Z0-9 \-@.,:]")
            if not pattern.search(concatenated_inputs):
                if  time.isdigit() or (
                    time.startswith("-") 
                    and time[1:].isdigit()):
                    try:
                        timeout = datetime.datetime.strptime(timeout_str, "%H:%M:%S") 
                        self.sql_query.set_client_setting(
                            tolerance_lvl= tolerance,
                            data_set_fldr= folder_name,
                            timeout_time= timeout,
                            detection_time= time)
                        messbx.showinfo("Info", "The changes to the settings have been successfully saved.")
                    except ValueError:
                        messbx.showerror("Error", "Please use the format HH:MM:SS as the "+
                        "data format provided is incorrect.")
                else:
                    messbx.showwarning(
                        "Warning",
                        "The provided input for the time is "+
                        "invalid and does not correspond to a valid number.",
                    )
            else:
                messbx.showwarning("Warning", "The input contains special characters.")
        else:
            messbx.showwarning("Warning", "Kindly ensure all fields are filled by entering a value.")