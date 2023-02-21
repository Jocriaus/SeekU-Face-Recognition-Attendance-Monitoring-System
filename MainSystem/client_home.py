import tkinter as tk
from tkinter import filedialog
import client_face_recog as cFG
import client_add_visitor as cAV

class HomeApp:
    def __init__(self,vid_source, login_mod, sel_cam):
        
        #assignment for passed parameters
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        print(self.video_source)

        # build ui
        self.home_app = tk.Toplevel()
        self.home_app.configure(background="#0072bc", height=200, width=200)
        self.home_app.geometry("500x500")
        self.home_app.resizable(False, False)
        self.home_app.title("SeekU - Home")
        self.home_app.iconbitmap(".\SeekU\SeekU.ico")

#-----------------------------------------------------------------------------------------
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


        self.sign_out_button = tk.Button(self.home_app_frame2)
        self.sign_out_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial} 12 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Sign out',
            width=10)
        self.sign_out_button.place(
            anchor="center",
            height=35,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=75,
            y=465)
        self.sign_out_button.bind("<ButtonPress>", self.signout_press, add="")
        self.home_app_frame2.place(
            anchor="center",
            height=500,
            width=500,
            x=250,
            y=250)


#---------------------------------------------------------------------------------------
        self.home_app_frame = tk.Frame(self.home_app)
        self.home_app_frame.configure(
            background="#F7FAE9", height=200, width=200)

        self.seeku_logo = tk.Label(self.home_app_frame)
        self.img_SeekU2 = tk.PhotoImage(file=".\SeekU\SeekU1.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekU2)
        self.seeku_logo.place(anchor="center", x=145, y=80)
        self.app_name_label = tk.Label(self.home_app_frame)
        self.app_name_label.configure(
            background="#F7FAE9",
            font="{arial black} 40 {}",
            foreground="#0072bc",
            relief="flat",
            text='SEEK')
        self.app_name_label.place(
            anchor="center", relx=0.0, rely=0.0, x=280, y=80)
        self.app_name_label2 = tk.Label(self.home_app_frame)
        self.app_name_label2.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial black} 40 {}",
            foreground="#fff200",
            relief="flat",
            text='U')
        self.app_name_label2.place(
            anchor="center", relx=0.0, rely=0.0, x=385, y=80)
        self.home_app_frame.place(
            anchor="center",
            height=150,
            width=500,
            x=250,
            y=75)


        self.home_app.protocol("WM_DELETE_WINDOW", self.show_cam_window )
        # Main widget
        self.mainwindow = self.home_app
        self.center(self.mainwindow)


#-----------------------------------------------------------------------------------------
    def center(self, win):
        win.update()
        w_req, h_req = win.winfo_width(), win.winfo_height()
        w_form = win.winfo_rootx() - win.winfo_x()
        w = w_req + w_form * 2
        h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry('{0}x{1}+{2}+{3}'.format(w_req, h_req, x, y))


    def hide_this_window(self):
        self.home_app.withdraw()

    def show_cam_window(self):
        self.sel_cam_window.deiconify()
        self.home_app.destroy()

    def show_log_window(self):
        self.login_window.deiconify()
        self.home_app.destroy()

    def select_folder(self):
        self.home_app.attributes('-topmost', False)
        self.folder_selected = filedialog.askdirectory()
        self.home_app.attributes('-topmost', True)


    def attendance_press(self, event=None):
        self.hide_this_window()
        self.select_folder()
        # add for handling the select folder function if nothing is chosen.
        cFG.ClientFaceRecogApp(
            self.video_source,self.login_window,self.sel_cam_window, self.home_app,self.folder_selected )

    def add_visitors_press(self, event=None):
        self.hide_this_window()
        cAV.AddVisitorApp(
            self.video_source,self.login_window,self.sel_cam_window, self.home_app )

    def signout_press(self, event=None):
        self.show_log_window()

