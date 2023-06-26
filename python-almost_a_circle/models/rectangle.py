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
            self.__y = y
