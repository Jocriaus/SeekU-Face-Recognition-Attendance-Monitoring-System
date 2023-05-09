#!/usr/bin/python3
import tkinter as tk
from datetime import datetime
from tkinter import filedialog
import tkinter.messagebox as messbx
import query_mod as qry
import edit_info_personnel as eIP
import edit_info_student as eIS
import edit_info_visitor as eIV
import user_create as uC
import user_edit as uE
import generate_report as gR
import add_client_select as aCS
import restore_data as rD
import backup_restore_mod as bR
import Treeview_table_mod as tbl
import os
import sys

class AdminHomeApp:
    def __init__(self, user, vid_source, login_mod, sel_cam):

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.user = user
        # add a condition if the user is high admin or low admin to restrict some access
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.now = datetime.now()
        self.current_date_n_time = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.backup = bR.BackupRestore()
        self.treeview = tbl.TreeviewGUI()
        self.sql_query = qry.dbQueries()
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
        self.treeview.student_treeview(self.admin_c_sec3_frame, "IsActive")
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
        # ATTENDANCE-------------------------------------------------------------------------------------------------------
        self.administrator_attendance_frame = tk.Frame(self.administrator_app)
        self.administrator_attendance_frame.configure(
            background="#E7E7E7", height=200, width=200
        )
        self.time_and_date_label_at = tk.Label(self.administrator_attendance_frame)
        self.time_and_date_label_at.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text=self.current_date_n_time,
        )
        self.time_and_date_label_at.place(
            anchor="center", relwidth=1, relx=0.5, rely=0.975, x=0, y=0
        )
        self.admin_at_sec1_frame = tk.Frame(self.administrator_attendance_frame)
        self.admin_at_sec1_frame.configure(background="#E7E7E7", height=200, width=200)
        self.search_clients_attendance = tk.Button(self.admin_at_sec1_frame)
        self.search_clients_attendance.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Search",
        )
        self.search_clients_attendance.place(
            anchor="center", relheight=0.5, relwidth=0.16, relx=0.9, rely=0.5, x=0, y=0
        )
        self.search_clients_attendance.bind(
            "<Button>", self.search_client_attendance, add=""
        )
        self.search_at_entry = tk.Entry(self.admin_at_sec1_frame)
        self.search_at_entry.configure(background="#F7FAE9", font="{arial} 24 {}")
        self.search_at_entry.place(anchor="center", relx=0.63, rely=0.5, x=0, y=0)
        self.admin_at_sec1_frame.place(
            anchor="center", relheight=0.1, relwidth=0.90, relx=0.5, rely=0.09
        )
        self.admin_at_sec2_frame = tk.Frame(self.administrator_attendance_frame)
        self.admin_at_sec2_frame.configure(background="#F7FAE9", height=200, width=200)
        self.treeview.visitor_attendance_treeview(self.admin_at_sec2_frame)
        self.treeview.personnel_attendance_treeview(self.admin_at_sec2_frame)
        self.treeview.student_attendance_treeview(self.admin_at_sec2_frame)
        self.admin_at_sec2_frame.place(
            anchor="center", relheight=0.65, relwidth=0.9, relx=0.5, rely=0.5, x=0, y=0
        )
        self.clients_at_var = tk.StringVar(value="Students Attendance")
        __values = [
            "Students Attendance",
            "Personnels Attendance",
            "Visitors Attendance",
        ]
        self.client_attendance_optionmenu = tk.OptionMenu(
            self.administrator_attendance_frame,
            self.clients_at_var,
            *__values,
            command=self.open_diff_attendance
        )
        self.client_attendance_optionmenu.place(
            anchor="center", relx=0.2, rely=0.09, x=0, y=0
        )
        self.client_attendance_optionmenu.configure(font="{arial} 20 {bold}")
        self.client_attendance_options = self.administrator_app.nametowidget(
            self.client_attendance_optionmenu.menuname
        )
        self.client_attendance_options.config(font="{arial} 16")
        self.administrator_attendance_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )
        # ATTENDANCE-------------------------------------------------------------------------------------------------------
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
        self.treeview.user_treeview(self.admin_u_sec2_frame, "IsActive")
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
        self.treeview.visitor_report_treeview(self.admin_r_sec2_frame)
        self.treeview.personnel_report_treeview(self.admin_r_sec2_frame)
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
        self.generate_report = tk.Button(self.administrator_report_frame)
        self.generate_report.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Generate Report",
        )
        self.generate_report.place(
            anchor="center",
            relheight=0.08,
            relwidth=0.20,
            relx=0.85,
            rely=0.875,
            x=0,
            y=0,
        )
        self.generate_report.bind("<Button>", self.generate_clients_reports, add="")
        self.administrator_report_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )
        # REPORT-------------------------------------------------------------------------------------------------------
        # ARCHIVED-------------------------------------------------------------------------------------------------------
        self.administrator_archived_frame = tk.Frame(self.administrator_app)
        self.administrator_archived_frame.configure(
            background="#E7E7E7", height=200, width=200
        )
        self.time_and_date_label_a = tk.Label(self.administrator_archived_frame)
        self.time_and_date_label_a.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text=self.current_date_n_time,
        )
        self.time_and_date_label_a.place(
            anchor="center", relwidth=1, relx=0.5, rely=0.975, x=0, y=0
        )
        self.admin_a_sec1_frame = tk.Frame(self.administrator_archived_frame)
        self.admin_a_sec1_frame.configure(background="#E7E7E7", height=200, width=200)
        self.edit_a_button = tk.Button(self.admin_a_sec1_frame)
        self.edit_a_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Edit Students",
        )
        self.edit_a_button.place(anchor="center", relx=0.85, rely=0.5, x=0, y=0)
        self.edit_a_button.bind("<Button>", self.edit_archiveds, add="")
        self.admin_a_sec1_frame.place(
            anchor="center", relheight=0.1, relwidth=1.0, relx=0.5, rely=0.09
        )
        self.admin_a_sec2_frame = tk.Frame(self.administrator_archived_frame)
        self.admin_a_sec2_frame.configure(background="#F7FAE9", height=200, width=200)
        self.search_a_button = tk.Button(self.admin_a_sec2_frame)
        self.search_a_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text="Search",
        )
        self.search_a_button.place(
            anchor="center", relheight=0.5, relwidth=0.16, relx=0.9, rely=0.5, x=0, y=0
        )
        self.admin_a_sec1_frame.place(
            anchor="center", relheight=0.1, relwidth=1.0, relx=0.5, rely=0.09
        )
        self.search_a_button.bind("<Button>", self.search_archived_info, add="")
        self.search_a_entry = tk.Entry(self.admin_a_sec2_frame)
        self.search_a_entry.configure(background="#E7E7E7", font="{arial} 24 {}")
        self.search_a_entry.place(anchor="center", relx=0.63, rely=0.5, x=0, y=0)
        self.archived_list = tk.Label(self.admin_a_sec2_frame)
        self.archived_list.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text="Students List",
        )
        self.archived_list.place(anchor="center", relx=0.125, rely=0.5, x=0, y=0)
        self.admin_a_sec2_frame.place(
            anchor="center", relheight=0.1, relwidth=0.90, relx=0.5, rely=0.22
        )
        self.admin_a_sec3_frame = tk.Frame(self.administrator_archived_frame)
        self.admin_a_sec3_frame.configure(background="#F7FAE9", height=200, width=200)
        self.treeview.student_treeview(self.admin_a_sec3_frame, "IsArchived")
        self.admin_a_sec3_frame.place(
            anchor="center", relheight=0.6, relwidth=0.9, relx=0.5, rely=0.6, x=0, y=0
        )
        self.archived_man_var = tk.StringVar(value="Archived Students")
        __values = [
            "Archived Students",
            "Archived Personnels",
            "Archived Visitors",
            "Archived User",
        ]
        self.manage_archived_optionmenu = tk.OptionMenu(
            self.administrator_archived_frame,
            self.archived_man_var,
            *__values,
            command=self.open_diff_archived
        )
        self.manage_archived_optionmenu.configure(font="{arial} 20 {bold}")
        self.manage_archived_optionmenu.place(
            anchor="center", relx=0.17, rely=0.09, x=0, y=0
        )
        self.manage_archived_options = self.administrator_app.nametowidget(
            self.manage_archived_optionmenu.menuname
        )
        self.manage_archived_options.config(font="{arial} 16")
        self.administrator_archived_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )
        # ARCHIVED-------------------------------------------------------------------------------------------------------

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
        self.student_stat_label.place(anchor="center", relx=0.22, rely=0.6, x=0, y=0)
        self.stud_stat_rem_label = tk.Label(self.admin_s_sec1_frame)
        self.stud_stat_rem_label.configure(
            background="#F7FAE9",
            font="{arial} 12 {}",
            justify="left",
            text="Student Informations will be\ndeactivated on selected date\nFormat = YYYY-MM-DD",
        )
        self.stud_stat_rem_label.place(anchor="center", relx=0.325, rely=0.68, x=0, y=0)
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
            rely=0.86,
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
            anchor="center", relx=0.23, rely=0.80, x=0, y=0
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
        self.display_settings()
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
        self.total_student = self.sql_query.get_student_count()
        self.ttl_students_no_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_students_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.total_student
        )
        self.ttl_students_no_label.place(
            anchor="center", relx=0.16, rely=0.65, x=0, y=0
        )
        self.ttl_personnels_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text="Total Personnels",
        )
        self.ttl_personnels_label.place(anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.total_personnel = self.sql_query.get_personnel_count()
        self.ttl_personnels_no_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_personnels_no_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 30 {bold}",
            text=self.total_personnel,
        )
        self.ttl_personnels_no_label.place(
            anchor="center", relx=0.5, rely=0.65, x=0, y=0
        )
        self.ttl_visitor_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_visitor_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Total Visitors"
        )
        self.ttl_visitor_label.place(anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.total_visitor = self.sql_query.get_visitor_count()
        self.ttl_visitor_no_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_visitor_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.total_visitor
        )
        self.ttl_visitor_no_label.place(anchor="center", relx=0.84, rely=0.65, x=0, y=0)
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

        self.present_students = self.sql_query.get_student_attendance_count()

        self.ol_students_no_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_students_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.present_students
        )
        self.ol_students_no_label.place(anchor="center", relx=0.16, rely=0.65, x=0, y=0)
        self.ol_personnels_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text="Present Personnels",
        )
        self.ol_personnels_label.place(anchor="center", relx=0.5, rely=0.25, x=0, y=0)

        self.present_personnels = self.sql_query.get_personnel_attendance_count()

        self.ol_personnels_no_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_personnels_no_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 30 {bold}",
            text=self.present_personnels,
        )
        self.ol_personnels_no_label.place(
            anchor="center", relx=0.5, rely=0.65, x=0, y=0
        )

        self.ol_visitor_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_visitor_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Present Visitors"
        )
        self.ol_visitor_label.place(anchor="center", relx=0.84, rely=0.25, x=0, y=0)

        self.present_visitor = self.sql_query.get_visitor_attendance_count()

        self.ol_visitor_no_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_visitor_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.present_visitor
        )
        self.ol_visitor_no_label.place(anchor="center", relx=0.84, rely=0.65, x=0, y=0)

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
        self.attendance_section_label = tk.Label(self.administrator_frame3)
        self.attendance_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Attendance",
        )
        self.attendance_section_label.place(anchor="w", relx=0.1, rely=0.22)
        self.attendance_section_label.bind("<1>", self.attendance_appear, add="")
        self.attendance_section_label.bind("<Enter>", self.attendance_hover, add="")
        self.attendance_section_label.bind("<Leave>", self.attendance_hover_out, add="")

        self.user_section_label = tk.Label(self.administrator_frame3)
        self.user_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="User",
        )
        self.user_section_label.place(anchor="w", relx=0.1, rely=0.28)
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
        self.report_section_label.place(anchor="w", relx=0.1, rely=0.34)
        self.report_section_label.bind("<1>", self.report_appear, add="")
        self.report_section_label.bind("<Enter>", self.report_hover, add="")
        self.report_section_label.bind("<Leave>", self.report_hover_out, add="")
        self.archived_section_label = tk.Label(self.administrator_frame3)
        self.archived_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Archived",
        )
        self.archived_section_label.place(anchor="w", relx=0.1, rely=0.40)
        self.archived_section_label.bind("<1>", self.archived_appear, add="")
        self.archived_section_label.bind("<Enter>", self.archived_hover, add="")
        self.archived_section_label.bind("<Leave>", self.archived_hover_out, add="")

        self.settings_section_label = tk.Label(self.administrator_frame3)
        self.settings_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text="Settings",
        )
        self.settings_section_label.place(anchor="w", relx=0.1, rely=0.46)
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
        self.set_user()

        # Main widget
        self.mainwindow = self.administrator_app
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)
        self.mainwindow.wm_attributes("-fullscreen", "True")
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)

    # -------------------------------------------------------------------------------------------

    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    def hide_this_window(self):
        self.administrator_app.withdraw()

    def fix_path(self, path):
        newpath = ""
        for char in path:
            if char == "/":
                newpath += "\\"
            else:
                newpath += char
        return newpath

    def select_folder(self):
        self.administrator_app.attributes("-topmost", False)
        folder_select = filedialog.askdirectory(title="Select Folder")
        if folder_select == "":
            folder_select = False
            return folder_select
        else:
            return folder_select

    def select_file(self):
        self.administrator_app.attributes("-topmost", False)
        file_select = filedialog.askopenfilename()
        if file_select == "":
            file_select = False
            return file_select
        else:
            return file_select

    def set_user(self):
        if self.user == "Staff":
            self.add_user_button.configure(state="disabled")
            self.edit_user_button.configure(state="disabled")
            self.import_db_button.configure(state="disabled")
            self.deactivation_date_entry.configure(state="disabled")
            self.login_attempt_entry.configure(state="disabled")
            self.pass_len_entry.configure(state="disabled")
            self.save_settings_button.configure(state="disabled")


    # this function updates the time below the window
    def update_time(self):
        self.now = datetime.now()
        self.current_date_n_time = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.time_and_date_label_c.configure(text=self.current_date_n_time)
        self.time_and_date_label_r.configure(text=self.current_date_n_time)
        self.time_and_date_label_db.configure(text=self.current_date_n_time)
        self.time_and_date_label_u.configure(text=self.current_date_n_time)
        self.time_and_date_label_s.configure(text=self.current_date_n_time)
        self.time_and_date_label_at.configure(text=self.current_date_n_time)
        self.time_and_date_label_a.configure(text=self.current_date_n_time)
        self.administrator_app.after(15, self.update_time)

    def starting_layout(self):
        self.treeview.student_treeview(self.admin_c_sec3_frame, "IsActive")
        self.treeview.student_treeview(self.admin_a_sec3_frame, "IsArchived")

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
        # archived_forget------------------------------------
        self.administrator_archived_frame.place_forget()
        # archived_forget-----------------------------------

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
        # archived_forget------------------------------------
        self.administrator_archived_frame.place_forget()
        # archived_forget-----------------------------------
        # attendance_forget-----------------------------------
        self.administrator_attendance_frame.place_forget()
        # attendance_forget-----------------------------------
        self.administrator_client_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    # this function removes all uncessesary widgets except the reports
    def attendance_appear_logic(self):
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
        # db_forget------------------------------------
        self.administrator_db_frame.place_forget()
        # db_forget------------------------------------
        # archived_forget------------------------------------
        self.administrator_archived_frame.place_forget()
        # archived_forget-----------------------------------
        self.administrator_attendance_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    def users_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # attendance_forget-----------------------------------
        self.administrator_attendance_frame.place_forget()
        # attendance_forget-----------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # settings_forget-------------------------------------
        self.administrator_settings_frame.place_forget()
        # settings_forget-------------------------------------
        # db_forget----------------------------------------
        self.administrator_db_frame.place_forget()
        # db_forget----------------------------------------
        # archived_forget------------------------------------
        self.administrator_archived_frame.place_forget()
        # archived_forget-----------------------------------
        self.administrator_users_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    # this function removes all uncessesary widgets except the reports
    def report_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # attendance_forget-----------------------------------
        self.administrator_attendance_frame.place_forget()
        # attendance_forget-----------------------------------
        # users_forget------------------------------------
        self.administrator_users_frame.place_forget()
        # users_forget------------------------------------
        # settings_forget-------------------------------------
        self.administrator_settings_frame.place_forget()
        # settings_forget-------------------------------------
        # db_forget------------------------------------
        self.administrator_db_frame.place_forget()
        # db_forget------------------------------------
        # archived_forget------------------------------------
        self.administrator_archived_frame.place_forget()
        # archived_forget-----------------------------------

        self.administrator_report_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    def archived_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # attendance_forget-----------------------------------
        self.administrator_attendance_frame.place_forget()
        # attendance_forget-----------------------------------
        # users_forget------------------------------------
        self.administrator_users_frame.place_forget()
        # users_forget------------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # db_forget------------------------------------
        self.administrator_db_frame.place_forget()
        # db_forget------------------------------------
        # settings_forget-------------------------------------
        self.administrator_settings_frame.place_forget()
        # settings_forget-------------------------------------
        self.administrator_archived_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    def settings_appear_logic(self):
        # client_forget------------------------------------
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # attendance_forget-----------------------------------
        self.administrator_attendance_frame.place_forget()
        # attendance_forget-----------------------------------
        # users_forget------------------------------------
        self.administrator_users_frame.place_forget()
        # users_forget------------------------------------
        # report_forget------------------------------------
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # db_forget------------------------------------
        self.administrator_db_frame.place_forget()
        # db_forget------------------------------------
        # archived_forget------------------------------------
        self.administrator_archived_frame.place_forget()
        # archived_forget-----------------------------------
        self.administrator_settings_frame.place(
            anchor="center", relheight=0.95, relwidth=0.78, relx=0.61, rely=0.525
        )

    # APPEAR-LOGIC-------------------------------------------------------------------------------------------------------
    #------------
    def set_dashboard(self):
        self.total_student = self.sql_query.get_student_count()
        self.total_personnel = self.sql_query.get_personnel_count()
        self.total_visitor = self.sql_query.get_visitor_count()
        self.present_students = self.sql_query.get_student_attendance_count()
        self.present_personnels = self.sql_query.get_personnel_attendance_count()
        self.present_visitor = self.sql_query.get_visitor_attendance_count()
        self.ol_visitor_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.present_visitor
        )
        self.ol_personnels_no_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 30 {bold}",
            text=self.present_personnels,
        )
        self.ol_students_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.present_students
        )
        self.ttl_students_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.total_student
        )
        self.ttl_personnels_no_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 30 {bold}",
            text=self.total_personnel,
        )
        self.ttl_visitor_no_label.configure(
            background="#F7FAE9", font="{arial} 30 {bold}", text=self.total_visitor
        )
    #------------
    # CLIENT-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    # this function will change the display according to the
    # selected option on the option menu for the clent section
    def change_layout_client(self):
        if self.clients_man_var.get() == "Manage Students":
            self.add_c_button.configure(text="Add Students")
            self.edit_c_button.configure(text="Edit Students")
            self.clients_list.configure(text="Students List")
            self.treeview.student_treeview(self.admin_c_sec3_frame, "IsActive")

        if self.clients_man_var.get() == "Manage Personnels":
            self.add_c_button.configure(text="Add Personnels")
            self.edit_c_button.configure(text="Edit Personnels")
            self.clients_list.configure(text="Personnels List")
            self.treeview.personnel_treeview(self.admin_c_sec3_frame, "IsActive")

        if self.clients_man_var.get() == "Manage Visitors":
            self.add_c_button.configure(text="Add Visitors")
            self.edit_c_button.configure(text="Edit Visitors")
            self.clients_list.configure(text="Visitors List")
            self.treeview.visitor_treeview(self.admin_c_sec3_frame, "IsActive")

    def add_clients_logic(self):
        # if self.clients_man_var.get() == "Manage Students":
        aCS.AddSelectorApp(
            self.video_source,
            self.administrator_app,
            self.clients_man_var.get(),
            self.refresh_clients_logic,
        )

    def edit_clients_logic(self):
        if self.clients_man_var.get() == "Manage Students":
            folder = self.select_folder()
            if folder:
                self.edit_student_function(folder, self.clients_man_var.get(), False)

        if self.clients_man_var.get() == "Manage Personnels":
            folder = self.select_folder()
            if folder:
                self.edit_personnel_function(folder, self.clients_man_var.get(),False)

        if self.clients_man_var.get() == "Manage Visitors":
            folder = self.select_folder()
            if folder:
                self.edit_visitor_function(folder, self.clients_man_var.get(),False)

    def search_clients_info_logic(self):
        if self.clients_man_var.get() == "Manage Students":
            data = self.search_c_entry.get()
            self.treeview.do_search_student(data, "IsActive")
        if self.clients_man_var.get() == "Manage Personnels":
            data = self.search_c_entry.get()
            self.treeview.do_search_personnel(data, "IsActive")
        if self.clients_man_var.get() == "Manage Visitors":
            data = self.search_c_entry.get()
            self.treeview.do_search_visitor(data, "IsActive")

    def edit_student_function(self, folder, types, this_is_archive):

        self.treeview.select_student_treeview_row()
        print(self.treeview.student_values)

        if self.treeview.student_values:
            student_num = self.treeview.student_values[0]
            student_firstname = self.treeview.student_values[1]
            student_lastname = self.treeview.student_values[2]
            student_middlename = self.treeview.student_values[3]
            student_program = self.treeview.student_values[4]
            student_section = self.treeview.student_values[5]
            student_contact_num = self.treeview.student_values[6]
            student_address = self.treeview.student_values[7]
            student_status = self.treeview.student_values[8]

            path_check = folder +f"/{student_num}.jpg"
            if os.path.exists(path_check):
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
                    folder,
                    types,
                    self.refresh_clients_logic,
                    this_is_archive
                )
                self.hide_this_window()
            else:
                messbx.showwarning("Warning",
                    "No image was found in the directory matching the entered client number.",
                    )
        else:
            messbx.showwarning("Warning", "Please choose an item to modify.")

    def edit_personnel_function(self, folder, types,this_is_archive):
        self.treeview.select_personnel_treeview_row()
        print(self.treeview.personnel_values)

        if self.treeview.personnel_values:
            personnel_number = self.treeview.personnel_values[0]
            personnel_firstname = self.treeview.personnel_values[1]
            personnel_lastname = self.treeview.personnel_values[2]
            personnel_middlename = self.treeview.personnel_values[3]
            personnel_contact_num = self.treeview.personnel_values[4]
            personnel_address = self.treeview.personnel_values[5]
            personnel_type = self.treeview.personnel_values[6]
            personnel_status = self.treeview.personnel_values[7]

            path_check = folder +f"/{personnel_number}.jpg"
            if os.path.exists(path_check):
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
                    folder,
                    types,
                    self.refresh_clients_logic,
                    this_is_archive
                )
                self.hide_this_window()
            else:
                messbx.showwarning("Warning",
                    "No image was found in the directory matching the entered client number.",
                    )
        else:
            messbx.showwarning("Warning", "Please choose an item to modify.")

    def edit_visitor_function(self, folder, types,this_is_archive):
        self.treeview.select_visitor_treeview_row()
        print(self.treeview.visitor_values)

        if self.treeview.visitor_values:

            visitor_number = self.treeview.visitor_values[0]
            visitor_firstname = self.treeview.visitor_values[1]
            visitor_lastname = self.treeview.visitor_values[2]
            visitor_contact_num = self.treeview.visitor_values[3]
            visitor_address = self.treeview.visitor_values[4]
            visitor_status = self.treeview.visitor_values[5]

            path_check = folder +f"/{visitor_number}.jpg"
            if os.path.exists(path_check):
                eIV.EditVisitorApp(
                    visitor_number,
                    visitor_firstname,
                    visitor_lastname,
                    visitor_contact_num,
                    visitor_address,
                    visitor_status,
                    self.video_source,
                    self.administrator_app,
                    folder,
                    types,
                    self.refresh_clients_logic,
                    this_is_archive
                )
                self.hide_this_window()
            else:
                messbx.showwarning("Warning",
                    "No image was found in the directory matching the entered client number.",
                    )
        else:
            messbx.showwarning("Warning", "Please choose an item to modify.")

    def refresh_clients_logic(self, types, status):
        if types == "Manage Students":
            self.treeview.refresh_student_treeview(status)

        if types == "Manage Personnels":
            self.treeview.refresh_personnel_treeview(status)

        if types == "Manage Visitors":
            self.treeview.refresh_visitor_treeview(status)

        if types == "Archived Students":
            self.treeview.refresh_student_treeview(status)

        if types == "Archived Personnels":
            self.treeview.refresh_personnel_treeview(status)

        if types == "Archived Visitors":
            self.treeview.refresh_visitor_treeview(status)

    # CLIENT-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    # ATTENDANCE-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------

    # this function will change the display according to the
    # selected option on the option menu for the report section
    def change_layout_attendance(self):
        if self.clients_at_var.get() == "Students Attendance":
            self.treeview.refresh_student_att_treeview()
            self.treeview.student_attendance_treeview(self.admin_at_sec2_frame)

        if self.clients_at_var.get() == "Personnels Attendance":
            self.treeview.refresh_personnel_att_treeview()
            self.treeview.personnel_attendance_treeview(self.admin_at_sec2_frame)

        if self.clients_at_var.get() == "Visitors Attendance":
            self.treeview.refresh_visitor_att_treeview()
            self.treeview.visitor_attendance_treeview(self.admin_at_sec2_frame)

    def search_attendance_info_logic(self):
        if self.clients_at_var.get() == "Students Attendance":
            data = self.search_at_entry.get()
            self.treeview.do_search_student_attendance(data)
        if self.clients_at_var.get() == "Personnels Attendance":
            data = self.search_at_entry.get()
            self.treeview.do_search_personnel_attendance(data)
        if self.clients_at_var.get() == "Visitors Attendance":
            data = self.search_at_entry.get()
            self.treeview.do_search_visitor_attendance(data)

    def refresh_attendance_treeviews(self):
        self.treeview.refresh_student_att_treeview()
        self.treeview.refresh_personnel_att_treeview()
        self.treeview.refresh_visitor_att_treeview()

    # ATTENDANCE-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
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
    def edit_user_function(self, this_is_archive):
        self.treeview.select_user_treeview_row()

        print(self.treeview.user_values)

        if self.treeview.user_values:
            username = self.treeview.user_values[1]
            password = self.treeview.user_values[2]
            firstname = self.treeview.user_values[3]
            lastname = self.treeview.user_values[4]
            user_type = self.treeview.user_values[5]
            user_status = self.treeview.user_values[6]
            uE.EditUserApp(
                username,
                password,
                firstname,
                lastname,
                user_type,
                user_status,
                self.administrator_app,
                self.refresh_user_logic,
                this_is_archive
            )
        else:
            messbx.showwarning("Warning", "Please choose an item to modify.")

    def register_user(self):
        uC.CreateUserApp(self.administrator_app, self.refresh_user_logic)

    def refresh_user_logic(self, status):
        self.treeview.refresh_user_treeview(status)

    # USERS-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    # ARCHIVED-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    # this function will change the display according to the
    # selected option on the option menu for the clent section
    def change_layout_archived(self):
        if self.archived_man_var.get() == "Archived Students":
            self.edit_a_button.configure(text="Edit Students", state = "normal")
            self.archived_list.configure(text="Students List")
            self.treeview.student_treeview(self.admin_a_sec3_frame, "IsArchived")
            self.refresh_clients_logic(self.archived_man_var.get(), "IsArchived")
            

        if self.archived_man_var.get() == "Archived Personnels":
            self.edit_a_button.configure(text="Edit Personnels", state = "normal")
            self.archived_list.configure(text="Personnels List")
            self.treeview.personnel_treeview(self.admin_a_sec3_frame, "IsArchived")
            self.refresh_clients_logic(self.archived_man_var.get(), "IsArchived")

        if self.archived_man_var.get() == "Archived Visitors":
            self.edit_a_button.configure(text="Edit Visitors", state = "normal")
            self.archived_list.configure(text="Visitors List")
            self.treeview.visitor_treeview(self.admin_a_sec3_frame, "IsArchived")
            self.refresh_clients_logic(self.archived_man_var.get(), "IsArchived")

        if self.archived_man_var.get() == "Archived User":
            if self.user == "Staff":
                self.edit_a_button.configure(text="Edit User", state= "disabled")
                self.archived_list.configure(text="User List")
                self.treeview.user_treeview(self.admin_a_sec3_frame, "IsArchived")
                self.refresh_clients_logic(self.archived_man_var.get(), "IsArchived")
            else:
                self.edit_a_button.configure(text="Edit User", state= "normal")
                self.archived_list.configure(text="User List")
                self.treeview.user_treeview(self.admin_a_sec3_frame, "IsArchived")
                self.refresh_clients_logic(self.archived_man_var.get(), "IsArchived")
                

    def edit_archived_logic(self):
        if self.archived_man_var.get() == "Archived Students":
            folder = self.select_folder()
            if folder:
                self.edit_student_function(folder, self.archived_man_var.get(), True)

        if self.archived_man_var.get() == "Archived Personnels":
            folder = self.select_folder()
            if folder:
                self.edit_personnel_function(folder, self.archived_man_var.get(), True)

        if self.archived_man_var.get() == "Archived Visitors":
            folder = self.select_folder()
            if folder:
                self.edit_visitor_function(folder, self.archived_man_var.get(), True)

        if self.archived_man_var.get() == "Archived User":
            if self.edit_a_button.state() == "disabled":
                pass
            else:
                self.edit_user_function(True)    

    def search_archived_info_logic(self):
        if self.archived_man_var.get() == "Archived Students":
            data = self.search_a_entry.get()
            self.treeview.do_search_student(data, "IsArchived")
        if self.archived_man_var.get() == "Archived Personnels":
            data = self.search_a_entry.get()
            self.treeview.do_search_personnel(data, "IsArchived")
        if self.archived_man_var.get() == "Archived Visitors":
            data = self.search_a_entry.get()
            self.treeview.do_search_visitor(data, "IsArchived")
        if self.archived_man_var.get() == "Archived User":
            data = self.search_a_entry.get()
            self.treeview.do_search_user(data, "IsArchived")

    # ARCHIVED-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------

    # SETTINGS-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------
    def display_settings(self):
        log_in_attempt = self.sql_query.get_login_attempts()
        password_len = self.sql_query.get_password_length()
        sem_end = self.sql_query.get_end_settings()

        self.login_attempt_entry.insert(0, log_in_attempt)
        self.pass_len_entry.insert(0, password_len)
        self.deactivation_date_entry.insert(0, sem_end)

    def activation_settings_save(self):
        if len(self.deactivation_date_entry.get()) != 0:
            try:
                self.sql_query.set_sem_settings(self.deactivation_date_entry.get())
                messbx.showinfo("Saved", "Settings have been saved successfully!")
            except ValueError:
                messbx.showerror(
                    "Error",
                    "Please use the format YYYY-MM-DD as the data format provided is incorrect.",
                )
            except Exception:
                messbx.showerror(
                    "Error",
                    "Please use the format YYYY-MM-DD as the data format provided is incorrect.",
                )
        else:
            messbx.showwarning(
                "Warning", "Kindly ensure all fields are filled by entering a value."
            )

    def security_settings_save(self):
        pass_len = self.pass_len_entry.get()
        login_attempt = self.login_attempt_entry.get()
        if pass_len.isnumeric() and login_attempt.isnumeric():
            self.sql_query.set_pass_len_log_att(pass_len, login_attempt)
            messbx.showinfo("Saved", "Settings have been saved successfully!")
        else:
            messbx.showerror("Error", "Please enter numerical values only.")

    # SETTINGS-SECTION-FUNCTIONS-LOGIC-------------------------------------------------------------------------------------------------

    # DASBOARD-COMMANDS---------------------------------------------------------------------------------------------------------------
    def dashboard_appear(self, event=None):
        self.set_dashboard()
        self.db_appear_logic()

    def dashboard_hover(self, event=None):
        self.dashboard_section_label.configure(foreground="#FFF200")

    def dashboard_hover_out(self, event=None):
        self.dashboard_section_label.configure(foreground="#F7FAE9")

    # DASBOARD-COMMANDS---------------------------------------------------------------------------------------------------------------

    # CLIENTS-COMMANDS---------------------------------------------------------------------------------------------------------------
    def client_appear(self, event=None):
        self.client_appear_logic()
        self.change_layout_client()

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

    # ATTENDANCE-COMMANDS---------------------------------------------------------------------------------------------------------------

    def attendance_appear(self, event=None):
        self.attendance_appear_logic()
        self.refresh_attendance_treeviews()

    def open_diff_attendance(self, event=None):
        self.change_layout_attendance()

    def attendance_hover(self, event=None):
        self.attendance_section_label.configure(foreground="#FFF200")

    def attendance_hover_out(self, event=None):
        self.attendance_section_label.configure(foreground="#F7FAE9")

    def search_client_attendance(self, event=None):
        self.search_attendance_info_logic()

    # ATTENDANCE-COMMANDS---------------------------------------------------------------------------------------------------------------

    # USER-COMMANDS---------------------------------------------------------------------------------------------------------------

    def user_appear(self, event=None):
        if self.user == "Staff":
            pass
        else:
            self.treeview.user_treeview(self.admin_u_sec2_frame, "IsActive")
            self.users_appear_logic()
            self.refresh_user_logic("IsActive")

    def user_hover(self, event=None):
        self.user_section_label.configure(foreground="#FFF200")

    def user_hover_out(self, event=None):
        self.user_section_label.configure(foreground="#F7FAE9")

    def search_user_infos(self, event=None):
        data = self.search_u_entry.get()
        self.treeview.do_search_user(data, "IsActive")

    def edit_user_infos(self, event=None):
        self.edit_user_function(False)

    def add_user_infos(self, event=None):
        self.register_user()

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

    def generate_clients_reports(self, event=None):
        gR.SavePrintReportApp(self.clients_rep_var.get())

    # REPORTS-COMMANDS---------------------------------------------------------------------------------------------------------------
    # ARCHIVED-COMMANDS---------------------------------------------------------------------------------------------------------------
    def archived_appear(self, event=None):
        self.archived_appear_logic()
        self.change_layout_archived()

    def archived_hover(self, event=None):
        self.archived_section_label.configure(foreground="#FFF200")

    def archived_hover_out(self, event=None):
        self.archived_section_label.configure(foreground="#F7FAE9")

    def open_diff_archived(self, event=None):
        self.change_layout_archived()

    def edit_archiveds(self, event=None):
        self.edit_archived_logic()

    def search_archived_info(self, event=None):
        self.search_archived_info_logic()

    # ARCHIVED-COMMANDS---------------------------------------------------------------------------------------------------------------

    # SETTINGS-COMMANDS---------------------------------------------------------------------------------------------------------------
    def settings_appear(self, event=None):
        self.settings_appear_logic()

    def settings_hover(self, event=None):
        self.settings_section_label.configure(foreground="#FFF200")

    def settings_hover_out(self, event=None):
        self.settings_section_label.configure(foreground="#F7FAE9")

    def export_database(self, event=None):
        folder = self.select_folder()
        if folder:
            self.backup.backup_data(folder)

    def import_database(self, event=None):
        rD.RestoreApp()

    def save_dates(self, event=None):
        self.activation_settings_save()

    def save_security(self, event=None):
        self.security_settings_save()

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
