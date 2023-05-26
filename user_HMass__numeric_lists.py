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
    10,
    22,
    37,
    21,
    8,
    22,
    40,
    7,
    5,
    50,
    24,
    30,
    22,
    13,
    26,
    18,
    22,
    32,
    45,
    33,
    23,
    ]

def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"age_list: {age_list}")

    # Descriptive: Averages and measures of central tendency
    # Use statisttics module to get mean, median, mode
    # for a values list

    mean = statistics.mean(age_list)
    median = statistics.median(age_list)
    mode = statistics.mode(age_list)

    logger.info(f"mean: {mean:0.2f}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(age_list)
    variance = statistics.variance(age_list)

    logger.info(f"stdev: {stdev:0.2f}")
    logger.info(f"variance: {variance:0.2f}")

def illustrate_list_built_in_functions():
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calcuate the max and min scores
    max_value = max(age_list)
    min_value = min(age_list)

    logger.info(f"Given score list: {age_list}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(age_list)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(age_list)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {age_list}")
    # Return a new list soreted in ascending order
    asc_age = sorted(age_list)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_age}")

    # Return a new list soreted in descending order
    desc_age = sorted(age_list, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_age}")
       

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    illustrate_list_statistics()
    
    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")

    show_log()