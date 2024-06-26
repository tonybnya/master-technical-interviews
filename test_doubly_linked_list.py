"""
Tests for Doubly Linked List implementation.
"""

import unittest

from dsa_doubly_linked_list import DoublyLinkedList


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
        self.assertEqual(self.dll.get_size(), 2)

    def test_insert_at_index(self):
        """Test the correct insertion at a specific index."""
        self.dll.insert_at_begin(10)
        self.dll.insert_at_begin(20)
        self.assertEqual(self.dll.get_size(), 2)

        self.dll.insert_at_index(15, 1)
        self.assertEqual(self.dll.root.data, 20)
        self.assertIsNone(self.dll.root.prevnode)
        self.assertEqual(self.dll.root.nextnode.data, 15)
        self.assertEqual(self.dll.root.nextnode.nextnode.data, 10)
        self.assertEqual(self.dll.get_size(), 3)

    def test_get_size(self):
        """Test get the correct size."""
        self.assertEqual(self.dll.get_size(), 0)

        self.dll.insert_at_begin(10)
        self.dll.insert_at_begin(20)
        self.dll.insert_at_begin(30)

        self.assertEqual(self.dll.get_size(), 3)
