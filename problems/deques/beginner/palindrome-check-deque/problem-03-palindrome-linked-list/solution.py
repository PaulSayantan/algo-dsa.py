"""Palindrome Linked List — LeetCode 234. Collect node values, deque two-end compare."""
from collections import deque  # noqa: F401
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TODO: push each node's val onto a deque, then compare popleft() vs pop()
        pass


def build(values: list) -> Optional[ListNode]:
    """Helper to build a linked list from a Python list of ints."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(build([1, 2, 2, 1])))     # expected: True
    print(sol.isPalindrome(build([1, 2])))           # expected: False
    print(sol.isPalindrome(build([1, 2, 3, 2, 1])))  # expected: True
    print(sol.isPalindrome(build([])))               # expected: True
    print(sol.isPalindrome(build([7])))              # expected: True
