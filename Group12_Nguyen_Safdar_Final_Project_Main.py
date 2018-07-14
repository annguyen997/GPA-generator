#-------------------------------------------------------------------------------
# File Name: Group10_Nguyen_Safdar_Final_Project_Main.py
# Student Names: An Nguyen, Sonia Safdar 
# Python version: Python 2.7
# Submission Date: 12/8/2017 
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation, Web (for facts and quotes)
# 1) Python Programming for the Absolute Beginner, Third Edition - Michael Dawson
#-------------------------------------------------------------------------------
# Notes to grader: Fully implemented for purpose and scope of this project
#-------------------------------------------------------------------------------
# Pseudocode: Write your pseudocode here
# An Nguyen
#
# Import all the functions from modules in main application file
#  - This icnludes generate_GPA, update_GPA, retrieve_GPA, delete_GPA, clear_screen_GPA
# Import pickle and shelve modules for saving data files
#
# DISCLAIMER Function
# 1) Print the disclaimer with a disclaimer variable.
# 2) Get option from user to continue program. 
# 3) If user selects yes, clear screen then run main() function. Otherwise, exit the program. 
# 
# MAIN function
# 1) Import the data from Student_GPA_Info.dat (via reading shelf file) and store them to appropriate dictionaries file if exists. 
#    Otherwise, create empty dictionaries. 
# 2) Print generator menu to user. 
# 3) Given a user types in a selection option based from menu (WHILE loop):
#    - Store generate_GPA, update_GPA, retrieve_GPA, delete_GPA, clear_screen_GPA into a, b, c, d, and e for 
#      easier retrieval of values
#    4) If user selects to generate GPA, call generate_GPA function.
#    5) Elif user selects to update GPA, call update_GPA function.
#    6) Elif user selects to retrieve GPA, call retrieve_GPA function.
#    7) Elif user selects to delete GPA record, call delete_GPA function.
#    8) Elif user selects to exit program, 
#       - Write the Student_GPA_Info.dat file. Store all data to appropriate areas to binary file. 
#       - If file does not exist, it is created. If file does exist, original data is overwritten. 
#       - Sync the file and then close the file. 
#    9) Else user needs to select a valid option. Menu prints again. 
#    - For steps 4-8, once function finishes running (call ends), return values are stored to appropriate 
#      variable dictionaries and prints main menu 
#
# Call the disclaimer () function.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

#import all the functions from the modules 
from generate_GPA import generate_GPA   
from update_GPA import update_GPA       
from retrieve_GPA import retrieve_GPA
from delete_GPA import delete_GPA
#This module and associated function are used to clear sceen from terminal when prompted.
from clear_screen_GPA import clear_screen 
#import the modules from Python library
import pickle, shelve   

def disclaimer():     #define disclaimer function
    '''
    Input: The user will input if they would like to continue with the program
    Output: Based on user input, either program continues with main function or program exits. 
    '''
    disclaimer = """
Disclaimer: 
This GPA calculation program is designed for undergraduate students, and it is used for students
that want to determine their cumulative GPA for all classes taken at George Mason University
(not semester GPAs). Additionally, this program is only for non-official and personal purposes only;
this does not replace Mason's official GPA calculation system, and it is used for students to
determine their GPAs.
    
    """
    
    print disclaimer
    print ""
    #Prompt user to enter Yes to continue the program; if not program ends
    option_d = raw_input("If you wish to continue with this program, type 'Yes' or 'Y'. Otherwise, press <ENTER> to continue: ")
    option_d = option_d.upper()
   
    if option_d == 'YES' or option_d == 'Y':  #If user selects yes
        clear_screen()  #Clear screen
        main()          #Call main function

