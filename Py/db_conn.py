
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Secret Key',
    port='3306',
    # database='python_crud'
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE python__crud")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)