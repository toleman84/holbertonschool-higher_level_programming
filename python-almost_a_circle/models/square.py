<<<<<<< HEAD
#!/usr/bin/python3
"""_summary_
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.width

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.width = value
        self.height = value

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        clsName = self.__class__.__name__
        id = self.id
        x = self.x
        y = self.y
        size = self.size

        return ("[{}] ({}) {}/{} - {}".format(clsName, id, x, y, size))

    def update(self, *args, **kwargs):
        """_summary_
        """
        attr = ['id', 'size', 'size', 'x', 'y']
        if args:
            [setattr(self, attr[i], arg) for i, arg in enumerate(args)]
        elif kwargs:
            [setattr(self, k, v) for k, v in kwargs.items()]

    def to_dictionary(self):
        """_summary_
        """
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.size
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
=======
#!/usr/bin/python3
"""_summary_
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.width

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.width = value
        self.heigth = value

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        clsName = self.__class__.__name__
        id = self.id
        x = self.x
        y = self.y
        size = self.size

        return ("[{}] ({}) {}/{} - {}".format(clsName, id, x, y, size))

    def update(self, *args, **kwargs):
        """_summary_
        """
        attr = ['id', 'size', 'size', 'x', 'y']
        if args:
            [setattr(self, attr[i], arg) for i, arg in enumerate(args)]
        elif kwargs:
            [setattr(self, k, v) for k, v in kwargs.items()]

    def to_dictionary(self):
        """_summary_
        """
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['size'] = self.size
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary
>>>>>>> 5840ea05fc9af925d1a7bece53bbf84bb1d32292
