#!/usr/bin/python3
"""Contains Class Node"""


class Node:
    """Class Node defines a node of a singly
    linked list"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves the value of instance attr data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of instance pri attr data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the instance attr next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of instance attr next_node"""
        if not isinstance(value, Node):
            if value is not None:
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList defines a singly
    linked list"""
    def __init__(self):
        """Initializes the instances attributes"""
        self.__head = None
        self.length = 0

    def sorted_insert(self, value):
        """Insert a new node in correct sort list (ascending order)"""
        new_node = Node(value)
        current_node = self.__head
        previous_node = None
        while current_node is not None and value > current_node.data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.__head = new_node
        else:
            previous_node.next_node = new_node
        new_node.next_node = current_node

    def __str__(self):
        """String representation of the linkedList"""
        current_node = self.__head
        lt = ""
        while current_node is not None:
            lt += str(current_node.data)
            current_node = current_node.next_node
            if current_node is not None:
                lt += '\n'
        return lt


if __name__ == "__main__":
    s1 = SinglyLinkedList()
    s1.sorted_insert(2)
    s1.sorted_insert(6)
    s1.sorted_insert(-1)
    s1.sorted_insert(4)
    s1.sorted_insert(1)
    s1.sorted_insert(0)
    print(s1)
