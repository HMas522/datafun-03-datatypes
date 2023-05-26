"""
Hayley M 
26May23 
Project 3 - Numeric Lists
Domain: Video Games

"""

# import some standard modules first - how many can you make use of?
import math

import statistics

import webbrowser

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# TODO: import from local util_datafun_logger.py DONE

# TODO: Call the setup_logger function to create a logger and get the log file name DONE

# TODO: Create some shared data lists if you like - or just create them in your functions

# TODO: define some custom functions

"""I will be making junk data from a real study from Nintendo"""

# citing the source where I'm getting my data from

str_response = input("Do you want to learn more about Age Distribution of Annual Nintendo Players? (y/n) ")

if str_response == "y":
    # import webbrowser at the top of the file
    webbrowser.open("https://www.nintendolife.com/news/2022/11/switch-is-most-popular-with-22-year-olds-nintendo-says")

# making a fake list of ages

age_list = [
    10
    22
    37
    21
    8
    22
    40
    7
    5
    50
    24
    30
    22
    13
    26
    18
    22
    32
    45
    33
    23
]


# Read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())