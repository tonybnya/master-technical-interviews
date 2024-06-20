"""
Tests for Stack implementation using list.
"""

import unittest
from typing import Iterable

from stack import Stack


class TestStack(unittest.TestCase):
    """Class for tests."""

    def setUp(self) -> None:
        """Initialize a Stack for all the tests."""
        self.stack = Stack()

    def test_is_initialized(self) -> None:
        """Test the correct initialization."""
        self.assertIsInstance(self.stack.stack, list)
        self.assertEqual(self.stack.length(), 0)

    def test_is_empty(self) -> None:
        """Test if the stack is empty."""
        self.assertIsInstance(self.stack.stack, list)
        self.assertEqual(self.stack.length(), 0)

    def test_push(self) -> None:
        """Test push method."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(self.stack.length(), 4)

    def test_peek(self) -> None:
        """Test peek method."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.peek(), 3)

    def test_pop(self) -> None:
        """Test pop method."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)

        self.assertEqual(self.stack.length(), 5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.length(), 4)

    def test_length(self) -> None:
        """Test length method."""
        rng: Iterable = range(10)
        for i in rng:
            self.stack.push(i)

        self.assertEqual(self.stack.length(), 10)
        last: int = self.stack.pop()
        second_last: int = self.stack.pop()
        self.assertEqual(self.stack.length(), 8)
