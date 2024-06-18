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
        self.assertEqual(self.dll.get_size(), 0)

    def test_insert_at_begin(self):
        """Test the correct insertion at the beginning."""
        self.dll.insert_at_begin(10)
        self.dll.insert_at_begin(20)

        self.assertEqual(self.dll.root.data, 20)
        self.assertEqual(self.dll.root.nextnode.data, 10)
        self.assertIsNone(self.dll.root.prevnode)

    # def test_get_size(self):
    #     """Test get the correct size."""
    #     self.assertEqual(self.dll.get_size(), 0)