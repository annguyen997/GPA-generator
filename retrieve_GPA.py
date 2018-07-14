#-------------------------------------------------------------------------------
# File Name: retrieve_GPA.py
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
#Sonia Safdar
#import clear_Screen
#def retrieve_gpa function & pass the parameters:(user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict):
#print GPA retrieve
#prompt user to enter NetID & make it lower case
#if user id is in user_GNUM:
    #user_GnumL = user_Gnum[user_id]
    #cumulative_class_list = stud_records[user_id] #cumulative class list for each student
    #attempted_credit = attempted_credits_dict[user_id]
    #earned_credit = earned_credits_dict[user_id]
    #cumulative_GPA = cumulative_GPA_dict[user_id]
    #clear screen
    #call GPA_report:GPA_report_run(user_id, user_GnumL, attempted_credit, earned_credit, cumulative_GPA, cumulative_class_list)
    #prompt user type yes or no to export the file:
        #if user enter yes then call GPA_report
    #return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
    #else:
        #print user does not exist. try adding it
        #return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict

#def GPA_report_run(user_id, user_GnumL, attempted_credit, earned_credit, cumulative_GPA, cumulative_class_list):
    #formation the report, print GMU gading scale, format header
#def GPA_report_generator(user_id, user_GnumL, attempted_credit, earned_credit, cumulative_GPA, cumulative_class_list):
    #file_name = str(user_id) + "GPAreport.txt"
    #open file in write mode
    #assign the gpa report to a var information
    #format header
    #write the files
    #use for loop to iterate through the cumulative_class_last to add spaces
    #format line
    #write the file
    #close the file
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

#This module and associated function are used to clear sceen from terminal when prompted.
from clear_screen_GPA import clear_screen

def retrieve_GPA(user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict):
    """
    Input: User's Net-ID
    Output: Retrieves the student records as a report (including attempted and earned credits, cumulative GPA)
            If user wishes to do so, the record can be exported as a text file.         
    """
    print "3. GPA Retrieve"
    print "---------------"
    user_id = raw_input("Enter your George Mason Net ID: ")  #Enter your Net-ID  (Run function each time for each student)
    user_id = user_id.lower()

    if user_id in user_Gnum:    #if user id is in the user Gnum then reteive the student information 
        user_GnumL = user_Gnum[user_id]
        cumulative_class_list = stud_records[user_id] #cumulative class list for each student
        attempted_credit = attempted_credits_dict[user_id]
        earned_credit = earned_credits_dict[user_id]
        cumulative_GPA = cumulative_GPA_dict[user_id]

        clear_screen()
        print "3. GPA Retrieve"
        print "---------------"
        print ""
        GPA_report_run(user_id, user_GnumL, attempted_credit, earned_credit, cumulative_GPA, cumulative_class_list)
        
        print ""

        #If student wants to save the file
        request = raw_input("Do you wish to export this report? (Type either 'Yes' or 'No'): ")
        request = request.upper()
        if request in ('YES', 'Y'):
            GPA_report_generate(user_id, user_GnumL, attempted_credit, earned_credit, cumulative_GPA, cumulative_class_list)
            print "This report has been exported as a Text file (.txt) containing your Net ID. Please remember that the report is not a transcript."
            
        print ""    
        raw_input("Press <ENTER> to continue and to return to main menu: ")

        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict

    else:
        print ""
        print "This user does not exist! Try adding it."
        raw_input("Press <ENTER> to continue and to return to main menu: ")
        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict

        

