"""LeetCode 23 - Merge k Sorted Lists.

Merge k sorted linked lists into one. The intended solution repeatedly applies
the two-list Two-Pointer Merge (divide and conquer over the k lists). Fill in
`mergeKLists` (a helper `mergeTwoLists` is a natural building block).
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge k sorted linked lists into a single sorted linked list.

        Args:
            lists: A list of k linked-list heads, each sorted non-decreasing.
                Individual heads may be None, and the outer list may be empty.

        Returns:
            The head of the merged sorted linked list, or None if there are no
            nodes at all.

        Example:
            lists = [1->4->5, 1->3->4, 2->6]
            returns 1->1->2->3->4->4->5->6
        """
        # TODO: implement
        pass


def build(values: list) -> Optional[ListNode]:
    """Helper: build a linked list from a Python list of ints."""
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(node: Optional[ListNode]) -> list:
    """Helper: convert a linked list back into a Python list of ints."""
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    s = Solution()

    print(
        to_list(s.mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]))
    )
    # expected: [1, 1, 2, 3, 4, 4, 5, 6]

    print(to_list(s.mergeKLists([])))        # expected: []
    print(to_list(s.mergeKLists([build([])])))  # expected: []
