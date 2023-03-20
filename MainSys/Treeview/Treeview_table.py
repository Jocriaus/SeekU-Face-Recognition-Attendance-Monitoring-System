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

    def personnel_treeview(self, root):
        self.personnel_treeview_root = root
        self.personnel_treeview_root.title("Learning code - Treeview")
        self.personnel_treeview_root.geometry("1600x900")

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

    def visitor_treeview(self, root):
        self.visitor_treeview_root = root
        self.visitor_treeview_root.title("Learning code - Treeview")
        self.visitor_treeview_root.geometry("1600x900")

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

    def run(self):
        self.visitor_treeview_root.mainloop()
