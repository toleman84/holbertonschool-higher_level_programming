#!/usr/bin/python3
"""
Square

"""

from models.rectangle import Rectangle


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
    def size(self, value):
        """ set size """
        self.width = value
        self.heigth = value

    def __str__(self):
        """ str """
        return ('[Square] ({}) {}/{} - {}'.format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.width))

    def update(self, *args, **kwargs):
        """update dict"""
        if (len(args) == 0):
            for (key, value) in kwargs.items():
                if (key == 'id'):
                    self.id = value
                if (key == 'size'):
                    self.width = value
                    self.height = value
                if (key == 'x'):
                    self.x = value
                if (key == 'y'):
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

    def to_dictionary(self):
        """ dictionary """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
