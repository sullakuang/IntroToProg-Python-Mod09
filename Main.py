# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# QKuang,12.06.2019,Created started script
# QKuang,12.06.2019,Added pseudo-code to start assignment 9
# QKuang,12.06.2019,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
import os
# Data -------------------------------------------------------------------- #
strFileName = 'EmployeeData.txt'
list_of_objects = []
lstFileData = []
if __name__ == "__main__":
    import DataClasses as DC
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as Eio

else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
if os.path.exists(strFileName):
    lstFileData = P.FileProcessor.read_data_from_file(strFileName) # read file data
    for line in lstFileData:
        list_of_objects.append(DC.Employee(line[0], line[1], line[2].strip()))
# Show user a menu of options
while(True):
    Eio.print_menu_items()

# Get user's menu option choice
    strChoice = Eio.input_menu_options()
    # Show user current data in the list of employee objects
    if (strChoice.strip() == '1'):
        Eio.print_current_list_items(list_of_objects)  # Show current data in the list
        continue  # to show the menu
    # Let user add data to the list of employee objects
    elif (strChoice.strip() == '2'):
        Emp = Eio.input_employee_data()
        list_of_objects.append(Emp)
        Eio.print_current_list_items(list_of_objects)  # Show current data in the list
        continue  # to show the menu
    # let user save current data to file
    elif (strChoice == '3'):

        Eio.print_current_list_items(list_of_objects)  # Show current data in the list

        # Step 3.4.b - Ask if user if they want save that data
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            P.FileProcessor.save_data_to_file(strFileName, list_of_objects)

            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu
    # Let user exit program
    elif (strChoice == '4'):
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #