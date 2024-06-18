"""
Implementation of a Doubly Linked List in Python.
"""

from typing import Optional


class Node:
    """Define a Node for a Doubly Linked List."""

    def __init__(self, value: int) -> None:
        """Define a Node."""
        self.data = value
        self.nextnode: Optional[Node] = None
        self.prevnode: Optional[Node] = None


class DoublyLinkedList:
    """Define a Doubly Linked List."""

    def __init__(self, root: Optional[Node] = None) -> None:
        """Initialize the Doubly Linked List."""
        self.root = Optional[Node] = None

    def insert_at_begin(self, value) -> None:
        """Insert a value at the beginning."""
        node: Node = Node(value)

        if self.root is None:
            self.root = node
            return

        node.nextnode = self.root
        self.root.prevnode = node
        self.root = node

    def get_size(self) -> int:
        """Get the size/length of a Doubly Linked List."""
        size: int = 0

        return size