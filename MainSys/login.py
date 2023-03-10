import connection as conn


class dbLogin:
    def __init__(self, master=None):
        self.db_connection = conn.dbConnect()

        self.cursor = self.db_connection.connection.cursor()

        self.cursor.execute("SELECT * FROM tbl_user")

        self.result = self.cursor.fetchall()

        for row in self.result:
            print(row)

        self.cursor.close()
        self.db_connection.connection.close()


if __name__ == "__main__":
    app = dbLogin()
