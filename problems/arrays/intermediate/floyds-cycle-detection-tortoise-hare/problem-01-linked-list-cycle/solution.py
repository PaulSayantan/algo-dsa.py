"""LeetCode 141 - Linked List Cycle.

Determine whether a singly linked list contains a cycle, using O(1) memory.
"""
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, x: int) -> None:
        self.val: int = x
        self.next: Optional["ListNode"] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Return True if the linked list starting at ``head`` contains a cycle.

        Args:
            head: The head node of the singly linked list (may be ``None``).

        Returns:
            ``True`` if following ``next`` pointers eventually revisits a node,
            otherwise ``False``.

        Example:
            >>> a, b = ListNode(1), ListNode(2)
            >>> a.next = b
            >>> b.next = a          # cycle: 1 -> 2 -> 1 -> ...
            >>> Solution().hasCycle(a)
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    # Build [1, 2] with the tail linking back to index 0 (a cycle).
    n1, n2 = ListNode(1), ListNode(2)
    n1.next = n2
    n2.next = n1
    print(Solution().hasCycle(n1))  # Expected: True

    # Build [1] with no cycle.
    single = ListNode(1)
    print(Solution().hasCycle(single))  # Expected: False
