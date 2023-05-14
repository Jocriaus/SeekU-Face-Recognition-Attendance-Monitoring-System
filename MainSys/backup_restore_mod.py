import os
import pyodbc as odbc
import pandas as pd
import tkinter.messagebox as messbx
import datetime


# REDO THE RESTORE USE UPDATE
# DELETE IF OK NA


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
                if "student_program" in df.columns:

                    """
                    drop_query = (f"ALTER TABLE tbl_student_report "+
                    "ADD CONSTRAINT FK_tbl_student_report_tbl_student "+
                    "FOREIGN KEY (student_no) REFERENCES tbl_student(student_no)")
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    """

                    table = self.reset_table("tbl_student_report")
                    print(table)
                    drop_query = f"ALTER TABLE tbl_student_report DROP CONSTRAINT FK_tbl_student_report_tbl_student"
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    self.delete_data("tbl_student_report")
                    self.delete_data("tbl_student")

                    for index, row in df.iterrows():
                        print(row)
                        query = f"INSERT INTO tbl_student (student_no, student_firstname, student_lastname, student_middlename, student_program, student_section, student_contact_no, student_address, student_status) values (?,?,?,?,?,?, ?, ?, ?)"
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
                    print("recover time")
                    drop_query = (
                        f"ALTER TABLE tbl_student_report "
                        + "ADD CONSTRAINT FK_tbl_student_report_tbl_student "
                        + "FOREIGN KEY (student_no) REFERENCES tbl_student(student_no)"
                    )
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    self.recover_student_report_table(table)
                    messbx.showinfo(
                        "Success", "The records have been updated successfully!"
                    )
                else:
                    print("no student program")
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
                "The CSV File you selected is not for Student Records.",
            )

    def restore_student_report(self, path):
        df2 = pd.read_csv(path)
        df = df2.fillna(value=0)
        try:
            if not df.empty:
                if "student_report_no" in df.columns:
                    """
                    drop_query = (f"ALTER TABLE tbl_student_report "+
                    "ADD CONSTRAINT FK_tbl_student_report_tbl_student "+
                    "FOREIGN KEY (student_no) REFERENCES tbl_student(student_no)")
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    """
                    table = self.reset_table("tbl_student")
                    drop_query = f"ALTER TABLE tbl_student_report DROP CONSTRAINT FK_tbl_student_report_tbl_student"
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    self.delete_data("tbl_student")
                    self.delete_data("tbl_student_report")

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

                        query = f"INSERT INTO tbl_student_report (student_report_no,student_no,student_attendance_date,student_time_in,student_time_out) values (?,?,?,?,?)"
                        self.cursor.execute(
                            query,
                            (
                                row.student_report_no,
                                row.student_no,
                                row.student_attendance_date,
                                row.student_time_in,
                                row.student_time_out,
                            ),
                        )
                        self.cursor.commit()
                    drop_query = (
                        f"ALTER TABLE tbl_student_report "
                        + "ADD CONSTRAINT FK_tbl_student_report_tbl_student "
                        + "FOREIGN KEY (student_no) REFERENCES tbl_student(student_no)"
                    )
                    self.cursor.execute(drop_query)
                    self.cursor.commit()

                    self.recover_student_records_table(table)
                    messbx.showinfo(
                        "Success", "The records have been updated successfully!"
                    )
                else:
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Student Report.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate  CSV File", "The CSV File you selected is empty."
                )
        except Exception as error:
            print(error)
            messbx.showerror(
                "Wrong CSV File", "The CSV File you selected is not for Student Report."
            )

    def restore_personnel(self, path):
        df = pd.read_csv(path)
        try:
            if not df.empty:
                if "personnel_type" in df.columns:

                    drop_query = f"ALTER TABLE tbl_personnel_report DROP CONSTRAINT FK_tbl_personnel_report_tbl_personnel"
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    self.delete_data("tbl_personnel")
                    for index, row in df.iterrows():
                        query = f"INSERT INTO tbl_personnel (personnel_no, personnel_firstname, personnel_lastname, personnel_middlename, personnel_contact_no, personnel_address, personnel_type, personnel_status) values (?, ?, ?, ?, ?, ?, ?, ?)"
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

                    drop_query = (
                        f"ALTER TABLE tbl_personnel_report "
                        + "ADD CONSTRAINT FK_tbl_personnel_report_tbl_personnel "
                        + "FOREIGN KEY (personnel_no) REFERENCES tbl_personnel(personnel_no)"
                    )
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    messbx.showinfo(
                        "Success", "The records have been updated successfully!"
                    )
                else:
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Personnel Records.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate  CSV File", "The CSV File you selected is empty."
                )
        except:
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Personnel Records.",
            )

    def restore_personnel_report(self, path):
        df = pd.read_csv(path)
        try:
            if not df.empty:
                if "personnel_report_no" in df.columns:

                    drop_query = f"ALTER TABLE tbl_personnel_report DROP CONSTRAINT FK_tbl_personnel_report_tbl_personnel"
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    self.delete_data("tbl_personnel_report")
                    for index, row in df.iterrows():

                        query = f"INSERT INTO tbl_personnel_report (personnel_report_no, personnel_no, personnel_attendance_date, personnel_time_in, personnel_time_out) values (?,?,?,?,?)"
                        self.cursor.execute(
                            query,
                            (
                                row.personnel_report_no,
                                row.personnel_no,
                                row.personnel_attendance_date,
                                row.personnel_time_in,
                                row.personnel_time_out,
                            ),
                        )
                        self.cursor.commit()
                    drop_query = (
                        f"ALTER TABLE tbl_personnel_report "
                        + "ADD CONSTRAINT FK_tbl_personnel_report_tbl_personnel "
                        + "FOREIGN KEY (personnel_no) REFERENCES tbl_personnel(personnel_no)"
                    )
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    messbx.showinfo(
                        "Success", "The records have been updated successfully!"
                    )
                else:
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Personnel Report.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate  CSV File", "The CSV File you selected is empty."
                )
        except:
            messbx.showerror(
                "Wrong CSV File",
                "The CSV File you selected is not for Personnel Report.",
            )

    def restore_visitor(self, path):
        df = pd.read_csv(path)
        # try:
        if not df.empty:
            if "visitor_status" in df.columns:
                """
                drop_query = (f"ALTER TABLE tbl_visitor_report "+
                "ADD CONSTRAINT FK_tbl_visitor_report_tbl_visitor "+
                "FOREIGN KEY (visitor_no) REFERENCES tbl_visitor(visitor_no)")
                self.cursor.execute(drop_query)
                self.cursor.commit()
                """
                drop_query = f"ALTER TABLE tbl_visitor_report DROP CONSTRAINT FK_tbl_visitor_report_tbl_visitor"
                self.cursor.execute(drop_query)
                self.cursor.commit()
                self.delete_data("tbl_visitor")
                for index, row in df.iterrows():
                    """
                    if not row.visitor_no:
                        query = (f"SET IDENTITY_INSERT tbl_visitor ON " +
                        "INSERT INTO tbl_visitor (visitor_no, visitor_firstname, visitor_lastname, visitor_contact_no, visitor_address, visitor_status) values (?, ?, ?, ?, ?, ?) "+
                        "SET IDENTITY_INSERT tbl_visitor OFF")
                    else:
                    """
                    """                     
                    query = (f"UPDATE tbl_visitor SET visitor_firstname = ?, visitor_lastname = ?, visitor_contact_no = ?, "+
                    "visitor_address = ?, visitor_status = ? WHERE visitor_no = ?")   
                    """
                    query = (
                        f"SET IDENTITY_INSERT tbl_visitor ON "
                        + "INSERT INTO tbl_visitor (visitor_no, visitor_firstname, visitor_lastname, visitor_contact_no, visitor_address, visitor_status) values (?, ?, ?, ?, ?, ?) "
                        + "SET IDENTITY_INSERT tbl_visitor OFF"
                    )
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
                    self.cursor.commit()
                drop_query = (
                    f"ALTER TABLE tbl_visitor_report "
                    + "ADD CONSTRAINT FK_tbl_visitor_report_tbl_visitor "
                    + "FOREIGN KEY (visitor_no) REFERENCES tbl_visitor(visitor_no)"
                )
                self.cursor.execute(drop_query)
                self.cursor.commit()

                messbx.showinfo(
                    "Success", "The records have been updated successfully!"
                )
            else:
                messbx.showerror(
                    "Wrong CSV File",
                    "The CSV File you selected is not for Visitor Records.",
                )
        else:
            messbx.showerror(
                "Inappropriate  CSV File", "The CSV File you selected is empty."
            )
        # except:
        #    messbx.showerror("Wrong CSV File", "The CSV File you selected is not for Visitor Records.")

    def restore_visitor_report(self, path):
        df = pd.read_csv(path)
        try:
            if not df.empty:
                if "visitor_report_no" in df.columns:
                    drop_query = f"ALTER TABLE tbl_visitor_report DROP CONSTRAINT FK_tbl_visitor_report_tbl_visitor"
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    self.delete_data("tbl_visitor_report")
                    for index, row in df.iterrows():
                        query = f"INSERT INTO tbl_visitor_report (visitor_report_no, visitor_no, visitor_attendance_date, visitor_time_in, visitor_time_out) values (?,?,?,?,?)"
                        self.cursor.execute(
                            query,
                            (
                                row.visitor_report_no,
                                row.visitor_no,
                                row.visitor_attendance_date,
                                row.visitor_time_in,
                                row.visitor_time_out,
                            ),
                        )
                        self.cursor.commit()
                    drop_query = (
                        f"ALTER TABLE tbl_visitor_report "
                        + "ADD CONSTRAINT FK_tbl_visitor_report_tbl_visitor "
                        + "FOREIGN KEY (visitor_no) REFERENCES tbl_visitor(visitor_no)"
                    )
                    self.cursor.execute(drop_query)
                    self.cursor.commit()
                    messbx.showinfo(
                        "Success", "The records have been updated successfully!"
                    )
                else:
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for Visitor Report.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate  CSV File", "The CSV File you selected is empty."
                )
        except:
            messbx.showerror(
                "Wrong CSV File", "The CSV File you selected is not for Visitor Report."
            )

    def restore_user(self, path):
        df = pd.read_csv(path)
        try:
            if not df.empty:
                if "user_no" in df.columns:
                    self.delete_data("tbl_user")
                    reset_startingid_query = f"DBCC CHECKIDENT ('tbl_user', RESEED, 0)"
                    self.cursor.execute(reset_startingid_query)
                    self.connection.commit()

                    set_startingid_query = f"DBCC CHECKIDENT ('tbl_user', RESEED, 1)"
                    self.cursor.execute(set_startingid_query)
                    self.connection.commit()

                    for index, row in df.iterrows():
                        query = (
                            f"SET IDENTITY_INSERT tbl_user ON "
                            + "INSERT INTO tbl_user (user_no, username, password, user_firstname, user_lastname, user_type, user_status) values (?, ?, ?, ?, ?, ?, ?) sa"
                            + "SET IDENTITY_INSERT tbl_user OFF"
                        )
                        self.cursor.execute(
                            query,
                            (
                                row.user_no,
                                row.username,
                                row.password,
                                row.user_firstname,
                                row.user_lastname,
                                row.user_type,
                                row.user_status,
                            ),
                        )
                        self.cursor.commit()
                    messbx.showinfo(
                        "Success", "The records have been updated successfully!"
                    )
                else:
                    messbx.showerror(
                        "Wrong CSV File",
                        "The CSV File you selected is not for User Records.",
                    )
            else:
                messbx.showerror(
                    "Inappropriate  CSV File", "The CSV File you selected is empty."
                )
        except:
            messbx.showerror(
                "Wrong CSV File", "The CSV File you selected is not for User Records."
            )

    def reset_table(self, table_name):
        reset_query = f"SELECT * FROM {table_name}"
        self.cursor.execute(reset_query)
        rows = self.cursor.fetchall()
        print("reset table")
        print(rows)
        return rows

    def recover_student_records_table(self, rows):
        if not len(rows) == 0:
            print("pumnasok sa if")
            for row in rows:
                print("pumasok sa for")
                query = "INSERT INTO tbl_student (student_no, student_firstname, student_lastname, student_middlename, student_program, student_section, student_contact_no, student_address, student_status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                self.cursor.execute(
                    query,
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                )
                self.cursor.commit()
        print("done")

    def recover_student_report_table(self, rows):
        if not len(rows) == 0:
            print("pumnasok sa if")
            for row in rows:
                print("pumasok sa for")
                print(rows)
                print("------------")
                print(row)
                print("rows printed")
                query = "INSERT INTO tbl_student_report (student_report_no, student_no, student_attendance_date, student_time_in, student_time_out) VALUES (?, ?, ?, ?, ?)"
                self.cursor.execute(query, row)
                self.cursor.commit()
        print("done")

    def recover_personnel_table(self, rows):
        if not rows.empty:
            for row in rows:
                query = "INSERT INTO tbl_personnel_report (personnel_report_no, personnel_no, personnel_attendance_date, personnel_time_in, personnel_time_out) VALUES (?, ?, ?, ?, ?)"
                self.cursor.execute(query, row)
                self.cursor.commit()

    def recover_visitor_table(self, rows):
        if not rows.empty:
            for row in rows:
                query = "INSERT INTO tbl_visitor_report (visitor_report_no, visitor_no, visitor_attendance_date, visitor_time_in, visitor_time_out) VALUES (?, ?, ?, ?, ?)"
                self.cursor.execute(query, row)
                self.cursor.commit()

    def delete_data(self, table_name):
        delete_query = f"DELETE FROM {table_name}"
        self.cursor.execute(delete_query)
        self.cursor.commit()

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
