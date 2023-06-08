import matplotlib.pyplot as plt

import controller as ctl

# To implement this program, need to user input that user can choose
# specific method that user wants to do.
# After choose the option, user needs to follow the steps
# for implement each specifid method.
# Author : Dongkwan Kim
# def get_user_input():
while True:
    print("")
    print("***********************")
    print("Program by Dongkwan Kim")
    print("***********************")
    print("")
    user_input = int(input("""Enter a number :
    1. Read records
    2. Insert record
    3. Delete record
    4. Update record
    5. Exit
    """))
    if user_input == 1:
        ctl.display_atlanticcod()
        print("")
        print("***********************")
        print("Program by Dongkwan Kim")
        print("***********************")
        print("")
    elif user_input == 2:
        source = input("Source: ")
        latin_name = input("Latin Name: ")
        english_name = input("English Name: ")
        french_name = input("French Name: ")
        year = input("Year: ")
        month = input("Month: ")
        number_otoliths = input("Number of otoliths: ")
        ctl.create_record(source, latin_name, english_name, french_name, year, month, number_otoliths)
        print("")
        print("***********************")
        print("Program by Dongkwan Kim")
        print("***********************")
        print("")
    elif user_input == 3:
        id = input("Enter the Id to Delete: ")
        ctl.delete_record(id)
        print("")
        print("***********************")
        print("Program by Dongkwan Kim")
        print("***********************")
        print("")
    elif user_input == 4:
        id = input("Id: ")
        source = input("Source: ")
        latin_name = input("Latin Name: ")
        english_name = input("English Name: ")
        french_name = input("French Name: ")
        year = input("Year: ")
        month = input("Month: ")
        number_otoliths = input("Number of otoliths: ")
        ctl.update_record(source, latin_name, english_name, french_name, year, month, number_otoliths, id)
        print("")
        print("***********************")
        print("Program by Dongkwan Kim")
        print("***********************")
        print("")
    elif user_input == 5:
        quit()
    else:
        print("Not a valid option")


# get_user_input()