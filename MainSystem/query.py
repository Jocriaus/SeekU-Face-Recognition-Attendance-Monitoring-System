import pyodbc as odbc


class dbQueries:
    def __init__(self, master=None):
        # "DESKTOP-DG7AK17\SQLEXPRESS"
        # "STAR-PLATINUM\SQLEXPRESS01"
        # "LAB-A-PC16\SQLEXPRESS"
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
            f"UPDATE tbl_personnel SET personnel_no = ?, personnel_firstname = ?, personnel_lastname = ?, personnel_middlename = ?,"
            + " personnel_contact_no = ?, personnel_address = ?, personnel_type = ?, personnel_status = ? WHERE personnel_no = ?"
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
            pass

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
            f"UPDATE tbl_student SET student_no = ?, student_firstname = ?, student_lastname = ?, student_middlename = ?,"
            + " student_program = ?, student_section = ?, student_contact_no = ?, student_address = ?,"
            + " student_status = ? WHERE student_no = ?"
        )
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
                student_status,
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

            print("Attendance added successfully!")

        else:
            print("Student not found.")

    # add exit time for every null entries on time out

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
            insert_query_attendance = f"INSERT INTO tbl_personnel_attendance (personnel_no, personnel_attendance_date, personnel_time_out) VALUES (?, ?, ?)"
            self.cursor.execute(
                insert_query_attendance,
                (personnel_number, personnel_attendance_date, personnel_time_out),
            )
            self.connection.commit()

            print("Attendance added successfully!")
        else:
            print("Student not found.")

    def visitor_attendance_entry(
        self, visitor_number, visitor_attendance_date, visitor_time_in
    ):
        query = f"SELECT * FROM tbl_visitor WHERE visitor_no = ?"
        self.cursor.execute(query(visitor_number))
        row = self.cursor.fetchone()

        if row:
            insert_query_attendance = f"INSERT INTO tbl_visitor_attendance (visitor_no, visitor_attendance_date, visitor_time_in) VALUES (?, ?, ?)"
            self.cursor.execute(
                insert_query_attendance,
                (visitor_number, visitor_attendance_date, visitor_time_in),
            )
            self.connection.commit()

            print("Attendance added successfully!")
        else:
            print("Student not found.")

    def visitor_attendance_exit(
        self, visitor_number, visitor_attendance_date, visitor_time_out
    ):
        query = f"SELECT * FROM tbl_visitor WHERE visitor_no = ?"
        self.cursor.execute(query(visitor_number))
        row = self.cursor.fetchone()

        if row:
            insert_query_attendance = f"INSERT INTO tbl_visitor_attendance (visitor_no, visitor_attendance_date, visitor_time_out) VALUES (?, ?, ?)"
            self.cursor.execute(
                insert_query_attendance,
                (visitor_number, visitor_attendance_date, visitor_time_out),
            )
            self.connection.commit()

            print("Attendance added successfully!")
        else:
            print("Student not found.")

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
            + " tbl_student.student_section, tbl_student_attendance.student_attendance_date, tbl_student_attendance.student_time_in, tbl_student_attendance.student_time_out "
            + "FROM tbl_student FULL JOIN tbl_student_attendance ON tbl_student.student_no = tbl_student_attendance.student_no WHERE  tbl_student.student_no LIKE ? "
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
            + " tbl_personnel_attendance.personnel_attendance_date, tbl_personnel_attendance.personnel_time_in, tbl_personnel_attendance.personnel_time_out"
            + " FROM tbl_personnel FULL JOIN tbl_personnel_attendance ON tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no"
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
            f"SELECT tbl_visitor.visitor_no, tbl_visitor.visitor_firstname, tbl_visitor.visitor_lastname, tbl_visitor_attendance.visitor_attendance_date,"
            + " tbl_visitor_attendance.visitor_time_in, tbl_visitor_attendance.visitor_time_out"
            + " FROM  tbl_visitor FULL JOIN tbl_visitor_attendance ON tbl_visitor.visitor_no = tbl_visitor_attendance.visitor_no"
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

    def get_password_length(self):
        query = f"SELECT password_length FROM tbl_setting"
        self.cursor.execute(query)
        # Select pasword length and display to entry text

    def get_login_attempts(self):
        query = f"SELECT login_attempt FROM tbl_setting"
        self.cursor.execute(query)
        # Select login attempt and display to entry text

    def set_pass_len_log_att(self, pass_length, log_attempt):
        query = (
            f"INSERT INTO tbl_setting (password_length, login_attempt) VALUES (?, ?, ?)"
        )
        self.cursor.execute(query, (pass_length, log_attempt))
        self.connection.commit()
        # Save pass len & log in attempt to the database

    def get_start_settings(self):
        query = f"SELECT sem_start_setting FROM tbl_setting"
        self.cursor.execute(query)
        # select date and insert to entry text

    def get_end_settings(self):
        query = f"SELECT sem_end_setting FROM tbl_setting"
        self.cursor.execute(query)
        # select date and insert to entry text

    def set_sem_settings(self, sem_start, sem_end):
        query = f"INSERT INTO tbl_setting (sem_start_setting, sem_end_setting) VALUES (?, ?)"
        self.cursor.execute(query, (sem_start, sem_end))
        self.connection.commit()
        # save date to the database

    def set_face_recog_path(self, facerecog_filepath):
        query = f"INSERT INTO tbl_setting (face_recog_file_path) VALUES (?)"
        self.cursor.execute(query, (facerecog_filepath))
        self.connection.commit()
        # save face recog path to database

    def get_face_recog_path(self):
        query = f"SELECT face_recog_file_path FROM tbl_setting"
        self.cursor.execute(query)
        # get face recog path from database

    def set_fr_path_file_date(self, facerecog_date):
        query = f"INSERT INTO tbl_setting (face_recog_date) VALUES (?)"
        self.cursor.execute(query, (facerecog_date))
        # save date

    def get_fr_path_file_date(self):
        query = f"SELECT face_recog_date FROM tbl_setting"
        self.cursor.execute(query)
        # get date

    def set_add_visitor_path(self, add_visitor_filepath):
        query = f"INSERT INTO tbl_setting (add_visitor_file_path) VALUES (?)"
        self.cursor.execute(query, (add_visitor_filepath))
        self.connection.commit()
        # save face recog path to database

    def get_add_visitor_path(self):
        query = f"SELECT add_visitor_file_path FROM tbl_setting"
        self.cursor.execute(query)
        # get face recog path from database

    def set_av_path_file_date(self, add_visitor_file_date):
        query = f"INSERT INTO tbl_setting (add_visitor_date) VALUES (?)"
        self.cursor.execute(query, (add_visitor_file_date))
        # save date

    def get_av_path_file_date(self):
        query = f"SELECT add_visitor_date FROM tbl_setting"
        self.cursor.execute(query)
        # get date

    def check_username(self, username, password):
        query = f"SELECT * FROM tbl_user WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
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
        query = f"SELECT student_no FROM tbl_student WHERE student_no = ?"
        self.cursor.execute(query(student_number))
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
            full_name = student_firstname +" "+ student_middlename +" "+ student_lastname
            return full_name

    def get_student_count(self, count):
        self.count = count
        query = f"SELECT COUNT(*) FROM tbl_student WHERE student_status = 'IsActive'"
        self.cursor.execute(query)
        self.count = self.cursor.fetchone()[0]

        return self.count

    def get_student_attendance_count(self, count):
        self.count = count
        query = (
            f"SELECT COUNT(*) FROM tbl_student INNER JOIN tbl_student_attendance"
            + " ON tbl_student.student_no = tbl_student_attendance.student_no"
        )

        self.cursor.execute(query)
        self.count = self.cursor.fetchone()[0]

        return self.count

    def check_personnel_no(self, personnel_number):
        query = f"SELECT personnel_no FROM tbl_personnel WHERE personnel_no = ?"
        self.cursor.execute(query(personnel_number))
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
            full_name = personnel_firstname +" "+ personnel_middlename+" " + personnel_lastname 

            return full_name

    def get_personnel_count(self, count):
        self.count = count
        query = (
            f"SELECT COUNT(*) FROM tbl_personnel WHERE personnel_status = 'IsActive'"
        )

        self.cursor.execute(query)
        self.count = self.cursor.fetchone()[0]

        return self.count

    def get_personnel_attendance_count(self, count):
        self.count = count
        query = (
            f"SELECT COUNT(*) FROM tbl_personnel INNER JOIN tbl_personnel_attendance"
            + " ON tbl_personnel.personnel_no = tbl_personnel_attendance.personnel_no"
        )

        self.cursor.execute(query)
        self.count = self.cursor.fetchone()[0]

        return self.count

    def check_visitor_no(self, visitor_number):
        query = f"SELECT visitor_no FROM tbl_visitor WHERE visitor_no = ?"
        self.cursor.execute(query(visitor_number))
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
            full_name = visitor_firstname +" "+ visitor_lastname
            return full_name
    def get_visitor_count(self, count):
        self.count = count
        query = f"SELECT COUNT(*) FROM tbl_visitor WHERE visitor_status = 'IsActive'"

        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]

        return count

    def get_visitor_attendance_count(self, count):
        self.count = count
        query = (
            f"SELECT COUNT(*) FROM tbl_visitor INNER JOIN tbl_visitor_attendance"
            + " ON tbl_visitor.visitor_no = tbl_visitor_attendance.visitor_no"
        )

        self.cursor.execute(query)
        self.count = self.cursor.fetchone()[0]

        return self.count


# if db.login_entry("systemeror12", "RanOnline124"):
# print("Login successful")
# else:
# print("Invalid username or password")
