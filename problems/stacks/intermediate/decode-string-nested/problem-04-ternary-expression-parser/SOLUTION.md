# Ternary Expression Parser — Solution

## Optimal Approach

Because `?:` is right-associative, scanning right-to-left lets each ternary be
resolved as soon as its condition is seen. Push characters onto a stack; the
moment the current character is a condition (`T`/`F`) and the stack top is `?`,
we have a complete `cond ? true : false` group on top — pop the five tokens
(`?`, true-branch, `:`, false-branch) and push back whichever branch the
condition selects. Nested ternaries collapse bottom-up exactly like the
partial-string frames in nested decoding.

### Reference implementation

```python
class Solution:
    def parseTernary(self, expression):
        stack = []
        for ch in reversed(expression):
            if stack and stack[-1] == '?':
                stack.pop()           # '?'
                true_expr = stack.pop()
                stack.pop()           # ':'
                false_expr = stack.pop()
                stack.append(true_expr if ch == 'T' else false_expr)
            else:
                stack.append(ch)
        return stack[-1]
```
