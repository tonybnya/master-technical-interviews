"""
Tests for Doubly Linked List implementation.
"""

import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    """Class for tests."""

    def setUp(self) -> None:
        """Initialize a Doubly Linked List for all the tests functions."""
        self.dll = DoublyLinkedList()

    def test_is_initialized(self) -> None:
        """Test the correct initialization."""
        self.assertIsNone(self.dll.root)