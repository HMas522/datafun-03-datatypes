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

    logger.info(f"Given age list: {age_list}")
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
    logger.info(f"The average is {avg_list:0.2f}")

    logger.info(f"Given age list: {age_list}")
    # Return a new list soreted in ascending order
    asc_age = sorted(age_list)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_age}")

    # Return a new list soreted in descending order
    desc_age = sorted(age_list, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_age}")

def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    # append an item to the end of the list
    lst = [11, 22, 33]
    lst.append(44)

    # extend the list with another list
    lst.extend([44, 55, 66])

    # insert an item at a given position (0 = first item)
    i = 0
    newvalue = 99
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 99
    lst.remove(item_to_remove)

    # Count how many times 22 appears in the list
    ct_of_twenty = age_list.count(22) 

    # Sort the list in ascending order using the sort() method
    asc_age2 = age_list.sort() 

    # Sort the list in descending order using the sort() method
    desc_age2 = age_list.sort(reverse=True) 

    # Copy the list to a new list
    new_age = age_list.copy()
    logger.info(f"new_age is: {new_age}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_age.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_scores is: {new_age}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_age.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_age is: {new_age}"
    )

    # Remove the item at index 3 from the new list
    fourth = new_age.pop(3)
    logger.info(
        f"Popped the fourth (index=3): {fourth} and now, new_age is: {new_age}"
    )

def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("Age list: {age_list}")

    # TRANFORMATIONS ............................

    # FILTER and MAP are critical tranformations in big data applications

    # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include scores greater than 100
    # You could pass in a named function, but honestly this is easier
    # Say "KEEP x such that x > 100 is True" given score_list
    # Cast the result using square brackets to get back a list
    ages_over_18 = [filter(lambda x: x > 18, age_list)]
    logger.info(f"Ages over 18: {ages_over_18}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its square
    # Say "map x to x squared" given score_list
    # Cast the result using square brackets to get a list
    doubled_age = [map(lambda x: x * 2, age_list)]
    logger.info(f"Doubled scores: {doubled_age}")

    # Map each element to its square root
    # Say "map x to the square root of x" given score_list
    # remember to cast the result to a list (using square brackets)
    sqrt_age = map(lambda x: math.sqrt(x), age_list)
    logger.info(f"Square root of scores: {sqrt_age}")

    # Map each element (radius) to its area
    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Radius list: {radius_list}")
    # Say "map r to pi r squared" given radius_list
    # cast the result to a list using square brackets
    area_list = [map(lambda r: math.pi * r * r, radius_list)]
    logger.info(f"Area of circles: {area_list}")

def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info("Age list: {age_list}")

    # TRANFORMATIONS - Using List Comprehensions
    # List comprehensions are a concise way to create lists
    # They work like map and filter, but are more concise
    # They are the preferred "pythonic" way to do transformations
    # They are faster than map / filter - it's quite impressive when you master them!

    # With comprehensions, we start with what we WANT
    # Filter the new list to only include scores greater than 100
    # Say "KEEP x (for each x in score_list) IF  x > 100"
    # Cast the result to a list using square brackets

    ages_over_18_=[x for x in age_list if x > 18]
    logger.info("Ages over 18 (using list comprehensions!): {ages_over_18}")

    # Try again "keep x (for each x in score_list) IF  x < 60"

    ages_under_60 = [x for x in age_list if x < 60] # pyright: ignore
    logger.info("Ages under 60 (using list comprehensions!): {ages_under_60}")

    # Map each element to its square
    # Say "give me x squared (for each x in score_list)"
    # Cast the result to a list using square brackets

    doubled_age = [x * 2 for x in age_list] # pyright: ignore
    logger.info("Doubled scores (using list comprehensions!): {doubled_age}")

    # Map each element to its square root
    # Say "give me the square root of x (for each x in score_list)"
    # Cast the result to a list using square brackets
    sqrt_age = [math.sqrt(x) for x in age_list] # pyright: ignore

    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Given radius_list: {radius_list}")

    # Map each element (radius) to its area
    # Say "give me pi r squared (for each r in radius_list)"
    # Cast the result to a list using square brackets
    area_list = [math.pi * r * r for r in radius_list]
    logger.info(f"Area of circles: {area_list}")

    # Map each element (radius) to its circumference
    # Say "give me 2 pi r (for each r in radius_list)"
    # Cast the result to a list using square brackets
    circumference_list = [2 * math.pi * r for r in radius_list]
    logger.info(f"Circumference of circles: {circumference_list}")

    logger.info("Mastering comprehesions is a valuable skill for data scientists.")
    numbers = [1, 2, 3, 4]
    squares = [x**2 for x in numbers]
    logger.info(f"Given numbers: {numbers}")
    logger.info(f"Squares of numbers using [x ** 2 for x in numbers] is {squares}")     

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
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()
    
    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")

    show_log()