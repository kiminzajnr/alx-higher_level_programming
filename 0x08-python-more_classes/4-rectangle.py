#!/usr/bin/python3
"""
defines a rectangle
"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """instantiation"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
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
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter"""
        perimeter = 0
        if self.__height is not 0 or self.__width is not 0:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter

    def __str__(self):
        """print rectangle using #"""
        str_ = ""
        if self.__width == 0 or self. __height == 0:
            return ""
        for i in range(self.__height):
            if i < (self.__height - 1):
                str_ += ("#" * self.__width) + "\n"
            else:
                str_ += ("#" * self.__width)
        return str_

    def __repr__(self):
        """repr method to enable create new instance using #"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
