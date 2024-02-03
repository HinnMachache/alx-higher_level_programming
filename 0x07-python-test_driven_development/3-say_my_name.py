#!/usr/bin/python3
#3-say_my_name.py
"""say_my_name: Prints user name
first_name = user first name, last_name - user last name
empty by default
"""


def say_my_name(first_name, last_name=""):
    """Function that prints user name"""
    if first_name == "":
        raise ValueError("Enter First Name")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
