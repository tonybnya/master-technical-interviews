"""
Implementation of a Doubly Linked List in Python.
"""

from typing import Optional


class Node:
    """Define a Node for a Doubly Linked List."""

    def __init__(self, value: int) -> None:
        """Initialize a Node."""
        self.data = value
        self.nextnode = None
        self.prevnode = None


class DoublyLinkedList:
    """Define a Doubly Linked List."""

    def __init__(self, root: Optional[Node] = None) -> None:
        """Initialize the Doubly Linked List."""
        self.root: Optional[Node] = None

    def insert_at_begin(self, value) -> None:
        """Insert a value at the beginning."""
        node: Node = Node(value)

        if self.root is None:
            self.root = node
            return

        node.nextnode = self.root
        self.root.prevnode = node
        self.root = node

    def insert_at_index(self, value: int, index: int) -> Optional[str]:
        """Insert a value at a specific index."""
        node: Node = Node(value)
        pos: int = 0
        temp: Optional[Node] = self.root

        if index == 0:
            self.insert_at_begin(value)
            return

        while temp and pos != index:
            temp = temp.nextnode
            pos += 1

        if temp is None:
            return "Index not found."

        node.nextnode = temp
        temp.prevnode = node
        temp.prevnode.nextnode = node
        node.prevnode = temp.prevnode

    def insert_at_end(self, value: int) -> None:
        """Insert a value at the end."""
        node: Node = Node(value)

        if self.root is None:
            self.root = node
            return

        temp: Optional[Node] = self.root
        while temp.nextnode:
            temp = temp.nextnode

        temp.nextnode = node
        node.prevnode = temp

    def update_at_index(self, value: int, index: int) -> Optional[str]:
        """Update a value at a specific index."""
        temp: Optional[Node] = self.root
        pos: int = 0

        while temp and pos != index:
            temp = temp.nextnode
            pos += 1

        if temp is None:
            return "Index not found."

        temp.data = value

    def remove_first_node(self) -> None:
        """Remove the first node."""
        if self.root is None:
            return

        self.root = self.root.nextnode

    def remove_last_node(self) -> None:
        """Remove the last node."""
        if self.root is None:
            return

        if self.root.nextnode is None:
            self.root = None
            return

        temp: Optional[Node] = self.root
        while temp.nextnode:
            temp = temp.nextnode

        temp = None

    def remove_node(self, value: int) -> Optional[str]:
        """Remove a node containing a specific value."""
        if self.root is None:
            return

        temp: Optional[Node] = self.root
        if temp.data == value:
            self.root = self.root.nextnode
            self.root.prevnode = None
            return

        while temp and temp.data != value:
            temp = temp.nextnode

        if temp is None:
            return "Value not found."

        temp.nextnode = temp.nextnode.nextnode
        temp.nextnode.nextnode.prevnode = temp

    def remove_at_index(self, index: int) -> Optional[str]:
        """Remove a node at a specific index."""
        if self.root is None:
            return

        temp: Optional[Node] = self.root
        pos: int = 0

        if index == 0:
            self.root = self.root.nextnode
            return

        while temp and pos != index:
            temp = temp.nextnode
            pos += 1

        if temp is None or temp.nextnode is None:
            return "Index not found."

        temp.nextnode = temp.nextnode.nextnode
        temp.nextnode.nextnode.prevnode = temp

    def get_size(self) -> int:
        """Get the size/length of a Doubly Linked List."""
        size: int = 0
        temp = self.root
        while temp:
            size += 1
            temp = temp.nextnode

        return size

    def print_dll(self) -> None:
        """Print a Doubly Linked List."""
        temp: Optional[Node] = self.root

        print("None<-")
        while temp:
            print(f"[{temp.data}]≈", end="")
            temp = temp.nextnode

        print("->None")

