#!/usr/bin/python3
"""_summary_
"""
from models.base import Base


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_
        Args:
            width (_type_): _description_
            heigth (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """_summary_
        """
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """_summary_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """_summary_
        """
        return self.__x

    @x.setter
    def x(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """_summary_
        """
        return self.__y

    @y.setter
    def y(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """_summary_
        """
        return self.__width * self.__height

    def display(self):
        """_summary_
        """
        [print() for y in range(self.__y)]
        [print(' '*self.x + '#'*self.__width) for i in range(self.__height)]

    def __str__(self):
        """_summary_

        Returns:
            _type_: _[Rectangle] (<id>) <x>/<y> - <width>/<height>_
        """
        id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h))

    def update(self, *args, **kwargs):
        """_summary_
        """
        """attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            [setattr(self, attr[i], arg) for i, arg in enumerate(args)]
        elif kwargs:
            [setattr(self, k, v) for k, v in kwargs.items()]"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """_summary_
        """
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
