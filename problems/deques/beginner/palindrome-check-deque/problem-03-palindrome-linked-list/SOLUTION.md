# Palindrome Linked List — Solution

## Optimal Approach

Walk the list once, pushing each node's value onto a deque. Now the sequence is
random-access from both ends, so a palindrome check reads like its definition:
repeatedly compare the front (`popleft()`) with the back (`pop()`). Any mismatch
means it is not a palindrome; if we consume down to zero or one element, every
mirrored pair agreed.

### Reference implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


class Solution:
    def isPalindrome(self, head):
        dq = deque()
        while head:
            dq.append(head.val)
            head = head.next
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
```

- **Time:** O(n) — one pass to copy, one pass to compare.
- **Space:** O(n) — the deque holds every value.
