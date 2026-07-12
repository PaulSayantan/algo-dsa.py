# Infix to Postfix via Expression Tree — Solution

## Optimal Approach

Scan the tokens left to right. Operands become leaf subtrees pushed on a node
stack. Operators and `(` go on an operator stack; on a `)` or a lower/equal
precedence incoming operator we pop an operator and combine the top two subtrees
into a new node. Draining the operator stack at the end leaves the root on the
node stack. A postorder walk of that tree is the postfix expression.

### Reference implementation

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def infixToPostfix(self, infix):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        nodes = []
        opstack = []

        def apply():
            op = opstack.pop()
            right = nodes.pop()
            left = nodes.pop()
            nodes.append(Node(op, left, right))

        for t in infix:
            if t == '(':
                opstack.append(t)
            elif t == ')':
                while opstack and opstack[-1] != '(':
                    apply()
                opstack.pop()  # discard the '('
            elif t in prec:
                while opstack and opstack[-1] != '(' and prec[opstack[-1]] >= prec[t]:
                    apply()
                opstack.append(t)
            else:
                nodes.append(Node(t))
        while opstack:
            apply()
        root = nodes.pop()

        out = []

        def post(n):
            if n.left is None and n.right is None:
                out.append(str(n.val))
                return
            post(n.left)
            post(n.right)
            out.append(n.val)

        post(root)
        return out
```
