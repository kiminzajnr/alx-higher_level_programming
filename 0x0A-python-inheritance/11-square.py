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
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """implementing area"""
        return self.__width * self.__height

    def __str__(self):
        """return a str representation of square"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """initializer"""
        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """area validation for square"""
        return self.__size * self.__size

    def __str__(self):
        """return a str representaion of square"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
