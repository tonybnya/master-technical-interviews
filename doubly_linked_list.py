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