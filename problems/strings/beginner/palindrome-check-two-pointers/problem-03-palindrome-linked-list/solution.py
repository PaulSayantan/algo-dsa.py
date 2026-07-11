from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Return whether the singly linked list is a palindrome.

        Args:
            head: The head node of the singly linked list (may be None).

        Returns:
            True if the sequence of node values reads the same forwards and
            backwards; False otherwise.

        Example:
            >>> # 1 -> 2 -> 2 -> 1
            >>> Solution().isPalindrome(
            ...     ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
            True
        """
        # TODO: find the middle (slow/fast), reverse the second half, then
        # compare the two halves with two pointers moving inward.
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
