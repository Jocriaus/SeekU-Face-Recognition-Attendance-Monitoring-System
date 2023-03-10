import pyodbc as odbc
import connection as conn


class dbQueries:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def connect(self):
        try:
            self.conn = odbc.connect(
                f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
            )
            self.cursor = self.conn.cursor()
            print("Connection successfully")
        except odbc.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed")

    def login_entry(self, username, password):
        query = f"SELECT * FROM tbl_user WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        row = self.cursor.fetchone()
        count = row[0]
        return count > 0


db = dbQueries("DESKTOP-DG7AK17\SQLEXPRESS", "seeku_database", "", "")

db.connect()

if db.login_entry("systemeror12", "RanOnline124"):
    print("Login successful")
else:
    print("Invalid username or password")

db.disconnect()
