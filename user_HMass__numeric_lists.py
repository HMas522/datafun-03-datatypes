"""
Hayley M 
26May23 
Project 3 - Numeric Lists
Domain: Video Games

"""

# import some standard modules first - how many can you make use of?
import math

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# TODO: import from local util_datafun_logger.py DONE

# TODO: Call the setup_logger function to create a logger and get the log file name DONE

# TODO: Create some shared data lists if you like - or just create them in your functions

# TODO: define some custom functions


def myfunction():
    print("Hello, Dr. Case! My define function will start off basic, and hopefully get more advanced.")






# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Replace this with calls to your functions." )



# Read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())