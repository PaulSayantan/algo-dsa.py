"""Reverse Linked List — LeetCode 206.

Empty solution template. Fill in the body yourself using Recursion.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse a singly linked list and return the new head.

        A list is recursively "a node followed by a smaller list". Solve it
        with Recursion: reverse the sublist starting at head.next, then relink
        the current node to the back of that reversed sublist as the calls
        unwind. Base case: an empty list or a single node is its own reverse.

        Args:
            head: The head node of the singly linked list (may be None).

        Returns:
            The head node of the reversed list (None if the input was empty).

        Example:
            1 -> 2 -> 3 -> None   reverses to   3 -> 2 -> 1 -> None
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
    print(_to_list(sol.reverseList(_build([1, 2, 3, 4, 5]))))  # expected: [5, 4, 3, 2, 1]
    print(_to_list(sol.reverseList(_build([1, 2]))))            # expected: [2, 1]
    print(_to_list(sol.reverseList(_build([]))))               # expected: []
