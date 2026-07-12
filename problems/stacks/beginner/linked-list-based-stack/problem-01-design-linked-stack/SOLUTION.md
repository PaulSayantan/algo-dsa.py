# Design a Linked-List Stack — Solution

## Optimal Approach

### Reference implementation

```python
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class LinkedStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, x):
        self._head = Node(x, self._head)
        self._size += 1

    def pop(self):
        node = self._head
        self._head = node.next
        self._size -= 1
        return node.val

    def top(self):
        return self._head.val

    def size(self):
        return self._size
```
