# Validate a Prefix Expression — Solution

## Optimal Approach

Run the prefix evaluation right to left, but instead of real values keep a stack
of markers that count how many *complete sub-expressions* are currently on the
stack. Push a marker for every operand. Each binary operator must consume two
sub-expressions, so it needs at least two markers to pop; if fewer are present
the expression is malformed (an operator with a missing operand). After popping
two, push one marker back (the operator plus its operands form one
sub-expression). The string is a valid prefix expression iff no operator ever
underflows and exactly one marker remains at the end (the empty string leaves
zero markers, so it is invalid).

- **Time:** `O(n)` — a single pass.
- **Space:** `O(n)` for the stack.

### Reference implementation

```python
class Solution:
    def isValidPrefix(self, expr):
        ops = set('+-*/')
        stack = []
        for ch in reversed(expr):
            if ch in ops:
                if len(stack) < 2:
                    return False
                stack.pop()
                stack.pop()
                stack.append(1)
            else:
                stack.append(1)
        return len(stack) == 1
```
