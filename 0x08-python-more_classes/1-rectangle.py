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
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set width"""
        self.__height = value
        try:
            assert isinstance(self.__height, int)
        except:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set height"""
        self.__width = value
        try:
            assert isinstance(self.__width, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
