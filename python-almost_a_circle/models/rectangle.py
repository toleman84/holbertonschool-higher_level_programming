#!/usr/bin/python3
"""_summary_
"""
from models.base import Base


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, heigth, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            heigth (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        self.width = width
        self.heigth = heigth
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """_summary_
        """
        return self.__width

    @width.setter
    def width(self, width):
        """_summary_

        Args:
            width (_type_): _description_
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def heigth(self):
        """_summary_
        """
        return self.__heigth

    @heigth.setter
    def heigth(self, heigth):
        """_summary_

        Args:
            heigth (_type_): _description_
        """
        if not isinstance(heigth, int):
            raise TypeError("heigth must be an integer")
        elif heigth <= 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = heigth

    @property
    def x(self):
        """_summary_
        """
        return self.__x

    @x.setter
    def x(self, x):
        """_summary_

        Args:
            x (_type_): _description_
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """_summary_
        """
        return self.__y

    @y.setter
    def y(self, y):
        """_summary_

        Args:
            y (_type_): _description_
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """_summary_
        """
        return self.__width * self.__heigth