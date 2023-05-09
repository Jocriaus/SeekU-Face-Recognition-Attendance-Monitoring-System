#!/usr/bin/python3
import tkinter as tk
import tkinter.filedialog as filedialog

class RestoreApp:
    def __init__(self):
        # build ui
        self.restore_db = tk.Toplevel()
        self.restore_db.configure(background="#0072bc", height=200, width=200)
        self.restore_db.geometry("500x700")
        self.restore_db.resizable(False, False)
        self.restore_db_frame2 = tk.Frame(self.restore_db)
        self.restore_db_frame2.configure(
            background="#0072bc", height=200, width=200)
        self.section_rec_label = tk.Label(self.restore_db_frame2)
        self.section_rec_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Client Records')
        self.section_rec_label.place(anchor="center", relx=0.5, rely=0.25)
        self.student_rec_button = tk.Button(self.restore_db_frame2)
        self.student_rec_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.student_rec_button.place(
            anchor="center",
            relheight=0.06,
            relwidth=0.20,
            relx=0.75,
            rely=0.325)
        self.student_rec_button.bind(
            "<ButtonPress>", self.import_s_records, add="")
        self.student_rec_label = tk.Label(self.restore_db_frame2)
        self.student_rec_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Students')
        self.student_rec_label.place(anchor="center", relx=0.25, rely=0.325)
        self.personnel_rec_button = tk.Button(self.restore_db_frame2)
        self.personnel_rec_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.personnel_rec_button.place(
            anchor="center",
            relheight=0.06,
            relwidth=0.20,
            relx=0.75,
            rely=0.4)
        self.personnel_rec_button.bind(
            "<ButtonPress>", self.import_p_records, add="")
        self.personnel_rec_label = tk.Label(self.restore_db_frame2)
        self.personnel_rec_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Personnels')
        self.personnel_rec_label.place(anchor="center", relx=0.25, rely=0.4)
        self.visitor_rec_button = tk.Button(self.restore_db_frame2)
        self.visitor_rec_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.visitor_rec_button.place(
            anchor="center",
            relheight=0.06,
            relwidth=0.20,
            relx=0.75,
            rely=0.475)
        self.visitor_rec_button.bind(
            "<ButtonPress>", self.import_v_records, add="")
        self.visitor_rec_label = tk.Label(self.restore_db_frame2)
        self.visitor_rec_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Visitors')
        self.visitor_rec_label.place(anchor="center", relx=0.25, rely=0.475)
        self.section_rep_label = tk.Label(self.restore_db_frame2)
        self.section_rep_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Client Reports')
        self.section_rep_label.place(anchor="center", relx=0.5, rely=0.675)
        self.student_rep_button = tk.Button(self.restore_db_frame2)
        self.student_rep_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.student_rep_button.place(
            anchor="center",
            relheight=0.06,
            relwidth=0.20,
            relx=0.75,
            rely=0.75)
        self.student_rep_button.bind(
            "<ButtonPress>", self.import_s_reports, add="")
        self.student_rep_label = tk.Label(self.restore_db_frame2)
        self.student_rep_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Students')
        self.student_rep_label.place(anchor="center", relx=0.25, rely=0.75)
        self.personnel_rep_button = tk.Button(self.restore_db_frame2)
        self.personnel_rep_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.personnel_rep_button.place(
            anchor="center",
            relheight=0.06,
            relwidth=0.20,
            relx=0.75,
            rely=0.825)
        self.personnel_rep_button.bind(
            "<ButtonPress>", self.import_p_reports, add="")
        self.personnel_rep_label = tk.Label(self.restore_db_frame2)
        self.personnel_rep_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Personnels')
        self.personnel_rep_label.place(anchor="center", relx=0.25, rely=0.825)
        self.visitor_rep_button = tk.Button(self.restore_db_frame2)
        self.visitor_rep_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.visitor_rep_button.place(
            anchor="center",
            relheight=0.06,
            relwidth=0.20,
            relx=0.75,
            rely=0.9)
        self.visitor_rep_button.bind(
            "<ButtonPress>", self.import_v_reports, add="")
        self.visitor_rep_label = tk.Label(self.restore_db_frame2)
        self.visitor_rep_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Visitors')
        self.visitor_rep_label.place(anchor="center", relx=0.25, rely=0.9)
        self.users_label = tk.Label(self.restore_db_frame2)
        self.users_label.configure(
            background="#0072bc",
            font="{lucida} 20 {bold}",
            foreground="#F7FAE9",
            text='Users')
        self.users_label.place(anchor="center", relx=0.25, rely=0.55)
        self.users_button = tk.Button(self.restore_db_frame2)
        self.users_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 14 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.users_button.place(
            anchor="center",
            relheight=0.06,
            relwidth=0.20,
            relx=0.75,
            rely=0.55)
        self.users_button.bind("<ButtonPress>", self.import_users, add="")
        self.restore_db_frame2.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=0.5,
            rely=0.5)
        self.restore_db_frame = tk.Frame(self.restore_db)
        self.restore_db_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.seeku_logo = tk.Label(self.restore_db_frame)
        self.img_SeekUsmall = tk.PhotoImage(file="./SeekU/SeekU small.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekUsmall,
            text='label1')
        self.seeku_logo.place(anchor="center", relx=0.3, rely=0.5)
        self.app_name_label = tk.Label(self.restore_db_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file="./SeekU/SeekU Logotype micro.png")
        self.app_name_label.configure(
            background="#F7FAE9",
            font="{arial black} 40 {}",
            foreground="#0072bc",
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text='SEEK')
        self.app_name_label.place(anchor="center", relx=0.65, rely=0.5)
        self.restore_db_frame.place(
            anchor="center",
            relheight=0.20,
            relwidth=1,
            relx=.5,
            rely=.1)

        self.mainwindow = self.restore_db
        self.center(self.mainwindow)
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_window)
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)
        self.mainwindow.grab_set()

    def exit_window(self):
        self.show_home_window()

    # this function will return to the login window
    def show_home_window(self):
        self.restore_db.grab_release()
        self.restore_db.destroy()

    def select_file(self):
        self.administrator_app.attributes("-topmost", False)
        file_select = filedialog.askopenfilename()
        if file_select == "":
            file_select = False
            return file_select
        else:
            return file_select

    def import_students_rec_logic(self):
        selected_file = self.select_file()
        if selected_file:
            pass

    def import_personnels_rec_logic(self):
        selected_file = self.select_file()
        if selected_file:
            pass

    def import_visitors_rec_logic(self):
        selected_file = self.select_file()
        if selected_file:
            pass

    def import_students_rep_logic(self):
        selected_file = self.select_file()
        if selected_file:
            pass

    def import_personnels_rep_logic(self):
        selected_file = self.select_file()
        if selected_file:
            pass

    def import_visitors_rep_logic(self):
        selected_file = self.select_file()
        if selected_file:
            pass

    def import_users_logic(self):
        selected_file = self.select_file()
        if selected_file:
            pass

    # this function will center the window
    def center(self, win):
        win.update()
        w_req, h_req = win.winfo_width(), win.winfo_height()
        w_form = win.winfo_rootx() - win.winfo_x()
        w = w_req + w_form * 2
        h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry("{0}x{1}+{2}+{3}".format(w_req, h_req, x, y))


    def import_s_records(self, event=None):
        self.import_students_rec_logic()

    def import_p_records(self, event=None):
        self.import_personnels_rec_logic()

    def import_v_records(self, event=None):
        self.import_visitors_rec_logic()

    def import_s_reports(self, event=None):
        self.import_students_rep_logic()

    def import_p_reports(self, event=None):
        self.import_personnels_rep_logic()

    def import_v_reports(self, event=None):
        self.import_visitors_rep_logic()

    def import_users(self, event=None):
        self.import_users_logic()


