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
        for key, value in kwargs.items():
            setattr(self, key, value)
