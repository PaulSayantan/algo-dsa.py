# Palindrome Check with a Deque — Solution

## Optimal Approach

Push every character onto a doubly-linked-list deque, then repeatedly pop one
from each end and compare. While more than one character remains, a `popFront()`
that differs from the matching `popBack()` proves the string is not a
palindrome. When 0 or 1 characters are left, every pair matched, so it is a
palindrome. Loading is O(n) and each comparison pop is O(1), for O(n) total.

### Reference implementation

```python
class _DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedDeque:
    def __init__(self):
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

    def size(self):
        return self._size


class Solution:
    def isPalindrome(self, s):
        dq = LinkedDeque()
        for ch in s:
            dq.pushBack(ch)
        while dq.size() > 1:
            if dq.popFront() != dq.popBack():
                return False
        return True
```
