import csv

import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate
# This class include method to connect to MySQL.
# Need to set specific information for connect to MySQL.
# Use try & catch exception to prevent program crash when connection failed.
# Author : Dongkwan Kim
def db_Connection():
    """Connects to the database"""
    try:
        db_conn = mysql.connector.connect(
            host='localhost',
            user='Python',
            passwd='Python',
            port='3308',
            database="pythonproject"
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with connection")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return db_conn


# print("still good")


# This is the method to create table.
# Can use this method to create table instead of in MySQL
# Author : Dongkwan Kim
def create_table():
    db_conn = db_Connection()
    cursor = db_conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `PythonProject`.`AtlanticCod`(`id` INT NOT NULL AUTO_INCREMENT," \
          "`source` VARCHAR(50) NOT NULL, `latin_name` VARCHAR(50) NOT NULL, `english_name` VARCHAR(50) NOT NULL, `french_name` VARCHAR(50) NOT NULL," \
          "`year` VARCHAR(30) NOT NULL, `month` VARCHAR(30) NOT NULL, `number_otoliths` VARCHAR(30) NOT NULL, PRIMARY KEY(`id`)) ENGINE = InnoDB;"
    cursor.execute(sql)
    db_conn.commit()

    sql1 = "INSERT INTO `PythonProject`.`AtlanticCod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','3','72');"
    sql2 = "INSERT INTO `PythonProject`.`AtlanticCod`(`source`, `latin_name`, `english_name`, `french_name`, `year`, `month`, `number_otoliths`) VALUES ('Commercial','Gadus morhua','Atlantic Cod','Morue franche','1948','3','72');"
    cursor.execute(sql1)
    cursor.execute(sql2)
    db_conn.commit()
    cursor.close()
    db_conn.close()


# print("checking bug")


# This method will load(Read) list of the data from MySQL database.
# Need to use cursor.
# Use SELECT * FROM query to list all the record from MySQL database.
# Author : Dongkwan Kim
def select_all_data():
    db_conn = db_Connection()
    cursor = db_conn.cursor()
    sql = "SELECT * FROM atlanticcod;"
    cursor.execute(sql)
    # listOfData=cursor.fetchall()
    # for data in listOfData:
         # print(data)
    data = cursor.fetchall()
    print(tabulate(data, headers=["ID", "SOURCE", "LATIN_NAME", "ENGLISH_NAME", "FRENCH_NAME", "YEAR", "MONTH", "NUMBER_OTOLITHS"]))
    # return cursor.fetchall()


# print("select all check")


# This is the method that create(Create) new values in MySQL database.
# Use INSERT INTO query with column name.
# Use DB connection and cursor with prepared statement.
# Author : Dongkwan Kim
def create_record(source, latin_name, english_name, french_name, year, month, number_otoliths):
    db_conn = db_Connection()
    cursor = db_conn.cursor(prepared=True)
    # sql = "INSERT INTO atlanticcod(source, latin_name, english_name, french_name, year, month, number_otoliths) VALUES (%S, %S, %S, %S, %S, %S, %S);"
    sql = "INSERT INTO atlanticcod(source, latin_name, english_name, french_name, year, month, number_otoliths) VALUES (?, ?, ?, ?, ?, ?, ?);"
    record = (source, latin_name, english_name, french_name, year, month, number_otoliths)
    cursor.execute(sql, record)
    db_conn.commit()
    print("")
    print("***********************")
    print("Data Insert Success")
    print("***********************")
    cursor.close()
    db_conn.close()


# print("select all check2")


# This is an update(Update) method.
# Need to add 'id' column so user can choose the specific row with id to edit and update.
# Need to invoke all column, so user can edit and update single value.
# Author : Dongkwan Kim
def update_record(source, latin_name, english_name, french_name, year, month, number_otoliths, id):
    db_conn = db_Connection()
    cursor = db_conn.cursor(prepared=True)
    #sql = "UPDATE atlanticcod SET(source, latin_name, english_name, french_name, year, month, number_otoliths) VALUES (?, ?, ?, ?, ?, ?, ?);"
    # sql = "UPDATE atlanticcod SET source=%s, latin_name=%s, english_name=%s, french_name=%s, year=%s, month=%s, number_otoliths=%s, id=%s);"
    sql = "UPDATE atlanticcod SET source=?, latin_name=?, english_name=?, french_name=?, year=?, month=?, number_otoliths=? WHERE id=?;"
    # cursor.execute(sql, (source, latin_name, english_name, french_name, year, month, oto_liths))
    record = (source, latin_name, english_name, french_name, year, month, number_otoliths, id)
    cursor.execute(sql, record)
    db_conn.commit()
    print("")
    print("***********************")
    print("Data Update Success")
    print("***********************")
    cursor.close()
    db_conn.close()


# print("select all check3")


# This is delete(Delete) method that user can delete value from MySQL database.
# This method also use id column, so user can choose specific row to delete.
# Author : Dongkwan Kim
def delete_record(id):
    db_conn = db_Connection()
    cursor = db_conn.cursor(prepared=True)
    sql = "DELETE FROM atlanticcod WHERE id = ?;"
    record = (id,)
    cursor.execute(sql, record)
    db_conn.commit()
    print("")
    print("***********************")
    print("Data Delete Success")
    print("***********************")
    cursor.close()
    db_conn.close()


# def import_csv(source, latin_name, english_name, french_name, year, month, number_otoliths):
#     db_conn = db_Connection()
#     cursor = db_conn.cursor(prepared=True)
#     csv_data = csv.reader(open('NAFO-4TVN-Atlantic-Cod-otoliths.csv'))
#     for row in csv_data:
#         print(row)
#         sql = "INSERT INTO atlanticcod(source, latin_name, english_name, french_name, year, month, number_otoliths) VALUES (?, ?, ?, ?, ?, ?, ?);"
#         record = (source, latin_name, english_name, french_name, year, month, number_otoliths)
#         cursor.execute(sql, record)
#         db_conn.commit()
#         print("CSV data is inserted")
#         cursor.close()
#         db_conn.close()
