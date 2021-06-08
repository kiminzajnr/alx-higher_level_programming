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

    def display(self):
        """print square instance using # character"""
        for line in range(self.__y):
            print()
        for i in range(self.__size):
            for space in range(self.__x):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """set width and height"""
        super().width
        self.__size = value
        self.__size = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        for key, value in kwargs.item():
            setattr(self, key, value)