def main():
    '''
    Input: The user selects an option from the menu to do a specific task (e.g. generate GPA, update GPA, etc.)
    Output: The program selects the option and runs the function based on user-input. 
    '''
    #Open the data from a shelved file
    try:
        s = shelve.open('Student_GPA_Info.dat', 'r')

    #If file does not exist, create dictionaries for program. 
    except:
        print ""
        user_Gnum = {}
        stud_records = {}
        attempted_credits_dict = {}
        earned_credits_dict = {}
        cumulative_GPA_dict = {}

    #If file exists, assign the data from a shelved file to respective dictionaries. 
    else:
        user_Gnum = s["user_Gnum"]
        stud_records = s["stud_records"]
        attempted_credits_dict = s["attempted_credits_dict"]
        earned_credits_dict = s["earned_credits_dict"]
        cumulative_GPA_dict = s["cumulative_GPA_dict"]

    #Prints the menu for GPA generator program ("Main Menu") with detailed descriptions.
    generator_menu = """
=== GPA Generator and Retreival System ==

1. GPA Generator
   This option allows students to calculate their GPA. You can add classes/grade information for one student at a time.
   
2. GPA Update
   This option allows students to update their grades for existing classes or add additional classes to calculate their GPA.
   You can update or add classes/grade information for one student at a time.
   
3. GPA Retrieve
   This option allows students to retrieve the GPA and all undergraduate classes taken.
   You can retrieve GPA information for one student at a time.

4. GPA Deletion
   This option is used if students want to delete their entire GPA and its associated information.
   You can delete GPA information for one student at a time.

5. Exit
   This option stores all information to a file annd closes the program.

    """

    print generator_menu
    option = raw_input("Select a menu option: ")  #User selects an option. 
    
    while option != '0':  #This checks if there is an option selected from user.
        #For easier retrieving of values, dictionaries are sent to corresponding variables. 
        a, b, c = user_Gnum, stud_records, attempted_credits_dict
        d, e = earned_credits_dict, cumulative_GPA_dict
        if option == '1':     #generate GPA
            print ""         
            clear_screen()
            user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict = generate_GPA(a, b, c, d, e)  #Calls cumulative_GPA function
            #Should this for loop used for instructors? - done at a later time. 
            #for student in range(int(input("How many students do you want to generate cumulative GPAs?: "))):  
                #print ""
                #print "For student #" + str(student + 1)
                #user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict = generate_GPA(a, b, c, d, e)
            print ""
            clear_screen()        #Clears screen
            print generator_menu  #Returns to main menu.
            option = raw_input("Select a menu option: ")
        elif option == '2':    #update GPA
            print ""
            clear_screen()     #Clears screen
            user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict = update_GPA(a, b, c, d, e)  #Calls update_GPA function
            print ""
            clear_screen()
            print generator_menu  #Returns to main menu.
            option = raw_input("Select a menu option: ")
        elif option == '3':    #Retrieve  GPA
            print ""
            clear_screen()     #Clears screen
            user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict = retrieve_GPA(a, b, c, d, e) #Calls retrieve_GPA function
            print ""
            clear_screen()
            print generator_menu  #Returns to main menu. 
            option = raw_input("Select a menu option: ")
        elif option == '4':   #Delete GPA record
            print ""
            clear_screen()    #Clears screen
            user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict = delete_GPA(a, b, c, d, e)  #Calls delete_GPA function
            print ""
            clear_screen()
            print generator_menu  #Returns to main menu
            option = raw_input("Select a menu option: ")
        elif option == '5':   #Exit program 
            #Store the data into a shelved file. 
            clear_screen()
            s = shelve.open("Student_GPA_Info.dat", "n") #Use shelving to write the data to a file.
            #All data stored is saved as a dictionary. 
            s["user_Gnum"] = a
            s["stud_records"] = b
            s["attempted_credits_dict"] = c
            s["earned_credits_dict"] = d
            s["cumulative_GPA_dict"] = e
            s.sync()    #Confirm that the file was written 
            s.close()   #Close the file. 

            #Informs user that application is exiting. 
            print "Exiting application..."
            print "Thank you for using the GPA Generator and Retrieval System."
            print ""
            raw_input("Press <ENTER> to continue: ")
            break
        else:  #If an invalid option is selected.
            clear_screen()
            print "You have selected an invalid option. Please select a valid option."
            print ""
            print generator_menu #Prints main menu again.
            option = raw_input("Select a menu option: ")

disclaimer()  #Calls the disclaimer function
