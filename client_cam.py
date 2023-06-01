import tkinter as tk
import client_home as cH
import admin_home as aH
import sys
import cv2
class ClientCameraSelectApp:
    def __init__(self, user ,login_module, ufname,ulname):

    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # Color ------------
        self.sub_complimentary_color = "#808080" #gray
        self.main_color = "#0072bc" #Blue
        self.sub_color = "#FFF875" #light Yellow
        self.complimentary_color_1 = "#E7E7E7" #light  gray
        self.complimentary_color_2 = "#F7FAE9" #Cream Color
        self.hover_color = "#FFF200" #pure Yellow
        # Color ------------
        self.user = user
        self.login_window = login_module # this is the login window
        self.on_radio = True
        self.users_firstname = ufname
        self.users_lastname = ulname
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        
        # build ui
        self.camera_app = tk.Toplevel()
        self.camera_app.configure(background=self.main_color, height=200, width=200)
        self.camera_app.geometry("500x600")
        self.camera_app.resizable(False, False)
        self.camera_app.title("SeekU - Camera")
        self.camera_app.iconbitmap(".\SeekU\SeekU.ico")
        # variable for the radiobuttons, to connect them
        self.camera_app.bind('<Return>',lambda event:self.open_logic())
    #Contains-the-radiobuttons-entry-and-button---------------------------------------------------------------------------------------------- 
        self.camera_frame = tk.Frame(self.camera_app)
        self.camera_frame.configure(
            background=self.main_color, height=200, width=200)   


        self.detecting_label = tk.Label(self.camera_frame)
        self.detecting_label.configure(
            background=self.main_color,
            font="{Lucida} 24 {}",
            foreground=self.complimentary_color_2,
            text='Detecting Camera...')
        self.detecting_label.place(
        anchor="center", relx=0.5, rely=0.5, x=0, y=0)

        self.camera_frame.place(
            anchor="center",
            relheight=1,
            relwidth=1,
            relx=.5,
            rely=.5)

    #Contains-the-radiobuttons-entry-and-button----------------------------------------------------------------------------------------------
    #Contains-the-IP SECTION----------------------------------------------------------------------------------------------------------------
        self.camera_frame4 = tk.Frame(self.camera_app)
        self.camera_frame4.configure(
            background=self.main_color, height=200, width=200)   
        
        self.ip_camera_label = tk.Label(self.camera_frame4)
        self.ip_camera_label.configure(
            background=self.main_color,
            font="{Lucida} 20 {}",
            foreground=self.complimentary_color_2,
            text='IP Camera')
        self.ip_camera_label.place(
            anchor="center", relx=0.5, rely=0.5, x=0, y=0)
        self.ip_cam_entry = tk.Entry(self.camera_frame4)
        self.ip_cam_entry.configure(
            background=self.complimentary_color_2,
            font="{arial} 18 {}",
            foreground="#010303",
            state='normal')
        self.ip_cam_entry.place(
            anchor="center",
            relheight=.06,
            relwidth=.6,
            relx=0.51,
            rely=0.6,
            )
        self.open_button2 = tk.Button(self.camera_frame4)
        self.open_button2.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 20 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='OPEN',
            width=10)
        self.open_button2.place(
            anchor="center",
            relheight=0.09,
            relwidth=0.4,
            relx=0.5,
            rely=0.8
            )
        self.open_button2.bind("<ButtonPress>", self.open_ip_press, add="")
        self.camera_frame4.place(
            anchor="center",
            relheight=1,
            relwidth=1,
            relx=.5,
            rely=.5)
    #Contains-the-IP SECTION----------------------------------------------------------------------------------------------------------------

    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
        self.camera_frame2 = tk.Frame(self.camera_app)
        self.camera_frame2.configure(
            background=self.complimentary_color_2, height=200, width=200)
        self.seeku_logo = tk.Label(self.camera_frame2)
        self.img_SeekUsmall = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.seeku_logo.configure(
            background=self.complimentary_color_2,
            image=self.img_SeekUsmall,
            text='label1')
        self.seeku_logo.place(anchor="center", relx=0.3, rely=0.5)
        self.app_name_label = tk.Label(self.camera_frame2)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png")
        self.app_name_label.configure(
            background=self.complimentary_color_2,
            font="{arial black} 40 {}",
            foreground=self.main_color,
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
            background=self.complimentary_color_2, height=200, width=200)        
        self.logout_label = tk.Label(self.camera_frame3)
        self.logout_label.config(            
            background=self.complimentary_color_2,
            font="{arial} 12 {}",
            foreground=self.main_color,
            relief="flat",
            text='Log out')
        self.logout_label.place(anchor="center", relx=0.9, rely=0.5)
        self.logout_label.bind("<1>", self.logout_press, add="")
        self.logout_label.bind("<Enter>", self.logout_hover, add="")
        self.logout_label.bind("<Leave>", self.logout_hover_out, add="")
        self.ip_label = tk.Label(self.camera_frame3)
        self.ip_label.config(            
            background=self.complimentary_color_2,
            font="{arial} 11 {}",
            foreground=self.main_color,
            relief="flat",
            text='IP Camera')
        # self.ip_label.place(anchor="center", relx=0.7, rely=0.5)
        self.ip_label.bind("<1>", self.ip_press, add="")
        self.ip_label.bind("<Enter>", self.ip_hover, add="")
        self.ip_label.bind("<Leave>", self.ip_hover_out, add="")
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
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)
        # refer to the function's comments
        self.center(self.mainwindow)
        self.show_radio_section()
        self.camera_app.after(1000, self.detect_cam_func)

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

    def sel(self):
        print(self.cam_var.get())

    def show_ip_section(self):
        self.camera_frame.place_forget()
        self.camera_frame4.place(
            anchor="center",
            relheight=1,
            relwidth=1,
            relx=.5,
            rely=.5)
    def show_radio_section(self):
        self.camera_frame4.place_forget()
        self.camera_frame.place(
            anchor="center",
            relheight=1,
            relwidth=1,
            relx=.5,
            rely=.5)

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
            vid_source = self.cam_var.get()
            print(vid_source)
            cH.HomeApp(vid_source, self.login_window, self.camera_app ) 

        if self.user == "System Admin" or self.user == "Staff": 
            vid_source = self.cam_var.get()
            print(vid_source)
            aH.AdminHomeApp(self.user, vid_source, self.login_window, self.camera_app,self.users_firstname  ,self.users_lastname)

    def open_with_ip_logic(self):
        self.hide_this_window()
        if self.user == "Security Guard":
            vid_source = self.ip_cam_entry.get()
            cH.HomeApp(vid_source, self.login_window, self.camera_app ) 

        if self.user == "System Admin" or self.user == "Staff": 
            vid_source = self.ip_cam_entry.get()
            aH.AdminHomeApp(self.user, vid_source, self.login_window, self.camera_app,self.users_firstname  ,self.users_lastname)

    def open_press(self, event=None):
        self.open_logic()

    def open_ip_press(self, event=None):
        self.open_with_ip_logic()

    def logout_press(self, event=None):
        self.show_log_window()

    def logout_hover(self, event=None):
        self.logout_label.configure(font="{arial} 12 {bold}")

    def logout_hover_out(self, event=None):
        self.logout_label.configure(font="{arial} 12 {}")

    def ip_press(self, event=None):
        if self.on_radio:
            self.on_radio = False
            self.show_ip_section()
            self.ip_label.configure(text='Cameras')
        elif not self.on_radio:
            self.on_radio = True
            self.ip_label.configure(text='IP Camera')
            self.show_radio_section()
            

    def ip_hover(self, event=None):
        self.ip_label.configure(font="{arial} 12 {bold}")

    def ip_hover_out(self, event=None):
        self.ip_label.configure(font="{arial} 12 {}")

    def detect_cam_func(self):
        cams = []
        index = 0
        while True:
            cam = cv2.VideoCapture(index)
            if (cam is None or not cam.isOpened()) or index == 4 :
                break
            cams.append(cam)
            index += 1
        self.cams_detected(cams)     

    def cams_detected(self, cams):
        self.cam_var = tk.IntVar()

        if cams:
            # Create radio buttons for each camera
            for i, cam in enumerate(cams):
                print(cam)
                cam_name = f"Camera {i+1}"
                cam_radiobutton = tk.Radiobutton(self.camera_frame)
                cam_radiobutton.configure(
                    background=self.main_color,
                    font="Arial 24",
                    foreground=self.complimentary_color_2,
                    text=cam_name,
                    selectcolor="black",
                    variable=self.cam_var,
                    value=i, command=self.sel
                    )
                cam_radiobutton.place(anchor="center", relx=.5, rely=.42 + i*.08)

            self.cam_var.set(0)
        
        
        else:
            self.no_cameras_label = tk.Label(self.camera_frame)
            self.no_cameras_label.configure(
                background=self.main_color,
                font="{Lucida} 24 {}",
                foreground=self.complimentary_color_2,
                text='No Camera Found!')
            self.no_cameras_label.place(
            anchor="center", relx=0.5, rely=0.5, x=0, y=0)
        self.detecting_label.place_forget()
        self.open_button = tk.Button(self.camera_frame)
        self.open_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 20 {}",
            foreground=self.main_color,
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