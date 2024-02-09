#!/usr/bin/python3
# 1-my_list.py
"""print_sorted: Print Lists in sorted order(ascending)

Arguments:
    No Arguments
"""


class MyList(list):
    """Subset Class : MyList, Parent Class: List"""
    def print_sorted(self):
        """Function that prints Lists in sorted order"""
        print(sorted(self))
