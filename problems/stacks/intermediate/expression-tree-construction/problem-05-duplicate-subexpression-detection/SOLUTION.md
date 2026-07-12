# Detect a Duplicate Subexpression — Solution

## Optimal Approach

Build the expression tree from postfix with the usual subtree stack. Then walk
the tree bottom-up, assigning each subtree a canonical signature: a leaf's
signature is its operand text, and an operator node's signature is the tuple
`(operator, left_signature, right_signature)`. Count how often each
operator-node signature is produced; if any is seen a second time, two identical
operator subtrees exist and the answer is `True`. Leaf signatures are not
counted, so repeated bare operands never trigger a match.

### Reference implementation

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasDuplicateSubexpr(self, postfix):
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

        seen = {}
        found = [False]

        def sign(node):
            if node.left is None and node.right is None:
                return str(node.val)
            sig = (node.val, sign(node.left), sign(node.right))
            seen[sig] = seen.get(sig, 0) + 1
            if seen[sig] == 2:
                found[0] = True
            return sig

        sign(root)
        return found[0]
```
