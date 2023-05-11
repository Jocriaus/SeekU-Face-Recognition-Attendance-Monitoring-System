import pyodbc as odbc
import datetime as datetime


class dbQueries:
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

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed")

    def login_entry(self, username, password):
        query = f"SELECT * FROM tbl_user WHERE username COLLATE Latin1_General_CS_AS = ? AND password COLLATE Latin1_General_CS_AS = ? AND user_status COLLATE Latin1_General_CS_AS = 'IsActive' "
        self.cursor.execute(query, (username, password))
        row = self.cursor.fetchone()
        if row:
            return True
        else:
            return False

    def register_user(
        self, username, password, user_firstname, user_lastname, user_type
    ):
        query = f"INSERT INTO tbl_user (username, password, user_firstname, user_lastname, user_type) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(
            query, (username, password, user_firstname, user_lastname, user_type)
        )
        self.connection.commit()
        print(f"User {user_firstname} has been registered successfully!")

    def update_user(
        self,
        user_username,
        user_password,
        user_firstname,
        user_lastname,
        user_role,
        user_status,
    ):
        query = f"UPDATE tbl_user SET username = ?, password = ?, user_firstname = ?, user_lastname = ?, user_type = ?, user_status = ? WHERE username = ?"
        self.cursor.execute(
            query,
            (
                user_username,
                user_password,
                user_firstname,
                user_lastname,
                user_role,
                user_status,
                user_username,
            ),
        )
        self.connection.commit()
        print(f"User {user_username} has been updated successfully!")

    def register_personnel(
        self,
        personnel_number,
        personnel_firstname,
        personnel_lastname,
        personnel_middlename,
        personnel_contact_number,
        personnel_address,
        personnel_type,
    ):
        query = (
            f"INSERT INTO tbl_personnel (personnel_no, personnel_firstname, personnel_lastname, personnel_middlename, personnel_contact_no,"
            + " personnel_address, personnel_type) VALUES  (?, ?, ?, ?, ?, ?, ?)"
        )
        self.cursor.execute(
            query,
            (
                personnel_number,
                personnel_firstname,
                personnel_lastname,
                personnel_middlename,
                personnel_contact_number,
                personnel_address,
                personnel_type,
            ),
        )
        self.connection.commit()
        print(f"User {personnel_firstname} has been registered successfully!")

    def update_personnel(
        self,
        personnel_number,
        personnel_firstname,
        personnel_lastname,
        personnel_middlename,
        personnel_contact_number,
        personnel_address,
        personnel_type,
        personnel_status,
    ):
        query = (
            f"UPDATE tbl_personnel SET personnel_firstname = ?, personnel_lastname = ?, personnel_middlename = ?,"
            + " personnel_contact_no = ?, personnel_address = ?, personnel_type = ?, personnel_status = ? WHERE personnel_no = ?"
        )
        self.cursor.execute(
            query,
            (
                personnel_firstname,
                personnel_lastname,
                personnel_middlename,
                personnel_contact_number,
                personnel_address,
                personnel_type,
                personnel_status,
                personnel_number,
            ),
        )
        self.connection.commit()
        print(f"Personnel {personnel_number} has been updated successfully!")

    def delete_personnel_status(self, personnel_status, personnel_number):
        query = f"UPDATE tbl_personnel SET personnel_status = IsDeleted WHERE personnel_no = ?"
        self.cursor.execute(query, (personnel_status, personnel_status))

        self.connection.commit()
        print(f"Personnel {personnel_number} has been updated successfully!")

    def register_visitor(
        self,
        visitor_firstname,
        visitor_lastname,
        visitor_contact_number,
        visitor_address,
    ):
        query = f"INSERT INTO tbl_visitor(visitor_firstname, visitor_lastname, visitor_contact_no, visitor_address) VALUES (?, ?, ?, ?)"
        self.cursor.execute(
            query,
            (
                visitor_firstname,
                visitor_lastname,
                visitor_contact_number,
                visitor_address,
            ),
        )
        self.connection.commit()
        print(f"User {visitor_firstname} has been registered successfully!")

    def capture_visitor_image(
        self,
        visitor_firstname,
        visitor_lastname,
        visitor_contact_number,
        visitor_address,
    ):
        query = f"SELECT visitor_no FROM tbl_visitor WHERE visitor_firstname = ? AND visitor_lastname = ? AND visitor_contact_no = ? AND visitor_address = ?"
        self.cursor.execute(
            query,
            (
                visitor_firstname,
                visitor_lastname,
                visitor_contact_number,
                visitor_address,
            ),
        )

        row = self.cursor.fetchone()

        if row:
            return row
        else:
            row = 0

    def update_visitor(
        self,
        visitor_number,
        visitor_firstname,
        visitor_lastname,
        visitor_contact_number,
        visitor_address,
        visitor_status,
    ):
        query = (
            f"UPDATE tbl_visitor SET visitor_firstname = ?, visitor_lastname = ?, visitor_contact_no = ?, "
            + "visitor_address = ?, visitor_status = ? WHERE visitor_no = ?"
        )
        self.cursor.execute(
            query,
            (
                visitor_firstname,
                visitor_lastname,
                visitor_contact_number,
                visitor_address,
                visitor_status,
                visitor_number,
            ),
        )
        self.connection.commit()
        print(f"Personnel {visitor_number} has been updated successfully!")

    # ano tong delete visitor status
    def delete_visitor_status(self, visitor_status, visitor_number):
        query = (
            f"UPDATE tbl_visitor SET visitor_status = IsDeleted WHERE visitor_no = ?"
        )
        self.cursor.execute(query, (visitor_status, visitor_number))

        self.connection.commit()
        print(f"Visitor {visitor_number} has been updated successfully!")

    def register_student(
        self,
        student_number,
        student_firstname,
        student_lastname,
        student_middlename,
        student_program,
        student_section,
        student_contact_number,
        student_address,
    ):
        query = f"INSERT INTO tbl_student(student_no, student_firstname, student_lastname, student_middlename, student_program, student_section, student_contact_no, student_address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(
            query,
            (
                student_number,
                student_firstname,
                student_lastname,
                student_middlename,
                student_program,
                student_section,
                student_contact_number,
                student_address,
            ),
        )
        self.connection.commit()
        print(f"Student {student_firstname} has been registered successfully!")

    def update_student(
        self,
        student_number,
        student_firstname,
        student_lastname,
        student_middlename,
        student_program,
        student_section,
        student_contact_number,
        student_address,
        student_status,
    ):
        query = (
            f"UPDATE tbl_student SET student_firstname = ?, student_lastname = ?, student_middlename = ?,"
            + " student_program = ?, student_section = ?, student_contact_no = ?, student_address = ?,"
            + " student_status = ? WHERE student_no = ?"
        )
        self.cursor.execute(
            query,
            (
                student_firstname,
                student_lastname,
                student_middlename,
                student_program,
                student_section,
                student_contact_number,
                student_address,
                student_status,
                student_number,
            ),
        )
        self.connection.commit()
        print(f"Student {student_number} has been updated successfully!")

        # CREATE MORE

    def student_attendance_record(
        self,
        custom_no,
        student_number,
        student_attendance_date,
        student_time,
    ):

        query = f"SELECT * FROM tbl_student WHERE student_no = ?"
        self.cursor.execute(query, (student_number))
        row = self.cursor.fetchone()
        

        if row:
            print("there is student")
            query2 = f"SELECT * FROM tbl_student_attendance"
            self.cursor.execute(query2)
            student_att_tbl = self.cursor.fetchall()
            print(student_att_tbl)

            if student_att_tbl:
                tbl_empty = False
                print("Table is not empty")
            else:
                tbl_empty = True
                print("Table is empty")

            query3 = f"SELECT * FROM tbl_student_attendance WHERE student_no = ?"
            self.cursor.execute(query3, (student_number))
            student_no_att_row = self.cursor.fetchone()
            print(student_no_att_row)

            if student_no_att_row:
                have_time_in = True
                print("Have record")
            else:
                have_time_in = False
                print("No record")

            # if attendance table is empty, first attendance will have a custom primary key
            if tbl_empty:
                print("first entry")
                reset_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_student_attendance', RESEED, 0)"
                )
                self.cursor.execute(reset_startingid_query)
                self.connection.commit()

                set_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_student_attendance', RESEED, ?)"
                )
                self.cursor.execute(set_startingid_query, (custom_no))
                self.connection.commit()
                print(custom_no)
                insert_query_attendance = f"INSERT INTO tbl_student_attendance (student_no, student_attendance_date, student_time_in) VALUES ( ?, ?, ?)"
                self.cursor.execute(
                    insert_query_attendance,
                    (
                        student_number,
                        student_attendance_date,
                        student_time,
                    ),
                )
                self.connection.commit()

            # if there is existing record with that student number
            elif have_time_in:
                print("time_out")
                insert_query_att_exit = f"UPDATE tbl_student_attendance SET student_time_out = ? WHERE student_no = ?"
                self.cursor.execute(
                    insert_query_att_exit,
                    (student_time, student_number),
                )
                self.connection.commit()

            # if the attendance table not empty and there is no record of the student with that student number
            elif (not tbl_empty) and  (not have_time_in):
                """
                print("time_in")
                last_record = self.get_last_record()
                reset_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_student_attendance', RESEED, 0)"
                )
                self.cursor.execute(reset_startingid_query)
                self.connection.commit()

                set_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_student_attendance', RESEED, ?)"
                )
                self.cursor.execute(set_startingid_query, (last_record))
                self.connection.commit()
                """
                insert_query_attendance = f"INSERT INTO tbl_student_attendance (student_no, student_attendance_date, student_time_in) VALUES (?, ?, ?)"
                self.cursor.execute(
                    insert_query_attendance,
                    (student_number, student_attendance_date, student_time),
                )
                self.connection.commit()
            print("Attendance added successfully!")
        else:
            print("Student not found.")

    def personnel_attendance_record(
        self, custom_no, personnel_number, personnel_attendance_date, personnel_time
    ):
        query = f"SELECT * FROM tbl_personnel WHERE personnel_no = ?"
        self.cursor.execute(query, (personnel_number))
        row = self.cursor.fetchone()

        if row:
            query2 = f"SELECT * FROM tbl_personnel_attendance"
            self.cursor.execute(query2)
            personnel_att_row = self.cursor.fetchone()

            if personnel_att_row:
                tbl_empty = False
                print(tbl_empty)
            else:
                tbl_empty = True
                print(tbl_empty)

            query3 = f"SELECT * FROM tbl_personnel_attendance WHERE personnel_no = ?"
            self.cursor.execute(query3, (personnel_number))
            personnel_no_att_row = self.cursor.fetchall()

            if personnel_no_att_row:
                have_time_in = True
                print(tbl_empty)
            else:
                have_time_in = False
                print(tbl_empty)

            # if attendance table is empty, first attendance will have a custom primary key
            if tbl_empty:

                reset_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_personnel_attendance', RESEED, 0)"
                )
                self.cursor.execute(reset_startingid_query)
                self.connection.commit()

                set_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_personnel_attendance', RESEED, ?)"
                )
                self.cursor.execute(set_startingid_query, (custom_no))
                self.connection.commit()

                insert_query_attendance = f"INSERT INTO tbl_personnel_attendance ( personnel_no, personnel_attendance_date, personnel_time_in) VALUES ( ?, ?, ?)"
                self.cursor.execute(
                    insert_query_attendance,
                    (
                        personnel_number,
                        personnel_attendance_date,
                        personnel_time,
                    ),
                )
                self.connection.commit()
                print("Attendance added successfully!")
            # if there is existing record with that personnel number
            elif have_time_in:
                insert_query_att_exit = f"UPDATE tbl_personnel_attendance SET personnel_time_out = ? WHERE personnel_no = ?"
                self.cursor.execute(
                    insert_query_att_exit, (personnel_time, personnel_number)
                )
                self.connection.commit()
                print("Attendance added successfully!")
            # if the attendance table not empty and there is no record of
            elif not tbl_empty:
                insert_query_attendance = f"INSERT INTO tbl_personnel_attendance (personnel_no, personnel_attendance_date, personnel_time_in) VALUES (?, ?, ?)"
                self.cursor.execute(
                    insert_query_attendance,
                    (personnel_number, personnel_attendance_date, personnel_time),
                )
                self.connection.commit()
                print("Attendance added successfully!")
        else:
            print("Personnel not found.")

    def visitor_attendance_record(
        self, custom_no, visitor_number, visitor_attendance_date, visitor_time
    ):
        query = f"SELECT * FROM tbl_visitor WHERE visitor_no = ?"
        self.cursor.execute(query, (visitor_number))
        row = self.cursor.fetchone()

        if row:

            query2 = f"SELECT * FROM tbl_visitor_attendance"
            self.cursor.execute(query2)
            visitor_att_row = self.cursor.fetchone()

            if visitor_att_row:
                tbl_empty = False
                print(tbl_empty)
            else:
                tbl_empty = True

            query3 = f"SELECT * FROM tbl_visitor_attendance WHERE visitor_no = ?"
            self.cursor.execute(query3, (visitor_number))
            visitor_no_att_row = self.cursor.fetchall()

            if visitor_no_att_row:
                have_time_in = True
                print(tbl_empty)
            else:
                have_time_in = False
                print(tbl_empty)

            # if attendance table is empty, first attendance will have a custom primary key
            if tbl_empty:

                reset_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_visitor_attendance', RESEED, 0)"
                )
                self.cursor.execute(reset_startingid_query)
                self.connection.commit()

                set_startingid_query = (
                    f"DBCC CHECKIDENT ('tbl_visitor_attendance', RESEED, ?)"
                )
                self.cursor.execute(set_startingid_query, (custom_no))
                self.connection.commit()

                insert_query_attendance = f"INSERT INTO tbl_visitor_attendance (visitor_no, visitor_attendance_date, visitor_time_in) VALUES ( ?, ?, ?)"
                self.cursor.execute(
                    insert_query_attendance,
                    (visitor_number, visitor_attendance_date, visitor_time),
                )
                self.connection.commit()
                
            # if there is existing record with that visitor number
            elif have_time_in:
                insert_query_att_exit = f"UPDATE tbl_visitor_attendance SET visitor_time_out = ? WHERE visitor_no = ?"
                self.cursor.execute(
                    insert_query_att_exit,
                    (visitor_time, visitor_number),
                )
                self.connection.commit()
                
            # if the attendance table not empty and there is no record of the visitor with that visitor number
            elif not tbl_empty:
                insert_query_attendance = f"INSERT INTO tbl_visitor_attendance (visitor_no, visitor_attendance_date, visitor_time_in) VALUES (?, ?, ?)"
                self.cursor.execute(
                    insert_query_attendance,
                    (visitor_number, visitor_attendance_date, visitor_time),
                )
                self.connection.commit()
                

            print("Attendance added successfully!")
        else:
            print("Visitor not found.")

    def search_student(self, search_term, status):
        query = (
            f"SELECT * FROM tbl_student WHERE (student_no LIKE ? OR student_firstname LIKE ? OR student_lastname LIKE ? "
            + "OR student_middlename LIKE ? OR student_program LIKE ? OR student_section LIKE ? OR student_contact_no LIKE ? OR "
            + "student_address LIKE ?) AND (student_status LIKE ?)"
        )
        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                status,
            ),
        )
        results = self.cursor.fetchall()
        return results

    def search_student_report(self, search_term):
        query = (
            f"SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, tbl_student.student_program,"
            + " tbl_student.student_section, tbl_student_report.student_attendance_date, tbl_student_report.student_time_in, tbl_student_report.student_time_out "
            + "FROM tbl_student RIGHT JOIN tbl_student_report ON tbl_student.student_no = tbl_student_report.student_no WHERE  tbl_student.student_no LIKE ? "
            + "OR tbl_student.student_firstname LIKE ? OR tbl_student.student_lastname LIKE ? OR tbl_student.student_program LIKE ? "
            + "OR tbl_student.student_section LIKE ? OR tbl_student_report.student_attendance_date LIKE ? OR tbl_student_report.student_time_in LIKE ?"
            + " OR tbl_student_report.student_time_out LIKE ? "
        )
        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
            ),
        )

        results = self.cursor.fetchall()
        return results

    def search_student_attendance(self, search_term):
        query = (
            f"SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, tbl_student.student_program,"
            + " tbl_student.student_section, tbl_student_attendance.student_attendance_date, tbl_student_attendance.student_time_in, tbl_student_attendance.student_time_out "
            + "FROM tbl_student RIGHT JOIN tbl_student_attendance ON tbl_student.student_no = tbl_student_attendance.student_no WHERE  tbl_student.student_no LIKE ? "
            + "OR tbl_student.student_firstname LIKE ? OR tbl_student.student_lastname LIKE ? OR tbl_student.student_program LIKE ? "
            + "OR tbl_student.student_section LIKE ? OR tbl_student_attendance.student_attendance_date LIKE ? OR tbl_student_attendance.student_time_in LIKE ?"
            + " OR tbl_student_attendance.student_time_out LIKE ? "
        )
        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
            ),
        )

        results = self.cursor.fetchall()
        return results

    def search_personnel(self, search_term, status):
        query = (
            f"SELECT * FROM tbl_personnel WHERE (personnel_no LIKE ? OR personnel_firstname LIKE ? OR personnel_lastname LIKE ? "
            + "OR personnel_middlename LIKE ? OR personnel_contact_no LIKE ? OR personnel_address LIKE ? OR personnel_type LIKE ?)"
            + " AND (personnel_status LIKE ?)"
        )
        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                status,
            ),
        )
        results = self.cursor.fetchall()
        return results

    def search_personnel_report(self, search_term):
        query = (
            f"SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname, tbl_personnel.personnel_type,"
            + " tbl_personnel_report.personnel_attendance_date, tbl_personnel_report.personnel_time_in, tbl_personnel_report.personnel_time_out"
            + " FROM tbl_personnel RIGHT JOIN tbl_personnel_report ON tbl_personnel.personnel_no = tbl_personnel_report.personnel_no"
            + " WHERE tbl_personnel.personnel_no LIKE ? OR tbl_personnel.personnel_firstname LIKE ? OR tbl_personnel.personnel_lastname LIKE ? OR tbl_personnel.personnel_type LIKE ? OR"
            + " tbl_personnel_report.personnel_attendance_date LIKE ? OR tbl_personnel_report.personnel_time_in LIKE ? OR tbl_personnel_report.personnel_time_out LIKE ?"
        )

        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
            ),
        )
        results = self.cursor.fetchall()
        return results

    def search_personnel_attendance(self, search_term):
        query = (
            f"SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname, tbl_personnel.personnel_type,"
            + " tbl_personnel_attendance.personnel_attendance_date, tbl_personnel_attendance.personnel_time_in, tbl_personnel_attendance.personnel_time_out"
            + " FROM tbl_personnel RIGHT JOIN tbl_personnel_attendance ON tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no"
            + " WHERE tbl_personnel.personnel_no LIKE ? OR tbl_personnel.personnel_firstname LIKE ? OR tbl_personnel.personnel_lastname LIKE ? OR tbl_personnel.personnel_type LIKE ? OR"
            + " tbl_personnel_attendance.personnel_attendance_date LIKE ? OR tbl_personnel_attendance.personnel_time_in LIKE ? OR tbl_personnel_attendance.personnel_time_out LIKE ?"
        )

        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
            ),
        )
        results = self.cursor.fetchall()
        return results

    def search_visitor(self, search_term, status):
        query = (
            f"SELECT * FROM tbl_visitor WHERE (visitor_firstname LIKE ? OR visitor_lastname LIKE ? OR visitor_contact_no LIKE ?"
            + " OR visitor_address LIKE ?) AND (visitor_status LIKE ?)"
        )
        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                status,
            ),
        )
        results = self.cursor.fetchall()
        return results

    def search_visitor_report(self, search_term):
        query = (
            f"SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, tbl_visitor_report.visitor_attendance_date,"
            + " tbl_visitor_report.visitor_time_in, tbl_visitor_report.visitor_time_out"
            + " FROM  tbl_visitor RIGHT JOIN tbl_visitor_report ON tbl_visitor.visitor_no = tbl_visitor_report.visitor_no"
            + " WHERE tbl_visitor.visitor_no LIKE ? OR tbl_visitor.visitor_firstname LIKE ? OR tbl_visitor.visitor_lastname LIKE ? OR"
            + " tbl_visitor_report.visitor_attendance_date LIKE ? OR tbl_visitor_report.visitor_time_in LIKE ? OR"
            + " tbl_visitor_report.visitor_time_out LIKE ?"
        )

        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
            ),
        )
        results = self.cursor.fetchall()
        return results

    def search_visitor_attendance(self, search_term):
        query = (
            f"SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, tbl_visitor_attendance.visitor_attendance_date,"
            + " tbl_visitor_attendance.visitor_time_in, tbl_visitor_attendance.visitor_time_out"
            + " FROM  tbl_visitor RIGHT JOIN tbl_visitor_attendance ON tbl_visitor.visitor_no = tbl_visitor_attendance.visitor_no"
            + " WHERE tbl_visitor.visitor_no LIKE ? OR tbl_visitor.visitor_firstname LIKE ? OR tbl_visitor.visitor_lastname LIKE ? OR"
            + " tbl_visitor_attendance.visitor_attendance_date LIKE ? OR tbl_visitor_attendance.visitor_time_in LIKE ? OR"
            + " tbl_visitor_attendance.visitor_time_out LIKE ?"
        )

        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
            ),
        )
        results = self.cursor.fetchall()
        return results

    def search_user(self, search_term, status):
        query = (
            f"SELECT * FROM tbl_user WHERE (username LIKE ? OR password LIKE ? OR user_firstname LIKE ? "
            + "OR user_lastname LIKE ? OR user_type LIKE ?) AND (user_status LIKE ?)"
        )
        self.cursor.execute(
            query,
            (
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                "%" + search_term + "%",
                status,
            ),
        )

        results = self.cursor.fetchall()
        return results

    def sort_student_report_bydate_excel(self, date1, date2):
        query = (
            f"SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, "
            + "tbl_student.student_program, tbl_student.student_section, tbl_student_report.student_attendance_date, "
            + "tbl_student_report.student_time_in, tbl_student_report.student_time_out FROM tbl_student "
            + "RIGHT JOIN tbl_student_report ON tbl_student.student_no = tbl_student_report.student_no "
            + "WHERE student_attendance_date BETWEEN ? AND ?"
        )
        self.cursor.execute(query, (date1, date2))
        column = [desc[0] for desc in self.cursor.description]
        rows = self.cursor.fetchall()
        print(len(column))

        if rows:
            selected_values = []

            # iterate through the rows of the result set
            for row in rows:
                # create a list to store the values for this row
                row_values = []
                # iterate through the columns of the row
                for i, col in enumerate(row):
                    # append the value to the row values list
                    if i >= len(row) - 2:
                        row_values.append(col[0:8])
                    else:
                        row_values.append(col)
                # append the row values list to the selected values list
                selected_values.append(row_values)
            print(len(selected_values))
            return selected_values, column
        else:
            return False, False

    def sort_student_report_bydate_docx(self, date1, date2):
        query = (
            f"SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, "
            + "tbl_student.student_program, tbl_student.student_section, tbl_student_report.student_attendance_date, "
            + "tbl_student_report.student_time_in, tbl_student_report.student_time_out FROM tbl_student "
            + "RIGHT JOIN tbl_student_report ON tbl_student.student_no = tbl_student_report.student_no "
            + "WHERE student_attendance_date BETWEEN ? AND ?"
        )
        self.cursor.execute(query, (date1, date2))
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return False

    def sort_personnel_report_bydate_excel(self, date1, date2):
        query = (
            f"SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname,"
            + "tbl_personnel.personnel_type, tbl_personnel_report.personnel_attendance_date, tbl_personnel_report.personnel_time_in, "
            + "tbl_personnel_report.personnel_time_out FROM tbl_personnel RIGHT JOIN tbl_personnel_report "
            + "ON tbl_personnel.personnel_no = tbl_personnel_report.personnel_no WHERE personnel_attendance_date BETWEEN ? AND ?"
        )
        self.cursor.execute(query, (date1, date2))
        column = [desc[0] for desc in self.cursor.description]
        rows = self.cursor.fetchall()
        print(len(column))

        if rows:
            selected_values = []

            # iterate through the rows of the result set
            for row in rows:
                # create a list to store the values for this row
                row_values = []
                # iterate through the columns of the row
                for i, col in enumerate(row):
                    # append the value to the row values list
                    if i >= len(row) - 2:
                        row_values.append(col[0:8])
                    else:
                        row_values.append(col)
                # append the row values list to the selected values list
                selected_values.append(row_values)
            print(len(selected_values))
            return selected_values, column
        else:
            return False, False

    def sort_personnel_report_bydate_docx(self, date1, date2):
        query = (
            f"SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname,"
            + "tbl_personnel.personnel_type, tbl_personnel_report.personnel_attendance_date, tbl_personnel_report.personnel_time_in, "
            + "tbl_personnel_report.personnel_time_out FROM tbl_personnel RIGHT JOIN tbl_personnel_report "
            + "ON tbl_personnel.personnel_no = tbl_personnel_report.personnel_no WHERE personnel_attendance_date BETWEEN ? AND ?"
        )
        self.cursor.execute(query, (date1, date2))
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return False

    def sort_visitor_report_bydate_excel(self, date1, date2):
        query = (
            f"SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, "
            + "tbl_visitor_report.visitor_attendance_date, tbl_visitor_report.visitor_time_in, tbl_visitor_report.visitor_time_out "
            + "FROM  tbl_visitor RIGHT JOIN tbl_visitor_report ON tbl_visitor.visitor_no = tbl_visitor_report.visitor_no "
            + "WHERE visitor_attendance_date BETWEEN ? AND ?"
        )
        self.cursor.execute(query, (date1, date2))
        column = [desc[0] for desc in self.cursor.description]
        rows = self.cursor.fetchall()
        print(len(column))

        if rows:
            selected_values = []

            # iterate through the rows of the result set
            for row in rows:
                # create a list to store the values for this row
                row_values = []
                # iterate through the columns of the row
                for i, col in enumerate(row):
                    # append the value to the row values list
                    if i >= len(row) - 2:
                        row_values.append(col[0:8])
                    else:
                        row_values.append(col)
                # append the row values list to the selected values list
                selected_values.append(row_values)
            print(len(selected_values))
            return selected_values, column
        else:
            return False, False

    def sort_visitor_report_bydate_docx(self, date1, date2):
        query = (
            f"SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, "
            + "tbl_visitor_report.visitor_attendance_date, tbl_visitor_report.visitor_time_in, tbl_visitor_report.visitor_time_out "
            + "FROM  tbl_visitor RIGHT JOIN tbl_visitor_report ON tbl_visitor.visitor_no = tbl_visitor_report.visitor_no"
            + "WHERE visitor_attendance_date BETWEEN ? AND ?"
        )
        self.cursor.execute(query, (date1, date2))
        rows = self.cursor.fetchall()
        if rows:
            return rows
        else:
            return False

    def check_username(self, username):
        query = f"SELECT * FROM tbl_user WHERE username = ?"
        self.cursor.execute(query, (username))
        row = self.cursor.fetchone()
        if row:
            return True
        else:
            return False
        # query for checking username if existed

    def check_user_type(self, username, password):
        query = f"SELECT user_type FROM tbl_user WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # query for checking user type

    def check_student_no(self, student_number):
        query = f"SELECT * FROM tbl_student WHERE student_no = ?"
        self.cursor.execute(query, (student_number))
        row = self.cursor.fetchone()

        if row:
            return True
        else:
            return False

    def get_student_name(self, student_number):
        query = f"SELECT student_firstname, student_lastname, student_middlename FROM tbl_student WHERE student_no = ?"
        self.cursor.execute(query, (student_number))

        row = self.cursor.fetchone()

        if row:
            student_firstname = row[0]
            student_lastname = row[1]
            student_middlename = row[2]
            return student_firstname, student_lastname, student_middlename

    def get_student_count(self):
        query = f"SELECT COUNT(*) FROM tbl_student WHERE student_status = 'IsActive'"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]

        return count

    def get_student_attendance_count(self):
        query = (
            f"SELECT COUNT(*) FROM tbl_student INNER JOIN tbl_student_attendance"
            + " ON tbl_student.student_no = tbl_student_attendance.student_no"
        )

        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]

        return count

    def check_personnel_no(self, personnel_number):
        query = f"SELECT * FROM tbl_personnel WHERE personnel_no = ?"
        self.cursor.execute(query, (personnel_number))
        row = self.cursor.fetchone()
        if row:
            return True
        else:
            return False

    def get_personnel_name(self, personnel_number):
        query = f"SELECT personnel_firstname, personnel_lastname, personnel_middlename FROM tbl_personnel WHERE personnel_no = ?"
        self.cursor.execute(query, (personnel_number))

        row = self.cursor.fetchone()

        if row:
            personnel_firstname = row[0]
            personnel_lastname = row[1]
            personnel_middlename = row[2]

            return personnel_firstname, personnel_lastname, personnel_middlename

    def get_personnel_count(self):
        query = (
            f"SELECT COUNT(*) FROM tbl_personnel WHERE personnel_status = 'IsActive'"
        )

        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]

        return count

    def get_personnel_attendance_count(self):
        query = (
            f"SELECT COUNT(*) FROM tbl_personnel INNER JOIN tbl_personnel_attendance"
            + " ON tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no"
        )

        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]

        return count

    def check_visitor_no(self, visitor_number):
        query = f"SELECT * FROM tbl_visitor WHERE visitor_no = ?"
        self.cursor.execute(query, (visitor_number))
        row = self.cursor.fetchone()

        if row:
            return True
        else:
            return False

    def get_visitor_name(self, visitor_number):
        query = f"SELECT visitor_firstname, visitor_lastname FROM tbl_visitor WHERE visitor_no = ?"
        self.cursor.execute(query, (visitor_number))

        row = self.cursor.fetchone()

        if row:
            visitor_firstname = row[0]
            visitor_lastname = row[1]
            return visitor_firstname, visitor_lastname

    def get_visitor_count(self):
        query = f"SELECT COUNT(*) FROM tbl_visitor WHERE visitor_status = 'IsActive'"

        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]

        return count

    def get_visitor_attendance_count(self):
        query = (
            f"SELECT COUNT(*) FROM tbl_visitor INNER JOIN tbl_visitor_attendance"
            + " ON tbl_visitor.visitor_no = tbl_visitor_attendance.visitor_no"
        )

        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]

        return count

    # USER-TABLE-QUERY--------------------------------------------------------------------------------------------------------------
    def default_user_if_not_exist(self):
        reset_startingid_query = (
            f"DBCC CHECKIDENT ('tbl_student_attendance', RESEED, 0)"
        )
        self.cursor.execute(reset_startingid_query)
        self.connection.commit()

        query = f"SELECT * FROM tbl_user"
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        condition = False
        if row:
            condition = True
            print(condition)
        else:
            condition = False
            print(condition)

        if not condition:
            query2 = f"INSERT INTO tbl_user (username, password, user_firstname, user_lastname, user_type) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(
                query2,
                (
                    "user",
                    "admin",
                    "default",
                    "user",
                    "System Admin",
                ),
            )
            self.connection.commit()

    def create_personnel_report(self):
        query = (
            f"INSERT INTO tbl_personnel_report SELECT * FROM tbl_personnel_attendance"
        )
        self.cursor.execute(query)
        self.connection.commit()

        query2 = f"Delete FROM tbl_personnel_attendance"
        self.cursor.execute(query2)
        self.connection.commit()

    def create_visitor_report(self):
        query = f"INSERT INTO tbl_visitor_report SELECT * FROM tbl_visitor_attendance"
        self.cursor.execute(query)
        self.connection.commit()

        query2 = f"Delete FROM tbl_visitor_attendance"
        self.cursor.execute(query2)
        self.connection.commit()

    def create_student_report(self):
        query = f"INSERT INTO tbl_student_report SELECT * FROM tbl_student_attendance"
        self.cursor.execute(query)
        self.connection.commit()

        query2 = f"Delete FROM tbl_student_attendance"
        self.cursor.execute(query2)
        self.connection.commit()

    # SETTINGS-TABLE-QUERY--------------------------------------------------------------------------------------------------------------

    def default_settings_if_not_exist(self):
        table_name = "tbl_setting"
        self.cursor.execute(f"SET IDENTITY_INSERT {table_name} ON")
        self.connection.commit()
        reset_startingid_query = f"DBCC CHECKIDENT ('tbl_setting', RESEED, 0)"
        self.cursor.execute(reset_startingid_query)
        self.connection.commit()

        query = f"SELECT * FROM tbl_setting"
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        condition = False
        if row:
            condition = True
            print(condition)
        else:
            condition = False
            print(condition)

        if not condition:
            setting_no = 1
            pass_length = 6
            log_attempt = 5
            sem_end = "2020-01-01"
            facerecog_filepath = "C:\\Users\\JC Austria\\Documents\\GitHub\\Face-Recognition-Attendance-Monitoring-System\\MainSystem\\DataSet"
            facerecog_date = "2020-01-01"
            add_visitor_filepath = "C:\\Users\\JC Austria\\Documents\\GitHub\\Face-Recognition-Attendance-Monitoring-System\\MainSystem\\DataSet\\Guest"
            add_visitor_date = "2020-01-01"
            today_date = "2020-01-01"
            date_set_fldr = "DataSet"
            tolerance_lvl = 0.5
            timeout_time = datetime.datetime.strptime("10:30:00", "%H:%M:%S")
            detection_time = 3
            query2 = (
                f"INSERT INTO tbl_setting (setting_no, password_length, login_attempt,sem_end_setting,"
                + "face_recog_file_path,face_recog_date,av_file_path,av_date, today_date, "
                + "data_set_fldr,tolerance_lvl,timeout_time,detection_time) VALUES (?,?, ?, ? ,?, ?, ?, ? ,? ,? ,? ,?,?)"
            )
            self.cursor.execute(
                query2,
                (
                    setting_no,
                    pass_length,
                    log_attempt,
                    sem_end,
                    facerecog_filepath,
                    facerecog_date,
                    add_visitor_filepath,
                    add_visitor_date,
                    today_date,
                    date_set_fldr,
                    tolerance_lvl,
                    timeout_time,
                    detection_time,
                ),
            )
            self.connection.commit()
            self.cursor.execute(f"SET IDENTITY_INSERT {table_name} OFF")
            self.connection.commit()

    def get_password_length(self):
        query = f"SELECT password_length FROM tbl_setting WHERE setting_no = 1 "
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # Select pasword length and display to entry text

    def get_login_attempts(self):
        query = f"SELECT login_attempt FROM tbl_setting WHERE setting_no = 1 "
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # Select login attempt and display to entry text

    def set_pass_len_log_att(self, pass_length, log_attempt):
        query = f"UPDATE tbl_setting SET password_length = ?, login_attempt = ? WHERE setting_no = 1 "
        self.cursor.execute(query, (pass_length, log_attempt))
        self.connection.commit()
        # Save pass len & log in attempt to the database

    def get_end_settings(self):
        query = f"SELECT sem_end_setting FROM tbl_setting WHERE setting_no = 1 "
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # select date and insert to entry text

    def set_sem_settings(self, sem_end):
        query = f"UPDATE tbl_setting SET sem_end_setting = ? WHERE setting_no = 1 "
        self.cursor.execute(query, (sem_end))
        self.connection.commit()
        # save date to the database

    def records_deactivation(self):
        query = f"UPDATE tbl_student SET student_status = 'IsArchived' "
        self.cursor.execute(query)
        self.connection.commit()
        query = f"UPDATE tbl_visitor SET visitor_status = 'IsArchived'  "
        self.cursor.execute(query)
        self.connection.commit()

    # FR-----------------------------------------
    def set_face_recog_path(self, facerecog_filepath):
        query = f"UPDATE tbl_setting SET face_recog_file_path = ? WHERE setting_no = 1 "
        self.cursor.execute(query, (facerecog_filepath))
        self.connection.commit()
        # save face recog path to database

    def get_face_recog_path(self):
        query = f"SELECT face_recog_file_path FROM tbl_setting WHERE setting_no = 1 "
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # get face recog path from database

    def set_fr_path_file_date(self, facerecog_date):
        query = f"UPDATE tbl_setting SET face_recog_date = ? WHERE setting_no = 1 "
        self.cursor.execute(query, (facerecog_date))
        self.connection.commit()
        # save date

    def get_fr_path_file_date(self):
        query = f"SELECT face_recog_date FROM tbl_setting WHERE setting_no = 1 "
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # get date

    # FR-----------------------------------------
    # AV-----------------------------------------
    def set_add_visitor_path(self, add_visitor_filepath):
        query = f"UPDATE tbl_setting SET av_file_path = ? WHERE setting_no = 1 "
        self.cursor.execute(query, (add_visitor_filepath))
        self.connection.commit()
        # save face recog path to database

    def get_add_visitor_path(self):
        query = f"SELECT av_file_path FROM tbl_setting WHERE setting_no = 1 "
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # get face recog path from database

    def set_av_path_file_date(self, add_visitor_file_date):
        query = f"UPDATE tbl_setting SET av_date = ? WHERE setting_no = 1 "
        self.cursor.execute(query, (add_visitor_file_date))
        self.connection.commit()
        # save date

    def get_av_path_file_date(self):
        query = f"SELECT av_date FROM tbl_setting WHERE setting_no = 1 "
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False
        # get date


    def get_last_record(self):
        query = f"SELECT * FROM tbl_student_attendance WHERE student_attendance_no = (SELECT MAX(student_attendance_no) FROM tbl_student_attendance)"
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            return False
    # AV-----------------------------------------
    def set_client_setting(
        self, tolerance_lvl, data_set_fldr, timeout_time, detection_time
    ):
        query = (
            f"UPDATE tbl_setting SET tolerance_lvl = ?, data_set_fldr = ?,"
            + "timeout_time = ?, detection_time = ? WHERE setting_no = 1"
        )
        self.cursor.execute(
            query, (tolerance_lvl, data_set_fldr, timeout_time, detection_time)
        )
        self.connection.commit()

    def get_detection_time(self):
        query = f"SELECT detection_time FROM tbl_setting WHERE setting_no = 1"
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False

    def get_time_out_time(self):
        query = f"SELECT timeout_time FROM tbl_setting WHERE setting_no = 1"
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False

    def get_today_date(self):
        query = f"SELECT today_date FROM tbl_setting WHERE setting_no = 1"
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False

    def set_today_date(self, today_date):
        query = f"UPDATE tbl_setting SET today_date = ? WHERE setting_no = 1"
        self.cursor.execute(query, (today_date))
        self.connection.commit()

    def update_student_time_out(self, time_out):
        query = f"UPDATE tbl_student_attendance SET student_time_out = ? WHERE student_time_out IS NULL"
        self.cursor.execute(query, (time_out))

    def update_personnel_time_out(self, time_out):
        query = f"UPDATE tbl_personnel_attendance SET personnel_time_out = ? WHERE personnel_time_out IS NULL"
        self.cursor.execute(query, (time_out))

    def update_visitor_time_out(self, time_out):
        query = f"UPDATE tbl_visitor_attendance SET visitor_time_out = ? WHERE visitor_time_out IS NULL"
        self.cursor.execute(query, (time_out))

    def get_data_set_fldr(self):
        query = f"SELECT data_set_fldr FROM tbl_setting WHERE setting_no = 1"
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False

    def get_tolerance_lvl(self):
        query = f"SELECT tolerance_lvl FROM tbl_setting WHERE setting_no = 1"
        self.cursor.execute(query)
        row = self.cursor.fetchone()[0]
        if row:
            return row
        else:
            return False

    def backup_database(self, path, date_time):
        self.backup_file_path = path + "/" + date_time + "_database_backup.bacpac"
        query = f"BACKUP DATABASE {self.database} TO DISK = '{self.backup_file_path}'"
        self.cursor.execute(query)
        self.cursor.commit()

    def restore_database(self, file):
        bacpac_file = file
        query = f"RESTORE DATABASE [{self.database}] FROM DISK = '{bacpac_file}' WITH FILE  = 1, NUONLOAD, REPLACE, STATS = 10"
        self.cursor.execute(query)
        print(f"The database {self.database} has been restored from {bacpac_file}.")

    # SETTINGS-TABLE-QUERY--------------------------------------------------------------------------------------------------------------


# if db.login_entry("systemeror12", "RanOnline124"):
# print("Login successful")
# else:
# print("Invalid username or password")


