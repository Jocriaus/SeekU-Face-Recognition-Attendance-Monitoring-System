import tkinter as tk
import tkinter.ttk as ttk
import query as qry


class sampleTable:
    def __init__(self, master=None):
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.sql_query = qry.dbQueries()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        self.root = tk.Tk()
        self.root.title("Learning code - Treeview")
        self.root.geometry("1600x900")

        # Create Treeview Frame
        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(pady=20)

        # Treeview Scrollbar
        self.tree_scrollbar = ttk.Scrollbar(self.tree_frame)
        self.tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create Treeview
        self.my_tree = ttk.Treeview(
            self.tree_frame, yscrollcommand=self.tree_scrollbar.set
        )

        # Configure the scrollbar
        self.tree_scrollbar.config(command=self.my_tree.yview)
        self.my_tree.pack()

        # Defining Columns
        self.my_tree["columns"] = (
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
        self.my_tree.column("#0", width=0, stretch=tk.NO)
        self.my_tree.column("Student Number", anchor=tk.CENTER, width=140)
        self.my_tree.column("Firstname", anchor=tk.W, width=100)
        self.my_tree.column("Lastname", anchor=tk.W, width=140)
        self.my_tree.column("Middlename", anchor=tk.W, width=140)
        self.my_tree.column("Program", anchor=tk.W, width=140)
        self.my_tree.column("Section", anchor=tk.W, width=140)
        self.my_tree.column("Contact Number", anchor=tk.W, width=140)
        self.my_tree.column("Address", anchor=tk.W, width=140)
        self.my_tree.column("Student Status", anchor=tk.W, width=140)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=tk.W)
        self.my_tree.heading("Student Number", text="Student Number", anchor=tk.CENTER)
        self.my_tree.heading("Firstname", text="Firstname", anchor=tk.W)
        self.my_tree.heading("Lastname", text="Lastname", anchor=tk.W)
        self.my_tree.heading("Middlename", text="Middlename", anchor=tk.W)
        self.my_tree.heading("Program", text="Program", anchor=tk.W)
        self.my_tree.heading("Section", text="Section", anchor=tk.W)
        self.my_tree.heading("Contact Number", text="Contact Number", anchor=tk.W)
        self.my_tree.heading("Address", text="Address", anchor=tk.W)
        self.my_tree.heading("Student Status", text="Student Status", anchor=tk.W)

        # Add Data
        """"
        self.data = [
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
            [
                "2000137439",
                "Jerome Vrixen",
                "Mendoza",
                "DC",
                "BSCS",
                "BSCS4A",
                "09693174185",
                "This is an address",
                "IsActive",
            ],
        ]
        """
        """"
        self.count = 0

        for self.record in self.data:
            self.my_tree.insert(
                parent="",
                index="end",
                iid=self.count,
                text="",
                values=(
                    self.record[0],
                    self.record[1],
                    self.record[2],
                    self.record[3],
                    self.record[4],
                    self.record[5],
                    self.record[6],
                    self.record[7],
                    self.record[8],
                ),
            )
            self.count += 1
        """

        self.sql_query.show_table_student(self.my_tree)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = sampleTable()
    app.run()
