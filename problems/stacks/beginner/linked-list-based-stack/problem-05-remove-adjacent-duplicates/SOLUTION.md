# Remove All Adjacent Duplicates In String — Solution

## Optimal Approach

Scan the string once, maintaining a stack of the characters kept so far. For
each character, if it equals the current top of the stack the two are an
adjacent duplicate pair, so pop the top and drop the incoming character;
otherwise push it. A linked-list stack pushes and pops at the head in O(1), so
the whole scan is O(n). At the end, the stack read from bottom to top is the
reduced string.

### Reference implementation

```python
class Solution:
    def removeDuplicates(self, s):
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
```
