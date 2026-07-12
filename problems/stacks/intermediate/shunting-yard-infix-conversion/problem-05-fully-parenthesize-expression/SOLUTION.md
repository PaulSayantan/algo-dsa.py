# Fully Parenthesize an Infix Expression — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def fullyParenthesize(self, tokens):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        operands = []  # stack of built sub-expression strings
        ops = []

        def combine():
            op = ops.pop()
            b = operands.pop()
            a = operands.pop()
            operands.append("(" + a + op + b + ")")

        for t in tokens:
            if t in prec:
                while ops and ops[-1] in prec and prec[ops[-1]] >= prec[t]:
                    combine()
                ops.append(t)
            elif t == '(':
                ops.append(t)
            elif t == ')':
                while ops and ops[-1] != '(':
                    combine()
                ops.pop()  # discard '('
            else:
                operands.append(t)
        while ops:
            combine()
        return operands[-1]
```
