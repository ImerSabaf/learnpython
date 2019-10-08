"""
How to play with some variables
"""


def hello_world():
    """
    this function print the string hello world
    """
    print("hello world")


def print_message(msg):
    """
    print a variable and its type
    """
    print(msg)
    print(type(msg))


# Boolean
SMART = True
DUMB = False
print_message(DUMB)
print_message(SMART)

# Numerics type
NUM_VALUE_A = 3
NUM_VALUE_B = 3.1415

NUM_C = NUM_VALUE_A + NUM_VALUE_B
print_message(NUM_C)

# strings
A_STRING = "Use the force Luke !"
TEST_CONTAINS = A_STRING.__contains__("Luky")
print(A_STRING.split())
print(A_STRING.split("the"))

# containers
list_of_things = ["things_a", "things_b", "things_c"]
list_variables = [SMART, A_STRING, list_of_things]  # this is a list in a list !
concatenate_list = list_of_things + list_variables


print_message(TEST_CONTAINS)
