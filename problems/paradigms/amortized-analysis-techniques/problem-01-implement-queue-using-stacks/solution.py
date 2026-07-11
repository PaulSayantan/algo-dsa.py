"""LeetCode 232 - Implement Queue using Stacks.

Implement a FIFO queue using only two stacks, achieving O(1) amortized time
per operation.
"""


class MyQueue:
    """A FIFO queue backed by two stacks (an "in" stack and an "out" stack).

    Example:
        >>> q = MyQueue()
        >>> q.push(1)
        >>> q.push(2)
        >>> q.peek()
        1
        >>> q.pop()
        1
        >>> q.empty()
        False
    """

    def __init__(self) -> None:
        """Initialize the two internal stacks."""
        # TODO: implement (e.g. set up an "in" stack and an "out" stack)
        pass

    def push(self, x: int) -> None:
        """Push element x to the back of the queue.

        Args:
            x: The integer to enqueue.
        """
        # TODO: implement
        pass

    def pop(self) -> int:
        """Remove the element from the front of the queue and return it.

        Returns:
            The value at the front of the queue.
        """
        # TODO: implement
        pass

    def peek(self) -> int:
        """Return the element at the front of the queue without removing it.

        Returns:
            The value at the front of the queue.
        """
        # TODO: implement
        pass

    def empty(self) -> bool:
        """Report whether the queue currently holds no elements.

        Returns:
            True if the queue is empty, False otherwise.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())   # expected: 1
    print(q.pop())    # expected: 1
    print(q.empty())  # expected: False
