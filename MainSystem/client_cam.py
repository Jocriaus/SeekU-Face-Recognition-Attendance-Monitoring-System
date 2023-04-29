import tkinter as tk
import client_home as cH
import admin_home as aH
import sys
class ClientCameraSelectApp:
    def __init__(self, user ,login_module):

    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.user = user
        self.login_window = login_module # this is the login window
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        # build ui
        self.camera_app = tk.Toplevel()
        self.camera_app.configure(background="#0072bc", height=200, width=200)
        self.camera_app.geometry("500x600")
        self.camera_app.resizable(False, False)
        self.camera_app.title("SeekU - Camera")
        self.camera_app.iconbitmap(".\SeekU\SeekU.ico")
        # variable for the radiobuttons, to connect them
        self.cam_var = tk.IntVar()
        self.cam_var.set(0)

    #Contains-the-radiobuttons-entry-and-button---------------------------------------------------------------------------------------------- 
        self.camera_frame = tk.Frame(self.camera_app)
        self.camera_frame.configure(
            background="#0072bc", height=200, width=200)    
        self.first_cam_radiobutton = tk.Radiobutton(self.camera_frame)
        self.first_cam_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            text='Camera 1',
            selectcolor='black',
            variable = self.cam_var,
            value = 0,
            command= self.check_selection)
        self.first_cam_radiobutton.place(anchor="center", relx=.5, rely=.42)
        self.second_cam_radiobutton = tk.Radiobutton(self.camera_frame)
        self.second_cam_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            text='Camera 2',
            selectcolor='black',
            variable = self.cam_var,
            value = 1,
            command= self.check_selection)
        self.second_cam_radiobutton.place(anchor="center", relx= .5, rely=.5)
        self.ip_cam_radiobutton = tk.Radiobutton(self.camera_frame)
        self.ip_cam_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            text='IP Camera',
            selectcolor='black',
            variable = self.cam_var,
            value = 2,
            command= self.check_selection)
        self.ip_cam_radiobutton.place(anchor="center", relx=0.5, rely=0.58)
        self.ip_cam_entry = tk.Entry(self.camera_frame)
        self.ip_cam_entry.configure(
            background="#F7FAE9",
            font="{arial} 18 {}",
            foreground="#010303",
            state='disabled')
        self.ip_cam_entry.place(
            anchor="center",
            relheight=.06,
            relwidth=.6,
            relx=0.51,
            rely=0.675,
            )
        self.open_button = tk.Button(self.camera_frame)
        self.open_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 20 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='OPEN',
            width=10)
        self.open_button.place(
            anchor="center",
            relheight=0.09,
            relwidth=0.4,
            relx=0.5,
            rely=0.8
            )
        self.open_button.bind("<ButtonPress>", self.open_press, add="")
        self.camera_frame.place(
            anchor="center",
            relheight=1,
            relwidth=1,
            relx=.5,
            rely=.5)

    #Contains-the-radiobuttons-entry-and-button----------------------------------------------------------------------------------------------

    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
        self.camera_frame2 = tk.Frame(self.camera_app)
        self.camera_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.seeku_logo = tk.Label(self.camera_frame2)
        self.img_SeekUsmall = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekUsmall,
            text='label1')
        self.seeku_logo.place(anchor="center", relx=0.3, rely=0.5)
        self.app_name_label = tk.Label(self.camera_frame2)
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
        self.camera_frame2.place(
            anchor="center",
            relheight=0.25,
            relwidth=1,
            relx=.5,
            rely=.12)
        self.camera_frame3 = tk.Frame(self.camera_app)
        self.camera_frame3.configure(
            background="#F7FAE9", height=200, width=200)        
        self.logout_label = tk.Label(self.camera_frame3)
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
        self.camera_frame3.place(
            anchor="center",
            relheight=0.05,
            relwidth=1,
            relx=.5,
            rely=.975)
    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
        # this protocol will do a function after pressing the close button.
        self.camera_app.protocol("WM_DELETE_WINDOW", self.exit_program )

        # Main widget
        self.mainwindow = self.camera_app

        # refer to the function's comments
        self.center(self.mainwindow)

    #-----------------------------------------------------------------------------------------
    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit() 

    # this function will hide this window
    def hide_this_window(self):
        self.camera_app.withdraw()

    # this function will return to the login window and destroy this window
    def show_log_window(self):
        self.login_window.deiconify()
        self.camera_app.destroy()

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

    # this function will enable the entry if you didn't chose the ip camera
    def check_selection(self, event=None):
        print(self.cam_var.get())
        if(self.cam_var.get() == 0):
            self.ip_cam_entry.configure(state='disabled')
        if(self.cam_var.get() == 1):
            self.ip_cam_entry.configure(state='disabled')
        if(self.cam_var.get() == 2):
            self.ip_cam_entry.configure(state='normal')

    # this function will send the videosource value to the next windows
    def open_logic(self):
        self.hide_this_window()
        if self.user == "Security Guard":
            if(self.cam_var.get() == 0):
                vid_source = 0
                cH.HomeApp(vid_source, self.login_window, self.camera_app )
            elif(self.cam_var.get() == 1):
                vid_source = 1
                cH.HomeApp(vid_source, self.login_window, self.camera_app )
            elif(self.cam_var.get() == 2):
                vid_source = self.ip_cam_entry.get()
                cH.HomeApp(vid_source, self.login_window, self.camera_app )  

        if self.user == "High Admin" or self.user == "Low Admin": 
            if(self.cam_var.get() == 0):
                vid_source = 0
                aH.AdminHomeApp(self.user, vid_source, self.login_window, self.camera_app )
            elif(self.cam_var.get() == 1):
                vid_source = 1
                aH.AdminHomeApp(self.user, vid_source, self.login_window, self.camera_app )
            elif(self.cam_var.get() == 2):
                vid_source = self.ip_cam_entry.get()
                aH.AdminHomeApp(self.user, vid_source, self.login_window, self.camera_app )

    def open_press(self, event=None):
        self.open_logic()

    def logout_press(self, event=None):
        self.show_log_window()

    def logout_hover(self, event=None):
        self.logout_label.configure(font="{arial} 12 {bold}")

    def logout_hover_out(self, event=None):
        self.logout_label.configure(font="{arial} 12 {}")