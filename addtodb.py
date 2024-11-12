import pandas as pd
import pyodbc

server = 'localhost'
database = 'game'
username = 'user'
password = 'user'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Connect to the SQL Server database
    connection = pyodbc.connect(connectionString)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM game_data")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if connection:
        connection.close()