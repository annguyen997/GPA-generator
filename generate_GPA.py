#-------------------------------------------------------------------------------
# File Name: generate_GPA.py
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
# Import clear_screen function for clear_screening of terminal where necessary
# Create generate_GPA function with 5 parameters (user_Gnum, stud_records, attempted_credits_dict,  earned_credits_dict, cumulative_GPA_dict)
# Input user Net ID, make it lowercase
#  - If user Net ID not yet exists in dictionary, request G-Number. Otherwise, user needs to exit function.
# Input number of classes to enter for calculate GPA
# Initalize cumulative_class_list as empty list
# FOR LOOP for each number of classes to enter:
#  - Display course number in range
#  - Enter course code, credit hours of that class, and earned grade
#  - Convert alphabetical grade to numeric GPA equivalent
#  - Add the course code, credit hours, and numeric GPA as a list to class_info variable.
#  - Append class_Info to cunulative_class_list.
# After all classes entered, initalize grade_list to zero. 
#  - Calculate TQP of each class, and add it to total TQP ("grade_list")
#  - Divide grade_list by total number of attempted credits. 
# Display cumulative GPA and other information.
# Input ENTER for user to exit option. 
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

#This module and associated function are used to clear sceen from terminal when prompted.
from clear_screen_GPA import clear_screen

def generate_GPA(user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict):
    """
    Input: User's Net-ID, G-Num, and all of the associated grades for each class user wishes to enter
    Output: Prints the GPA, number of attempted credits and earend credits, number of courses
    """
    print "1. GPA Generator"
    print "----------------"
    user_id = raw_input("Enter your George Mason Net ID: ")  #Enter your Net-ID  (Run function each time for each student)
    user_id = user_id.lower()

    #Checks if user_id is already in user_Gnum, if not continue - if yes, then ask user to either retrieve or update.
    if user_id in user_Gnum:
        print ""
        print "This user already exists! You can always update grades, add additional classes or retrieve them."
        raw_input("Press <ENTER> to continue and to return to main menu: ")
        #Returns user to main menu promptly
        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict

    else:  #User ID not yet in system and needs to be created. 
        user_Gnum[user_id] = raw_input("Enter your G-Number: ").upper() #Input G-Number

        #Input number of classes user wants to enter
        number_classes = input("Enter the number of classes you want to calculate for the cumulative GPA: ")

        cumulative_class_list = []     #cumulative class list for each student
        class_string = ""              #displays types of classes entered
        number_entered = 0             #dispalys number of classes entered - initialized at zero
        
        attempted_credit = 0           #initialized attempted credit to zero for each new record.
        earned_credit = 0              #initialized earned credit to zero for each new record.
        
        for course in range(number_classes):
            clear_screen()             #clear screen
            print "1. GPA Generator"
            print "----------------"
            print "Net ID: " + user_id
            print "G-Number: " + user_Gnum[user_id]
            if class_string: #If there is something in class_string; if False it does not print 
                print ""
                print "There is/are " + str(number_entered) + " course(s) you have entered into the system: "
                print class_string
                print ""
            print "Course " + str(course+1) + " of " + str(number_classes)
            print ""
            print "For course # " + str(course+1) + ":"  #Displays user course number out of "number_classes" to enter. 
            course_code = raw_input("Enter the course code (e.g. IT 106): ") 
            credit_num =  input("Enter the number of credit hours associated with " + str(course_code) + " (e.g. 3): ") 
            class_grade = raw_input("Enter your grade for " + str(course_code) + "\n"
                                    + "(e.g. A+, A, A-, B+, B, B-, C+, C, C-, D, F, W, I): ") 

            course_code = course_code.upper()  #Make course uppercase for systematic purposes.
            class_grade = class_grade.upper()  #Make grade uppercase for systematic purposes.
        
            if not class_string: #Used to display classes have entered - done for aesthetic purposes 
                class_string += str(course_code) + ", "  #First class entered
            else:
                class_string += ", " + str(course_code) + ", "  #Subsequent classes entered
            class_string = class_string[:-2]  #Removes extra comma
            number_entered += 1  #Increases number entered by one
            
            if class_grade == 'F':  #Failed class; no earned credit; impacts GPA
                attempted_credit += credit_num
                class_grade = 0.0

            elif class_grade == 'W': #Withdrawn courses; impacts GPA 
                attempted_credit += credit_num
                #There is no corresponding numeric GPA grade for these letter grades.

            elif class_grade == 'I':  #Used for incomplete courses; no impact on GPA 
                attempted_credit += 0
                earned_credit += 0
                
            else:
                attempted_credit += credit_num  #Student gets attempted and earned credit   
                earned_credit += credit_num

                #equivalent GPA of each letter grade
                if class_grade == 'A+':       
                    class_grade = 4.0
                    
                elif class_grade == 'A':
                    class_grade = 4.0

                elif class_grade == 'A-':
                    class_grade = 3.67

                elif class_grade == 'B+':
                    class_grade = 3.33
                    
                elif class_grade == 'B':
                    class_grade = 3.0

                elif class_grade == 'B-':
                    class_grade = 2.67

                elif class_grade == 'C+':
                    class_grade = 2.33
                    
                elif class_grade == 'C':
                    class_grade = 2.0

                elif class_grade == 'C-':
                    class_grade = 1.67

                elif class_grade == 'D':
                    class_grade = 1.0
                    
            class_info = [course_code, credit_num, class_grade]  #comprehensive class info for each class
            cumulative_class_list.append(class_info)             #add class_info list to cumulative_class_list

        stud_records[user_id] = cumulative_class_list  #Adds to cumulative class list. 

        #THIS SECTION GENERATES THE GPA 
        #Note TQP stands for "Total Quality Points"
        grade_list = 0 #Initializes grade_list (total TQP) to zero.
        for item in range(0, len(cumulative_class_list)): #iterates through each class in the student record 
            try:
                TQP = int(cumulative_class_list[item][1]) * float(cumulative_class_list[item][2]) #mutiplying the credit number for each class with the grade(GPA)= Total quality points
            except ValueError:         #if a letter does not have a GPA equivalent 
                print ""
            else:
                grade_list += TQP      #add the TQP to grade list 

        try:
            cumulative_GPA = (grade_list)/attempted_credit  #Divide total TQP by number of attempted credits
        except ZeroDivisionError:    
            cumulative_GPA = 0.0  #If attempted credit is zero. 

        #adding the attempted credit, earned credit & cumulative GPA as the values in the dictionaries 
        attempted_credits_dict[user_id] = attempted_credit  
        earned_credits_dict[user_id] = earned_credit        
        cumulative_GPA_dict[user_id] = cumulative_GPA
        
        clear_screen() #Clears screen
        print "1. GPA Generator"
        print "----------------"
        print "Net ID: " + user_id  #Prints Net ID
        print "G-Number: " + user_Gnum[user_id]  #Prints G-Number
        print ""
        print "The cumulative GPA for " + "'" + user_id + "'" + " is: " + str(round(cumulative_GPA, 3))   #rounding the cumaltive GPA for printing purposes. It is not rounded in the dictionary values
        print ""
        #Shows attemped and earned credits
        print "This is based on " + str(attempted_credit) + " attempted credits earned, " + str(earned_credit)+ " of which are earned credits." 
        print "This is also based on " + str(len(cumulative_class_list)) + " course(s) entered: "
        print class_string #Displays types of classes entered.
        
        print ""
        raw_input("Press <ENTER> to continue and to return to main menu: ")  #Returns user to main menu. 
        
        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict




