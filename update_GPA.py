#-------------------------------------------------------------------------------
# File Name: update_GPA.py
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
# Input user his/her Net ID. If user exists, continue. If not, request user to exit function. 
# Generate class list to check if class user will enter has already taken. If so, it will only ask for enter new grade. 
#
# Input number of classes to enter/update for calculate GPA

# FOR LOOP for each number of classes to enter:
#  - Display course number in range
#  - IF USER Enters class not in class table 
#       - Display course number in range
#       - Enter course code, credit hours of that class, and earned grade
#       - Convert alphabetical grade to numeric GPA equivalent
#       - Add the course code, credit hours, and numeric GPA as a list to class_info variable.
#       - Append class_Info to cunulative_class_list.
#  - ELSE (User enters classes that is in class table)
#       - Search for class, place it into course_update variable, and then user enters updated grade 
#       - Convert alphabetical grade to numeric GPA equivalent based on certain conditions of original grade.
#           - If grade was F, W, or I - do grade_converter_original 
#           - If grade was between A+ to D - do grade_converter_update
#       - Add the course code, credit hours, and numeric GPA as a list to course_update variable.
#       - Append class_Info to cunulative_class_list.
#       - Remove original record from cumulative_class_list
# After all classes entered, initalize grade_list to zero. 
#  - Calculate TQP of each class, and add it to total TQP ("grade_list")
#  - Divide grade_list by total number of attempted credits. 
# Display cumulative GPA and other information.
# Input ENTER for user to exit option. 
#
# GRADE_CONVERTER_UPDATE function
# This function is used only if retaken class has originally a passing grade. 
# Assigned credit number to attempted_credit
# Convert grade to numeric GPA.
# Return attempted_credit and class_grade.
#
# GRADE_CONVERTER_ORIGINAL function
# This function is used only if retaken class was an F, W, or I or student wants to input additional classes.
# Initialize earned credit as zero. 
# Convert grade to numeric GPA eqivalent (not applicable for W and I). Increase attempted/earned credit where necessary.
# Return attempted_credit, earned_credit and class_grade.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

#This module and associated function are used to clear sceen from terminal when prompted.
from clear_screen_GPA import clear_screen

