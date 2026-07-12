# Build & Evaluate a Prefix Expression Tree — Solution

## Optimal Approach

Prefix notation is the mirror of postfix: an operator precedes its operands. If
you scan the tokens **right to left**, the same subtree-stack construction that
works for postfix applies. On an operator, the first subtree popped is its left
child and the second popped is its right child (because the left operand sits
immediately to the operator's right in the token stream). Evaluate the resulting
tree bottom-up; division truncates toward zero via `int(a / b)`.

### Reference implementation

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evalPrefix(self, prefix):
        ops = {'+', '-', '*', '/'}
        stack = []
        for t in reversed(prefix):
            if t in ops:
                left = stack.pop()
                right = stack.pop()
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
