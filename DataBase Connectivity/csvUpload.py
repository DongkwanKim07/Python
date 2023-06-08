import csv
import mysql.connector
# This class includes the method that insert data from csv file to MySQL database.
# First, check the connection to MySQL database.
# Second, read csv file and insert to MySQL database.
# Use INSERT INTO query.
# Author : Dongkwan Kim.
db_conn = mysql.connector.connect(
            host='localhost',
            user='Python',
            passwd='Python',
            port='3308',
            database="pythonproject"
        )
print("database connected")
print("")
print("***********************")
print("Program by Dongkwan Kim")
print("***********************")
print("")

cursor = db_conn.cursor(prepared=True)
csv_data = csv.reader(open('NAFO-4TVN-Atlantic-Cod-otoliths.csv'))
for row in csv_data:
    cursor.execute("INSERT INTO atlanticcod(source, latin_name, english_name, french_name, year, month, number_otoliths) VALUES (?, ?, ?, ?, ?, ?, ?);", row)
    print(row)


db_conn.commit()
cursor.close()
db_conn.close()
print("Done")
print("")
print("***********************")
print("Program by Dongkwan Kim")
print("***********************")
print("")
