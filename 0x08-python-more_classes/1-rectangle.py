#!/usr/bin/python3
"""
Defines a rectancle
"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation of width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set height"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
