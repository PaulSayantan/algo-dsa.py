"""LeetCode 21 - Merge Two Sorted Lists.

Splice two sorted linked lists into one sorted list using the Two-Pointer Merge
technique. Fill in `mergeTwoLists`.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """Merge two sorted linked lists into one sorted linked list.

        Args:
            list1: Head of the first sorted linked list (may be None).
            list2: Head of the second sorted linked list (may be None).

        Returns:
            The head of the merged sorted linked list, or None if both inputs
            are empty.

        Example:
            list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
            returns 1 -> 1 -> 2 -> 3 -> 4 -> 4
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

    print(to_list(s.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))
    # expected: [1, 1, 2, 3, 4, 4]

    print(to_list(s.mergeTwoLists(build([]), build([]))))
    # expected: []

    print(to_list(s.mergeTwoLists(build([]), build([0]))))
    # expected: [0]
