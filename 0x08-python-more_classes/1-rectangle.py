#!/usr/bin/python3
"""
Defines a rectancle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Instantiation of width and height"""
        self.__width = 0
        self.__height = 0

    def width(self):
        """retrieve width"""
        return self.__width

    def height(self):
        """retrieve height"""
        return self.__height

    def width(self, value):
        """Set width"""
        self.__width = value
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    def height(self, value):
        """set height"""
        self.__height = value
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if self.__height != int:
            raise ValueError("height must be >= 0")
