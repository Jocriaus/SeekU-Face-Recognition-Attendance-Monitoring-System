import pyodbc as odbc

server = "DESKTOP-DG7AK17\SQLEXPRESS"
database = "seeku_database"
username = ""
password = ""

connection_string = f"Driver={{SQL Server}};Server={server};Database={database};UID={username};PWD={password}"

connection = odbc.connect(connection_string)
print(connection)

connection.close()
