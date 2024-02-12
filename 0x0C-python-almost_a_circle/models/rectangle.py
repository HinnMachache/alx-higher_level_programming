#!/usr/bin/python3
# rectangle.py

"""Defines class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base and has:
        Private instance attributes,
        each with its own public getter and setter:
            __width -> width
            __height -> height
            __x -> x
            __y -> y
        Class constructor: def __init__(self, width, height, x=0, y=0, id=None)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instatiates class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
     
     def area(self):
         """Returns area of the rectangle"""
         return (self.__width * self.__height)

     def display(self):
         """Prints the rectanglr instance with symbol '#'"""
        if self.__width == 0 || self.__height == 0:
            print("")
        for i in range(0, self.__width):
            for j in range(0, self.__height):
                print("#")
            print("")

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        info = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
        return (info)

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute:"""
        if args and len(args) != 0:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if num_args >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns Dictionary Representation of Rectangle Class"""
        list_attr = ['id', 'width', 'height', 'x', 'y']
        rect_dict = {}
        for key in list_attr:
            rect_dict[key] = getattr(self, key)

        return (rect_dict)
