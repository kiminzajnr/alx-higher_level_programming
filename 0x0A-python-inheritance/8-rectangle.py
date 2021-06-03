#!/usr/bin/python3
"""inherits from BaseGeometry"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        x = isinstance(value, int)
        if not x:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of privates"""
        self.__width = width
        self.__height = height

    def integer_validator(self, height, __height):
        validator = super().integer_validator(height, __height)

    def integer_validator(self, width, __width):
        super().integer_validator(width, __width)
