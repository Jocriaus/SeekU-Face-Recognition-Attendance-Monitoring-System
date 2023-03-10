import connection as conn


class dbQuery:
    def login_user(username_input, password_input):

        db_connection = conn.dbConnect()
        cursor = db_connection.connection.cursor()
        query = "SELECT * FROM tbl_user WHERE username = ? AND password = ?"

        cursor.execute(query, (username_input, password_input))
        user = cursor.fetchone()
        cursor.close()

        if user:
            return True
        else:
            return False
