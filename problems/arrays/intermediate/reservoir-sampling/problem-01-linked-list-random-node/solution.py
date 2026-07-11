"""Linked List Random Node (LeetCode 382).

Fill in `Solution` using Reservoir Sampling (k = 1) so that `getRandom`
returns each node value with equal probability without counting the list first.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]) -> None:
        """Initialize the object with the head of the singly linked list.

        Args:
            head: The first node of the list (guaranteed non-empty per constraints).
        """
        # TODO: store whatever you need (a reference to head is enough)
        pass

    def getRandom(self) -> int:
        """Return the value of a uniformly random node in the list.

        Each node's value is returned with probability 1/n, where n is the
        (unknown-in-advance) number of nodes. Use a single pass and O(1) space.

        Returns:
            The value stored in the randomly selected node.

        Example:
            >>> s = Solution(ListNode(1, ListNode(2, ListNode(3))))
            >>> s.getRandom() in (1, 2, 3)
            True
        """
        # TODO: implement using Reservoir Sampling with k = 1
        pass


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    s = Solution(head)
    print(s.getRandom())  # expected: one of 1, 2, 3 (uniformly at random)
    print(s.getRandom())  # expected: one of 1, 2, 3 (uniformly at random)
