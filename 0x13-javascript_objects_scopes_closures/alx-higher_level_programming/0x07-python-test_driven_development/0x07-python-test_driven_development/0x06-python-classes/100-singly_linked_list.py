#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node (with private data and next_node)
Defines class SinglyLinkedList (with private head and public sorted_insert)
"""


class Node:
    """
    class Node definition

    Args:
        data (int): private
        next_node : private; can be None or Node object

    Functions:
        __init__(self, data, next_node=None)
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
    """

    def __init__(self, data, next_node=None):
        """
        Initializes node

        Attributes:
            data (int): private
            next_node : private; can be None or Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """"
        Getter

        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter

        Args:
            value: sets data to value if int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """"
        Getter

        Return: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter

        Args:
            value: sets next_node if value is next_node or None
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList definition

    Args:
        head: private

    Functions:
        __init__(self)
        sorted_insert(self, value)
    """

    def __init__(self):
        """
        Initializes singly linked list

        Attributes:
            head: private
        """
        self.__head = None

    def __str__(self):
        """
        String representation of singly linked list needed to print
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        Inserts new nodes into singly linked list in sorted order

        Args:
        value: int data for node
        """
        new1 = Node(value)
        if self.__head is None:
            self.__head = new1
            return

        temp = self.__head
        if new1.data < temp.data:
            new1.next_node = self.__head
            self.__head = new1
            return

        while (temp.next_node is not None) and (new1.data > temp.next_node.data):
            temp = temp.next_node
        new1.next_node = temp.next_node
        temp.next_node = new1
        return
