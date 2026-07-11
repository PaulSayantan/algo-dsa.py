"""Swap Nodes in Pairs — LeetCode 24.

Empty solution template. Fill in the body yourself using Recursion.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Swap every two adjacent nodes and return the new head.

        Do not modify node values — relink the nodes themselves. Solve it with
        Recursion: swap the first pair, then recursively swap the remainder of
        the list and attach it. Base case: zero or one remaining node is left
        as-is.

        Args:
            head: The head node of the singly linked list (may be None).

        Returns:
            The head node of the list after swapping adjacent pairs.

        Example:
            1 -> 2 -> 3 -> 4   becomes   2 -> 1 -> 4 -> 3
        """
        # TODO: implement
        pass


def _build(values: list) -> Optional[ListNode]:
    """Helper: build a linked list from a Python list of values."""
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def _to_list(head: Optional[ListNode]) -> list:
    """Helper: convert a linked list back to a Python list of values."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    print(_to_list(sol.swapPairs(_build([1, 2, 3, 4]))))  # expected: [2, 1, 4, 3]
    print(_to_list(sol.swapPairs(_build([1, 2, 3]))))      # expected: [2, 1, 3]
    print(_to_list(sol.swapPairs(_build([1]))))            # expected: [1]
    print(_to_list(sol.swapPairs(_build([]))))             # expected: []
