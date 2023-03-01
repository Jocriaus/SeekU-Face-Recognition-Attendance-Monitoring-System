#!/usr/bin/python3
import tkinter as tk


class AdmindHomeApp:
    def __init__(self, master=None):
        # build ui
        self.administrator_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.administrator_app.configure(
            background="#E7E7E7", height=200, width=200)
        width= self.administrator_app.winfo_screenwidth()               
        height= self.administrator_app.winfo_screenheight()               
        self.administrator_app.geometry("%dx%d" % (width, height))
        self.administrator_app.resizable(False, False)


#CLIENT-------------------------------------------------------------------------------------------------------  
        self.administrator_client_frame = tk.Frame(self.administrator_app)
        self.administrator_client_frame.configure(
            background="#E7E7E7", height=200, width=200)
        self.time_and_date_label_c = tk.Label(self.administrator_client_frame)
        self.time_and_date_label_c.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text='Time and Date')
        self.time_and_date_label_c.place(
            anchor="center",
            relwidth=1,
            relx=0.5,
            rely=0.975,
            x=0,
            y=0)
        self.admin_c_sec1_frame = tk.Frame(self.administrator_client_frame)
        self.admin_c_sec1_frame.configure(
            background="#E7E7E7", height=200, width=200)
        self.add_c_button = tk.Button(self.admin_c_sec1_frame)
        self.add_c_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text='Add Students')
        self.add_c_button.place(
            anchor="center", relx=0.85, rely=.5, x=0, y=0)
        self.add_c_button.bind("<Button>", self.add_clients, add="")
        self.admin_c_sec1_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=1.0,
            relx=0.5,
            rely=0.09)
        self.admin_c_sec2_frame = tk.Frame(self.administrator_client_frame)
        self.admin_c_sec2_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.search_c_button = tk.Button(self.admin_c_sec2_frame)
        self.search_c_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text='Search')
        self.search_c_button.place(
            anchor="center",
            relheight=.5,
            relwidth=0.16,
            relx=0.9,
            rely=.5,
            x=0,
            y=0)
        self.admin_c_sec1_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=1.0,
            relx=0.5,
            rely=0.09)
        self.search_c_button.bind("<Button>", self.search_clients_info, add="")
        self.search_c_entry = tk.Entry(self.admin_c_sec2_frame)
        self.search_c_entry.configure(background="#E7E7E7", font="{arial} 24 {}")
        self.search_c_entry.place(anchor="center", relx=0.63, rely=.5, x=0, y=0)
        self.clients_list = tk.Label(self.admin_c_sec2_frame)
        self.clients_list.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Students List')
        self.clients_list.place(anchor="center", relx=0.125, rely=.5, x=0, y=0)        
        self.admin_c_sec2_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=.90,
            relx=0.5,
            rely=0.22)
        self.admin_c_sec3_frame = tk.Frame(self.administrator_client_frame)
        self.admin_c_sec3_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.admin_c_sec3_frame.place(
            anchor="center",
            relheight=0.6,
            relwidth=0.9,
            relx=.5,
            rely=.6,
            x=0,
            y=0)
        self.clients_man_var = tk.StringVar(value='Manage Students')
        __values = [
            'Manage Students',
            'Manage Personnels',
            'Manage Visitors']
        self.manage_client_optionmenu = tk.OptionMenu(
            self.administrator_client_frame,
            self.clients_man_var,
            *__values,
            command=self.open_diff_client)
        self.manage_client_optionmenu.configure(font="{arial} 20 {bold}")
        self.manage_client_optionmenu.place(anchor="center", relx=0.17, rely=0.09, x=0, y=0)
        self.manage_client_options = self.administrator_app.nametowidget(self.manage_client_optionmenu.menuname)
        self.manage_client_options.config(font="{arial} 16")
        self.administrator_client_frame.place(
            anchor="center",
            relheight=0.95,
            relwidth=.78,
            relx=0.61,
            rely=0.525)
#CLIENT-------------------------------------------------------------------------------------------------------  



