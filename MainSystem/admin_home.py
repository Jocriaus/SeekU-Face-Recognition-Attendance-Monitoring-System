#!/usr/bin/python3
import tkinter as tk
from datetime import datetime
from tkinter import filedialog
import sys
import register_personnel as rP
import register_student as rS
import edit_info_personnel as eIP
import edit_info_student as eIS
import user_create as uC
import user_edit as uE
import admin_camera_app as aCA
import Treeview_table as tbl


class AdminHomeApp:
    def __init__(self, user ,vid_source, login_mod, sel_cam):

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.user = user
        # add a condition if the user is high admin or low admin to restrict some access
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.now = datetime.now()
        self.current_date_n_time = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.treeview = tbl.TreeviewGUI()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.administrator_app = tk.Toplevel()
        self.administrator_app.configure(background="#E7E7E7", height=200, width=200)
        width = self.administrator_app.winfo_screenwidth()
        height = self.administrator_app.winfo_screenheight()
        self.administrator_app.geometry("%dx%d" % (width, height))
        self.administrator_app.resizable(False, False)
        self.administrator_app.title("SeekU - Administrator")
        self.administrator_app.iconbitmap(".\SeekU\SeekU.ico")
        # CLIENT-------------------------------------------------------------------------------------------------------
        self.administrator_client_frame = tk.Frame(self.administrator_app)
        self.administrator_client_frame.configure(
            background="#E7E7E7", height=200, width=200
        )
        self.time_and_date_label_c = tk.Label(self.administrator_client_frame)
        self.time_and_date_label_c.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text=self.current_date_n_time,
        )
        self.time_and_date_label_c.place(
            anchor="center", relwidth=1, relx=0.5, rely=0.975, x=0, y=0
        )
        self.admin_c_sec1_frame = tk.Frame(self.administrator_client_frame)
        self.admin_c_sec1_frame.configure(background="#E7E7E7", height=200, width=200)
        self.add_c_button = tk.Button(self.admin_c_sec1_frame)
        self.add_c_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Add Students",
        )
        self.add_c_button.place(anchor="center", relx=0.85, rely=0.5, x=0, y=0)
        self.add_c_button.bind("<Button>", self.add_clients, add="")
        self.edit_c_button = tk.Button(self.admin_c_sec1_frame)
        self.edit_c_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Edit Students",
        )
        self.edit_c_button.place(anchor="center", relx=0.65, rely=0.5, x=0, y=0)
        self.edit_c_button.bind("<Button>", self.edit_clients, add="")
        self.admin_c_sec1_frame.place(
            anchor="center", relheight=0.1, relwidth=1.0, relx=0.5, rely=0.09
        )
        self.admin_c_sec2_frame = tk.Frame(self.administrator_client_frame)
        self.admin_c_sec2_frame.configure(background="#F7FAE9", height=200, width=200)
        self.search_c_button = tk.Button(self.admin_c_sec2_frame)
        self.search_c_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Search",
        )
        self.search_c_button.place(
            anchor="center", relheight=0.5, relwidth=0.16, relx=0.9, rely=0.5, x=0, y=0
        )
        self.admin_c_sec1_frame.place(
            anchor="center", relheight=0.1, relwidth=1.0, relx=0.5, rely=0.09
        )
        self.search_c_button.bind("<Button>", self.search_clients_info, add="")
        self.search_c_entry = tk.Entry(self.admin_c_sec2_frame)
        self.search_c_entry.configure(background="#E7E7E7", font="{arial} 24 {}")
        self.search_c_entry.place(anchor="center", relx=0.63, rely=0.5, x=0, y=0)
        self.clients_list = tk.Label(self.admin_c_sec2_frame)
        self.clients_list.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text="Students List",
        )
        self.clients_list.place(anchor="center", relx=0.125, rely=0.5, x=0, y=0)
        self.admin_c_sec2_frame.place(
            anchor="center", relheight=0.1, relwidth=0.90, relx=0.5, rely=0.22
        )
        self.admin_c_sec3_frame = tk.Frame(self.administrator_client_frame)
        self.admin_c_sec3_frame.configure(background="#F7FAE9", height=200, width=200)
        self.treeview.student_treeview(self.admin_c_sec3_frame)
        self.admin_c_sec3_frame.place(
            anchor="center", relheight=0.6, relwidth=0.9, relx=0.5, rely=0.6, x=0, y=0
        )
        self.clients_man_var = tk.StringVar(value="Manage Students")
        __values = ["Manage Students", "Manage Personnels", "Manage Visitors"]
        self.manage_client_optionmenu = tk.OptionMenu(
            self.administrator_client_frame,
            self.clients_man_var,
            *__values,
            command=self.open_diff_client
        )
        self.manage_client_optionmenu.configure(font="{arial} 20 {bold}")
        self.manage_client_optionmenu.place(
            anchor="center", relx=0.17, rely=0.09, x=0, y=0
        )
        self.manage_client_options = self.administrator_app.nametowidget(
            self.manage_client_optionmenu.menuname
        )
        self.manage_client_options.config(font="{arial} 16")
        self.administrator_client_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )
        # CLIENT-------------------------------------------------------------------------------------------------------

        # USERS-------------------------------------------------------------------------------------------------------
        self.administrator_users_frame = tk.Frame(self.administrator_app)
        self.administrator_users_frame.configure(
            background="#E7E7E7", height=200, width=200
        )
        self.time_and_date_label_u = tk.Label(self.administrator_users_frame)
        self.time_and_date_label_u.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text="Time and Date",
        )
        self.time_and_date_label_u.place(
            anchor="center", relwidth=1, relx=0.5, rely=0.975, x=0, y=0
        )
        self.admin_u_sec1_frame = tk.Frame(self.administrator_users_frame)
        self.admin_u_sec1_frame.configure(background="#E7E7E7", height=200, width=200)
        self.search_user_info = tk.Button(self.admin_u_sec1_frame)
        self.search_user_info.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Search",
        )
        self.search_user_info.place(
            anchor="center", relheight=0.5, relwidth=0.16, relx=0.9, rely=0.5, x=0, y=0
        )
        self.search_user_info.bind("<Button>", self.search_user_infos, add="")
        self.search_u_entry = tk.Entry(self.admin_u_sec1_frame)
        self.search_u_entry.configure(background="#F7FAE9", font="{arial} 24 {}")
        self.search_u_entry.place(anchor="center", relx=0.63, rely=0.5, x=0, y=0)
        self.admin_u_sec1_frame.place(
            anchor="center", relheight=0.1, relwidth=0.90, relx=0.5, rely=0.09
        )
        self.admin_u_sec2_frame = tk.Frame(self.administrator_users_frame)
        self.admin_u_sec2_frame.configure(background="#F7FAE9", height=200, width=200)
        self.treeview.user_treeview(self.admin_u_sec2_frame)
        self.admin_u_sec2_frame.place(
            anchor="center", relheight=0.65, relwidth=0.88, relx=0.5, rely=0.5, x=0, y=0
        )
        self.user_info_label = tk.Label(self.administrator_users_frame)
        self.user_info_label.configure(
            background="#E7E7E7",
            font="{arial} 20 {bold}",
            foreground="#000000",
            text="Users Information",
        )
        self.user_info_label.place(anchor="center", relx=0.15, rely=0.09, x=0, y=0)

        self.edit_user_button = tk.Button(self.administrator_users_frame)
        self.edit_user_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Edit",
        )
        self.edit_user_button.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.87,
            rely=0.875,
            x=0,
            y=0,
        )
        self.edit_user_button.bind("<Button>", self.edit_user_infos, add="")
        self.add_user_button = tk.Button(self.administrator_users_frame)
        self.add_user_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Add",
        )
        self.add_user_button.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.7,
            rely=0.875,
            x=0,
            y=0,
        )
        self.add_user_button.bind("<Button>", self.add_user_infos, add="")
        self.administrator_users_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )
        # USERS-------------------------------------------------------------------------------------------------------

        # REPORT-------------------------------------------------------------------------------------------------------
        self.administrator_report_frame = tk.Frame(self.administrator_app)
        self.administrator_report_frame.configure(
            background="#E7E7E7", height=200, width=200
        )
        self.time_and_date_label_r = tk.Label(self.administrator_report_frame)
        self.time_and_date_label_r.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text=self.current_date_n_time,
        )
        self.time_and_date_label_r.place(
            anchor="center", relwidth=1, relx=0.5, rely=0.975, x=0, y=0
        )
        self.admin_r_sec1_frame = tk.Frame(self.administrator_report_frame)
        self.admin_r_sec1_frame.configure(background="#E7E7E7", height=200, width=200)
        self.search_clients_report = tk.Button(self.admin_r_sec1_frame)
        self.search_clients_report.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Search",
        )
        self.search_clients_report.place(
            anchor="center", relheight=0.5, relwidth=0.16, relx=0.9, rely=0.5, x=0, y=0
        )
        self.search_clients_report.bind("<Button>", self.search_clients_reports, add="")
        self.search_r_entry = tk.Entry(self.admin_r_sec1_frame)
        self.search_r_entry.configure(background="#F7FAE9", font="{arial} 24 {}")
        self.search_r_entry.place(anchor="center", relx=0.63, rely=0.5, x=0, y=0)
        self.admin_r_sec1_frame.place(
            anchor="center", relheight=0.1, relwidth=0.90, relx=0.5, rely=0.09
        )
        self.admin_r_sec2_frame = tk.Frame(self.administrator_report_frame)
        self.admin_r_sec2_frame.configure(background="#F7FAE9", height=200, width=200)
        self.treeview.student_report_treeview(self.admin_r_sec2_frame)
        self.admin_r_sec2_frame.place(
            anchor="center", relheight=0.65, relwidth=0.9, relx=0.5, rely=0.5, x=0, y=0
        )

        self.clients_rep_var = tk.StringVar(value="Students Report")
        __values = ["Students Report", "Personnels Report", "Visitors Report"]
        self.client_report_optionmenu = tk.OptionMenu(
            self.administrator_report_frame,
            self.clients_rep_var,
            *__values,
            command=self.open_diff_report
        )
        self.client_report_optionmenu.place(
            anchor="center", relx=0.17, rely=0.09, x=0, y=0
        )
        self.client_report_optionmenu.configure(font="{arial} 20 {bold}")
        self.client_report_options = self.administrator_app.nametowidget(
            self.client_report_optionmenu.menuname
        )
        self.client_report_options.config(font="{arial} 16")
        self.print_report = tk.Button(self.administrator_report_frame)
        self.print_report.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Print",
        )
        self.print_report.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.87,
            rely=0.875,
            x=0,
            y=0,
        )
        self.print_report.bind("<Button>", self.print_clients_reports, add="")
        self.save_button = tk.Button(self.administrator_report_frame)
        self.save_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Save",
        )
        self.save_button.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.7,
            rely=0.875,
            x=0,
            y=0,
        )
        self.save_button.bind("<Button>", self.save_clients_reports, add="")
        self.administrator_report_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )
        # REPORT-------------------------------------------------------------------------------------------------------

        # SETTINGS-------------------------------------------------------------------------------------------------------
        self.administrator_settings_frame = tk.Frame(self.administrator_app)
        self.administrator_settings_frame.configure(
            background="#E7E7E7", height=200, width=200
        )
        self.time_and_date_label_s = tk.Label(self.administrator_settings_frame)
        self.time_and_date_label_s.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text="Time and Date",
        )
        self.time_and_date_label_s.place(
            anchor="center", relwidth=1, relx=0.5, rely=0.975, x=0, y=0
        )
        self.admin_s_sec1_frame = tk.Frame(self.administrator_settings_frame)
        self.admin_s_sec1_frame.configure(background="#F7FAE9", height=200, width=200)
        self.export_db_button = tk.Button(self.admin_s_sec1_frame)
        self.export_db_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Export",
        )
        self.export_db_button.place(
            anchor="center",
            relheight=0.08,
            relwidth=0.25,
            relx=0.25,
            rely=0.29,
            x=0,
            y=0,
        )
        self.export_db_button.bind("<Button>", self.export_database, add="")
        self.import_db_button = tk.Button(self.admin_s_sec1_frame)
        self.import_db_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Import",
        )
        self.import_db_button.place(
            anchor="center", relheight=0.08, relwidth=0.25, relx=0.25, rely=0.47
        )
        self.import_db_button.bind("<Button>", self.import_database, add="")
        self.gen_settings_label = tk.Label(self.admin_s_sec1_frame)
        self.gen_settings_label.configure(
            background="#F7FAE9", font="{arial} 20 {bold}", text="General Settings"
        )
        self.gen_settings_label.place(anchor="center", relx=0.5, rely=0.1, x=0, y=0)
        self.backup_db_label = tk.Label(self.admin_s_sec1_frame)
        self.backup_db_label.configure(
            background="#F7FAE9", font="{arial} 14 {bold}", text="Backup Database"
        )
        self.backup_db_label.place(anchor="center", relx=0.25, rely=0.19, x=0, y=0)
        self.restore_db_label = tk.Label(self.admin_s_sec1_frame)
        self.restore_db_label.configure(
            background="#F7FAE9", font="{arial} 14 {bold}", text="Restore Database"
        )
        self.restore_db_label.place(anchor="center", relx=0.25, rely=0.38, x=0, y=0)
        self.student_stat_label = tk.Label(self.admin_s_sec1_frame)
        self.student_stat_label.configure(
            background="#F7FAE9", font="{arial} 14 {bold}", text="Student Status"
        )
        self.student_stat_label.place(anchor="center", relx=0.22, rely=0.55, x=0, y=0)
        self.stud_stat_rem_label = tk.Label(self.admin_s_sec1_frame)
        self.stud_stat_rem_label.configure(
            background="#F7FAE9",
            font="{arial} 12 {}",
            justify="left",
            text="Student Informations will be activated\nand deactivated on selected dates\nFormat = MM/DD/YY",
        )
        self.stud_stat_rem_label.place(anchor="center", relx=0.325, rely=0.63, x=0, y=0)
        self.activation_date_entry = tk.Entry(self.admin_s_sec1_frame)
        self.activation_date_entry.configure(
            borderwidth=2,
            font="{arial} 12 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.activation_date_entry.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.3,
            relx=0.25,
            rely=0.79,
            x=0,
            y=0,
        )
        self.activation_date_label = tk.Label(self.admin_s_sec1_frame)
        self.activation_date_label.configure(
            background="#F7FAE9",
            font="{arial} 11 {bold}",
            text="Account Activation Date",
        )
        self.activation_date_label.place(
            anchor="center", relx=0.23, rely=0.73, x=0, y=0
        )
        self.deactivation_date_entry = tk.Entry(self.admin_s_sec1_frame)
        self.deactivation_date_entry.configure(
            borderwidth=2,
            font="{arial} 12 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.deactivation_date_entry.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.3,
            relx=0.25,
            rely=0.92,
            x=0,
            y=0,
        )
        self.deactivation_date_label = tk.Label(self.admin_s_sec1_frame)
        self.deactivation_date_label.configure(
            background="#F7FAE9",
            font="{arial} 11 {bold}",
            text="Account Deactivation Date",
        )
        self.deactivation_date_label.place(
            anchor="center", relx=0.23, rely=0.86, x=0, y=0
        )
        self.save_dates_button = tk.Button(self.admin_s_sec1_frame)
        self.save_dates_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Save Dates",
        )
        self.save_dates_button.place(
            anchor="center",
            relheight=0.08,
            relwidth=0.3,
            relx=0.68,
            rely=0.87,
            x=0,
            y=0,
        )
        self.save_dates_button.bind("<Button>", self.save_dates, add="")
        self.admin_s_sec1_frame.place(
            anchor="center",
            relheight=0.65,
            relwidth=0.45,
            relx=0.26,
            rely=0.5,
            x=0,
            y=0,
        )
        self.admin_s_sec2_frame = tk.Frame(self.administrator_settings_frame)
        self.admin_s_sec2_frame.configure(background="#F7FAE9", height=200, width=200)
        self.secu_settings_label = tk.Label(self.admin_s_sec2_frame)
        self.secu_settings_label.configure(
            background="#F7FAE9", font="{arial} 20 {bold}", text="Security Settings"
        )
        self.secu_settings_label.place(anchor="center", relx=0.5, rely=0.1)
        self.min_pass_req_label = tk.Label(self.admin_s_sec2_frame)
        self.min_pass_req_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text="Minimum Password Requirements",
        )
        self.min_pass_req_label.place(anchor="center", relx=0.4, rely=0.19)
        self.pass_len_entry = tk.Entry(self.admin_s_sec2_frame)
        self.pass_len_entry.configure(
            borderwidth=2,
            font="{arial} 12 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.pass_len_entry.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.12,
            rely=0.28,
            x=0,
            y=0,
        )
        self.pass_len_label = tk.Label(self.admin_s_sec2_frame)
        self.pass_len_label.configure(
            background="#F7FAE9", font="{arial} 14 {bold}", text="Password Length"
        )
        self.pass_len_label.place(anchor="center", relx=0.35, rely=0.28)
        self.account_lockout_label = tk.Label(self.admin_s_sec2_frame)
        self.account_lockout_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="Account Lockout"
        )
        self.account_lockout_label.place(anchor="center", relx=0.26, rely=0.4)
        self.login_attempt_entry = tk.Entry(self.admin_s_sec2_frame)
        self.login_attempt_entry.configure(
            borderwidth=2,
            font="{arial} 12 {}",
            highlightbackground="#000000",
            highlightthickness=2,
        )
        self.login_attempt_entry.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.12,
            rely=0.49,
            x=0,
            y=0,
        )
        self.login_attem_label = tk.Label(self.admin_s_sec2_frame)
        self.login_attem_label.configure(
            background="#F7FAE9", font="{arial} 14 {bold}", text="Login Attempts"
        )
        self.login_attem_label.place(anchor="center", relx=0.35, rely=0.49, x=0, y=0)
        self.acc_lockout_rem_label = tk.Label(self.admin_s_sec2_frame)
        self.acc_lockout_rem_label.configure(
            background="#F7FAE9",
            font="{arial} 12 {}",
            justify="left",
            text="Consecutive failed log in attempts will \nresult of a locked account ",
        )
        self.acc_lockout_rem_label.place(anchor="center", relx=0.3, rely=0.57, x=0, y=0)
        self.save_settings_button = tk.Button(self.admin_s_sec2_frame)
        self.save_settings_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Save Settings",
        )
        self.save_settings_button.place(
            anchor="center", relheight=0.08, relwidth=0.4, relx=0.29, rely=0.7, x=0, y=0
        )
        self.save_settings_button.bind("<Button>", self.save_security, add="")
        self.admin_s_sec2_frame.place(
            anchor="center",
            relheight=0.65,
            relwidth=0.45,
            relx=0.74,
            rely=0.5,
            x=0,
            y=0,
        )
        self.settings_label = tk.Label(self.administrator_settings_frame)
        self.settings_label.configure(
            background="#E7E7E7",
            font="{arial} 24 {bold}",
            foreground="#000000",
            text="Settings",
        )
        self.settings_label.place(anchor="center", relx=0.1, rely=0.09, x=0, y=0)
        self.administrator_settings_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

        # SETTINGS-------------------------------------------------------------------------------------------------------

        # DB-SECTION--------------------------------------------------------------------------------------
        self.administrator_db_frame = tk.Frame(self.administrator_app)
        self.administrator_db_frame.configure(
            background="#E7E7E7", height=200, width=200
        )
        self.time_and_date_label_db = tk.Label(self.administrator_db_frame)
        self.time_and_date_label_db.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text=self.current_date_n_time,
        )
        self.time_and_date_label_db.place(
            anchor="center", relwidth=1, relx=0.5, rely=0.975, x=0, y=0
        )
        self.administrator_db_ttl_frame = tk.Frame(self.administrator_db_frame)
        self.administrator_db_ttl_frame.configure(
            background="#F7FAE9", height=200, width=200
        )
        self.ttl_students_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_students_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Total Students"
        )
        self.ttl_students_label.place(anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ttl_personnels_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text="Total Personnels",
        )
        self.ttl_personnels_label.place(anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.ttl_visitor_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_visitor_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Total Visitors"
        )
        self.ttl_visitor_label.place(anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ttl_frame.place(
            anchor="center", relheight=0.35, relwidth=0.9, relx=0.5, rely=0.72, x=0, y=0
        )
        self.administrator_db_ol_frame = tk.Frame(self.administrator_db_frame)
        self.administrator_db_ol_frame.configure(
            background="#F7FAE9", height=200, width=200
        )
        self.ol_students_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_students_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Present Students"
        )
        self.ol_students_label.place(anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ol_personnels_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text="Present Personnels",
        )
        self.ol_personnels_label.place(anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.ol_visitor_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_visitor_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Present Visitors"
        )
        self.ol_visitor_label.place(anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ol_frame.place(
            anchor="center", relheight=0.35, relwidth=0.9, relx=0.5, rely=0.33, x=0, y=0
        )
        self.dashboard_label = tk.Label(self.administrator_db_frame)
        self.dashboard_label.configure(
            background="#E7E7E7", font="{arial black} 48 {}", text="Dashboard"
        )
        self.dashboard_label.place(
            anchor="center",
            relheight=0.1,
            relx=0.5,
            rely=0.09,
        )
        self.administrator_db_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )
        # DB-SECTION--------------------------------------------------------------------------------------
        # HIDE-OTHER--------------------------------------------------------------------------------
        # to remove other sections
        self.db_appear_logic()
        # HIDE-OTHER--------------------------------------------------------------------------------
        self.administrator_frame3 = tk.Frame(self.administrator_app)
        self.administrator_frame3.configure(background="#0072bc", height=200, width=200)
        self.dashboard_section_label = tk.Label(self.administrator_frame3)
        self.dashboard_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Dashboard",
        )
        self.dashboard_section_label.place(anchor="w", relx=0.1, rely=0.1)
        self.dashboard_section_label.bind("<1>", self.dashboard_appear, add="")
        self.dashboard_section_label.bind("<Enter>", self.dashboard_hover, add="")
        self.dashboard_section_label.bind("<Leave>", self.dashboard_hover_out, add="")
        self.client_section_label = tk.Label(self.administrator_frame3)
        self.client_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Client",
        )
        self.client_section_label.place(anchor="w", relx=0.1, rely=0.16)
        self.client_section_label.bind("<1>", self.client_appear, add="")
        self.client_section_label.bind("<Enter>", self.client_hover, add="")
        self.client_section_label.bind("<Leave>", self.client_hover_out, add="")
        self.user_section_label = tk.Label(self.administrator_frame3)
        self.user_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="User",
        )
        self.user_section_label.place(anchor="w", relx=0.1, rely=0.22)
        self.user_section_label.bind("<1>", self.user_appear, add="")
        self.user_section_label.bind("<Enter>", self.user_hover, add="")
        self.user_section_label.bind("<Leave>", self.user_hover_out, add="")
        self.report_section_label = tk.Label(self.administrator_frame3)
        self.report_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Report",
        )
        self.report_section_label.place(anchor="w", relx=0.1, rely=0.28)
        self.report_section_label.bind("<1>", self.report_appear, add="")
        self.report_section_label.bind("<Enter>", self.report_hover, add="")
        self.report_section_label.bind("<Leave>", self.report_hover_out, add="")
        self.settings_section_label = tk.Label(self.administrator_frame3)
        self.settings_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Settings",
        )
        self.settings_section_label.place(anchor="w", relx=0.1, rely=0.34)
        self.settings_section_label.bind("<1>", self.settings_appear, add="")
        self.settings_section_label.bind("<Enter>", self.settings_hover, add="")
        self.settings_section_label.bind("<Leave>", self.settings_hover_out, add="")
        self.logout_label = tk.Label(self.administrator_frame3)
        self.logout_label.configure(
            background="#0072bc",
            font="{arial} 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Log Out",
        )
        self.logout_label.place(anchor="w", relx=0.1, rely=0.85)
        self.logout_label.bind("<1>", self.logout, add="")
        self.logout_label.bind("<Enter>", self.logout_hover, add="")
        self.logout_label.bind("<Leave>", self.logout_hover_out, add="")
        self.administrator_frame3.place(
            anchor="center", relheight=0.92, relwidth=0.22, relx=0.11, rely=0.54
        )
        # ----------------------------------------------------------------------------------
        self.administrator_frame2 = tk.Frame(self.administrator_app)
        self.administrator_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.administrator_frame2)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png"
        )
        self.app_name_logo.configure(
            background="#F7FAE9", image=self.img_SeekULogotypemicro, text="label1"
        )
        self.app_name_logo.place(anchor="center", relx=0.15, rely=0.55, x=0, y=0)
        self.app_logo_label = tk.Label(self.administrator_frame2)
        self.img_SeekUmicro = tk.PhotoImage(file=".\SeekU\SeekU micro.png")
        self.app_logo_label.configure(
            background="#F7FAE9", image=self.img_SeekUmicro, text="label1"
        )
        self.app_logo_label.place(anchor="center", relx=0.05, rely=0.5)
        self.administrator_frame2.place(
            anchor="center", relheight=0.08, relwidth=1.0, relx=0.50, rely=0.04
        )

        self.update_time()

        # Main widget
        self.mainwindow = self.administrator_app
        self.mainwindow.wm_attributes("-fullscreen", "True")

    # -------------------------------------------------------------------------------------------

    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    def hide_this_window(self):
        self.administrator_app.withdraw()

    def select_folder(self):
        self.administrator_app.attributes('-topmost', False)
        self.folder_selected = filedialog.askdirectory()
        print(self.folder_selected)
        self.administrator_app.attributes('-topmost', True)


    # this function updates the time below the window
    def update_time(self):
        self.now = datetime.now()
        self.current_date_n_time = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.time_and_date_label_c.configure(text=self.current_date_n_time)
        self.time_and_date_label_r.configure(text=self.current_date_n_time)
        self.time_and_date_label_db.configure(text=self.current_date_n_time)
        self.time_and_date_label_u.configure(text=self.current_date_n_time)
        self.time_and_date_label_s.configure(text=self.current_date_n_time)
        self.administrator_app.after(15, self.update_time)

    # APPEAR-LOGIC-------------------------------------------------------------------------------------------------------
    # this function removes all uncessesary widgets except the dasboard
    def db_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # users_forget------------------------------------
        self.administrator_users_frame.place_forget()
        # users_forget------------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # settings_forget-------------------------------------
        self.administrator_settings_frame.place_forget()
        # settings_forget-------------------------------------
        self.administrator_db_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    # this function removes all uncessesary widgets except the client
    def client_appear_logic(self):
        # users_forget------------------------------------
        self.administrator_users_frame.place_forget()
        # users_forget------------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # settings_forget-------------------------------------
        self.administrator_settings_frame.place_forget()
        # settings_forget-------------------------------------
        # db_forget----------------------------------------
        self.administrator_db_frame.place_forget()
        # db_forget----------------------------------------
        self.administrator_client_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    def users_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # settings_forget-------------------------------------
        self.administrator_settings_frame.place_forget()
        # settings_forget-------------------------------------
        # db_forget----------------------------------------
        self.administrator_db_frame.place_forget()
        # db_forget----------------------------------------
        self.administrator_users_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    # this function removes all uncessesary widgets except the reports
    def report_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # users_forget------------------------------------
        self.administrator_users_frame.place_forget()
        # users_forget------------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # settings_forget-------------------------------------
        self.administrator_settings_frame.place_forget()
        # settings_forget-------------------------------------
        #db_forget------------------------------------
        self.administrator_db_frame.place_forget()
        #db_forget------------------------------------
        self.administrator_report_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    def settings_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # users_forget------------------------------------
        self.administrator_users_frame.place_forget()
        # users_forget------------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        #db_forget------------------------------------
        self.administrator_db_frame.place_forget()
        #db_forget------------------------------------
        self.administrator_settings_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    # APPEAR-LOGIC-------------------------------------------------------------------------------------------------------

    # CLIENT-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    # this function will change the display according to the
    # selected option on the option menu for the clent section
    def change_layout_client(self):
        if self.clients_man_var.get() == "Manage Students":
            self.add_c_button.configure(text="Add Students")
            self.edit_c_button.configure(text="Edit Students")
            self.clients_list.configure(text="Students List")
            self.treeview.student_treeview(self.admin_c_sec3_frame)

        if self.clients_man_var.get() == "Manage Personnels":
            self.add_c_button.configure(text="Add Personnels")
            self.edit_c_button.configure(text="Edit Personnels")
            self.clients_list.configure(text="Personnels List")
            self.treeview.personnel_treeview(self.admin_c_sec3_frame)

        if self.clients_man_var.get() == "Manage Visitors":
            self.add_c_button.configure(text="Add Visitors")
            self.edit_c_button.configure(text="Edit Visitors")
            self.clients_list.configure(text="Visitors List")
            self.treeview.visitor_treeview(self.admin_c_sec3_frame)

    def add_clients_logic(self):
        # if self.clients_man_var.get() == "Manage Students":
        self.hide_this_window()
        self.select_folder()
        aCA.CameraApp(self.video_source,self.login_window,self.sel_cam_window, self.administrator_app,self.folder_selected, self.clients_man_var.get())
        """
            pass
        if self.clients_man_var.get() == "Manage Personnels":
            self.hide_this_window()
            self.select_folder()
            aCA.CameraApp(self.video_source,self.login_window,self.sel_cam_window, self.administrator_app,self.folder_selected, self.clients_man_var.get())
            pass
        if self.clients_man_var.get() == "Manage Visitors":
            self.hide_this_window()
            self.select_folder()
            aCA.CameraApp(self.video_source,self.login_window,self.sel_cam_window, self.administrator_app,self.folder_selected, self.clients_man_var.get())
            pass
        """

    def edit_clients_logic(self):
        if self.clients_man_var.get() == "Manage Students":
            self.hide_this_window()
            self.select_folder()
            self.edit_student_function()

        if self.clients_man_var.get() == "Manage Personnels":
            self.hide_this_window()
            self.select_folder()
            self.edit_personnel_function()

        if self.clients_man_var.get() == "Manage Visitors":
            self.select_folder()
            pass

    def search_clients_info_logic(self):
        if self.clients_man_var.get() == "Manage Students":
            data = self.search_c_entry.get()
            self.treeview.do_search_student(data)
        if self.clients_man_var.get() == "Manage Personnels":
            data = self.search_c_entry.get()
            self.treeview.do_search_personnel(data)
        if self.clients_man_var.get() == "Manage Visitors":
            data = self.search_c_entry.get()
            self.treeview.do_search_visitor(data)

    def edit_student_function(self):
        self.treeview.select_student_treeview_row()
        print(self.treeview.student_values)

        student_num = self.treeview.student_values[0]
        student_firstname = self.treeview.student_values[1]
        student_lastname = self.treeview.student_values[2]
        student_middlename = self.treeview.student_values[3]
        student_program = self.treeview.student_values[4]
        student_section = self.treeview.student_values[5]
        student_contact_num = self.treeview.student_values[6]
        student_address = self.treeview.student_values[7]
        student_status = self.treeview.student_values[8]

        eIS.EditStudentApp(
            student_num,
            student_firstname,
            student_lastname,
            student_middlename,
            student_program,
            student_section,
            student_contact_num,
            student_address,
            student_status,
            self.video_source,
            self.administrator_app,
            self.folder_selected ,
        )

    def edit_personnel_function(self):
        self.treeview.select_personnel_treeview_row()
        print(self.treeview.personnel_values)

        personnel_number = self.treeview.personnel_values[0]
        personnel_firstname = self.treeview.personnel_values[1]
        personnel_lastname = self.treeview.personnel_values[2]
        personnel_middlename = self.treeview.personnel_values[3]
        personnel_contact_num = self.treeview.personnel_values[4]
        personnel_address = self.treeview.personnel_values[5]
        personnel_type = self.treeview.personnel_values[6]
        personnel_status = self.treeview.personnel_values[7]

        eIP.EditPersonnelApp(
            personnel_number,
            personnel_firstname,
            personnel_lastname,
            personnel_middlename,
            personnel_contact_num,
            personnel_address,
            personnel_type,
            personnel_status,
            self.video_source,
            self.administrator_app,
            self.folder_selected ,
        )

    # CLIENT-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------

    # REPORT-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------

    # this function will change the display according to the
    # selected option on the option menu for the report section
    def change_layout_reports(self):
        if self.clients_rep_var.get() == "Students Report":
            self.treeview.student_report_treeview(self.admin_r_sec2_frame)

        if self.clients_rep_var.get() == "Personnels Report":
            self.treeview.personnel_report_treeview(self.admin_r_sec2_frame)

        if self.clients_rep_var.get() == "Visitors Report":
            self.treeview.visitor_report_treeview(self.admin_r_sec2_frame)

    def search_report_info_logic(self):
        if self.clients_rep_var.get() == "Students Report":
            data = self.search_r_entry.get()
            self.treeview.do_search_student_report(data)
        if self.clients_rep_var.get() == "Personnels Report":
            data = self.search_r_entry.get()
            self.treeview.do_search_personnel_report(data)
        if self.clients_rep_var.get() == "Visitors Report":
            data = self.search_r_entry.get()
            self.treeview.do_search_visitor_report(data)

    # REPORT-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    # USERS-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    def edit_user_function(self):
        self.treeview.select_user_treeview_row()

        print(self.treeview.user_values)
        username = self.treeview.user_values[1]
        password = self.treeview.user_values[2]
        firstname = self.treeview.user_values[3]
        lastname = self.treeview.user_values[4]
        user_type = self.treeview.user_values[5]
        user_status = self.treeview.user_values[6]
        uE.EditUserApp(username, password, firstname, lastname, user_type, user_status, self.administrator_app)
        self.hide_this_window()

    def register_user(self):
        uC.CreateUserApp(self.administrator_app)
        self.hide_this_window()

    # USERS-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    # SETTINGS-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------

    # SETTINGS-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    
    # DASBOARD-COMMANDS---------------------------------------------------------------------------------------------------------------
    def dashboard_appear(self, event=None):
        self.db_appear_logic()

    def dashboard_hover(self, event=None):
        self.dashboard_section_label.configure(foreground="#FFF200")

    def dashboard_hover_out(self, event=None):
        self.dashboard_section_label.configure(foreground="#F7FAE9")

    # DASBOARD-COMMANDS---------------------------------------------------------------------------------------------------------------

    # CLIENTS-COMMANDS---------------------------------------------------------------------------------------------------------------
    def client_appear(self, event=None):
        self.client_appear_logic()

    def client_hover(self, event=None):
        self.client_section_label.configure(foreground="#FFF200")

    def client_hover_out(self, event=None):
        self.client_section_label.configure(foreground="#F7FAE9")

    def open_diff_client(self, event=None):
        self.change_layout_client()

    def add_clients(self, event=None):
        self.add_clients_logic()

    def edit_clients(self, event=None):
        self.edit_clients_logic()

    def search_clients_info(self, event=None):
        self.search_clients_info_logic()

    # CLIENTS-COMMANDS---------------------------------------------------------------------------------------------------------------
    # USER-COMMANDS---------------------------------------------------------------------------------------------------------------

    def user_appear(self, event=None):
        self.users_appear_logic()

    def user_hover(self, event=None):
        self.user_section_label.configure(foreground="#FFF200")

    def user_hover_out(self, event=None):
        self.user_section_label.configure(foreground="#F7FAE9")

    def search_user_infos(self, event=None):
        data = self.search_u_entry.get()
        self.treeview.do_search_user(data)

    def edit_user_infos(self, event=None):
        self.hide_this_window()
        self.edit_user_function()

    def add_user_infos(self, event=None):
        self.hide_this_window()
        # uC.CreateUserApp()
        pass

    # USER-COMMANDS---------------------------------------------------------------------------------------------------------------
    # REPORTS-COMMANDS---------------------------------------------------------------------------------------------------------------

    def report_appear(self, event=None):
        self.report_appear_logic()

    def report_hover(self, event=None):
        self.report_section_label.configure(foreground="#FFF200")

    def report_hover_out(self, event=None):
        self.report_section_label.configure(foreground="#F7FAE9")

    def open_diff_report(self, event=None):
        self.change_layout_reports()

    def search_clients_reports(self, event=None):
        self.search_report_info_logic()

    def print_clients_reports(self, event=None):
        pass

    def save_clients_reports(self, event=None):
        pass

    # REPORTS-COMMANDS---------------------------------------------------------------------------------------------------------------
    # SETTINGS-COMMANDS---------------------------------------------------------------------------------------------------------------
    def settings_appear(self, event=None):
        self.settings_appear_logic()

    def settings_hover(self, event=None):
        self.settings_section_label.configure(foreground="#FFF200")

    def settings_hover_out(self, event=None):
        self.settings_section_label.configure(foreground="#F7FAE9")

    def export_database(self, event=None):
        pass

    def import_database(self, event=None):
        pass

    def save_dates(self, event=None):
        pass

    def save_security(self, event=None):
        pass

    # SETTINGS-COMMANDS---------------------------------------------------------------------------------------------------------------
    # LOGOUT-COMMANDS---------------------------------------------------------------------------------------------------------------
    def logout(self, event=None):
        # log in module appear
        self.login_window.deiconify()
        self.administrator_app.destroy()

    def logout_hover(self, event=None):
        self.logout_label.configure(foreground="#FFF200")

    def logout_hover_out(self, event=None):
        self.logout_label.configure(foreground="#F7FAE9")


# LOGOUT-COMMANDS---------------------------------------------------------------------------------------------------------------
