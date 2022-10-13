#!/usr/bin/python3
""" creating a square class from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defing a square as a subclass of rectangle based on 9-rectangle.py"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
