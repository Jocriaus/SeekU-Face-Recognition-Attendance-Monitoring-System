import tkinter as tk
from tkinter import filedialog
import splash_screen as sS
import client_camera_app as cCA
import datetime
import query_mod as qry
import sys
class HomeApp:
    def __init__(self,vid_source, login_mod, sel_cam):
        
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.sql_query = qry.dbQueries()
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        # build ui
        self.home_app = tk.Toplevel()
        self.home_app.configure(background="#0072bc", height=200, width=200)
        self.home_app.geometry("500x500")
        self.home_app.resizable(False, False)
        self.home_app.title("SeekU - Home")
        self.home_app.iconbitmap(".\SeekU\SeekU.ico")

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
            height=75,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=300,
            x=250,
            y=230)
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
            height=75,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=300,
            x=250,
            y=350)
        self.add_visitor.bind("<ButtonPress>", self.add_visitors_press, add="")


        self.log_out_button = tk.Button(self.home_app_frame2)
        self.log_out_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial} 12 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Log out',
            width=10)
        self.log_out_button.place(
            anchor="center",
            height=35,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=75,
            y=465)
        self.log_out_button.bind("<ButtonPress>", self.logout_press, add="")
        self.home_app_frame2.place(
            anchor="center",
            height=500,
            width=500,
            x=250,
            y=250)
    #Contains-the-buttons----------------------------------------------------------------------------------------------------- 


    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
        self.home_app_frame = tk.Frame(self.home_app)
        self.home_app_frame.configure(
            background="#F7FAE9", height=200, width=200)

        self.seeku_logo = tk.Label(self.home_app_frame)
        self.img_SeekU2 = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekU2)
        self.seeku_logo.place(anchor="center", x=145, y=80)
        self.app_name_logo = tk.Label(self.home_app_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png")
        self.app_name_logo.configure(
            background="#F7FAE9",
            foreground="#0072bc",
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text='SEEK')
        self.app_name_logo.place(
            anchor="center",
            relx=0.052,
            rely=0.04,
            x=290,
            y=80)
        self.home_app_frame.place(
            anchor="center",
            height=150,
            width=500,
            x=250,
            y=75)
    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 

        # this protocol will do a function after pressing the close button.
        self.home_app.protocol("WM_DELETE_WINDOW", self.exit_program )
        # Main widget
        self.mainwindow = self.home_app
        # refer to the function's comments
        self.center(self.mainwindow)

    #-----------------------------------------------------------------------------------------
    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit() 

    # this function will hide the window after logging in.
    def hide_this_window(self):
        self.home_app.withdraw()

    # this function will return to the login window
    def show_log_window(self):
        self.login_window.deiconify()
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
            self.home_app.attributes('-topmost', False)
            folder_select = filedialog.askdirectory(title = "Select Folder")
            if folder_select == "":
                folder_select = False
                return folder_select
            else:
                return folder_select

    # this command will open the attendance module
    def attendance_press(self, event=None):
        folder_selected = ""
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
        sS.SplashScreenWin(
            self.video_source,self.login_window,self.sel_cam_window, self.home_app, folder_selected )
        
    # this command will open the add visitor module
    def add_visitors_press(self, event=None):
        folder_selected = ""
        self.hide_this_window()
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        setting = self.sql_query.get_av_path_file_date().strip()
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
        cCA.CameraApp(
            self.video_source,self.login_window,self.sel_cam_window, self.home_app, folder_selected )

    # this command will open the log in window
    def logout_press(self, event=None):
        self.show_log_window()