def update_GPA(user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict,cumulative_GPA_dict):
    """
    Input: User's Net-ID, G-Num, and all of the associated grades for each class user wishes to enter/update
    Output: Prints the GPA, number of attempted credits and earend credits, number of courses
    """
    print "2. GPA Update"
    print "-------------"
    print ""
    #Checks if user_id is already in user_Gnum, if yes continue - if not, then ask user go to generate GPA.
    user_id = raw_input("Enter your George Mason Net ID: ")  #Enter your Net-ID  (Run function each time for each student)
    user_id = user_id.lower()

    if user_id in user_Gnum:
        #Retrieve data of student's record (from dictionaries) to appropriate variables 
        cumulative_class_list = stud_records[user_id] #cumulative class list for each student
        attempted_credit = attempted_credits_dict[user_id]
        earned_credit = earned_credits_dict[user_id]
        cumulative_GPA = cumulative_GPA_dict[user_id]

        #Input number of classes user wants to enter
        number_classes = input("Enter the number of classes you want to add/update in order to calculate the cumulative GPA: ")

        class_table = []  #Generates class table to display classes already entered
        class_string = "" #Displays classes already entered into program; empty string
        number_entered = 0 #Displays number of classes entered, initialized to zero.
        for class_course in cumulative_class_list:
            class_table.append(class_course[0])
            class_string += str(class_course[0]) + ", "
            number_entered += 1
        class_string = class_string[:-2] #Removes last comma

        entered_string = ""  #Displays classes just ntered into program; empty string
        entered_number = 0   #Displays number of classes just entered; initialized to zero.
        
        for course in range(number_classes):
            clear_screen()
            print "2. GPA Update"
            print "-------------"
            print "Net ID: " + user_id
            print "G-Number: " + user_Gnum[user_id]
            print ""
            print "There is/are " + str(number_entered) + " course(s) already entered into the system: "
            print class_string
            print ""
            if entered_string:  #If entered_string True, shows classes just entered. Otherwise False 
                print "There is/are " + str(entered_number) + " course(s) you have just entered/updated into the system." + \
                " If you updated a course grade, the course number will appear in both lists:" 
                print entered_string
                print ""
            print "Note: If you are putting in a course that you have taken and you are taking it again, the previous grade is overwritten with the new one."
            print "This calculator does not consider courses that are taken as repeats - i.e. you want to gain more earned credits."
            print ""
            print "Course " + str(course+1) + " of " + str(number_classes)  #Shows 
            print ""
            print "For course # " + str(course+1) + ":"
            course_code = raw_input("Enter the course code (e.g. IT 106): ")
            course_code = course_code.upper()

            if course_code not in class_table:  #User enters additional class (same process at generate_GPA)
                class_info = []
                credit_num = input("Enter the number of credit hours associated with " + str(course_code) + " (e.g. 3): ")
                class_grade = raw_input("Enter your grade for " + str(course_code) + "\n"
                               + "(e.g. A+, A, A-, B+, B, B-, C+, C, C-, D, F, W, I): ")
                class_grade = class_grade.upper()
                attempt_num, earned_num, grade = grade_converter_original(credit_num, class_grade)

                #Shows user in subsuquent enterings of what classes user has entered. 
                if not entered_string:
                    entered_string += str(course_code) + ", "
                else:
                    entered_string += ", " + str(course_code) + ", "
                entered_string = entered_string[:-2]
                entered_number += 1
            
                attempted_credit += attempt_num
                earned_credit += earned_num
                class_grade = grade
                class_info = [course_code, credit_num, class_grade]  #comprehensive class info for each class
                cumulative_class_list.append(class_info)             #add class_info list to cumulative_class_list

            else:  #User enters class to update grade of that class 
            #Shows user in subsuquent enterings of what classes user has entered. 
                if not entered_string:
                    entered_string += str(course_code) + ", "
                else:
                    entered_string += ", " + str(course_code) + ", "
                entered_string = entered_string[:-2]
                entered_number += 1
                
                #Finds class in the cumulative_class_list to update. 
                for class_data in range(0, len(cumulative_class_list)):
                    if course_code == cumulative_class_list[class_data][0]:
                        course_update = cumulative_class_list[class_data]
                        credit_num = cumulative_class_list[class_data][1]
                        class_grade = raw_input("Enter your grade for " + str(course_code) + "\n"
                                    + "(e.g. A+, A, A-, B+, B, B-, C+, C, C-, D, F, W, I): ")
                        class_grade = class_grade.upper()

                        if course_update[2] in (0.0, 'W', 'I'):
                            #Process is the same as in generate_GPA 
                            attempt_num, earned_num, grade = grade_converter_original(credit_num, class_grade)
                            attempted_credit += attempt_num
                            earned_credit += earned_num
                            class_grade = grade
                            course_update = [course_code, credit_num, class_grade] #comprehensive class info for each class

                        elif course_update[2] in (4.0, 3.67, 3.33, 3.0, 2.67, 2.33, 2.0, 1.67, 1.0):
                            #This process only updates attempted grade and new grade 
                            attempt_num, grade = grade_converter_update(credit_num, class_grade)
                            attempted_credit += attempt_num
                            class_grade = grade
                            course_update = [course_code, credit_num, class_grade] #comprehensive class info for each clas
                        
                for remove_items in range(0, len(cumulative_class_list)):
                    if course_code == cumulative_class_list[remove_items][0]:
                        cumulative_class_list.remove(cumulative_class_list[remove_items])
                        break
                    
                cumulative_class_list.append(course_update)             #add class_info list to cumulative_class_list
        
        stud_records[user_id] = cumulative_class_list

        #THIS SECTION GENERATES THE GPA 
        #Note TQP stands for "Total Quality Points" - Same process in generate GPA. 
        grade_list = 0

        for item in range(0, len(cumulative_class_list)):
            try:
                TQP = int(cumulative_class_list[item][1]) * float(cumulative_class_list[item][2])
            except ValueError:
                print ""
            else:
                grade_list += TQP

        try:
            cumulative_GPA = (grade_list)/attempted_credit
        except ZeroDivisionError:
            cumulative_GPA = 0.0
            
        attempted_credits_dict[user_id] = attempted_credit
        earned_credits_dict[user_id] = earned_credit
        cumulative_GPA_dict[user_id] = cumulative_GPA

        clear_screen()
        print "2. GPA Update"
        print "-------------"
        print "Net ID: " + user_id
        print "G-Number: " + user_Gnum[user_id]
        print ""
        print "The cumulative GPA for " + "'" + user_id + "'" +  " is: " + str(round(cumulative_GPA, 3))
        print ""
        print "This is based on " + str(attempted_credit) + " attempted credits earned, " + str(earned_credit)+ " of which are earned credits."
        print "This is also based on " + str(len(cumulative_class_list)) + " course(s) entered: "
        print " - Class Already Entered (" + str(number_entered) + "): " + class_string
        print " - Class Just Entered/Updated (" + str(entered_number) + "): " + entered_string

        print ""
        raw_input("Press <ENTER> to continue and to return to main menu: ")

        #Returns user to main menu
        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict

    else: #If user Net ID does not exist in dictionary. 
        print ""
        print "This user does not exist! Try adding it."
        raw_input("Press <ENTER> to continue and to return to main menu: ")

        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict

def grade_converter_update(credit_num, class_grade):
    """
    Input: Credit number and class grade of class retaken
           This function is used only when there was a passing grade originally for a class
    Returns: Attempted Credit and Numeric Class Grade
    """
    attempted_credit = credit_num  #If student retakes class with original grade was passing, only attempted credit increases.

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

    elif class_grade == 'F':
        class_grade = 0.0

    elif class_grade in ('W', 'I'):
        class_grade = class_grade

    return attempted_credit, class_grade

def grade_converter_original(credit_num, class_grade):
    """
    Input: Credit number and class grade of class.
           This function is used only to input additional classes or if student original grade for a class was an F, W, or I (and is retaken).
    Returns: Attempted Credit and Numeric Class Grade
    """
    earned_credit = 0 #Initialized earned credit as zero. This mechanism is used if student somehow again fails to pass a class. 
    
    if class_grade == 'F':  
        attempted_credit = credit_num
        class_grade = 0.0
            
    elif class_grade == 'W':
        attempted_credit = credit_num

    elif class_grade == 'I':
        attempted_credit = 0
    
    #Mechanism is the same as in generate GPA 
    else:   
        attempted_credit = credit_num
        earned_credit = credit_num

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
            
    return attempted_credit, earned_credit, class_grade
