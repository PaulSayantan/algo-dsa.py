# Build & Evaluate an Expression Tree — Solution

## Optimal Approach

### Reference implementation

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evalTree(self, postfix):
        ops = {'+', '-', '*', '/'}
        stack = []
        for t in postfix:
            if t in ops:
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(t, left, right))
            else:
                stack.append(Node(int(t)))
        root = stack.pop()

        def ev(node):
            if node.left is None and node.right is None:
                return node.val
            a = ev(node.left)
            b = ev(node.right)
            if node.val == '+':
                return a + b
            if node.val == '-':
                return a - b
            if node.val == '*':
                return a * b
            return int(a / b)

        return ev(root)
```
