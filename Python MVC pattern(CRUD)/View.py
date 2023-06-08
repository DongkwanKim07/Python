# THis class is implement View part for MVC pattern.
# Most of methods will implement in this class.
# This class include C R U D method and implement the other
# requirments
# Author : Dongkwan Kim
import Cod
from Cod import CodFish


class View:
    dataList = list()


# This method will load(Read) list of the date from csv file
# Author : Dongkwan Kim
def load_data_from_file(filename):
    data = Cod.load_data(filename)
    print("Data loaded")
    View.dataList = data
    print("Program by Dongkwan Kim")


# By this method, I can implement the requirment
# that I can set the number of rows to print out.
# Author Dongkwan Kim
def print_data(num_of_records):
    # deal with header
    for i in range(num_of_records):
        print(View.dataList[i].toString())
        print("Program by Dongkwan Kim")


# This is the method that create(Create) new values in the csv file.
# Need to set a parameters to get a collect values.
# Author : Dongkwan Kim
def create_record(source, latin_name, english_name, french_name, year, month, number_otoliths):
    View.dataList.append(CodFish(source, latin_name, english_name, french_name, year, month, number_otoliths))
    print(View.dataList[-1].toString())
    print("Program by Dongkwan Kim")


# This is the delete method that user can delete value from csv file.
# For the delete method, I set the index number that user can
# delete specific line of the list.
# Author : Dongkwan Kim
def delete_record(user_input_index):
    print("Record is removed:")
    print(View.dataList[user_input_index].toString())
    View.dataList.pop(user_input_index)
    print("Program by Dongkwan Kim")


# This is the method that call just one specific row
# So user can edit and update that specific row of value
# Author : Dongkwan Kim
def view_one_record(index):
    print("Record:")
    print(View.dataList[index].toString())
    print("Program by Dongkwan Kim")


# This is an update method.
# User can select specific row to edit or update.
# Need to invoke all column, so user can edit and update single value.
# Author : Dongkwan Kim
def update_record(index, source, latin_name, english_name, french_name, year, month, number_otoliths):
    View.dataList[index].source = source
    View.dataList[index].latin_name = latin_name
    View.dataList[index].english_name = english_name
    View.dataList[index].french_name = french_name
    View.dataList[index].year = year
    View.dataList[index].month = month
    View.dataList[index].number_otoliths = number_otoliths
    print("Record updated:")
    print(View.dataList[index].toString())
    print("Program by Dongkwan Kim")

# This method will use to make a new csv file.
# Author : Dongkwan Kim
def make_new(filename):
    Cod.contents_list(View.dataList, filename)
    print("Create new file")
    print("Program by Dongkwan Kim")
