#!/usr/bin/python3
"""public instance method"""


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
