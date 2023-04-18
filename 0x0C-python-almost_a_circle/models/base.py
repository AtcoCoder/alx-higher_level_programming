#!/usr/bin/python3
"""Contains Base Class"""
import json
import csv


class Base:
    """Base class of my project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs"""
        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        class_name = cls.__name__
        path = f"{class_name}.json"
        with open(path, mode='w', encoding="utf-8") as f:
            string_to_write = cls.to_json_string(dict_list)
            f.write(string_to_write)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the
        JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all
        attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(50)
        else:
            dummy = cls(50, 50)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        string_from_file = ""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, encoding="utf-8") as f:
                string_from_file = f.read()
        except FileNotFoundError:
            pass
        list_dictionaries = cls.from_json_string(string_from_file)
        list_objects = []
        for dictionary in list_dictionaries:
            list_objects.append(cls.create(dictionary))
        return list_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves data to csv file"""
        list_dictionaries = []
        instance_attrs = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Square":
            instance_attrs = ['id', 'size', 'x', 'y']
        attrs = []
        filename = f"{cls.__name__}.csv"
        if list_objs is not None:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())
            for dictionary in list_dictionaries:
                list_attrs = []
                for attr in instance_attrs:
                    list_attrs.append(dictionary[attr])
                attrs.append(list_attrs)
        with open(filename, 'w') as csv_file:
            file_writer = csv.writer(csv_file)
            file_writer.writerows(attrs)

    @classmethod
    def load_from_file_csv(cls):
        """Loads data from csv file"""
        list_of_dict_attrs = []
        filename = f"{cls.__name__}.csv"
        instances_attrs = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == 'Square':
            instances_attrs = ['id', 'size', 'x', 'y']
        list_of_list_attrs = []
        try:
            with open(filename, 'r') as csv_file:
                file_reader = csv.reader(csv_file)
                list_of_list_attrs = list(file_reader)
        except FileNotFoundError:
            pass
        for list_attrs in list_of_list_attrs:
            dict_attrs = {}
            for idx in range(len(list_attrs)):
                dict_attrs[instances_attrs[idx]] = int(list_attrs[idx])
            list_of_dict_attrs.append(dict_attrs)
        list_objs = []

        for dictionary in list_of_dict_attrs:
            list_objs.append(cls(**dictionary))
        return list_objs
