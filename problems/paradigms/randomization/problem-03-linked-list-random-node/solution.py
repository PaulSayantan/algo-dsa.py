"""LeetCode 382 - Linked List Random Node.

Return a uniformly random node value from a singly linked list. The follow-up asks for a
single pass with O(1) extra space when the length is unknown: use reservoir sampling with
reservoir size 1.
"""

from __future__ import annotations

import random
from typing import Optional


class ListNode:
    """A singly linked list node."""

    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    """Return a uniformly random node value from a linked list."""

    def __init__(self, head: Optional[ListNode]) -> None:
        """Initialize the object with the head of the linked list.

        Args:
            head: The head node of the singly linked list (non-empty).
        """
        # TODO: store what you need (for the O(1)-space approach, just keep head)
        pass

    def getRandom(self) -> int:
        """Return the value of a uniformly random node in the list.

        Every node must be returned with equal probability 1/n, where n is the
        number of nodes.

        Returns:
            The value stored at a uniformly random node.

        Example:
            >>> s = Solution(ListNode(1, ListNode(2, ListNode(3))))
            >>> s.getRandom() in (1, 2, 3)
            True
        """
        # TODO: implement (reservoir sampling, reservoir size 1)
        pass


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    obj = Solution(head)
    print(obj.getRandom())  # expected: one of 1, 2, 3 (each with probability 1/3)
    print(obj.getRandom())  # expected: one of 1, 2, 3 (independent draw)
    print(obj.getRandom())  # expected: one of 1, 2, 3 (independent draw)
