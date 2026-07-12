# Infix to Postfix Conversion — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def toPostfix(self, tokens):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        out = []
        ops = []
        for t in tokens:
            if t in prec:
                while ops and ops[-1] in prec and prec[ops[-1]] >= prec[t]:
                    out.append(ops.pop())
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
