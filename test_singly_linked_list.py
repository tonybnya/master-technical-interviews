"""
Tests for Singly Linked List implementation.
"""

import unittest

from dsa_singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    """Class for tests."""

    def setUp(self) -> None:
        """Initialize a Singly Linked List for all the tests functions."""
        self.sll = SinglyLinkedList()

    def test_is_initialized(self) -> None:
        """Test the correct initialization."""
        self.assertIsNone(self.sll.root)
        self.assertEqual(self.sll.get_size(), 0)

    def test_insert_at_begin(self):
        """Test the correct insertion at the beginning."""
        self.sll.insert_at_begin(10)
        self.sll.insert_at_begin(20)

        self.assertEqual(self.sll.root.data, 20)
        self.assertEqual(self.sll.root.nextnode.data, 10)
        self.assertEqual(self.sll.get_size(), 2)

    def test_insert_at_end(self):
        """Test the correct insertion at the end."""
        self.sll.insert_at_end(30)
        self.sll.insert_at_end(40)

        self.assertEqual(self.sll.root.data, 30)
        self.assertEqual(self.sll.root.nextnode.data, 40)
        self.assertEqual(self.sll.get_size(), 2)

    def test_insert_at_index(self):
        """Test the correct insertion at a specific index."""
        self.sll.insert_at_end(10)
        self.sll.insert_at_end(30)
        self.assertEqual(self.sll.get_size(), 2)

        self.sll.insert_at_index(20, 1)
        self.assertEqual(self.sll.root.data, 10)
        self.assertEqual(self.sll.root.nextnode.data, 20)
        self.assertEqual(self.sll.root.nextnode.nextnode.data, 30)
        self.assertEqual(self.sll.get_size(), 3)

        output = self.sll.insert_at_index(1, 10)
        self.assertEqual(output, "Index not found.")

    def test_update_at_index(self):
        """Test the correct update at a specific index."""
        self.sll.insert_at_end(10)
        self.sll.insert_at_end(10)
        self.sll.insert_at_end(20)
        self.assertEqual(self.sll.root.nextnode.data, 10)
        self.assertEqual(self.sll.get_size(), 3)

        self.sll.update_at_index(15, 1)
        self.assertEqual(self.sll.root.nextnode.data, 15)
        self.assertEqual(self.sll.get_size(), 3)

        output = self.sll.update_at_index(1, 10)
        self.assertEqual(output, "Index not found.")

    def test_remove_first_node(self):
        """Test the correct remove of the first node."""
        self.sll.insert_at_end(10)
        self.sll.insert_at_end(20)

        self.assertEqual(self.sll.root.data, 10)
        self.assertEqual(self.sll.get_size(), 2)

        self.sll.remove_first_node()
        self.assertEqual(self.sll.root.data, 20)
        self.assertEqual(self.sll.get_size(), 1)

    def test_remove_last_node(self):
        """Tesf the correct remove of the last node."""
        self.sll.insert_at_end(10)
        self.sll.insert_at_end(20)
        self.sll.insert_at_end(30)

        self.assertEqual(self.sll.root.nextnode.nextnode.data, 30)
        self.assertEqual(self.sll.get_size(), 3)

        self.sll.remove_last_node()
        self.assertIsNone(self.sll.root.nextnode.nextnode)
        self.assertEqual(self.sll.get_size(), 2)

    def test_remove_at_index(self):
        """Test the correct remove at a specific index."""
        self.sll.insert_at_end(10)
        self.sll.insert_at_end(15)
        self.sll.insert_at_end(20)
        self.assertEqual(self.sll.root.nextnode.data, 15)
        self.assertEqual(self.sll.get_size(), 3)

        self.sll.remove_at_index(1)
        self.assertEqual(self.sll.root.nextnode.data, 20)
        self.assertEqual(self.sll.get_size(), 2)

        output = self.sll.remove_at_index(5)
        self.assertEqual(output, "Index not found.")

    def test_get_size(self):
        """Test get the correct size."""
        self.assertEqual(self.sll.get_size(), 0)

        self.sll.insert_at_end(10)
        self.sll.insert_at_begin(20)
        self.assertEqual(self.sll.get_size(), 2)

        self.sll.remove_first_node()
        self.assertEqual(self.sll.get_size(), 1)

        self.sll.remove_last_node()
        self.assertEqual(self.sll.get_size(), 0)


if __name__ == "__main__":
    unittest.main()
