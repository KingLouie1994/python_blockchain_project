# Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random


def return_num_1():
    return random.uniform(0, 1)


def return_num_2():
    return random.randrange(1, 10)


print(return_num_1())
print(return_num_2())

# Use the datetime library together with the random number to generate a random, unique value.
import datetime


def return_unique_string():
    return str(datetime.datetime.now()) + str(return_num_1())


print(return_unique_string())
