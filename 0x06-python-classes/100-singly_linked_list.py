#!/usr/bin/python3

"""Define a class for a singly-linked list"""

class Node

    def __init__(self, data, next_node=None):
        """Init a new node
        Args:
            data (int): the data of new node
            next_node (Node): he next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("Data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node"""
        return (self.__next_node)

   @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


