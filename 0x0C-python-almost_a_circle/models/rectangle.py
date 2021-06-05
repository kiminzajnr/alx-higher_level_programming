#!/usr/bin/python3
"""class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        try:
            assert isinstance(self.__width, int)
        except:
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

        try:
            assert isinstance(self.__height, int)
        except:
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

        try:
            assert isinstance(self.id, int)
        except:
            raise TypeError("id must be an integer")
        if self.id < 0:
            raise ValueError("id must be >= 0")

        try:
            assert isinstance(self.__x, int)
        except:
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

        try:
            assert isinstance(self.__y, int)
        except BaseException:
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.__width = value
        try:
            assert isinstance(self.__width, int)
        except:
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.__height = value
        try:
            assert isinstance(value, int)
        except:
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value
        try:
            assert isinstance(self.__x, int)
        except:
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
        try:
            assert isinstance(self.__y, int)
        except BaseException:
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """returns the area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle instance using # character"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