#REPORT------------------------------------------------------------------------------------------------------- 
        self.administrator_report_frame = tk.Frame(self.administrator_app)
        self.administrator_report_frame.configure(
            background="#E7E7E7", height=200, width=200)
        self.time_and_date_label_r = tk.Label(self.administrator_report_frame)
        self.time_and_date_label_r.configure(
            background="#F7FAE9",
            compound="top",
            font="{arial} 30 {bold}",
            foreground="#0072bc",
            text='Time and Date')
        self.time_and_date_label_r.place(
            anchor="center",
            relwidth=1,
            relx=0.5,
            rely=0.975,
            x=0,
            y=0)
        self.admin_r_sec1_frame = tk.Frame(self.administrator_report_frame)
        self.admin_r_sec1_frame.configure(
            background="#E7E7E7", height=200, width=200)
        self.search_clients_report = tk.Button(self.admin_r_sec1_frame)
        self.search_clients_report.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text='Search')
        self.search_clients_report.place(
            anchor="center",
            relheight=.5,
            relwidth=0.16,
            relx=0.9,
            rely=.5,
            x=0,
            y=0)
        self.search_clients_report.bind(
            "<Button>", self.search_clients_reports, add="")
        self.search_r_entry = tk.Entry(self.admin_r_sec1_frame)
        self.search_r_entry.configure(background="#F7FAE9", font="{arial} 24 {}")
        self.search_r_entry.place(anchor="center", relx=0.63, rely=.5, x=0, y=0)
        self.admin_r_sec1_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=.90,
            relx=0.5,
            rely=0.09)
        self.admin_r_sec2_frame = tk.Frame(self.administrator_report_frame)
        self.admin_r_sec2_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.admin_r_sec2_frame.place(
            anchor="center",
            relheight=0.65,
            relwidth=0.9,
            relx=.5,
            rely=0.5,
            x=0,
            y=0)
        

        self.clients_rep_var = tk.StringVar(value='Students Report')
        __values = ['Students Report', 'Personnels Report', 'Visitors Report']
        self.client_report_optionmenu = tk.OptionMenu(
            self.administrator_report_frame, self.clients_rep_var, *__values, command=None)
        self.client_report_optionmenu.place(
            anchor="center", relx=0.17, rely=0.09, x=0, y=0)
        self.client_report_optionmenu.configure(font="{arial} 20 {bold}")
        self.client_report_options = self.administrator_app.nametowidget(self.client_report_optionmenu.menuname)
        self.client_report_options.config(font="{arial} 16")
        self.print_report = tk.Button(self.administrator_report_frame)
        self.print_report.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text='Print')
        self.print_report.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.87,
            rely=0.875,
            x=0,
            y=0)
        self.print_report.bind("<Button>", self.print_clients_reports, add="")
        self.save_button = tk.Button(self.administrator_report_frame)
        self.save_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#f7fae9",
            text='Extra')
        self.save_button.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.7,
            rely=0.875,
            x=0,
            y=0)
        self.save_button.bind("<Button>", self.save_clients_reports, add="")
        self.administrator_report_frame.place(
            anchor="center",
            relheight=0.95,
            relwidth=.78,
            relx=0.61,
            rely=0.525)
