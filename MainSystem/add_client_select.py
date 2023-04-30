#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import admin_camera_app as aCA
import os
import sys

class AddSelectorApp:
    def __init__(self,vid_source, admin_hom, condition, refresh):

    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.video_source = vid_source
        self.admin_home_window = admin_hom
        self.window_will_open = condition
        self.refresh_func = refresh
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------        
        # build ui
        self.add_select_app = tk.Toplevel()
        self.add_select_app.configure(
            background="#0072bc", height=200, width=200)
        self.add_select_app.geometry("500x400")
        self.add_select_app.resizable(False, False)
        self.add_select_app.title("SeekU - Camera")
        self.add_select_app.iconbitmap(".\SeekU\SeekU.ico")  


        self.add_select_frame2 = tk.Frame(self.add_select_app)
        self.add_select_frame2.configure(
            background="#0072bc", height=200, width=200)
        self.capture_n_save_button = tk.Button(self.add_select_frame2)
        self.capture_n_save_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 20 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Capture and Save',
            width=10)
        self.capture_n_save_button.place(
            anchor="center",
            relheight=0.175,
            relwidth=0.55,
            relx=.5,
            rely=0.45)
        self.capture_n_save_button.bind(
            "<ButtonPress>", self.capture_and_save_press, add="")
        self.save_button = tk.Button(self.add_select_frame2)
        self.save_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 24 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Save',
            width=10)
        self.save_button.place(
            anchor="center",
            relheight=.175,
            relwidth=0.55,
            relx=.5,
            rely=0.7)
        self.save_button.bind("<ButtonPress>", self.save_press, add="")
        self.reminder_label = tk.Label(self.add_select_frame2)
        self.reminder_label.configure(
            background="#0072bc",
            font="{lucida} 10 {}",
            foreground="#F7FAE9",
            text='client should already have a photo on the data set.')
        self.reminder_label.place(anchor="center", relx=0.5, rely=0.825)
        self.add_select_frame2.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=0.5,
            rely=0.5)
        self.add_select_frame = tk.Frame(self.add_select_app)
        self.add_select_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.seeku_logo = tk.Label(self.add_select_frame)
        self.img_SeekUsmall = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekUsmall,
            text='label1')
        self.seeku_logo.place(anchor="center", relx=0.3, rely=0.5)
        self.app_name_label = tk.Label(self.add_select_frame)
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
        self.add_select_frame.place(
            anchor="center",
            relheight=0.25,
            relwidth=1,
            relx=.5,
            rely=.125)
        self.add_select_frame3 = tk.Frame(self.add_select_app)
        self.add_select_frame3.configure(
            background="#F7FAE9", height=200, width=200)       
        self.return_label = tk.Label(self.add_select_frame3)
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
        
        self.add_select_frame3.place(
            anchor="center",
            relheight=0.1,
            relwidth=1,
            relx=.5,
            rely=.95)


        # Main widget
        self.mainwindow = self.add_select_app
        self.center(self.mainwindow)        
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_window)
        self.mainwindow.attributes('-topmost', True)
        self.mainwindow.grab_set()
        
    # this function will destroy the window and closes the system/program.
    def exit_window(self):
        self.show_home_window()

    # this function will hide the window after logging in.
    def hide_this_window(self):
        self.add_select_app.withdraw()

    # this function will return to the login window
    def show_home_window(self):
        self.add_select_app.grab_release()
        self.admin_home_window.deiconify()
        self.add_select_app.destroy()

    def capture_save_clients_logic(self):
        saveonly = False
        folder = self.select_folder()
        if folder:
            aCA.CameraApp(
                 self.video_source, 
                 self.add_select_app,
                 self.admin_home_window, 
                 folder, 
                 self.window_will_open, 
                 self.refresh_func,
                 saveonly)
            self.add_select_app.grab_release()
        self.hide_this_window()

    def save_clients_logic(self):
        saveonly = True
        folder = self.select_folder()
        if folder:
            aCA.CameraApp(
                 self.video_source, 
                 self.add_select_app,
                 self.admin_home_window, 
                 folder, 
                 self.window_will_open, 
                 self.refresh_func,
                 saveonly)
            self.add_select_app.grab_release()
        self.hide_this_window()


    def select_folder(self):
            self.mainwindow.attributes('-topmost', False)
            folder_select = filedialog.askdirectory(title = "Select Folder")
            if folder_select == "":
                folder_select = False
                return folder_select
            else:
                return folder_select

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



    def capture_and_save_press(self, event=None):
        self.capture_save_clients_logic()

    def save_press(self, event=None):
        self.save_clients_logic

    def return_press(self, event=None):
        self.show_home_window()

    def return_hover(self, event=None):
        self.return_label.configure(font="{arial} 12 {bold}")

    def return_hover_out(self, event=None):
        self.return_label.configure(font="{arial} 12 {}")
