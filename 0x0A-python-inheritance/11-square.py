#!/usr/bin/python3
"""inherits from BaseGeometry"""


class BaseGeometry:
    """public instance method"""

    def area(self):
        """calculate area"""
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
        """validate height"""
        integer_validator(height, __height)

    def integer_validator(self, width, __width):
        """validate width"""
        integer_validator(width, __width)

    def area(self):
        """implementing area"""
        self.__width * self.__height

    def __str__(self):
        """return a str representation of square"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """initializer"""
        super().__init__(size, size)
        self.__size = size

    def integer_validator(self, size, __size):
        """validator for size"""
        super().integer_validator(size, __size)

    def area(self):
        """area validation for square"""
        return self.__size * self.__size

    def __str__(self):
        """return a str representaion of square"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