#REPORT-------------------------------------------------------------------------------------------------------   
#DB-SECTION--------------------------------------------------------------------------------------          
        self.administrator_db_frame = tk.Frame(self.administrator_app)
        self.administrator_db_frame.configure(
            background="#E7E7E7", height=200, width=200)
        self.time_and_date_label_db = tk.Label(self.administrator_db_frame)
        self.time_and_date_label_db.configure(
            background="#F7FAE9",
            font="{arial} 36 {bold}",
            foreground="#0072bc",
            text='Time and Date')
        self.time_and_date_label_db.place(
            anchor="center",
            relwidth=1,
            relx=0.5,
            rely=0.97,
            x=0,
            y=0) 
        self.administrator_db_ttl_frame = tk.Frame(self.administrator_db_frame)
        self.administrator_db_ttl_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.ttl_students_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_students_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Total Students')
        self.ttl_students_label.place(
            anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ttl_personnels_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Total Personnels')
        self.ttl_personnels_label.place(
            anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.ttl_visitor_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_visitor_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Total Visitors')
        self.ttl_visitor_label.place(
            anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ttl_frame.place(
            anchor="center",
            relheight=0.35,
            relwidth=0.9,
            relx=0.5,
            rely=0.72,
            x=0,
            y=0)
        self.administrator_db_ol_frame = tk.Frame(self.administrator_db_frame)
        self.administrator_db_ol_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.ol_students_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_students_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Present Students')
        self.ol_students_label.place(
            anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ol_personnels_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Present Personnels')
        self.ol_personnels_label.place(
            anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.ol_visitor_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_visitor_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Present Visitors')
        self.ol_visitor_label.place(
            anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ol_frame.place(
            anchor="center",
            relheight=0.35,
            relwidth=0.9,
            relx=0.5,
            rely=0.33,
            x=0,
            y=0)
        self.dashboard_label = tk.Label(self.administrator_db_frame)
        self.dashboard_label.configure(
            background="#E7E7E7",
            font="{arial black} 48 {}",
            text='Dashboard')
        self.dashboard_label.place(
            anchor="center", relheight=0.1, relx=0.5, rely=0.09,)
        self.administrator_db_frame.place(
            anchor="center",
            relheight=0.95,
            relwidth=.78,
            relx=0.61,
            rely=0.525)
#DB-SECTION-------------------------------------------------------------------------------------- 
        self.admin_c_sec1_frame.place_forget()
        self.add_c_button.place_forget()
        self.search_c_button.place_forget()
        self.search_c_entry.place_forget()
        self.clients_list.place_forget()
        self.admin_c_sec2_frame.place_forget()
        self.admin_c_sec3_frame.place_forget()
        self.manage_client_optionmenu.place_forget()    
        self.time_and_date_label_c.place_forget()
        self.administrator_client_frame.place_forget()

        self.admin_r_sec1_frame.place_forget()
        self.print_report.place_forget()
        self.save_button.place_forget()
        self.admin_c_sec2_frame.place_forget()
        self.search_clients_report.place_forget()
        self.search_r_entry.place_forget()
        self.clients_list.place_forget()
        self.admin_r_sec2_frame.place_forget()
        self.client_report_optionmenu.place_forget()
        self.time_and_date_label_r.place_forget()
        self.administrator_report_frame.place_forget()
        
        """
        self.time_and_date_label_db.place_forget()
        self.ttl_students_label.place_forget()
        self.ttl_personnels_label.place_forget()       	
        self.ttl_visitor_label.place_forget()
        self.administrator_db_ttl_frame.place_forget()
        self.ol_students_label.place_forget()
        self.ol_personnels_label.place_forget()
        self.ol_visitor_label.place_forget()
        self.administrator_db_ol_frame.place_forget()
        self.dashboard_label.place_forget()
        self.administrator_db_frame.place_forget()
        """
#HIDE-OTHER--------------------------------------------------------------------------------
        self.administrator_frame3 = tk.Frame(self.administrator_app)
        self.administrator_frame3.configure(
            background="#0072bc", height=200, width=200)
        self.dashboard_section_label = tk.Label(self.administrator_frame3)
        self.dashboard_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Dashboard')
        self.dashboard_section_label.place(anchor="w", relx=.1, rely=0.1)
        self.dashboard_section_label.bind("<1>", self.dashboard_appear, add="")
        self.dashboard_section_label.bind(
            "<Enter>", self.dashboard_hover, add="")
        self.dashboard_section_label.bind(
            "<Leave>", self.dashboard_hover_out, add="")
        self.client_section_label = tk.Label(self.administrator_frame3)
        self.client_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Client')
        self.client_section_label.place(anchor="w", relx=.1, rely=0.16)
        self.client_section_label.bind("<1>", self.client_appear, add="")
        self.client_section_label.bind("<Enter>", self.client_hover, add="")
        self.client_section_label.bind(
            "<Leave>", self.client_hover_out, add="")
        self.user_section_label = tk.Label(self.administrator_frame3)
        self.user_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='User')
        self.user_section_label.place(anchor="w", relx=.1, rely=0.22)
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
            text='Report')
        self.report_section_label.place(anchor="w", relx=.1, rely=0.28)
        self.report_section_label.bind("<1>", self.report_appear, add="")
        self.report_section_label.bind("<Enter>", self.report_hover, add="")
        self.report_section_label.bind(
            "<Leave>", self.report_hover_out, add="")
        self.settings_section_label = tk.Label(self.administrator_frame3)
        self.settings_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Settings')
        self.settings_section_label.place(anchor="w", relx=.1, rely=0.34)
        self.settings_section_label.bind("<1>", self.settings_appear, add="")
        self.settings_section_label.bind(
            "<Enter>", self.settings_hover, add="")
        self.settings_section_label.bind(
            "<Leave>", self.settings_hover_out, add="")
        self.logout_label = tk.Label(self.administrator_frame3)
        self.logout_label.configure(
            background="#0072bc",
            font="{arial} 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Log Out')
        self.logout_label.place(anchor="w", relx=.1, rely=0.85)
        self.logout_label.bind("<1>", self.logout, add="")
        self.logout_label.bind("<Enter>", self.logout_hover, add="")
        self.logout_label.bind("<Leave>", self.logout_hover_out, add="")
        self.administrator_frame3.place(
            anchor="center",
            relheight=.92,
            relwidth=0.22,
            relx=0.11,
            rely=.54)
#----------------------------------------------------------------------------------
        self.administrator_frame2 = tk.Frame(self.administrator_app)
        self.administrator_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.administrator_frame2)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png")
        self.app_name_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekULogotypemicro,
            text='label1')
        self.app_name_logo.place(
            anchor="center", relx=0.15, rely=0.55, x=0, y=0)
        self.app_logo_label = tk.Label(self.administrator_frame2)
        self.img_SeekUmicro = tk.PhotoImage(
            file=".\SeekU\SeekU micro.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUmicro,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.05, rely=0.5)
        self.administrator_frame2.place(
            anchor="center",
            relheight=0.08,
            relwidth=1.0,
            relx=0.50,
            rely=0.04)

        # Main widget
        self.mainwindow = self.administrator_app
        self.mainwindow.wm_attributes('-fullscreen', 'True')

    def run(self):
        self.mainwindow.mainloop()
    
    def db_appear_logic(self):
        # client_forget------------------------------------
        self.admin_c_sec1_frame.place_forget()
        self.add_c_button.place_forget()
        self.search_c_button.place_forget()
        self.search_c_entry.place_forget()
        self.clients_list.place_forget()
        self.admin_c_sec2_frame.place_forget()
        self.admin_c_sec3_frame.place_forget()
        self.manage_client_optionmenu.place_forget()    
        self.time_and_date_label_c.place_forget()
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        # report_forget------------------------------------
        self.admin_r_sec1_frame.place_forget()
        self.print_report.place_forget()
        self.save_button.place_forget()
        self.admin_c_sec2_frame.place_forget()
        self.search_clients_report.place_forget()
        self.search_r_entry.place_forget()
        self.clients_list.place_forget()
        self.admin_r_sec2_frame.place_forget()
        self.client_report_optionmenu.place_forget()
        self.time_and_date_label_r.place_forget()
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------

        self.time_and_date_label_db.place(
            anchor="center",
            relwidth=1,
            relx=0.5,
            rely=0.97,
            x=0,
            y=0) 
        self.ttl_students_label.place(
            anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ttl_personnels_label.place(
            anchor="center", relx=0.5, rely=0.25, x=0, y=0)        	
        self.ttl_visitor_label.place(
            anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ttl_frame.place(
            anchor="center",
            relheight=0.35,
            relwidth=0.9,
            relx=0.5,
            rely=0.72,
            x=0,
            y=0)
        self.ol_students_label.place(
            anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ol_personnels_label.place(
            anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.ol_visitor_label.place(
            anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ol_frame.place(
            anchor="center",
            relheight=0.35,
            relwidth=0.9,
            relx=0.5,
            rely=0.33,
            x=0,
            y=0)
        self.dashboard_label.place(
            anchor="center", relheight=0.1, relx=0.5, rely=0.09,)
        self.administrator_db_frame.place(
            anchor="center",
            relheight=0.95,
            relwidth=.78,
            relx=0.61,
            rely=0.525)
        
    def client_appear_logic(self):
        # report_forget------------------------------------
        self.admin_r_sec1_frame.place_forget()
        self.print_report.place_forget()
        self.save_button.place_forget()
        self.admin_c_sec2_frame.place_forget()
        self.search_clients_report.place_forget()
        self.search_r_entry.place_forget()
        self.clients_list.place_forget()
        self.admin_r_sec2_frame.place_forget()
        self.client_report_optionmenu.place_forget()
        self.time_and_date_label_r.place_forget()
        self.administrator_report_frame.place_forget()
        # report_forget------------------------------------
        # db_forget----------------------------------------
        self.time_and_date_label_db.place_forget()
        self.ttl_students_label.place_forget()
        self.ttl_personnels_label.place_forget()       	
        self.ttl_visitor_label.place_forget()
        self.administrator_db_ttl_frame.place_forget()
        self.ol_students_label.place_forget()
        self.ol_personnels_label.place_forget()
        self.ol_visitor_label.place_forget()
        self.administrator_db_ol_frame.place_forget()
        self.dashboard_label.place_forget()
        self.administrator_db_frame.place_forget()
        # db_forget----------------------------------------
        self.time_and_date_label_c.place(
            anchor="center",
            relwidth=1,
            relx=0.5,
            rely=0.975,
            x=0,
            y=0)
        self.add_c_button.place(
            anchor="center", relx=0.85, rely=.5, x=0, y=0)
        self.admin_c_sec1_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=1.0,
            relx=0.5,
            rely=0.09)
        self.search_c_button.place(
            anchor="center",
            relheight=.5,
            relwidth=0.16,
            relx=0.9,
            rely=.5,
            x=0,
            y=0)
        self.admin_c_sec1_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=1.0,
            relx=0.5,
            rely=0.09)
        self.search_c_entry.place(anchor="center", relx=0.63, rely=.5, x=0, y=0)
        self.clients_list.place(anchor="center", relx=0.125, rely=.5, x=0, y=0)        
        self.admin_c_sec2_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=.90,
            relx=0.5,
            rely=0.22)
        self.admin_c_sec3_frame.place(
            anchor="center",
            relheight=0.6,
            relwidth=0.9,
            relx=.5,
            rely=.6,
            x=0,
            y=0)
        self.manage_client_optionmenu.place(anchor="center", relx=0.17, rely=0.09, x=0, y=0)
        self.administrator_client_frame.place(
            anchor="center",
            relheight=0.95,
            relwidth=.78,
            relx=0.61,
            rely=0.525)


    def report_appear_logic(self):
        # client_forget------------------------------------
        self.admin_c_sec1_frame.place_forget()
        self.add_c_button.place_forget()
        self.search_c_button.place_forget()
        self.search_c_entry.place_forget()
        self.clients_list.place_forget()
        self.admin_c_sec2_frame.place_forget()
        self.admin_c_sec3_frame.place_forget()
        self.manage_client_optionmenu.place_forget()    
        self.time_and_date_label_c.place_forget()
        self.administrator_client_frame.place_forget()
        # client_forget------------------------------------
        #db_forget------------------------------------
        self.time_and_date_label_db.place_forget()
        self.ttl_students_label.place_forget()
        self.ttl_personnels_label.place_forget()       	
        self.ttl_visitor_label.place_forget()
        self.administrator_db_ttl_frame.place_forget()
        self.ol_students_label.place_forget()
        self.ol_personnels_label.place_forget()
        self.ol_visitor_label.place_forget()
        self.administrator_db_ol_frame.place_forget()
        self.dashboard_label.place_forget()
        self.administrator_db_frame.place_forget()
        #db_forget------------------------------------
        self.time_and_date_label_r.place(
            anchor="center",
            relwidth=1,
            relx=0.5,
            rely=0.975,
            x=0,
            y=0)
        self.search_clients_report.place(
            anchor="center",
            relheight=.5,
            relwidth=0.16,
            relx=0.9,
            rely=.5,
            x=0,
            y=0)
        self.search_r_entry.place(anchor="center", relx=0.63, rely=.5, x=0, y=0)
        self.admin_r_sec1_frame.place(
            anchor="center",
            relheight=0.1,
            relwidth=.90,
            relx=0.5,
            rely=0.09)
        self.admin_r_sec2_frame.place(
            anchor="center",
            relheight=0.65,
            relwidth=0.9,
            relx=.5,
            rely=0.5,
            x=0,
            y=0)
        self.client_report_optionmenu.place(
            anchor="center", relx=0.17, rely=0.09, x=0, y=0)
        self.print_report.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.87,
            rely=0.875,
            x=0,
            y=0)
        self.save_button.place(
            anchor="center",
            relheight=0.05,
            relwidth=0.12,
            relx=0.7,
            rely=0.875,
            x=0,
            y=0)
        self.administrator_report_frame.place(
            anchor="center",
            relheight=0.95,
            relwidth=.78,
            relx=0.61,
            rely=0.525)



    def change_layout(self):
        if(self.clients_man_var.get() == 'Manage Students'):
            self.add_c_button.configure(text='Add Students')
            self.clients_list.configure(text='Students List')
        if(self.clients_man_var.get() == 'Manage Personnels'):
            self.add_c_button.configure(text='Add Personnels')
            self.clients_list.configure(text='Personnels List')
        if(self.clients_man_var.get() == 'Manage Visitors'):
            self.add_c_button.configure(text='Add Visitors')
            self.clients_list.configure(text='Visitors List')

    def add_clients_logic(self):
        if(self.clients_man_var.get() == 'Manage Students'):
            pass
        if(self.clients_man_var.get() == 'Manage Personnels'):
            pass
        if(self.clients_man_var.get() == 'Manage Visitors'):
            pass

    def search_clients_info_logic(self):
        if(self.clients_man_var.get() == 'Manage Students'):
            pass
        if(self.clients_man_var.get() == 'Manage Personnels'):
            pass
        if(self.clients_man_var.get() == 'Manage Visitors'):
            pass


    def open_diff_client(self, event):
        self.change_layout()


    def add_clients(self, event=None):
        self.add_clients_logic()

    def search_clients_info(self, event=None):
        self.search_clients_info_logic()


    def search_clients_reports(self, event=None):
        pass

    def print_clients_reports(self, event=None):
        pass

    def save_clients_reports(self, event=None):
        pass


    def dashboard_appear(self, event=None):
        self.db_appear_logic()

    def dashboard_hover(self, event=None):
        self.dashboard_section_label.configure(foreground="#FFF200")

    def dashboard_hover_out(self, event=None):
        self.dashboard_section_label.configure(foreground="#F7FAE9")

    def client_appear(self, event=None):
        self.client_appear_logic()

    def client_hover(self, event=None):
        self.client_section_label.configure(foreground="#FFF200")

    def client_hover_out(self, event=None):
        self.client_section_label.configure(foreground="#F7FAE9")

    def user_appear(self, event=None):
        pass

    def user_hover(self, event=None):
        self.user_section_label.configure(foreground="#FFF200")

    def user_hover_out(self, event=None):
        self.user_section_label.configure(foreground="#F7FAE9")

    def report_appear(self, event=None):
        self.report_appear_logic()

    def report_hover(self, event=None):
        self.report_section_label.configure(foreground="#FFF200")

    def report_hover_out(self, event=None):
        self.report_section_label.configure(foreground="#F7FAE9")

    def settings_appear(self, event=None):
        pass

    def settings_hover(self, event=None):
        self.settings_section_label.configure(foreground="#FFF200")

    def settings_hover_out(self, event=None):
        self.settings_section_label.configure(foreground="#F7FAE9")

    def logout(self, event=None):
        # log in module appear
        self.administrator_app.destroy()

    def logout_hover(self, event=None):
        self.logout_label.configure(foreground="#FFF200")

    def logout_hover_out(self, event=None):
        self.logout_label.configure(foreground="#F7FAE9")




if __name__ == "__main__":
    app = AdmindHomeApp()
    app.run()

