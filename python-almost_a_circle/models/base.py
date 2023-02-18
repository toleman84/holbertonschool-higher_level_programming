#!/usr/bin/python3
"""
Python - Almost a circle

"""

import json
import csv


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
