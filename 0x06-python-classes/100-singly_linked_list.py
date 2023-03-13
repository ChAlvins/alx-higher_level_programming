#!/usr/bin/python3
"""defining class node"""


class Node:
    """Node class of a singly linked list"""
    def __init__(self, data, next_node=None):
        """inititializing the node class"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter for Private instance attribute: data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for private attribute:data"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for Private instance attribute: next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for Private instance attribute: next_node"""
        if value is not None and type(value) is not Node:
            raise TypeEror("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class singly linked list"""

    def __init__(self):
        """initializing singlylinkedlist class"""
        self.__head = head

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
