#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square extends from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor for square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str representation of square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set width and height with the same value, value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if (args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of square"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
