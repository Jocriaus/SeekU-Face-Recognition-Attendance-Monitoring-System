import pyodbc as odbc


class dbQueries:
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

    def login_entry(self, username, password):
        query = f"SELECT * FROM tbl_user WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        row = self.cursor.fetchone()
        if row:
            return True
        else:
            return False

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
        query = f"INSERT INTO tbl_personnel (personnel_no, personnel_firstname, personnel_lastname, personnel_middlename, personnel_contact_no, personnel_address, personnel_type) VALUES  (?, ?, ?, ?, ?, ?, ?)"
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
    ):
        query = f"UPDATE tbl_personnel SET personnel_firstname = ?, personnel_lastname = ?, personnel_middlename = ?, personnel_contact_no = ?, personnel_address = ?, personnel_type = ? WHERE personnel_no = ?"
        self.cursor.execute(
            query,
            (
                personnel_firstname,
                personnel_lastname,
                personnel_middlename,
                personnel_contact_number,
                personnel_address,
                personnel_type,
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

    def update_visitor(
        self,
        visitor_number,
        visitor_firstname,
        visitor_lastname,
        visitor_contact_number,
        visitor_address,
    ):
        query = f"UPDATE tbl_visitor SET visitor_firstname = ?, visitor_lastname = ?, visitor_contact_no = ?, visitor_address = ? WHERE visitor_no = ?"
        self.cursor.execute(
            query,
            (
                visitor_firstname,
                visitor_lastname,
                visitor_contact_number,
                visitor_address,
                visitor_number,
            ),
        )
        self.connection.commit()
        print(f"Personnel {visitor_number} has been updated successfully!")

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
    ):
        query = f"UPDATE tbl_student SET student_firstname = ?, student_lastname = ?, student_middlename = ?, student_program = ?, student_section = ?, student_contact_number = ?, student_address = ? WHERE student_number = ?"
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
                student_number,
            ),
        )
        self.connection.commit()
        print(f"Student {student_number} has been updated successfully!")

    def delete_student_status(self, student_status, student_number):
        query = (
            f"UPDATE tbl_student SET student_status = IsDeleted WHERE student_no = ?"
        )
        self.cursor.execute(query, (student_status, student_number))

        self.connection.commit()
        print(f"Student {student_number} has been updated successfully!")

    def student_attendance_entry(
        self, student_number, student_attendance_date, student_time_in
    ):
        query = f"SELECT * FROM tbl_student WHERE student_no = ?"
        self.cursor.execute(query, (student_number))
        row = self.cursor.fetchone()

        if row:
            insert_query_attendance = f"INSERT INTO tbl_student_attendance (student_no, student_attendance_date, student_time_in) VALUES (?, ?, ?)"
            self.cursor.execute(
                insert_query_attendance,
                (student_number, student_attendance_date, student_time_in),
            )
            self.connection.commit()

            join_query_attendance = f"SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, tbl_student.student_middlename, tbl_student.student_contact_no, tbl_student.student_address, tbl_student.student_status, tbl_student_attendance.student_attendance_date, tbl_student_attendance.student_time_in FROM tbl_student INNER JOIN tbl_student_attendance ON tbl_student.student_no = tbl_student_attendance.student_no WHERE tbl_student.student_no = ? AND tbl_student_attendance.student_attendance_date = ?"

            self.cursor.execute(
                join_query_attendance, (student_number, student_attendance_date)
            )
            print("Attendance added successfully!")

        else:
            print("Student not found.")

    def student_attendance_exit(
        self, student_number, student_attendance_date, student_time_out
    ):
        query = f"SELECT * FROM tbl_student WHERE student_no = ?"
        self.cursor.execute(query, (student_number))
        row = self.cursor.fetchone()

        if row:
            insert_query_attendance = f"INSERT INTO tbl_student_attendance (student_no, student_attendance_date, student_time_out) VALUES (?, ?, ?)"
            self.cursor.execute(
                insert_query_attendance,
                (student_number, student_attendance_date, student_time_out),
            )
            self.connection.commit()

            join_query_attendance = f"SELECT tbl_student.student_no, tbl_student.student_firstname, tbl_student.student_lastname, tbl_student.student_middlename, tbl_student.student_contact_no, tbl_student.student_address, tbl_student.student_status, tbl_student_attendance.student_attendance_date, tbl_student_attendance.student_time_out FROM tbl_student INNER JOIN tbl_student_attendance ON tbl_student.student_no = tbl_student_attendance.student_no WHERE tbl_student.student_no = ? AND tbl_student_attendance.student_attendance_date = ?"

            self.cursor.execute(
                join_query_attendance, (student_number, student_attendance_date)
            )
            print("Attendance added successfully!")

        else:
            print("Student not found.")

    def personnel_attendance_entry(
        self, personnel_number, personnel_attendance_date, personnel_time_in
    ):
        query = f"SELECT * FROM tbl_personnel WHERE personnel_no = ?"
        self.cursor.execute(query, (personnel_number))
        row = self.cursor.fetchone()

        if row:
            insert_query_attendance = f"INSERT INTO tbl_personnel_attendance(personnel_no, personnel_attendance_date, personnel_time_in) VALUES (?, ?, ?)"
            self.cursor.execute(
                insert_query_attendance,
                (personnel_number, personnel_attendance_date, personnel_time_in),
            )
            self.connection.commit()

            join_query_attendance = f"SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname, tbl_personnel.personnel_middlename, tbl_personnel.personnel_contact_no, tbl_personnel.personnel_address, tbl_personnel.personnel_type, tbl_personnel.personnel_status, tbl_personnel_attendance.personnel_attendance_date, tbl_personnel_attendance.personnel_time_in FROM tbl_personnel INNER JOIN tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no WHERE tbl_personnel.personnel_no = ? AND tbl_personnel_attendance.personnel_attendance_date = ?"

            self.cursor.execute(
                join_query_attendance, (personnel_number, personnel_attendance_date)
            )
            print("Attendance added successfully!")
        else:
            print("Student not found.")

    def personnel_attendance_exit(
        self, personnel_number, personnel_attendance_date, personnel_time_out
    ):
        query = f"SELECT * FROM tbl_personnel WHERE personnel_no = ?"
        self.cursor.execute(query, (personnel_number))
        row = self.cursor.fetchone()

        if row:
            insert_query_attendance = f"INSERT INTO tbl_personnel_attendance(personnel_no, personnel_attendance_date, personnel_time_out) VALUES (?, ?, ?)"
            self.cursor.execute(
                insert_query_attendance,
                (personnel_number, personnel_attendance_date, personnel_time_out),
            )
            self.connection.commit()

            join_query_attendance = f"SELECT tbl_personnel.personnel_no, tbl_personnel.personnel_firstname, tbl_personnel.personnel_lastname, tbl_personnel.personnel_middlename, tbl_personnel.personnel_contact_no, tbl_personnel.personnel_address, tbl_personnel.personnel_type, tbl_personnel.personnel_status, tbl_personnel_attendance.personnel_attendance_date, tbl_personnel_attendance.personnel_time_out FROM tbl_personnel INNER JOIN tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no WHERE tbl_personnel.personnel_no = ? AND tbl_personnel_attendance.personnel_attendance_date = ?"

            self.cursor.execute(
                join_query_attendance, (personnel_number, personnel_attendance_date)
            )
            print("Attendance added successfully!")
        else:
            print("Student not found.")

    def visitor_attendance_entry(
        self, visitor_number, visitor_attendance_date, visitor_time_in
    ):
        pass

    def visitor_attendance_exit(
        self, visitor_number, visitor_attendance_date, visitor_time_in
    ):
        pass


# if db.login_entry("systemeror12", "RanOnline124"):
# print("Login successful")
# else:
# print("Invalid username or password")
