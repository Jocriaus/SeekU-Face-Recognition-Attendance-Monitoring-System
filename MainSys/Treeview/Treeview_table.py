import pyodbc as odbc
import tkinter as tk
import tkinter.ttk as ttk


class TreeviewGUI:
    def __init__(self, master=None):

        self.server = "DESKTOP-DG7AK17\SQLEXPRESS"
        self.database = "seeku_database"
        self.username = ""
        self.password = ""

        self.connection_string = f"Driver={{SQL Server}};Server={self.server};Database={self.database};UID={self.username};PWD={self.password}"

        self.connection = odbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed")

    def student_treeview(self, root):
        self.student_treeview_root = root
        self.student_treeview_root.title("Learning code - Treeview")
        self.student_treeview_root.geometry("1600x900")

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 10 {bold}",
        )

        # Create Treeview Frame
        self.student_treeview_frame = tk.Frame(self.student_treeview_root)
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
        self.student_tree.pack()

        # Defining Columns
        self.student_tree["columns"] = (
            "Student Number",
            "Firstname",
            "Lastname",
            "Middlename",
            "Program",
            "Section",
            "Contact Number",
            "Address",
            "Student Status",
        )

        # Format the columns
        self.student_tree.column("#0", width=0, stretch=tk.NO)
        self.student_tree.column("Student Number", anchor=tk.CENTER, width=140)
        self.student_tree.column("Firstname", anchor=tk.W, width=100)
        self.student_tree.column("Lastname", anchor=tk.W, width=140)
        self.student_tree.column("Middlename", anchor=tk.W, width=140)
        self.student_tree.column("Program", anchor=tk.W, width=140)
        self.student_tree.column("Section", anchor=tk.W, width=140)
        self.student_tree.column("Contact Number", anchor=tk.W, width=140)
        self.student_tree.column("Address", anchor=tk.W, width=140)
        self.student_tree.column("Student Status", anchor=tk.W, width=140)

        # Create Headings
        self.student_tree.heading("#0", text="", anchor=tk.W)
        self.student_tree.heading(
            "Student Number", text="Student Number", anchor=tk.CENTER
        )
        self.student_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.student_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.student_tree.heading("Middlename", text="Middlename", anchor=tk.W)
        self.student_tree.heading("Program", text="Program", anchor=tk.W)
        self.student_tree.heading("Section", text="Section", anchor=tk.W)
        self.student_tree.heading("Contact Number", text="Contact Number", anchor=tk.W)
        self.student_tree.heading("Address", text="Address", anchor=tk.W)
        self.student_tree.heading("Student Status", text="Student Status", anchor=tk.W)

        self.populate_student_treeview()

        return self.student_treeview_frame

    def student_report_treeview(self, root):
        self.student_report_treeview_root = root
        self.student_report_treeview_root.title("Learning code - Treeview")
        self.student_report_treeview_root.geometry("1600x900")

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 10 {bold}",
        )

        # Create Treeview Frame
        self.student_report_treeview_frame = tk.Frame(self.student_report_treeview_root)
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

        self.student_report_tree.pack()

        # Defining Columns
        self.student_report_tree["columns"] = (
            "Student Number",
            "Firstname",
            "Lastname",
            "Middlename",
            "Program",
            "Section",
            "Contact Number",
            "Address",
            "Student Status",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.student_report_tree.column("#0", width=0, stretch=tk.NO)
        self.student_report_tree.column("Student Number", anchor=tk.CENTER, width=140)
        self.student_report_tree.column("Firstname", anchor=tk.W, width=100)
        self.student_report_tree.column("Lastname", anchor=tk.W, width=140)
        self.student_report_tree.column("Middlename", anchor=tk.W, width=140)
        self.student_report_tree.column("Program", anchor=tk.W, width=140)
        self.student_report_tree.column("Section", anchor=tk.W, width=140)
        self.student_report_tree.column("Contact Number", anchor=tk.W, width=140)
        self.student_report_tree.column("Address", anchor=tk.W, width=140)
        self.student_report_tree.column("Student Status", anchor=tk.W, width=140)
        self.student_report_tree.column("Date", anchor=tk.W, width=140)
        self.student_report_tree.column("Time In", anchor=tk.W, width=140)
        self.student_report_tree.column("Time Out", anchor=tk.W, width=140)

        # Create Headings
        self.student_report_tree.heading("#0", text="", anchor=tk.W)
        self.student_report_tree.heading(
            "Student Number", text="Student Number", anchor=tk.CENTER
        )
        self.student_report_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.student_report_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.student_report_tree.heading("Middlename", text="Middlename", anchor=tk.W)
        self.student_report_tree.heading("Program", text="Program", anchor=tk.W)
        self.student_report_tree.heading("Section", text="Section", anchor=tk.W)
        self.student_report_tree.heading(
            "Contact Number", text="Contact Number", anchor=tk.W
        )
        self.student_report_tree.heading("Address", text="Address", anchor=tk.W)
        self.student_report_tree.heading(
            "Student Status", text="Student Status", anchor=tk.W
        )
        self.student_report_tree.heading("Date", text="Date", anchor=tk.W)
        self.student_report_tree.heading("Time In", text="Time In", anchor=tk.W)
        self.student_report_tree.heading("Time Out", text="Time Out", anchor=tk.W)

        self.populate_student_report_treeview()

        return self.student_report_treeview_frame

    def personnel_treeview(self, root):
        self.personnel_treeview_root = root
        self.personnel_treeview_root.title("Learning code - Treeview")
        self.personnel_treeview_root.geometry("1600x900")

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 10 {bold}",
        )

        # Create Treeview Frame
        self.personnel_treeview_frame = tk.Frame(self.personnel_treeview_root)
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

        self.personnel_tree.pack()

        # Defining Columns
        self.personnel_tree["columns"] = (
            "Personnel Number",
            "Firstname",
            "Lastname",
            "Middlename",
            "Contact Number",
            "Address",
            "Personnel Type",
            "Personnel Status",
        )

        # Format the columns
        self.personnel_tree.column("#0", width=0, stretch=tk.NO)
        self.personnel_tree.column("Personnel Number", anchor=tk.CENTER, width=140)
        self.personnel_tree.column("Firstname", anchor=tk.W, width=100)
        self.personnel_tree.column("Lastname", anchor=tk.W, width=140)
        self.personnel_tree.column("Middlename", anchor=tk.W, width=140)
        self.personnel_tree.column("Contact Number", anchor=tk.W, width=140)
        self.personnel_tree.column("Address", anchor=tk.W, width=140)
        self.personnel_tree.column("Personnel Type", anchor=tk.W, width=140)
        self.personnel_tree.column("Personnel Status", anchor=tk.W, width=140)

        # Create Headings
        self.personnel_tree.heading("#0", text="", anchor=tk.W)
        self.personnel_tree.heading(
            "Personnel Number", text="Personnel Number", anchor=tk.CENTER
        )
        self.personnel_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.personnel_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.personnel_tree.heading("Middlename", text="Middlename", anchor=tk.W)
        self.personnel_tree.heading(
            "Contact Number", text="Contact Number", anchor=tk.W
        )
        self.personnel_tree.heading("Address", text="Address", anchor=tk.W)
        self.personnel_tree.heading(
            "Personnel Type", text="Personnel Type", anchor=tk.W
        )
        self.personnel_tree.heading(
            "Personnel Status", text="Personnel Status", anchor=tk.W
        )

        self.populate_personnel_treeview()

        return self.personnel_treeview_frame

    def personnel_report_treeview(self, root):
        self.personnel_report_treeview_root = root
        self.personnel_report_treeview_root.title("Learning code - Treeview")
        self.personnel_report_treeview_root.geometry("1600x900")

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 10 {bold}",
        )

        # Create Treeview Frame
        self.personnel_report_treeview_frame = tk.Frame(
            self.personnel_report_treeview_root
        )
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

        self.personnel_report_tree.pack()

        # Defining Columns
        self.personnel_report_tree["columns"] = (
            "Personnel Number",
            "Firstname",
            "Lastname",
            "Middlename",
            "Contact Number",
            "Address",
            "Personnel Type",
            "Personnel Status",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.personnel_report_tree.column("#0", width=0, stretch=tk.NO)
        self.personnel_report_tree.column(
            "Personnel Number", anchor=tk.CENTER, width=140
        )
        self.personnel_report_tree.column("Firstname", anchor=tk.W, width=100)
        self.personnel_report_tree.column("Lastname", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Middlename", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Contact Number", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Address", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Personnel Type", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Personnel Status", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Date", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Time In", anchor=tk.W, width=140)
        self.personnel_report_tree.column("Time Out", anchor=tk.W, width=140)

        # Create Headings
        self.personnel_report_tree.heading("#0", text="", anchor=tk.W)
        self.personnel_report_tree.heading(
            "Personnel Number", text="Personnel Number", anchor=tk.CENTER
        )
        self.personnel_report_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.personnel_report_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.personnel_report_tree.heading("Middlename", text="Middlename", anchor=tk.W)
        self.personnel_report_tree.heading(
            "Contact Number", text="Contact Number", anchor=tk.W
        )
        self.personnel_report_tree.heading("Address", text="Address", anchor=tk.W)
        self.personnel_report_tree.heading(
            "Personnel Type", text="Personnel Type", anchor=tk.W
        )
        self.personnel_report_tree.heading(
            "Personnel Status", text="Personnel Status", anchor=tk.W
        )
        self.personnel_report_tree.heading("Date", text="Date", anchor=tk.W)
        self.personnel_report_tree.heading("Time In", text="Time In", anchor=tk.W)
        self.personnel_report_tree.heading("Time Out", text="Time Out", anchor=tk.W)

        self.populate_personnel_report_treeview()
        return self.personnel_report_treeview_frame

    def visitor_treeview(self, root):
        self.visitor_treeview_root = root
        self.visitor_treeview_root.title("Learning code - Treeview")
        self.visitor_treeview_root.geometry("1600x900")

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 10 {bold}",
        )

        # Create Treeview Frame
        self.visitor_treeview_frame = tk.Frame(self.visitor_treeview_root)
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

        self.visitor_tree.pack()

        # Defining Columns
        self.visitor_tree["columns"] = (
            "Visitor Number",
            "Firstname",
            "Lastname",
            "Middlename",
            "Contact Number",
            "Address",
            "Visitor Status",
        )

        # Format the columns
        self.visitor_tree.column("#0", width=0, stretch=tk.NO)
        self.visitor_tree.column("Visitor Number", anchor=tk.CENTER, width=140)
        self.visitor_tree.column("Firstname", anchor=tk.W, width=100)
        self.visitor_tree.column("Lastname", anchor=tk.W, width=140)
        self.visitor_tree.column("Middlename", anchor=tk.W, width=140)
        self.visitor_tree.column("Contact Number", anchor=tk.W, width=140)
        self.visitor_tree.column("Address", anchor=tk.W, width=140)
        self.visitor_tree.column("Visitor Status", anchor=tk.W, width=140)

        # Create Headings
        self.visitor_tree.heading("#0", text="", anchor=tk.W)
        self.visitor_tree.heading(
            "Visitor Number", text="Visitor Number", anchor=tk.CENTER
        )
        self.visitor_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.visitor_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.visitor_tree.heading("Middlename", text="Middlename", anchor=tk.W)
        self.visitor_tree.heading("Contact Number", text="Contact Number", anchor=tk.W)
        self.visitor_tree.heading("Address", text="Address", anchor=tk.W)
        self.visitor_tree.heading("Visitor Status", text="Visitor Status", anchor=tk.W)

        self.populate_visitor_treeview()
        return self.visitor_treeview_frame

    def visitor_report_treeview(self, root):
        self.visitor_report_treeview_root = root
        self.visitor_report_treeview_root.title("Learning code - Treeview")
        self.visitor_report_treeview_root.geometry("1600x900")

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 10 {bold}",
        )

        # Create Treeview Frame
        self.visitor_report_treeview_frame = tk.Frame(self.visitor_report_treeview_root)
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

        self.visitor_report_tree.pack()

        # Defining Columns
        self.visitor_report_tree["columns"] = (
            "Visitor Number",
            "Firstname",
            "Lastname",
            "Middlename",
            "Contact Number",
            "Address",
            "Visitor Status",
            "Date",
            "Time In",
            "Time Out",
        )

        # Format the columns
        self.visitor_report_tree.column("#0", width=0, stretch=tk.NO)
        self.visitor_report_tree.column("Visitor Number", anchor=tk.CENTER, width=140)
        self.visitor_report_tree.column("Firstname", anchor=tk.W, width=100)
        self.visitor_report_tree.column("Lastname", anchor=tk.W, width=140)
        self.visitor_report_tree.column("Middlename", anchor=tk.W, width=140)
        self.visitor_report_tree.column("Contact Number", anchor=tk.W, width=140)
        self.visitor_report_tree.column("Address", anchor=tk.W, width=140)
        self.visitor_report_tree.column("Visitor Status", anchor=tk.W, width=140)
        self.visitor_report_tree.column("Date", anchor=tk.W, width=140)
        self.visitor_report_tree.column("Time In", anchor=tk.W, width=140)
        self.visitor_report_tree.column("Time Out", anchor=tk.W, width=140)

        # Create Headings
        self.visitor_report_tree.heading("#0", text="", anchor=tk.W)
        self.visitor_report_tree.heading(
            "Visitor Number", text="Visitor Number", anchor=tk.CENTER
        )
        self.visitor_report_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.visitor_report_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.visitor_report_tree.heading("Middlename", text="Middlename", anchor=tk.W)
        self.visitor_report_tree.heading(
            "Contact Number", text="Contact Number", anchor=tk.W
        )
        self.visitor_report_tree.heading("Address", text="Address", anchor=tk.W)
        self.visitor_report_tree.heading(
            "Visitor Status", text="Visitor Status", anchor=tk.W
        )
        self.visitor_report_tree.heading("Date", text="Date", anchor=tk.W)
        self.visitor_report_tree.heading("Time In", text="Time In", anchor=tk.W)
        self.visitor_report_tree.heading("Time Out", text="Time Out", anchor=tk.W)

        self.populate_visitor_report_treeview()
        return self.visitor_report_treeview_frame

    def user_treeview(self, root):
        self.user_treeview_root = root
        self.user_treeview_root.title("Learning code - Treeview")
        self.user_treeview_root.geometry("1600x900")

        # Configure Style of Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#F7FAE9",
            fieldbackground="F7FAE9",
            font="{arial} 10 {bold}",
        )

        # Create Treeview Frame
        self.user_treeview_frame = tk.Frame(self.user_treeview_root)
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

        self.user_tree.pack()

        # Defining Columns
        self.user_tree["columns"] = (
            "User Number",
            "Username",
            "Password",
            "Firstname",
            "Lastname",
            "User Type",
            "User Status",
        )

        # Format the columns
        self.user_tree.column("#0", width=0, stretch=tk.NO)
        self.user_tree.column("User Number", anchor=tk.CENTER, width=140)
        self.user_tree.column("Username", anchor=tk.W, width=100)
        self.user_tree.column("Password", anchor=tk.W, width=140)
        self.user_tree.column("Firstname", anchor=tk.W, width=140)
        self.user_tree.column("Lastname", anchor=tk.W, width=140)
        self.user_tree.column("User Type", anchor=tk.W, width=140)
        self.user_tree.column("User Status", anchor=tk.W, width=140)

        # Create Headings
        self.user_tree.heading("#0", text="", anchor=tk.W)
        self.user_tree.heading("User Number", text="User Number", anchor=tk.CENTER)
        self.user_tree.heading("Username", text="Username", anchor=tk.W)
        self.user_tree.heading("Password", text="Password", anchor=tk.W)
        self.user_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.user_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.user_tree.heading("User Type", text="User Type", anchor=tk.W)
        self.user_tree.heading("User Status", text="User Status", anchor=tk.W)

        self.populate_user_treeview()
        return self.user_treeview_frame

    def populate_student_treeview(self):
        self.cursor.execute("SELECT * FROM tbl_student")

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

    def populate_student_report_treeview(self):
        self.cursor.execute(
            "SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, tbl_student.student_middlename, tbl_student.student_program, tbl_student.student_section, tbl_student.student_contact_no, tbl_student.student_address, tbl_student.student_status, tbl_student_attendance.student_attendance_date, tbl_student_attendance.student_time_in, tbl_student_attendance.student_time_out FROM tbl_student JOIN tbl_student_attendance ON tbl_student.student_no = tbl_student_attendance.student_no"
        )

        for row in self.cursor.fetchall():
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
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                ),
            )

    def populate_personnel_treeview(self):
        self.cursor.execute("SELECT * FROM tbl_personnel")

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

    def populate_personnel_report_treeview(self):
        self.cursor.execute(
            "SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname, tbl_personnel.personnel_middlename, tbl_personnel.personnel_contact_no, tbl_personnel.personnel_address, tbl_personnel.personnel_type, tbl_personnel.personnel_status, tbl_personnel_attendance.personnel_attendance_date, tbl_personnel_attendance.personnel_time_in, tbl_personnel_attendance.personnel_time_out FROM tbl_personnel JOIN tbl_personnel_attendance ON tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no"
        )
        for row in self.cursor.fetchall():
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
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                ),
            )

    def populate_visitor_treeview(self):
        self.cursor.execute("SELECT * FROM tbl_visitor")

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
                    row[6],
                ),
            )

    def populate_visitor_report_treeview(self):
        self.cursor.execute(
            "SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, tbl_visitor.visitor_contact_no, tbl_visitor.visitor_address, tbl_visitor.visitor_status, tbl_visitor_attendance.visitor_attendance_date, tbl_visitor_attendance.visitor_time_in, tbl_visitor_attendance.visitor_time_out FROM  tbl_visitor JOIN tbl_visitor_attendance ON tbl_visitor.visitor_no = tbl_visitor_attendance.visitor_no"
        )

        for row in self.cursor.fetchall():
            self.visitor_report_tree.insert(
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
                    row[9],
                ),
            )

    def populate_user_treeview(self):
        self.cursor.execute("SELECT * FROM tbl_user")

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

    def run(self):
        self.visitor_report_treeview_root.mainloop()
