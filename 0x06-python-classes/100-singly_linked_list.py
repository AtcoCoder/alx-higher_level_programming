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

    def __str__(self):
        """String representation of the object"""
        return self.print_list()

    def sorted_insert(self, value):
        new_node = Node(value)
        current_node = self.__head
        previous_node = self.__head
        if current_node == None:
            self.__head = new_node
            new_node.next_node = None
            self.length += 1
        else:
            while current_node != None:
                if value < current_node.data:
                    new_node.next_node = current_node
                    previous_node.next_node = new_node
                    self.length += 1
                    break
                previous_node = current_node
                current_node = current_node.next_node

    def old_sorted_insert(self, value):
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
        current_node = self.__head
        count = 0
        lt = ""
        while (current_node != None):
            lt += str(current_node.data)
            current_node = current_node.next_node
            count += 1
            if self.length != count:
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
