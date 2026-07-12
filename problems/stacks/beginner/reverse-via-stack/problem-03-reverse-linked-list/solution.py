"""Reverse a singly linked list using an explicit stack."""
from typing import List, Optional  # noqa: F401


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: push every node value onto a stack, then pop to relink in reverse
        pass


def build(values: List[int]) -> Optional[ListNode]:
    """Helper to build a linked list from a Python list of ints."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    """Helper to read a linked list back into a Python list of ints."""
    out: List[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.reverseList(build([1, 2, 3, 4, 5]))))  # expected: [5, 4, 3, 2, 1]
    print(to_list(sol.reverseList(build([1, 2]))))  # expected: [2, 1]
    print(to_list(sol.reverseList(build([]))))  # expected: []
