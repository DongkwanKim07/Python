# This is contoller class.
# Spent a lot of time how to implement each requirement.
# Then decide to use user input method,
# so user can choose what they want to
# such as create, read, update, delete, make a new file
# Author : Dongkwan Kim
import View


# User can choose the options that what user want to implement
# Use user input statement for specific order.
# Author : Dongkwan Kim
def get_user_input():
    user_input = int(input("""Enter a number:
    1. Read records
    2. Insert record
    3. Delete record
    4. Update record
    5. Replace data using new file
    6. Write data to new csv file\n"""))
    # print(user_input)
    if user_input == 1:
        user_input_reading = int(input("How many records do you want to read? \n"))
        View.print_data(user_input_reading)
    elif user_input == 2:
        user_input_source = input("Source:")
        user_input_ln = input("Latin Name:")
        user_input_en = input("English Name:")
        user_input_fn = input("French Name:")
        user_input_y = input("Year:")
        user_input_m = input("Month:")
        user_input_num_otoliths = input("Number of otoliths:")
        View.create_record(user_input_source, user_input_ln, user_input_en, user_input_fn, user_input_y, user_input_m, user_input_num_otoliths)
    elif user_input == 3:
        user_input_index = int(input("Type the index of the record to be deleted: "))
        View.delete_record(user_input_index)
    elif user_input == 4:
        user_input_index = int(input("call method to update. Enter index of the record to update:"))
        View.view_one_record(user_input_index)
        print("Enter new data")
        user_input_source = input("Source:")
        user_input_ln = input("Latin Name:")
        user_input_en = input("English Name:")
        user_input_fn = input("French Name:")
        user_input_y = input("Year:")
        user_input_m = input("Month:")
        user_input_num_otoliths = input("Number of otoliths:")
        View.update_record(user_input_index, user_input_source, user_input_ln, user_input_en, user_input_fn, user_input_y, user_input_m, user_input_num_otoliths)
    elif user_input == 5:
        user_input_filename = input("Enter filename:")
        View.load_data_from_file(user_input_filename)
    elif user_input == 6:
        user_input_filename = input("Enter filename:")
        View.make_new(user_input_filename)

    else:
        print("Not a valid option")


View.load_data_from_file("NAFO-4TVN-Atlantic-Cod-otoliths.csv")


get_user_input()
