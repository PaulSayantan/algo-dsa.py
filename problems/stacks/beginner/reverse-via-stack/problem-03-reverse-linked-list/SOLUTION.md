# Reverse a Linked List — Solution

## Optimal Approach

### Reference implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        dummy = ListNode()
        tail = dummy
        while stack:
            tail.next = ListNode(stack.pop())
            tail = tail.next
        return dummy.next


def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
```

Pushing every value and popping them reverses the sequence (LIFO), and rebuilding
nodes from the popped values yields the reversed list. Runs in O(n) time and O(n)
extra space for the stack.
