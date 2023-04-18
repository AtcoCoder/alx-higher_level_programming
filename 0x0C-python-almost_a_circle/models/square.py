#!/usr/bin/python3
"""Contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Subclass of the Rectangle class subclass
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of the instance attributes"""
        Rectangle.__init__(self, size, size, x=x, y=y, id=id)

    def __str__(self):
        """String representation of instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the value of attrs"""
        list_attrs = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for idx in range(len(args)):
                setattr(self, list_attrs[idx], args[idx])
        else:
            for attr_name in kwargs:
                setattr(self, attr_name, kwargs[attr_name])

    def to_dictionary(self):
        """Returns the dictionary
        representation of a square"""
        attr_list = ['id', 'size', 'x', 'y']
        attr_dict = {}
        for attr in attr_list:
            attr_dict[attr] = getattr(self, attr)
        return attr_dict
