import pyodbc as odbc
import tkinter as tk
import tkinter.ttk as ttk
import query_mod as qry
import tkinter.messagebox as messbx


class TreeviewGUI:
    def __init__(self, master=None):
        self.sql_query = qry.dbQueries()
        # "DESKTOP-DG7AK17\SQLEXPRESS"
        # "STAR-PLATINUM\SQLEXPRESS01"
        # "DESKTOP-3MNAAKG\SQLEXPRESS"
        self.server = "DESKTOP-DG7AK17\SQLEXPRESS"
        self.database = "seeku_database"
        self.username = ""
        self.password = ""
        # self.connection_string = f"Driver={{ODBC Driver 18 for SQL Server}};Server={self.server};Database={self.database};UID={self.username};PWD={self.password};TrustServerCertificate=yes"
        self.connection_string = f"Driver={{SQL Server}};Server={self.server};Database={self.database};UID={self.username};PWD={self.password}"

        self.connection = odbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed")

    def student_treeview(self, root, status):
        self.student_treeview_root = root
        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )

        # Create Treeview Frame
        self.student_treeview_frame = tk.Frame(self.student_treeview_root)
        self.student_treeview_frame.configure(background="#F7FAE9")
        self.student_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.student_treeview_scrollbar = tk.Scrollbar(self.student_treeview_frame)
        self.student_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.student_tree = ttk.Treeview(
            self.student_treeview_frame,
            yscrollcommand=self.student_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.student_treeview_scrollbar.config(command=self.student_tree.yview)

        # Configure Treeview Position
        self.student_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )
        self.student_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.student_tree["columns"] = (
            "Student Number",
            "First Name",
            "Last Name",
            "Middle Name",
            "Program",
            "Section",
            "Contact Number",
            "Address",
            "Student Status",
        )

        # Format the columns
        self.student_tree.column("#0", width=0, stretch=tk.NO)
        self.student_tree.column("Student Number", anchor=tk.CENTER, width=140)
        self.student_tree.column("First Name", anchor=tk.CENTER, width=180)
        self.student_tree.column("Last Name", anchor=tk.CENTER, width=140)
        self.student_tree.column("Middle Name", anchor=tk.CENTER, width=110)
        self.student_tree.column("Program", anchor=tk.CENTER, width=110)
        self.student_tree.column("Section", anchor=tk.CENTER, width=120)
        self.student_tree.column("Contact Number", anchor=tk.CENTER, width=150)
        self.student_tree.column("Address", anchor=tk.CENTER, width=240)
        self.student_tree.column("Student Status", anchor=tk.CENTER, width=140)
        # Hide status, show only on edit
        # di daw pede sabi ni vrix

        # Create Headings
        self.student_tree.heading("#0", text="", anchor=tk.CENTER)
        self.student_tree.heading(
            "Student Number", text="Student Number", anchor=tk.CENTER
        )
        self.student_tree.heading("First Name", text="First Name", anchor=tk.CENTER)
        self.student_tree.heading("Last Name", text="Last Name", anchor=tk.CENTER)
        self.student_tree.heading("Middle Name", text="Middle Name", anchor=tk.CENTER)
        self.student_tree.heading("Program", text="Program", anchor=tk.CENTER)
        self.student_tree.heading("Section", text="Section", anchor=tk.CENTER)
        self.student_tree.heading(
            "Contact Number", text="Contact Number", anchor=tk.CENTER
        )
        self.student_tree.heading("Address", text="Address", anchor=tk.CENTER)
        self.student_tree.heading(
            "Student Status", text="Student Status", anchor=tk.CENTER
        )

        self.populate_student_treeview(status)

        return self.student_treeview_frame

    def student_attendance_treeview(self, root):
        self.student_attendance_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )

        # Create Treeview Frame
        self.student_attendance_treeview_frame = tk.Frame(
            self.student_attendance_treeview_root
        )
        self.student_attendance_treeview_frame.configure(background="#F7FAE9")
        self.student_attendance_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.student_attendance_treeview_scrollbar = tk.Scrollbar(
            self.student_attendance_treeview_frame
        )
        self.student_attendance_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.student_attendance_tree = ttk.Treeview(
            self.student_attendance_treeview_frame,
            yscrollcommand=self.student_attendance_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.student_attendance_treeview_scrollbar.config(
            command=self.student_attendance_tree.yview
        )

        # Configure Treeview Position
        self.student_attendance_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.student_attendance_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.student_attendance_tree["columns"] = (
            "Student Number",
            "First Name",
            "Last Name",
            "Program",
            "Section",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.student_attendance_tree.column("#0", width=0, stretch=tk.NO)
        self.student_attendance_tree.column(
            "Student Number", anchor=tk.CENTER, width=140
        )
        self.student_attendance_tree.column("First Name", anchor=tk.CENTER, width=180)
        self.student_attendance_tree.column("Last Name", anchor=tk.CENTER, width=180)
        self.student_attendance_tree.column("Program", anchor=tk.CENTER, width=140)
        self.student_attendance_tree.column("Section", anchor=tk.CENTER, width=140)
        self.student_attendance_tree.column("Date", anchor=tk.CENTER, width=180)
        self.student_attendance_tree.column("Time In", anchor=tk.CENTER, width=185)
        self.student_attendance_tree.column("Time Out", anchor=tk.CENTER, width=185)

        # Create Headings
        self.student_attendance_tree.heading("#0", text="", anchor=tk.CENTER)
        self.student_attendance_tree.heading(
            "Student Number", text="Student Number", anchor=tk.CENTER
        )
        self.student_attendance_tree.heading(
            "First Name", text="First Name", anchor=tk.CENTER
        )
        self.student_attendance_tree.heading(
            "Last Name", text="Last Name", anchor=tk.CENTER
        )
        self.student_attendance_tree.heading(
            "Program", text="Program", anchor=tk.CENTER
        )
        self.student_attendance_tree.heading(
            "Section", text="Section", anchor=tk.CENTER
        )
        self.student_attendance_tree.heading("Date", text="Date", anchor=tk.CENTER)
        self.student_attendance_tree.heading(
            "Time In", text="Time In", anchor=tk.CENTER
        )
        self.student_attendance_tree.heading(
            "Time Out", text="Time Out", anchor=tk.CENTER
        )

        self.populate_student_attendance_treeview()

        return self.student_attendance_treeview_frame

    def student_report_treeview(self, root):
        self.student_report_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )

        # Create Treeview Frame
        self.student_report_treeview_frame = tk.Frame(self.student_report_treeview_root)
        self.student_report_treeview_frame.configure(background="#F7FAE9")
        self.student_report_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.student_report_treeview_scrollbar = tk.Scrollbar(
            self.student_report_treeview_frame
        )
        self.student_report_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.student_report_tree = ttk.Treeview(
            self.student_report_treeview_frame,
            yscrollcommand=self.student_report_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.student_report_treeview_scrollbar.config(
            command=self.student_report_tree.yview
        )

        # Configure Treeview Position
        self.student_report_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.student_report_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.student_report_tree["columns"] = (
            "Student Number",
            "First Name",
            "Last Name",
            "Program",
            "Section",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.student_report_tree.column("#0", width=0, stretch=tk.NO)
        self.student_report_tree.column("Student Number", anchor=tk.CENTER, width=140)
        self.student_report_tree.column("First Name", anchor=tk.CENTER, width=180)
        self.student_report_tree.column("Last Name", anchor=tk.CENTER, width=180)
        self.student_report_tree.column("Program", anchor=tk.CENTER, width=140)
        self.student_report_tree.column("Section", anchor=tk.CENTER, width=140)
        self.student_report_tree.column("Date", anchor=tk.CENTER, width=180)
        self.student_report_tree.column("Time In", anchor=tk.CENTER, width=185)
        self.student_report_tree.column("Time Out", anchor=tk.CENTER, width=185)

        # Create Headings
        self.student_report_tree.heading("#0", text="", anchor=tk.CENTER)
        self.student_report_tree.heading(
            "Student Number", text="Student Number", anchor=tk.CENTER
        )
        self.student_report_tree.heading(
            "First Name", text="First Name", anchor=tk.CENTER
        )
        self.student_report_tree.heading(
            "Last Name", text="Last Name", anchor=tk.CENTER
        )
        self.student_report_tree.heading("Program", text="Program", anchor=tk.CENTER)
        self.student_report_tree.heading("Section", text="Section", anchor=tk.CENTER)
        self.student_report_tree.heading("Date", text="Date", anchor=tk.CENTER)
        self.student_report_tree.heading("Time In", text="Time In", anchor=tk.CENTER)
        self.student_report_tree.heading("Time Out", text="Time Out", anchor=tk.CENTER)

        self.populate_student_report_treeview()

        return self.student_report_treeview_frame

    def personnel_treeview(self, root, status):
        self.personnel_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )

        # Create Treeview Frame
        self.personnel_treeview_frame = tk.Frame(self.personnel_treeview_root)
        self.personnel_treeview_frame.configure(background="#F7FAE9")
        self.personnel_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.personnel_treeview_scrollbar = tk.Scrollbar(self.personnel_treeview_frame)
        self.personnel_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.personnel_tree = ttk.Treeview(
            self.personnel_treeview_frame,
            yscrollcommand=self.personnel_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.personnel_treeview_scrollbar.config(command=self.personnel_tree.yview)

        # Configure Treeview Position
        self.personnel_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.personnel_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.personnel_tree["columns"] = (
            "Personnel Number",
            "First Name",
            "Last Name",
            "Middle Name",
            "Contact Number",
            "Address",
            "Personnel Type",
            "Personnel Status",
        )

        # Format the columns
        self.personnel_tree.column("#0", width=0, stretch=tk.NO)
        self.personnel_tree.column("Personnel Number", anchor=tk.CENTER, width=170)
        self.personnel_tree.column("First Name", anchor=tk.CENTER, width=160)
        self.personnel_tree.column("Last Name", anchor=tk.CENTER, width=160)
        self.personnel_tree.column("Middle Name", anchor=tk.CENTER, width=140)
        self.personnel_tree.column("Contact Number", anchor=tk.CENTER, width=160)
        self.personnel_tree.column("Address", anchor=tk.CENTER, width=240)
        self.personnel_tree.column("Personnel Type", anchor=tk.CENTER, width=140)
        self.personnel_tree.column("Personnel Status", anchor=tk.CENTER, width=160)

        # Create Headings
        self.personnel_tree.heading("#0", text="", anchor=tk.CENTER)
        self.personnel_tree.heading(
            "Personnel Number", text="Personnel Number", anchor=tk.CENTER
        )
        self.personnel_tree.heading("First Name", text="First Name", anchor=tk.CENTER)
        self.personnel_tree.heading("Last Name", text="Last Name", anchor=tk.CENTER)
        self.personnel_tree.heading("Middle Name", text="Middle Name", anchor=tk.CENTER)
        self.personnel_tree.heading(
            "Contact Number", text="Contact Number", anchor=tk.CENTER
        )
        self.personnel_tree.heading("Address", text="Address", anchor=tk.CENTER)
        self.personnel_tree.heading(
            "Personnel Type", text="Personnel Type", anchor=tk.CENTER
        )
        self.personnel_tree.heading(
            "Personnel Status", text="Personnel Status", anchor=tk.CENTER
        )

        self.populate_personnel_treeview(status)

        return self.personnel_treeview_frame

    def personnel_attendance_treeview(self, root):
        self.personnel_attendance_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )
        # Create Treeview Frame
        self.personnel_attendance_treeview_frame = tk.Frame(
            self.personnel_attendance_treeview_root
        )
        self.personnel_attendance_treeview_frame.configure(background="#F7FAE9")
        self.personnel_attendance_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.personnel_attendance_treeview_scrollbar = tk.Scrollbar(
            self.personnel_attendance_treeview_frame
        )
        self.personnel_attendance_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.personnel_attendance_tree = ttk.Treeview(
            self.personnel_attendance_treeview_frame,
            yscrollcommand=self.personnel_attendance_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.personnel_attendance_treeview_scrollbar.config(
            command=self.personnel_attendance_tree.yview
        )

        # Configure Treeview Position
        self.personnel_attendance_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.personnel_attendance_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.personnel_attendance_tree["columns"] = (
            "Personnel Number",
            "First Name",
            "Last Name",
            "Personnel Type",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.personnel_attendance_tree.column("#0", width=0, stretch=tk.NO)
        self.personnel_attendance_tree.column(
            "Personnel Number", anchor=tk.CENTER, width=170
        )
        self.personnel_attendance_tree.column("First Name", anchor=tk.CENTER, width=200)
        self.personnel_attendance_tree.column("Last Name", anchor=tk.CENTER, width=190)
        self.personnel_attendance_tree.column(
            "Personnel Type", anchor=tk.CENTER, width=160
        )
        self.personnel_attendance_tree.column("Date", anchor=tk.CENTER, width=190)
        self.personnel_attendance_tree.column("Time In", anchor=tk.CENTER, width=210)
        self.personnel_attendance_tree.column("Time Out", anchor=tk.CENTER, width=210)

        # Create Headings
        self.personnel_attendance_tree.heading("#0", text="", anchor=tk.CENTER)
        self.personnel_attendance_tree.heading(
            "Personnel Number", text="Personnel Number", anchor=tk.CENTER
        )
        self.personnel_attendance_tree.heading(
            "First Name", text="First Name", anchor=tk.CENTER
        )
        self.personnel_attendance_tree.heading(
            "Last Name", text="Last Name", anchor=tk.CENTER
        )
        self.personnel_attendance_tree.heading(
            "Personnel Type", text="Personnel Type", anchor=tk.CENTER
        )
        self.personnel_attendance_tree.heading("Date", text="Date", anchor=tk.CENTER)
        self.personnel_attendance_tree.heading(
            "Time In", text="Time In", anchor=tk.CENTER
        )
        self.personnel_attendance_tree.heading(
            "Time Out", text="Time Out", anchor=tk.CENTER
        )

        self.populate_personnel_attendance_treeview()
        return self.personnel_attendance_treeview_frame

    def personnel_report_treeview(self, root):
        self.personnel_report_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )
        # Create Treeview Frame
        self.personnel_report_treeview_frame = tk.Frame(
            self.personnel_report_treeview_root
        )
        self.personnel_report_treeview_frame.configure(background="#F7FAE9")
        self.personnel_report_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.personnel_report_treeview_scrollbar = tk.Scrollbar(
            self.personnel_report_treeview_frame
        )
        self.personnel_report_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.personnel_report_tree = ttk.Treeview(
            self.personnel_report_treeview_frame,
            yscrollcommand=self.personnel_report_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.personnel_report_treeview_scrollbar.config(
            command=self.personnel_report_tree.yview
        )

        # Configure Treeview Position
        self.personnel_report_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.personnel_report_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.personnel_report_tree["columns"] = (
            "Personnel Number",
            "First Name",
            "Last Name",
            "Personnel Type",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.personnel_report_tree.column("#0", width=0, stretch=tk.NO)
        self.personnel_report_tree.column(
            "Personnel Number", anchor=tk.CENTER, width=170
        )
        self.personnel_report_tree.column("First Name", anchor=tk.CENTER, width=200)
        self.personnel_report_tree.column("Last Name", anchor=tk.CENTER, width=190)
        self.personnel_report_tree.column("Personnel Type", anchor=tk.CENTER, width=160)
        self.personnel_report_tree.column("Date", anchor=tk.CENTER, width=190)
        self.personnel_report_tree.column("Time In", anchor=tk.CENTER, width=210)
        self.personnel_report_tree.column("Time Out", anchor=tk.CENTER, width=210)

        # Create Headings
        self.personnel_report_tree.heading("#0", text="", anchor=tk.CENTER)
        self.personnel_report_tree.heading(
            "Personnel Number", text="Personnel Number", anchor=tk.CENTER
        )
        self.personnel_report_tree.heading(
            "First Name", text="First Name", anchor=tk.CENTER
        )
        self.personnel_report_tree.heading(
            "Last Name", text="Last Name", anchor=tk.CENTER
        )
        self.personnel_report_tree.heading(
            "Personnel Type", text="Personnel Type", anchor=tk.CENTER
        )
        self.personnel_report_tree.heading("Date", text="Date", anchor=tk.CENTER)
        self.personnel_report_tree.heading("Time In", text="Time In", anchor=tk.CENTER)
        self.personnel_report_tree.heading(
            "Time Out", text="Time Out", anchor=tk.CENTER
        )

        self.populate_personnel_report_treeview()
        return self.personnel_report_treeview_frame

    def visitor_treeview(self, root, status):
        self.visitor_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )
        # Create Treeview Frame
        self.visitor_treeview_frame = tk.Frame(self.visitor_treeview_root)
        self.visitor_treeview_frame.configure(background="#F7FAE9")
        self.visitor_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.visitor_treeview_scrollbar = tk.Scrollbar(self.visitor_treeview_frame)
        self.visitor_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.visitor_tree = ttk.Treeview(
            self.visitor_treeview_frame,
            yscrollcommand=self.visitor_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.visitor_treeview_scrollbar.config(command=self.visitor_tree.yview)

        # Configure Treeview Position
        self.visitor_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.visitor_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.visitor_tree["columns"] = (
            "Visitor Number",
            "First Name",
            "Last Name",
            "Contact Number",
            "Address",
            "Visitor Status",
        )

        # Format the columns
        self.visitor_tree.column("#0", width=0, stretch=tk.NO)
        self.visitor_tree.column("Visitor Number", anchor=tk.CENTER, width=140)
        self.visitor_tree.column("First Name", anchor=tk.CENTER, width=240)
        self.visitor_tree.column("Last Name", anchor=tk.CENTER, width=240)
        self.visitor_tree.column("Contact Number", anchor=tk.CENTER, width=150)
        self.visitor_tree.column("Address", anchor=tk.CENTER, width=400)
        self.visitor_tree.column("Visitor Status", anchor=tk.CENTER, width=160)

        # Create Headings
        self.visitor_tree.heading("#0", text="", anchor=tk.CENTER)
        self.visitor_tree.heading(
            "Visitor Number", text="Visitor Number", anchor=tk.CENTER
        )
        self.visitor_tree.heading("First Name", text="First Name", anchor=tk.CENTER)
        self.visitor_tree.heading("Last Name", text="Last Name", anchor=tk.CENTER)
        self.visitor_tree.heading(
            "Contact Number", text="Contact Number", anchor=tk.CENTER
        )
        self.visitor_tree.heading("Address", text="Address", anchor=tk.CENTER)
        self.visitor_tree.heading(
            "Visitor Status", text="Visitor Status", anchor=tk.CENTER
        )

        self.populate_visitor_treeview(status)
        return self.visitor_treeview_frame

    def visitor_attendance_treeview(self, root):
        self.visitor_attendance_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )
        # Create Treeview Frame
        self.visitor_attendance_treeview_frame = tk.Frame(
            self.visitor_attendance_treeview_root
        )
        self.visitor_attendance_treeview_frame.configure(background="#F7FAE9")
        self.visitor_attendance_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.visitor_attendance_treeview_scrollbar = tk.Scrollbar(
            self.visitor_attendance_treeview_frame
        )
        self.visitor_attendance_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.visitor_attendance_tree = ttk.Treeview(
            self.visitor_attendance_treeview_frame,
            yscrollcommand=self.visitor_attendance_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.visitor_attendance_treeview_scrollbar.config(
            command=self.visitor_attendance_tree.yview
        )

        # Configure Treeview Position
        self.visitor_attendance_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.visitor_attendance_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.visitor_attendance_tree["columns"] = (
            "Visitor Number",
            "First Name",
            "Last Name",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.visitor_attendance_tree.column("#0", width=0, stretch=tk.NO)
        self.visitor_attendance_tree.column(
            "Visitor Number", anchor=tk.CENTER, width=200
        )
        self.visitor_attendance_tree.column("First Name", anchor=tk.CENTER, width=240)
        self.visitor_attendance_tree.column("Last Name", anchor=tk.CENTER, width=230)
        self.visitor_attendance_tree.column("Date", anchor=tk.CENTER, width=220)
        self.visitor_attendance_tree.column("Time In", anchor=tk.CENTER, width=220)
        self.visitor_attendance_tree.column("Time Out", anchor=tk.CENTER, width=220)

        # Create Headings
        self.visitor_attendance_tree.heading("#0", text="", anchor=tk.CENTER)
        self.visitor_attendance_tree.heading(
            "Visitor Number", text="Visitor Number", anchor=tk.CENTER
        )
        self.visitor_attendance_tree.heading(
            "First Name", text="First Name", anchor=tk.CENTER
        )
        self.visitor_attendance_tree.heading(
            "Last Name", text="Last Name", anchor=tk.CENTER
        )
        self.visitor_attendance_tree.heading("Date", text="Date", anchor=tk.CENTER)
        self.visitor_attendance_tree.heading(
            "Time In", text="Time In", anchor=tk.CENTER
        )
        self.visitor_attendance_tree.heading(
            "Time Out", text="Time Out", anchor=tk.CENTER
        )

        self.populate_visitor_attendance_treeview()
        return self.visitor_attendance_treeview_frame

    def visitor_report_treeview(self, root):
        self.visitor_report_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )

        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )
        # Create Treeview Frame
        self.visitor_report_treeview_frame = tk.Frame(self.visitor_report_treeview_root)
        self.visitor_report_treeview_frame.configure(background="#F7FAE9")
        self.visitor_report_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.visitor_report_treeview_scrollbar = tk.Scrollbar(
            self.visitor_report_treeview_frame
        )
        self.visitor_report_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.visitor_report_tree = ttk.Treeview(
            self.visitor_report_treeview_frame,
            yscrollcommand=self.visitor_report_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.visitor_report_treeview_scrollbar.config(
            command=self.visitor_report_tree.yview
        )

        # Configure Treeview Position
        self.visitor_report_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.visitor_report_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.visitor_report_tree["columns"] = (
            "Visitor Number",
            "First Name",
            "Last Name",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.visitor_report_tree.column("#0", width=0, stretch=tk.NO)
        self.visitor_report_tree.column("Visitor Number", anchor=tk.CENTER, width=200)
        self.visitor_report_tree.column("First Name", anchor=tk.CENTER, width=240)
        self.visitor_report_tree.column("Last Name", anchor=tk.CENTER, width=230)
        self.visitor_report_tree.column("Date", anchor=tk.CENTER, width=220)
        self.visitor_report_tree.column("Time In", anchor=tk.CENTER, width=220)
        self.visitor_report_tree.column("Time Out", anchor=tk.CENTER, width=220)

        # Create Headings
        self.visitor_report_tree.heading("#0", text="", anchor=tk.CENTER)
        self.visitor_report_tree.heading(
            "Visitor Number", text="Visitor Number", anchor=tk.CENTER
        )
        self.visitor_report_tree.heading(
            "First Name", text="First Name", anchor=tk.CENTER
        )
        self.visitor_report_tree.heading(
            "Last Name", text="Last Name", anchor=tk.CENTER
        )
        self.visitor_report_tree.heading("Date", text="Date", anchor=tk.CENTER)
        self.visitor_report_tree.heading("Time In", text="Time In", anchor=tk.CENTER)
        self.visitor_report_tree.heading("Time Out", text="Time Out", anchor=tk.CENTER)

        self.populate_visitor_report_treeview()
        return self.visitor_report_treeview_frame

    def user_treeview(self, root, status):
        self.user_treeview_root = root

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 11 {}",
        )
        self.style.configure(
            "Treeview.Heading",
            font="{arial} 11 {bold}",
        )
        # Create Treeview Frame
        self.user_treeview_frame = tk.Frame(self.user_treeview_root)
        self.user_treeview_frame.configure(background="#F7FAE9")
        self.user_treeview_frame.pack(pady=20)

        # Treeview Scrollbar
        self.user_treeview_scrollbar = tk.Scrollbar(self.user_treeview_frame)
        self.user_treeview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.user_tree = ttk.Treeview(
            self.user_treeview_frame,
            yscrollcommand=self.user_treeview_scrollbar.set,
        )

        # Configure the scrollbar
        self.user_treeview_scrollbar.config(command=self.user_tree.yview)

        # Configure Treeview Position
        self.user_treeview_frame.place(
            anchor="center", relheight=1, relwidth=1, relx=0.5, rely=0.5
        )

        self.user_tree.pack(fill="both", expand=1)

        # Defining Columns
        self.user_tree["columns"] = (
            "User Number",
            "Username",
            "Password",
            "First Name",
            "Last Name",
            "User Type",
            "User Status",
        )

        # Format the columns
        self.user_tree.column("#0", width=0, stretch=tk.NO)
        self.user_tree.column("User Number", anchor=tk.CENTER, width=140)
        self.user_tree.column("Username", anchor=tk.CENTER, width=200)
        self.user_tree.column("Password", anchor=tk.CENTER, width=200)
        self.user_tree.column("First Name", anchor=tk.CENTER, width=220)
        self.user_tree.column("Last Name", anchor=tk.CENTER, width=200)
        self.user_tree.column("User Type", anchor=tk.CENTER, width=200)
        self.user_tree.column("User Status", anchor=tk.CENTER, width=140)

        # Create Headings
        self.user_tree.heading("#0", text="", anchor=tk.CENTER)
        self.user_tree.heading("User Number", text="User Number", anchor=tk.CENTER)
        self.user_tree.heading("Username", text="Username", anchor=tk.CENTER)
        self.user_tree.heading("Password", text="Password", anchor=tk.CENTER)
        self.user_tree.heading("First Name", text="First Name", anchor=tk.CENTER)
        self.user_tree.heading("Last Name", text="Last Name", anchor=tk.CENTER)
        self.user_tree.heading("User Type", text="User Type", anchor=tk.CENTER)
        self.user_tree.heading("User Status", text="User Status", anchor=tk.CENTER)

        self.populate_user_treeview(status)
        return self.user_treeview_frame

    def populate_student_treeview(self, status):
        self.cursor.execute(
            "SELECT * FROM tbl_student WHERE student_status = '" + status + "'"
        )  # add where status is isActive

        for row in self.cursor.fetchall():
            self.student_tree.insert(
                "",
                "end",
                text=[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                ),
            )

    def populate_student_attendance_treeview(self):
        self.cursor.execute(
            "SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, tbl_student.student_program, tbl_student.student_section, tbl_student_attendance.student_attendance_date, tbl_student_attendance.student_time_in, tbl_student_attendance.student_time_out FROM tbl_student RIGHT JOIN tbl_student_attendance ON tbl_student.student_no = tbl_student_attendance.student_no ORDER BY student_attendance_no"
        )

        for row in self.cursor.fetchall():
            if row[7] is None:
                timein = row[6]
                timeout = row[7]
                self.student_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[6]
                timeout = row[7]
                self.student_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def populate_student_report_treeview(self):
        self.cursor.execute(
            "SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, tbl_student.student_program, tbl_student.student_section, tbl_student_report.student_attendance_date, tbl_student_report.student_time_in, tbl_student_report.student_time_out FROM tbl_student RIGHT JOIN tbl_student_report ON tbl_student.student_no = tbl_student_report.student_no ORDER BY student_report_no"
        )

        for row in self.cursor.fetchall():
            if row[7] is None:
                timein = row[6]
                timeout = row[7]
                self.student_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[6]
                timeout = row[7]
                self.student_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def populate_personnel_treeview(self, status):
        self.cursor.execute(
            "SELECT * FROM tbl_personnel WHERE personnel_status = '" + status + "'"
        )  # add where status is isActive

        for row in self.cursor.fetchall():
            self.personnel_tree.insert(
                "",
                "end",
                text=[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                ),
            )

    def populate_personnel_attendance_treeview(self):
        self.cursor.execute(
            "SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname, tbl_personnel.personnel_type, tbl_personnel_attendance.personnel_attendance_date, tbl_personnel_attendance.personnel_time_in, tbl_personnel_attendance.personnel_time_out FROM tbl_personnel RIGHT JOIN tbl_personnel_attendance ON tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no ORDER BY personnel_attendance_no"
        )
        for row in self.cursor.fetchall():
            if row[6] is None:
                timein = row[5]
                timeout = row[6]
                self.personnel_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[5]
                timeout = row[6]
                self.personnel_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def populate_personnel_report_treeview(self):
        self.cursor.execute(
            "SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname, tbl_personnel.personnel_type, tbl_personnel_report.personnel_attendance_date, tbl_personnel_report.personnel_time_in, tbl_personnel_report.personnel_time_out FROM tbl_personnel RIGHT JOIN tbl_personnel_report ON tbl_personnel.personnel_no = tbl_personnel_report.personnel_no ORDER BY personnel_report_no"
        )
        for row in self.cursor.fetchall():
            if row[6] is None:
                timein = row[5]
                timeout = row[6]
                self.personnel_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[5]
                timeout = row[6]
                self.personnel_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def populate_visitor_treeview(self, status):
        self.cursor.execute(
            "SELECT * FROM tbl_visitor WHERE visitor_status = '" + status + "'"
        )  # add where status is isActive

        for row in self.cursor.fetchall():
            self.visitor_tree.insert(
                "",
                "end",
                text=[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                ),
            )

    def populate_visitor_attendance_treeview(self):
        self.cursor.execute(
            "SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, tbl_visitor_attendance.visitor_attendance_date, tbl_visitor_attendance.visitor_time_in, tbl_visitor_attendance.visitor_time_out FROM  tbl_visitor RIGHT JOIN tbl_visitor_attendance ON tbl_visitor.visitor_no = tbl_visitor_attendance.visitor_no ORDER BY visitor_attendance_no"
        )

        for row in self.cursor.fetchall():
            if row[5] is None:
                timein = row[4]
                timeout = row[5]
                self.visitor_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[4]
                timeout = row[5]
                self.visitor_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def populate_visitor_report_treeview(self):
        self.cursor.execute(
            "SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, tbl_visitor_report.visitor_attendance_date, tbl_visitor_report.visitor_time_in, tbl_visitor_report.visitor_time_out FROM  tbl_visitor RIGHT JOIN tbl_visitor_report ON tbl_visitor.visitor_no = tbl_visitor_report.visitor_no ORDER BY visitor_report_no"
        )

        for row in self.cursor.fetchall():
            if row[5] is None:
                timein = row[4]
                timeout = row[5]
                self.visitor_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[4]
                timeout = row[5]
                self.visitor_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def populate_user_treeview(self, status):
        self.cursor.execute(
            "SELECT * FROM tbl_user WHERE user_status = '" + status + "'"
        )  # add where status is isActive

        for row in self.cursor.fetchall():
            self.user_tree.insert(
                "",
                "end",
                text=[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                ),
            )

    def select_user_treeview_row(self):
        self.selected = self.user_tree.focus()
        self.user_values = self.user_tree.item(self.selected, "values")

    def select_student_treeview_row(self):
        self.selected = self.student_tree.focus()
        self.student_values = self.student_tree.item(self.selected, "values")

    def select_personnel_treeview_row(self):
        self.selected = self.personnel_tree.focus()
        self.personnel_values = self.personnel_tree.item(self.selected, "values")

    def select_visitor_treeview_row(self):
        self.selected = self.visitor_tree.focus()
        self.visitor_values = self.visitor_tree.item(self.selected, "values")

    def do_search_student(self, search_term, status):
        self.search_term = search_term
        for child in self.student_tree.get_children():
            self.student_tree.delete(child)

        # search_term = search_entry.get()
        result = self.sql_query.search_student(search_term, status)

        for row in result:
            self.student_tree.insert(
                "",
                "end",
                text=row[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                ),
            )

    def do_search_student_report(self, search_term):
        self.search_term = search_term
        for child in self.student_report_tree.get_children():
            self.student_report_tree.delete(child)

        # search_term = search_entry.get()
        result = self.sql_query.search_student_report(search_term)

        for row in result:
            if row[7] is None:
                timein = row[6]
                timeout = row[7]
                self.student_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[6]
                timeout = row[7]
                self.student_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def populate_student_report_bydate(self, date1, date2):
        for child in self.student_report_tree.get_children():
            self.student_report_tree.delete(child)
        result = self.sql_query.sort_student_report_bydate_docx(date1, date2)

        if result:
            for row in result:
                if row[7] is None:
                    timein = row[6]
                    timeout = row[7]
                    self.student_report_tree.insert(
                        "",
                        "end",
                        text=[0],
                        values=(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            row[4],
                            row[5],
                            timein[0:8],
                            timeout,
                        ),
                    )
                else:
                    timein = row[6]
                    timeout = row[7]
                    self.student_report_tree.insert(
                        "",
                        "end",
                        text=[0],
                        values=(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            row[4],
                            row[5],
                            timein[0:8],
                            timeout[0:8],
                        ),
                    )

            return True
        else:
            messbx.showwarning(
                "Warning", "There are no records of attendance for the selected date."
            )
            return False

    def populate_personnel_report_bydate(self, date1, date2):
        for child in self.personnel_report_tree.get_children():
            self.personnel_report_tree.delete(child)
        result = self.sql_query.sort_personnel_report_bydate_docx(date1, date2)

        if result:
            for row in result:
                if row[6] is None:
                    timein = row[5]
                    timeout = row[6]
                    self.personnel_report_tree.insert(
                        "",
                        "end",
                        text=[0],
                        values=(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            row[4],
                            timein[0:8],
                            timeout,
                        ),
                    )
                else:
                    timein = row[5]
                    timeout = row[6]
                    self.personnel_report_tree.insert(
                        "",
                        "end",
                        text=[0],
                        values=(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            row[4],
                            timein[0:8],
                            timeout[0:8],
                        ),
                    )
            return True
        else:
            messbx.showwarning(
                "Warning", "There are no records of attendance for the selected date."
            )
            return False

    def populate_visitor_report_bydate(self, date1, date2):
        for child in self.visitor_report_tree.get_children():
            self.visitor_report_tree.delete(child)
        result = self.sql_query.sort_visitor_report_bydate_docx(date1, date2)

        if result:
            for row in result:
                if row[5] is None:
                    timein = row[4]
                    timeout = row[5]
                    self.visitor_report_tree.insert(
                        "",
                        "end",
                        text=[0],
                        values=(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            timein[0:8],
                            timeout,
                        ),
                    )
                else:
                    timein = row[4]
                    timeout = row[5]
                    self.visitor_report_tree.insert(
                        "",
                        "end",
                        text=[0],
                        values=(
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            timein[0:8],
                            timeout[0:8],
                        ),
                    )
            return True
        else:
            messbx.showwarning(
                "Warning", "There are no records of attendance for the selected date."
            )
            return False

    # JOCRIAUS--------------------------------------------------------------------------

    def do_search_student_attendance(self, search_term):
        self.search_term = search_term
        for child in self.student_attendance_tree.get_children():
            self.student_attendance_tree.delete(child)

        # search_term = search_entry.get()
        result = self.sql_query.search_student_attendance(search_term)

        for row in result:
            if row[7] is None:
                timein = row[6]
                timeout = row[7]
                self.student_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[6]
                timeout = row[7]
                self.student_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def do_search_personnel(self, search_term, status):
        self.search_term = search_term
        for child in self.personnel_tree.get_children():
            self.personnel_tree.delete(child)

        result = self.sql_query.search_personnel(self.search_term, status)

        for row in result:
            self.personnel_tree.insert(
                "",
                "end",
                text=[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                ),
            )

    def do_search_personnel_report(self, search_term):
        self.search_term = search_term
        for child in self.personnel_report_tree.get_children():
            self.personnel_report_tree.delete(child)

        result = self.sql_query.search_personnel_report(self.search_term)

        for row in result:
            if row[6] is None:
                timein = row[5]
                timeout = row[6]
                self.personnel_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[5]
                timeout = row[6]
                self.personnel_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def do_search_personnel_attendance(self, search_term):
        self.search_term = search_term
        for child in self.personnel_attendance_tree.get_children():
            self.personnel_attendance_tree.delete(child)

        result = self.sql_query.search_personnel_attendance(self.search_term)

        for row in result:
            if row[6] is None:
                timein = row[5]
                timeout = row[6]
                self.personnel_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[5]
                timeout = row[6]
                self.personnel_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def do_search_visitor(self, search_term, status):
        self.search_term = search_term
        for child in self.visitor_tree.get_children():
            self.visitor_tree.delete(child)

        result = self.sql_query.search_visitor(self.search_term, status)

        for row in result:
            self.visitor_tree.insert(
                "",
                "end",
                text=[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                ),
            )

    def do_search_visitor_report(self, search_term):
        self.search_term = search_term
        for child in self.visitor_report_tree.get_children():
            self.visitor_report_tree.delete(child)

        result = self.sql_query.search_visitor_report(self.search_term)

        for row in result:
            if row[5] is None:
                timein = row[4]
                timeout = row[5]
                self.visitor_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[4]
                timeout = row[5]
                self.visitor_report_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def do_search_visitor_attendance(self, search_term):
        self.search_term = search_term
        for child in self.visitor_attendance_tree.get_children():
            self.visitor_attendance_tree.delete(child)

        result = self.sql_query.search_visitor_attendance(self.search_term)

        for row in result:
            if row[5] is None:
                timein = row[4]
                timeout = row[5]
                self.visitor_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout,
                    ),
                )
            else:
                timein = row[4]
                timeout = row[5]
                self.visitor_attendance_tree.insert(
                    "",
                    "end",
                    text=[0],
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        timein[0:8],
                        timeout[0:8],
                    ),
                )

    def do_search_user(self, search_term, status):
        self.search_term = search_term
        for child in self.user_tree.get_children():
            self.user_tree.delete(child)

        result = self.sql_query.search_user(self.search_term, status)

        for row in result:
            self.user_tree.insert(
                "",
                "end",
                text=row[0],
                values=(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                ),
            )

    def refresh_student_treeview(self, status):
        for child in self.student_tree.get_children():
            self.student_tree.delete(child)
        self.populate_student_treeview(status)

    def refresh_personnel_treeview(self, status):
        for child in self.personnel_tree.get_children():
            self.personnel_tree.delete(child)
        self.populate_personnel_treeview(status)

    def refresh_visitor_treeview(self, status):
        for child in self.visitor_tree.get_children():
            self.visitor_tree.delete(child)
        self.populate_visitor_treeview(status)

    def refresh_user_treeview(self, status):
        for child in self.user_tree.get_children():
            self.user_tree.delete(child)
        self.populate_user_treeview(status)

    def refresh_student_att_treeview(self):
        if not self.student_attendance_tree.selection():
            for child in self.student_attendance_tree.get_children():
                self.student_attendance_tree.delete(child)
        self.populate_student_attendance_treeview()

    def refresh_personnel_att_treeview(self):
        if not self.personnel_attendance_tree.selection():
            for child in self.personnel_attendance_tree.get_children():
                self.personnel_attendance_tree.delete(child)
        self.populate_personnel_attendance_treeview()

    def refresh_visitor_att_treeview(self):
        if not self.visitor_attendance_tree.selection():
            for child in self.visitor_attendance_tree.get_children():
                self.visitor_attendance_tree.delete(child)
        self.populate_visitor_attendance_treeview()
