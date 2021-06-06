#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square extends from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x=0, y=0, id=None)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """str representation of square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.__x, self.__y, self.__size)
