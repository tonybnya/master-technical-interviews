"""
Tests for Queue implementation using list.
"""

import unittest
from typing import Iterable

from dsa_queue import Queue


class TestQueue(unittest.TestCase):
    """Class for tests."""

    def setUp(self) -> None:
        """Initialize a Queue for all the tests."""
        self.queue = Queue()

    def test_is_initialized(self) -> None:
        """Test the correct Initialization."""
        self.assertIsInstance(self.queue.queue, list)
        self.assertEqual(self.queue.length(), 0)

    def test_is_empty(self) -> None:
        """Test if the queue is empty."""
        self.assertIsInstance(self.queue.queue, list)
        self.assertEqual(self.queue.length(), 0)

    def test_enqueue(self) -> None:
        """Test enqueue method."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.length(), 3)

    def test_dequeue(self) -> None:
        """Test dequeue method."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.length(), 3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.length(), 2)

    def test_peek(self) -> None:
        """Test peek method."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.length(), 3)

        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.length(), 3)

    def test_length(self) -> None:
        """Test length method."""
        rng: Iterable = range(10)
        for i in rng:
            self.queue.enqueue(i)

        self.assertEqual(self.queue.length(), 10)

        last: int = self.queue.dequeue()
        second_last: int = self.queue.dequeue()

        self.assertEqual(last, 0)
        self.assertEqual(second_last, 1)

        self.assertEqual(self.queue.length(), 8)
