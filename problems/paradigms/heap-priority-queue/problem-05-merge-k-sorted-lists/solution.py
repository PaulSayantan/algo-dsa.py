"""Merge k Sorted Lists — LeetCode 23.

Empty solution template. Fill in the body yourself.
"""
from typing import List, Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge k ascending sorted linked lists into one sorted linked list.

        Args:
            lists: A list of k linked-list heads, each sorted ascending; any head
                may be None (an empty list), and the whole array may be empty.

        Returns:
            The head of the merged sorted linked list, or None if empty.

        Example:
            lists = [1->4->5, 1->3->4, 2->6]
            returns 1->1->2->3->4->4->5->6
        """
        # TODO: implement
        pass


def build(values: List[int]) -> Optional[ListNode]:
    """Helper: build a linked list from a Python list of values."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    """Helper: convert a linked list back to a Python list of values."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    print(to_list(sol.mergeKLists(lists)))   # expected: [1, 1, 2, 3, 4, 4, 5, 6]
    print(to_list(sol.mergeKLists([])))      # expected: []
    print(to_list(sol.mergeKLists([None])))  # expected: []
