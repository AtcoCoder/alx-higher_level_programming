#!/usr/bin/python3
"""Contains Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """
    Subclass of Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """Prints in stdout the Rectangle instance
        with the character #"""
        rectangle = ""
        rectangle += self.__y * '\n'
        for step in range(self.__height):
            rectangle += self.__x * ' '
            for move in range(self.__width):
                rectangle += '#'
            rectangle += '\n'
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Updates the instances attributes"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for index in range(len(args)):
                setattr(self, attrs[index], args[index])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def __str__(self):
        """String representation of Rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"\
            f" - {self.__width}/{self.__height}"

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        self.validate_int('width', value)
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height"""
        self.validate_int('height', value)
        self.__height = value

    @property
    def x(self):
        """Retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        self.validate_int('x', value)
        self.__x = value

    @property
    def y(self):
        """Retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        self.validate_int('y', value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def validate_int(self, name, value):
        """Validates value is an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def to_dictionary(self):
        """Returns the dictionary reprsentation
        of an instance"""
        attr_list = ['id', 'width', 'height', 'x', 'y']
        attr_dict = {}
        for attr in attr_list:
            attr_dict[attr] = getattr(self, attr)
        return attr_dict
