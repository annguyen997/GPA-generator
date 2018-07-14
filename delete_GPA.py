#-------------------------------------------------------------------------------
# File Name: delete_GPA.py
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
# from clear_screen_GPA import clear_screen
#def delete_GPA(user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict):
    #print GPA deletion
    #prompt user to enter their net id & make it lower case
    #if user id is in user_Gnum:
        #cumulative_class_list = stud_records[user_id] #cumulative class list for each student
        #attempted_credit = attempted_credits_dict[user_id]
        #earned_credit = earned_credits_dict[user_id]
        #cumulative_GPA = cumulative_GPA_dict[user_id]

        #clear screen
        #print 4. GPA deletion
        #print "G-Number: " + user_Gnum[user_id]
        #print deletion message
        #prompt user to type yes to delete their record & no to keep their record
        #if user types in yes:
            #prompt use to enter their net id
            #if net id matches then
            #delete  user_Gnum[user_id] , stud_records[user_id] ,del attempted_credits_dict[user_id],del earned_credits_dict[user_id],del cumulative_GPA_dict[user_id]

        #clear screen
        #print GPA deletion
        #prompt user to press enter to continue
        #return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
    #else:
        #clear screen
        #return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
#else:
    #prompt user to press enter to contiue
    #return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

#This module and associated function are used to clear sceen from terminal when prompted.
from clear_screen_GPA import clear_screen

def delete_GPA(user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict):
    """
    Input: The Net ID, G-Number, Attempted and Earned Credits, Cumulative GPA (when user enters a vlaid Net ID; this funciton runs).
    Returns/Output: Deletes the student record (all information stated in input) from the system when successfully deleted upon request.
    """
    print "4. GPA Deletion"
    print "---------------"
    user_id = raw_input("Enter your George Mason Net ID: ")  #Enter your Net-ID  (Run function each time for each student)
    user_id = user_id.lower()

    if user_id in user_Gnum:
        cumulative_class_list = stud_records[user_id] #cumulative class list for each student
        attempted_credit = attempted_credits_dict[user_id]
        earned_credit = earned_credits_dict[user_id]
        cumulative_GPA = cumulative_GPA_dict[user_id]

        clear_screen()
        print "4. GPA Deletion"
        print "---------------"
        print "Net ID: " + user_id
        Ginfo = "G-Number: " + user_Gnum[user_id]
        print Ginfo
        print ""
            
        deletion_message = """
*** IMPORTANT NOTICE ***
You can use this deletion option if you need to reformat the classes and related information, there are lots of errors in the record, or
you would like to delete the information for other reason(s). Please note deleting a entire student record is not recoverable!

After you delete the record, if you need to re-enter the student record again to generate the GPA calculation, please return to main menu.
You can then re-create student record and re-enter the applicable information with GPA Generator.
        """
        print deletion_message
        print ""
        option = raw_input("Do you wish to delete your record? (Type 'Yes' or 'No'): ")
        option = option.upper() 
        if option in ('YES', 'Y'):
            user_id_del = raw_input("Enter your George Mason Net ID to delete your record: ")  #Enter your Net-ID
            user_id_del = user_id_del.lower()

            if user_id_del == user_id: #affrim it 
                print "" 
                del_request = raw_input("Are you sure you want to do this? If so, type Yes or Y: ")
                del_request = del_request.upper()
                if del_request in ('YES', 'Y'):
                    user_id_del = raw_input("Enter your George Mason Net ID to affirm that you want to PERMANENTLY your record: ")
                    user_id_del = user_id_del.lower()
                    if user_id_del == user_id:
                        del user_Gnum[user_id]
                        del stud_records[user_id]
                        del attempted_credits_dict[user_id]
                        del earned_credits_dict[user_id]
                        del cumulative_GPA_dict[user_id]
                        print ""
                        clear_screen()
                        print "4. GPA Deletion"
                        print "---------------"
                        print "Net ID: " + user_id
                        print Ginfo
                        print ""
                        print "This record, " + str(user_id) + ", has successfully been deleted. You will now be returned to main menu."
                        raw_input("Press <ENTER> to continue: ")
                        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
                else:
                    clear_screen() 
                    print "4. GPA Deletion"
                    print "---------------"
                    print "Net ID: " + user_id
                    print Ginfo
                    print ""
                    print "Now returning to main menu..."
                    raw_input("Press <ENTER> to continue.")
                    return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
        else:
            clear_screen()
            print "4. GPA Deletion"
            print "---------------"
            print "Net ID: " + user_id
            print Ginfo
            print ""
            print "Now returning to main menu..."
            raw_input("Press <ENTER> to continue.")
            return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
                
    else:
        print ""
        print "This user does not exist! Try adding it first."
        raw_input("Press <ENTER> to continue and to return to main menu: ")

        return user_Gnum, stud_records, attempted_credits_dict, earned_credits_dict, cumulative_GPA_dict
