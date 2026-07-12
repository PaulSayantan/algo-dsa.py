# Infix to Prefix Conversion — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def toPrefix(self, tokens):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        # Reverse the token list and swap parentheses.
        rev = []
        for t in reversed(tokens):
            if t == '(':
                rev.append(')')
            elif t == ')':
                rev.append('(')
            else:
                rev.append(t)
        out = []
        ops = []
        for t in rev:
            if t in prec:
                # Pop only STRICTLY greater precedence so left-associativity
                # survives the reversal (equal operators stay stacked).
                while ops and ops[-1] in prec and prec[ops[-1]] > prec[t]:
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
        out.reverse()
        return out
```
