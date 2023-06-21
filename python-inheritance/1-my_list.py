#!/usr/bin/python3
"""_summary_
"""


class MyList(list):
    """_summary_
    that prints the list, but sorted (ascending sort)
    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """_summary_
        """
        print(sorted(self))