def GPA_report_run(user_id, user_GnumL, attempted_credit, earned_credit, cumulative_GPA, cumulative_class_list):
    """
    Input: The Net ID, G-Number, Attempted and Earned Credits, Cumulative GPA (when user enters a vlaid Net ID; this funciton runs).
    Returns/Output: A report of given information in input with a list of classes taken under the record
    """
    #this section formats the report 
    information = ' === GPA Report === \n' + \
                  'Net ID: ' + str(user_id) + '\n' + \
                  'G-Number: ' + str(user_GnumL) + '\n' + \
                  'Attempted Credits: ' + str(attempted_credit) + '\n' + \
                  'Earned Credits: ' + str(earned_credit) + '\n' + \
                  "Cumulative GPA: " + str(round(cumulative_GPA, 3)) + '\n' + \
                  "Number of Classes Entered: " + str(len(cumulative_class_list)) + '\n' + \
                  '' + '\n' + \
                  'GPA Undergraduate Grading Scale - George Mason University' + '\n' + \
                  '---------------------------------------------------------' + '\n'  + \
                  'A/A+: 4.0   A-: 3.67  B+: 3.33  B: 3.0  B-: 2.67' + '\n' + \
                  'C+: 2.33    C: 2.00   C-: 1.67  D: 1.0  F: 0.00' + '\n' + \
                  'W, I: No GPA equivalent' + '\n' + \
                  '' + '\n' + \
                  'These are all the undergraduate classes you have completed along with the grade of your most recent attempt of each class.' + '\n' + \
                  'Please note that this report does NOT replace a transcript. This is used for personal purposes only.' + '\n' + \
                  '' + '\n'
    print information 
    header = '{0:15s} {1:15s} {2:15s}'.format('Class', 'Credits', 'Grade (GPA)')
    header_lines = '{0:15s} {1:15s} {2:15s}'.format('-----', '-------', '-----------')
    print header
    print header_lines
    
    #formating
    for class_item in cumulative_class_list:
        class_list_item = ""
        for course_item in class_item:
            class_list_item += str(course_item) + ","
        
        line = '{0:15s} {1:15s} {2:15s}'.format(class_list_item.split(",")[0], class_list_item.split(",")[1], class_list_item.split(",")[2])
        print line

def GPA_report_generate(user_id, user_GnumL, attempted_credit, earned_credit, cumulative_GPA, cumulative_class_list):
    """
    Input: The Net ID, G-Number, Attempted and Earned Credits, Cumulative GPA (when user enters a vlaid Net ID; this funciton runs).
    Returns/Output: A report of given information in input with a list of classes taken under the record (as an export file). 
    """
    file_name = str(user_id) + "GPAreport.txt"
    fp = open(file_name, 'w')
    information = ' === GPA Report === \n' + \
                  'Net ID: ' + str(user_id) + '\n' + \
                  'G-Number: ' + str(user_GnumL) + '\n' + \
                  'Attempted Credits: ' + str(attempted_credit) + '\n' + \
                  'Earned Credits: ' + str(earned_credit) + '\n' + \
                  "Cumulative GPA: " + str(round(cumulative_GPA, 3)) + '\n' + \
                  "Number of Classes Entered: " + str(len(cumulative_class_list)) + '\n' + \
                  '' + '\n' + \
                  'GPA Undergraduate Grading Scale - George Mason University' + '\n' + \
                  '---------------------------------------------------------' + '\n'  + \
                  'A/A+: 4.0   A-: 3.67  B+: 3.33  B: 3.0  B-: 2.67' + '\n' + \
                  'C+: 2.33    C: 2.00   C-: 1.67  D: 1.0  F: 0.00' + '\n' + \
                  'W, I: No GPA equivalent' + '\n' + \
                  '' + '\n' + \
                  'These are all the undergraduate classes you have completed along with the grade of your most recent attempt of each class.' + '\n' + \
                  'Please note that this report does NOT replace a transcript. This is used for personal purposes only.' + '\n' + \
                  '' + '\n'
    header = '{0:15s} {1:15s} {2:15s}'.format('Class', 'Credits', 'Grade (GPA)')
    header_lines = '{0:15s} {1:15s} {2:15s}'.format('-----', '-------', '-----------')

    #write it to the file 
    fp.write(information)
    fp.write(header + '\n')
    fp.write(header_lines + '\n')

    #formating
    for class_item in cumulative_class_list:
        class_list_item = ""
        for course_item in class_item:
            class_list_item += str(course_item) + ","
        
        line = '{0:15s} {1:15s} {2:15s}'.format(class_list_item.split(",")[0], class_list_item.split(",")[1], class_list_item.split(",")[2])
        fp.write(line + '\n')
        
    fp.close()
