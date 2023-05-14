import os
import pyodbc as odbc
import pandas as pd
import tkinter.messagebox as messbx
import datetime

class BackupRestore:
    def __init__(self, master=None):
        # "DESKTOP-DG7AK17\SQLEXPRESS"
        # "STAR-PLATINUM\SQLEXPRESS01"
        # "DESKTOP-3MNAAKG\SQLEXPRESS"
        self.server = "STAR-PLATINUM\SQLEXPRESS01"
        self.database = "seeku_database"
        self.username = ""
        self.password = ""

        self.connection_string = f"Driver={{SQL Server}};Server={self.server};Database={self.database};UID={self.username};PWD={self.password}"

        self.connection = odbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def restore_student(self, path):
        df2 = pd.read_csv(path)
        df = df2.fillna(value=0)
        try:
            if not df.empty:
                print(df)
                if "student_status" in df.columns:
                    for index, row in df.iterrows():
                        if row.student_no:
                            query = (f"UPDATE tbl_student SET student_firstname = ?, student_lastname = ?, student_middlename = ?, "+
                            "student_program = ?, student_section = ?, student_contact_no = ?, student_address = ?, student_status = ? "+
                            "WHERE student_no = ?")
                            self.cursor.execute(
                                query,
                                (
                                    row.student_firstname,
                                    row.student_lastname,
                                    row.student_middlename,
                                    row.student_program,
                                    row.student_section,
                                    row.student_contact_no,
                                    row.student_address,
                                    row.student_status,
                                    row.student_no,
                                ),
                            )
                        else:    
                            query = (f"SET IDENTITY_INSERT tbl_student ON " +
                            "INSERT INTO tbl_student (student_no, student_firstname, student_lastname, student_lastname, student_middlename, student_program,student_section,student_contact_no,student_address,student_status ) values (?, ?, ?, ?, ?, ?,?,?,?) "+
                            "SET IDENTITY_INSERT tbl_student OFF")
                            self.cursor.execute(
                                query,
                                (
                                    row.student_no,
                                    row.student_firstname,
                                    row.student_lastname,
                                    row.student_middlename,
                                    row.student_program,
                                    row.student_section,
                                    row.student_contact_no,
                                    row.student_address,
                                    row.student_status,
                                ),
                            )
                        self.cursor.commit()                 

                else:
                    print("No Student Status")
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Student Records.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate CSV File", "The CSV File you selected is empty."
                )
        except Exception as error:
            print(error)
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Student Records. There is a different error",
            )

    def restore_student_report(self, path):
        df2 = pd.read_csv(path)
        df = df2.fillna(value=0)
        try:
            if not df.empty:
                print(df)
                if "student_report_no" in df.columns:
                    for index, row in df.iterrows():
                        date = datetime.datetime.strptime(
                            row.student_attendance_date, "%d/%m/%Y"
                        ).date()
                        time_in = datetime.datetime.strptime(
                            row.student_time_in, "%H:%M:%S"
                        ).time()
                        time_out = datetime.datetime.strptime(
                            row.student_time_out, "%H:%M:%S"
                        ).time()

                        if row.student_report_no:
                            query = (f"UPDATE tbl_student SET student_no = ?, student_attendance_date = ?, "+
                            "student_time_in = ? WHERE student_report_no = ?")
                            self.cursor.execute(
                                query,
                                (
                                    row.student_report_no,
                                    row.student_no,
                                    date,
                                    time_in,
                                    time_out,
                                ),
                            )
                        else:    
                            query = (f"SET IDENTITY_INSERT tbl_student_report ON " +
                            "INSERT INTO tbl_student_report (student_report_no,student_no,student_attendance_date,student_time_in,student_time_out) values (?,?,?,?,?) "+
                            "SET IDENTITY_INSERT tbl_student_report OFF")
                            self.cursor.execute(
                                query,
                                (
                                    row.student_report_no,
                                    row.student_no,
                                    date,
                                    time_in,
                                    time_out,
                                ),
                            )
                        self.cursor.commit()                 

                else:
                    print("No Student Report no.")
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Student Reports.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate CSV File", "The CSV File you selected is empty."
                )
        except Exception as error:
            print(error)
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Student Reports. There is a different error",
            )


    def restore_personnel(self, path):
        df2 = pd.read_csv(path)
        df = df2.fillna(value=0)
        try:
            if not df.empty:
                print(df)
                if "personnel_status" in df.columns:
                    for index, row in df.iterrows():
                        if row.personnel_no:
                            query = (f"UPDATE tbl_personnel SET personnel_firstname = ?, personnel_lastname = ?, personnel_middlename = ?, "+
                            "personnel_contact_no = ?, personnel_address = ?, personnel_type = ?, personnel_status = ? "+
                            "WHERE personnel_no = ?")
                            self.cursor.execute(
                                query,
                                (
                                    row.personnel_firstname,
                                    row.personnel_lastname,
                                    row.personnel_middlename,
                                    row.personnel_contact_no,
                                    row.personnel_address,
                                    row.personnel_type,
                                    row.personnel_status,
                                    row.personnel_no,
                                ),
                            )
                        else:    
                            query = (f"SET IDENTITY_INSERT tbl_personnel ON " +
                            "INSERT INTO tbl_personnel (personnel_no, personnel_firstname, personnel_lastname, personnel_middlename, personnel_contact_no, personnel_address,personnel_type,personnel_status ) values (?, ?, ?, ?, ?, ?,?,?,?) "+
                            "SET IDENTITY_INSERT tbl_personnel OFF")
                            self.cursor.execute(
                                query,
                                (
                                    row.personnel_no,
                                    row.personnel_firstname,
                                    row.personnel_lastname,
                                    row.personnel_middlename,
                                    row.personnel_contact_no,
                                    row.personnel_address,
                                    row.personnel_type,
                                    row.personnel_status,
                                ),
                            )
                        self.cursor.commit()                 

                    messbx.showinfo(
                        "Success", "The records have been updated successfully!"
                    )
                else:
                    print("No Personnel Status")
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Personnel Records.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate  CSV File", "The CSV File you selected is empty."
                )
        except Exception as error:
            print(error)
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Personnel Records. There is different error",
            )

    def restore_personnel_report(self, path):
        df2 = pd.read_csv(path)
        df = df2.fillna(value=0)
        try:
            if not df.empty:
                print(df)
                if "personnel_report_no" in df.columns:
                    for index, row in df.iterrows():
                        date = datetime.datetime.strptime(
                            row.personnel_attendance_date, "%d/%m/%Y"
                        ).date()
                        time_in = datetime.datetime.strptime(
                            row.personnel_time_in, "%H:%M:%S"
                        ).time()
                        time_out = datetime.datetime.strptime(
                            row.personnel_time_out, "%H:%M:%S"
                        ).time()

                        if row.personnel_report_no:
                            query = (f"UPDATE tbl_personnel SET personnel_no = ?, personnel_attendance_date = ?, "+
                            "personnel_time_in = ? WHERE personnel_report_no = ?")
                            self.cursor.execute(
                                query,
                                (
                                    row.personnel_report_no,
                                    row.personnel_no,
                                    date,
                                    time_in,
                                    time_out,
                                ),
                            )
                        else:    
                            query = (f"SET IDENTITY_INSERT tbl_personnel_report ON " +
                            "INSERT INTO tbl_personnel_report (personnel_report_no,personnel_no,personnel_attendance_date,personnel_time_in,personnel_time_out) values (?,?,?,?,?) "+
                            "SET IDENTITY_INSERT tbl_personnel_report OFF")
                            self.cursor.execute(
                                query,
                                (
                                    row.personnel_report_no,
                                    row.personnel_no,
                                    date,
                                    time_in,
                                    time_out,
                                ),
                            )
                        self.cursor.commit()                 

                else:
                    print("No Personnel report no.")
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Personnel Reports.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate CSV File", "The CSV File you selected is empty."
                )
        except Exception as error:
            print(error)
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Personnel Reports. There is a different error",
            )

    def restore_visitor(self, path):
        df2 = pd.read_csv(path)
        df = df2.fillna(value=0)
        try:
            if not df.empty:
                print(df)
                if "visitor_status" in df.columns:
                    for index, row in df.iterrows():
                        if row.visitor_no:
                            query = (f"UPDATE tbl_visitor SET visitor_firstname = ?, visitor_lastname = ?, visitor_contact_no = ?, "+
                            "visitor_address = ?, visitor_status = ? WHERE visitor_no = ?")         
                            self.cursor.execute(
                                query,
                                (
                                    row.visitor_no,
                                    row.visitor_firstname,
                                    row.visitor_lastname,
                                    row.visitor_contact_no,
                                    row.visitor_address,
                                    row.visitor_status,
                                ),
                            )
                        else:    
                            query = (f"SET IDENTITY_INSERT tbl_visitor ON " +
                            "INSERT INTO tbl_visitor (visitor_no, visitor_firstname, visitor_lastname, visitor_contact_no, visitor_address, visitor_status) values (?, ?, ?, ?, ?, ?) "+
                            "SET IDENTITY_INSERT tbl_visitor OFF") 
                            self.cursor.execute(
                                query,
                                (
                                    row.visitor_firstname,
                                    row.visitor_lastname,
                                    row.visitor_contact_no,
                                    row.visitor_address,
                                    row.visitor_status,
                                    row.visitor_no,
                                ),
                            )
                        self.cursor.commit()                 

                else:
                    print("No Visitor Status")
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Visitor Records.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate CSV File", "The CSV File you selected is empty."
                )
        except Exception as error:
            print(error)
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Visitor Records. There is a different error",
            )

    def restore_visitor_report(self, path):
        df2 = pd.read_csv(path)
        df = df2.fillna(value=0)
        try:
            if not df.empty:
                print(df)
                if "visitor_report_no" in df.columns:
                    for index, row in df.iterrows():
                        date = datetime.datetime.strptime(
                            row.visitor_attendance_date, "%d/%m/%Y"
                        ).date()
                        time_in = datetime.datetime.strptime(
                            row.visitor_time_in, "%H:%M:%S"
                        ).time()
                        time_out = datetime.datetime.strptime(
                            row.visitor_time_out, "%H:%M:%S"
                        ).time()

                        if row.visitor_report_no:
                            query = (f"UPDATE tbl_visitor SET visitor_no = ?, visitor_attendance_date = ?, "+
                            "visitor_time_in = ? WHERE visitor_report_no = ?")
                            self.cursor.execute(
                                query,
                                (
                                    row.visitor_report_no,
                                    row.visitor_no,
                                    date,
                                    time_in,
                                    time_out,
                                ),
                            )
                        else:    
                            query = (f"SET IDENTITY_INSERT tbl_visitor_report ON " +
                            "INSERT INTO tbl_visitor_report (visitor_report_no,visitor_no,visitor_attendance_date,visitor_time_in,visitor_time_out) values (?,?,?,?,?) "+
                            "SET IDENTITY_INSERT tbl_visitor_report OFF")
                            self.cursor.execute(
                                query,
                                (
                                    row.visitor_report_no,
                                    row.visitor_no,
                                    date,
                                    time_in,
                                    time_out,
                                ),
                            )
                        self.cursor.commit()                 

                else:
                    print("No visitor report no.")
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Visitor Reports.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate CSV File", "The CSV File you selected is empty."
                )
        except Exception as error:
            print(error)
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Visitor Reports. There is a different error",
            )

    def backup_data(self, path):
        query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='seeku_database'"
        self.cursor.execute(query)
        table_names = self.cursor.fetchall()
        for table_name in table_names:
            name = table_name[0]
            if (
                name != "tbl_setting"
                and name != "tbl_visitor_attendance"
                and name != "tbl_personnel_attendance"
                and name != "tbl_student_attendance"
            ):
                df = pd.DataFrame()  # reset df for each table
                query = f"SELECT * FROM {name}"

                self.cursor.execute(query)
                column = [desc[0] for desc in self.cursor.description]
                rows = self.cursor.fetchall()
                print(name)

                if rows:
                    selected_values = []

                    # iterate through the rows of the result set
                    for row in rows:
                        # create a list to store the values for this row
                        row_values = []
                        # iterate through the columns of the row
                        for col in enumerate(row):
                            # append the value to the row values list
                            row_values.append(col[1])
                        # append the row values list to the selected values list
                        selected_values.append(row_values)
                    if selected_values and column:
                        df = pd.DataFrame(data=selected_values, columns=column)

                data_filename = os.path.join(path, f"{name}_data.csv")

                df.to_csv(data_filename, index=False)
        messbx.showinfo("Success", "The records have been successfully backed up.")
