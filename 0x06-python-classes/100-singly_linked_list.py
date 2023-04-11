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
        if not isinstance(value , int):
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
            if not isinstance(value, None):
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList defines a singly
    linked list"""
    def __init__(self):
        self.linked_list = []

    def __str__(self):
        return self.print_list()

    def sorted_insert(self, value):
        """inserts a new Node
        into the correct sorted position
        in the list (increasing order)"""
        new_node = Node(value)
        if len(self.linked_list) == 0:
            self.linked_list.append(new_node)
        else:
            for index, node in enumerate(self.linked_list):
                if value < node.data:
                    self.linked_list.insert(index, new_node)
                    break
                elif index == len(self.linked_list) - 1:
                    self.linked_list.append(new_node)
                    break

    def print_list(self):
        """Prints the data at each node"""
        lt = ""
        for node in self.linked_list[:-1]:
            lt += str(node.data)
            lt += '\n'
        lt += str(self.linked_list[-1].data)
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
