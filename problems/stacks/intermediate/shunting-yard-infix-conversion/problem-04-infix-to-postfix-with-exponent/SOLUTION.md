# Infix to Postfix with Right-Associative Exponent — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def toPostfix(self, tokens):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        right_assoc = {'^'}
        out = []
        ops = []
        for t in tokens:
            if t in prec:
                while ops and ops[-1] in prec:
                    top = ops[-1]
                    if prec[top] > prec[t] or (
                        prec[top] == prec[t] and t not in right_assoc
                    ):
                        out.append(ops.pop())
                    else:
                        break
                ops.append(t)
            elif t == '(':
                ops.append(t)
            elif t == ')':
                while ops and ops[-1] != '(':
                    out.append(ops.pop())
                ops.pop()  # discard '('
            else:
                out.append(t)
        while ops:
            out.append(ops.pop())
        return out
```
