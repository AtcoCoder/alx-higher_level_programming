#!/usr/bin/python3
"""Student class module
"""


class Student:
    """Defines a student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialises the attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation
            of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            attr_list = []
            for attribute in self.__dict__:
                if attribute in attrs:
                    attr_list.append((attribute, self.__dict__[attribute]))
            return dict(attr_list)

    def reload_from_json(self, json):
        """ Replaces attributes of the student
            instance with value from json
        """
        for attr in json:
            self.__dict__[attr] = json[attr]
        return self.__dict__
