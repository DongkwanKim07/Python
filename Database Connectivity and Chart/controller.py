import connection as cn
# This is Controller class.
# Need to use methods in connection class.
# Author : Dongkwan Kim


class Controller:
    dataList = list()


# This method will load(Read) list of the data from MySQL database.
# Need to use cursor.
# Use SELECT * FROM query to list all the record from MySQL database.
# Author : Dongkwan Kim
def display_atlanticcod():
    return cn.select_all_data()


# This is the method that create(Create) new values in MySQL database.
# Use INSERT INTO query with column name.
# Use DB connection and cursor with prepared statement.
# Author : Dongkwan Kim
def create_record(source, latin_name, english_name, french_name, year, month, number_otoliths):
    cn.create_record(source, latin_name, english_name, french_name, year, month, number_otoliths)


# This is an update(Update) method.
# Need to add 'id' column so user can choose the specific row with id to edit and update.
# Need to invoke all column, so user can edit and update single value.
# Author : Dongkwan Kim
def update_record(source, latin_name, english_name, french_name, year, month, number_otoliths, id):
    cn.update_record(
        source, latin_name, english_name, french_name, year, month, number_otoliths, id
    )


# This is delete(Delete) method that user can delete value from MySQL database.
# This method also use id column, so user can choose specific row to delete.
# Author : Dongkwan Kim
def delete_record(id):
    cn.delete_record(id)


def record_chart():
    cn.record_chart()


