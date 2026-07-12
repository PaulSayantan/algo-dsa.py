# Matching Bracket Indices — Solution

## Optimal Approach

This is the purest form of bracket matching: instead of pushing the opener *characters*, push their *indices*. When a closer arrives, the index on top of the stack is precisely its partner (the string is guaranteed balanced, so the stack is never empty at a closer and the top always matches). Record both directions of the pairing. O(n) time, O(n) space.

### Reference implementation

```python
class Solution:
    def matchingBrackets(self, s):
        pairs = {')': '(', ']': '[', '}': '{'}
        openers = set(pairs.values())
        match = [-1] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c in openers:
                stack.append(i)
            else:
                j = stack.pop()
                match[i] = j
                match[j] = i
        return match
```
