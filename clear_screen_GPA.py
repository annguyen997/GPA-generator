# Clear Screen Function

# Function to retrieve lines from the file "data.dat" and return in a list
# Input: None
# I/O: Clears screen on terminal 
# Returns: Clear screen

import os

def clear_screen():
	if os.name == "posix":
                clear_cmd = "clear"
    	elif os.name == "nt":
        	clear_cmd = "cls"
    	else:
        	print "\n" * 10
        os.system(clear_cmd)	
