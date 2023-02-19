#!/usr/bin/python3
"""
Square

"""

import models.rectangle from Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, size):
        """ set size """
        self.width = size
        self.heigth = size

    def __str__(self):
        """ str """
        return ('[Square] ({}) {}/{} - {}'.format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.size))

    def update(self, *args, **kwargs):
        """update dict"""
        if (len(args) is 0):
#            if (len(kwargs) is 0):
#                raise TypeError("missing 2 required positional arguments:'width' and 'height")
            for (key, value) in kwargs.items():
                if (key is 'id'):
                    self.id = value
                if (key is 'size'):
                    self.width = value
                    self.height = value
                if (key is 'x'):
                    self.x = value
                if (key is 'y'):
                    self.y = value
        else:
            length = len(args)
            i = 0
            if (length > i):
                self.id = args[0]
                i += 1
            if (length > i):
                self.width = args[1]
                self.height = args[1]
                i += 1
            if (length > i):
                self.x = args[2]
                i += 1
            if (length > i):
                self.y = args[3]
