"""Palindrome check using a doubly-linked-list deque.

Load each character into the deque, then pop the front and back together and
compare; any mismatch means the string is not a palindrome. Comparing from both
ends inward is exactly what a deque's O(1) both-end pops are for.
"""


class _DNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None


class LinkedDeque:
    def __init__(self) -> None:
        self._head = _DNode(None)  # sentinel
        self._tail = _DNode(None)  # sentinel
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def pushBack(self, val):
        last = self._tail.prev
        node = _DNode(val)
        node.next = self._tail
        node.prev = last
        self._tail.prev = node
        last.next = node
        self._size += 1

    def popFront(self):
        node = self._head.next
        self._head.next = node.next
        node.next.prev = self._head
        self._size -= 1
        return node.val

    def popBack(self):
        node = self._tail.prev
        self._tail.prev = node.prev
        node.prev.next = self._tail
        self._size -= 1
        return node.val

    def size(self) -> int:
        return self._size


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TODO: push each char, then compare popFront() vs popBack() inward
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("racecar"))  # expected: True
    print(sol.isPalindrome("level"))  # expected: True
    print(sol.isPalindrome("noon"))  # expected: True
    print(sol.isPalindrome("hello"))  # expected: False
    print(sol.isPalindrome("ab"))  # expected: False
    print(sol.isPalindrome("a"))  # expected: True
    print(sol.isPalindrome(""))  # expected: True
