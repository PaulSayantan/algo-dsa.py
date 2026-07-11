"""Merge Two Sorted Lists — LeetCode 21.

Empty solution template. Fill in the body yourself using Recursion.
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two sorted linked lists into one sorted list.

        Solve it with Recursion: the smaller of the two current heads is the
        head of the merged list, and its tail is the merge of the rest of that
        list with the other list. Base case: if either list is empty, the merge
        is just the other list.

        Args:
            list1: Head of the first non-decreasing sorted list (may be None).
            list2: Head of the second non-decreasing sorted list (may be None).

        Returns:
            The head of the merged sorted linked list (None if both are empty).

        Example:
            list1 = 1 -> 2 -> 4,  list2 = 1 -> 3 -> 4
            merged = 1 -> 1 -> 2 -> 3 -> 4 -> 4
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
    print(_to_list(sol.mergeTwoLists(_build([1, 2, 4]), _build([1, 3, 4]))))  # expected: [1, 1, 2, 3, 4, 4]
    print(_to_list(sol.mergeTwoLists(_build([]), _build([]))))                # expected: []
    print(_to_list(sol.mergeTwoLists(_build([]), _build([0]))))               # expected: [0]
