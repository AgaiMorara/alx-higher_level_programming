#!/usr/bin/python3
""" Let us try to put classes to practice by defining a node of a
singly linked list and the list itself... Later we can bind operations
expected of the singly linked list to the class """
class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list.

        Raises:
            TypeError: If data is not an integer or if next_node is not None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets the data of the node. """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the data of the node. """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Gets the next node in the linked list. """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the next node in the linked list. """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be None or a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Represents a singly linked list. """
    def __init__(self):
        """ Initializes an empty singly linked list. """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ Returns a string representation of the linked list. """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
