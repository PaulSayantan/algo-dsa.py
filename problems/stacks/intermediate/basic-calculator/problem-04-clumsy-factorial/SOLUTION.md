# Clumsy Factorial — Solution

## Optimal Approach

Although the operators come from a fixed rotation rather than a parsed string,
this is exactly the term-stack calculator from Basic Calculator II. We seed the
stack with `n`, then walk the numbers `n-1, n-2, ..., 1`, and for each we look up
the operator that precedes it in the repeating `* / + -` cycle:

- `*` and `/` bind tighter, so we fold the number straight into the last pushed
  term (`stack[-1] * i` or `int(stack[-1] / i)`, truncating toward zero).
- `+` and `-` start a new term, so we push `+i` or `-i`.

Because the higher-precedence operations are always applied to the top of the
stack immediately, the additive terms never need reordering, and `sum(stack)` at
the end gives the answer. The scan is O(n) with O(n) stack space.

### Reference implementation

```python
class Solution:
    def clumsy(self, n):
        ops = ['*', '/', '+', '-']
        stack = [n]
        for i in range(n - 1, 0, -1):
            op = ops[(n - 1 - i) % 4]
            if op == '*':
                stack.append(stack.pop() * i)
            elif op == '/':
                stack.append(int(stack.pop() / i))
            elif op == '+':
                stack.append(i)
            else:
                stack.append(-i)
        return sum(stack)
```
