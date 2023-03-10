import pyodbc as odbc
import connection as conn


class dbLogin:
    def __init__(self, master=None):
        self.db_connection = conn.dbConnect()

        self.username_input = input("Enter username: ")
        self.password_input = input("Enter password: ")

        self.cursor = self.db_connection.connection.cursor()

        self.query = "SELECT * FROM tbl_user WHERE username = ? AND password = ?"
        self.cursor.execute(self.query, (self.username_input, self.password_input))

        self.user = self.cursor.fetchone()

        if self.user is None:
            print("Invalid username or password")
        else:
            print("Welcome, " + self.user[1] + "!")

        self.cursor.close()
        self.db_connection.connection.close()


if __name__ == "__main__":
    app = dbLogin()
