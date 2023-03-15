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


# if db.login_entry("systemeror12", "RanOnline124"):
# print("Login successful")
# else:
# print("Invalid username or password")
