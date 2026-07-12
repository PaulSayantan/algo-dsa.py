# Postfix to Fully Parenthesized Infix — Solution

## Optimal Approach

Build the expression tree exactly as when evaluating postfix — but instead of a
numeric value, evaluate each subtree to its parenthesized string. An inorder walk
of the tree, wrapping every operator node in parentheses, reproduces the infix.

### Reference implementation

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def toInfix(self, postfix):
        ops = {'+', '-', '*', '/'}
        stack = []
        for t in postfix:
            if t in ops:
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(t, left, right))
            else:
                stack.append(Node(t))
        root = stack.pop()

        def walk(node):
            if node.left is None and node.right is None:
                return str(node.val)
            return '(' + walk(node.left) + node.val + walk(node.right) + ')'

        return walk(root)
```
