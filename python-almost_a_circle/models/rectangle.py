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
        def width(self, value):
            """_summary_

            Args:
                value (_type_): _description_
            """
            self.__width = value

        @property
        def heigth(self):
            """_summary_
            """
            return self.__heigth

        @heigth.setter
        def heigth(self, value):
            """_summary_

            Args:
                value (_type_): _description_
            """
            self.__heigth = value

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
            self.__x = value

        @property
        def y(self):
            """_summary_
            """
            return self.__y

        @heigth.setter
        def y(self, value):
            """_summary_

            Args:
                value (_type_): _description_
            """
            self.__y = value
