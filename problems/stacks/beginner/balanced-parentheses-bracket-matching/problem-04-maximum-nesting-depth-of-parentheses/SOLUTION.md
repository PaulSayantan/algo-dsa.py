# Maximum Nesting Depth of the Parentheses — Solution

## Optimal Approach

The nesting depth at any point is exactly the height of the bracket-matching stack there. We never need to store the brackets themselves — only the count of currently-open ones. Increment on `(`, decrement on `)`, and remember the largest value the counter reaches. Non-bracket characters are ignored. O(n) time, O(1) space.

### Reference implementation

```python
class Solution:
    def maxDepth(self, s):
        depth = 0
        best = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > best:
                    best = depth
            elif c == ')':
                depth -= 1
        return best
```
