"""LeetCode 142 - Linked List Cycle II.

Return the node where the cycle begins, or None if the list has no cycle,
using O(1) memory and without modifying the list.
"""
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, x: int) -> None:
        self.val: int = x
        self.next: Optional["ListNode"] = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Return the node where the cycle begins, or ``None`` if acyclic.

        Args:
            head: The head node of the singly linked list (may be ``None``).

        Returns:
            The first node that is part of the cycle, or ``None`` if the list
            contains no cycle.

        Example:
            >>> a, b, c = ListNode(3), ListNode(2), ListNode(0)
            >>> a.next, b.next = b, c
            >>> c.next = b            # cycle enters at node b (value 2)
            >>> Solution().detectCycle(a).val
            2
        """
        # TODO: implement
        # Phase 1: slow = slow.next, fast = fast.next.next until they meet.
        # Phase 2: move one pointer back to head; advance both by one until
        #          they meet again -> that node is the cycle entrance.
        pass


if __name__ == "__main__":
    # [3, 2, 0, -4] with tail -> index 1 (node value 2).
    n0, n1, n2, n3 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n0.next, n1.next, n2.next, n3.next = n1, n2, n3, n1
    result = Solution().detectCycle(n0)
    print(result.val if result else None)  # Expected: 2

    # [1] with no cycle.
    single = ListNode(1)
    print(Solution().detectCycle(single))  # Expected: None
