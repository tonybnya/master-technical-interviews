"""
Implementation of a Queue using a list.
"""


class Queue:
    """Define a Queue."""

    def __init__(self) -> None:
        """Initialize an empty list."""
        self.queue = []

    def is_empty(self) -> bool:
        """Check if the queue is empty or not."""
        return len(self.queue) == 0

    def enqueue(self, n: int) -> None:
        """Add an element to the queue."""
        self.queue.insert(0, n)

    def dequeue(self) -> int:
        """Remove and return the first element added."""
        return self.queue.pop()

    def peek(self) -> int:
        """Get the first element added."""
        return self.queue[-1]

    def length(self) -> int:
        """Get the length of the queue."""
        return len(self.queue)

    def print_queue(self) -> None:
        """Print the queue."""
        n: int = self.length()
        i: int = 0
        while i < n:
            print(f"|{self.queue[i]}|", end="")
            i += 1
        print()
