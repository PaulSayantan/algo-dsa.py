# Reverse the Order of Words in a String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def reverseWords(self, s):
        stack = s.split(" ")
        out = []
        while stack:
            out.append(stack.pop())
        return " ".join(out)
```

`split(" ")` produces the words in order; pushing them onto a stack and popping
reverses the sequence, exactly as reversing characters does but at word
granularity. Runs in O(n) time and space.
