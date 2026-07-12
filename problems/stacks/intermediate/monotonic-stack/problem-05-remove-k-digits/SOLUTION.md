# Remove K Digits — Solution

## Optimal Approach

Scan the digits left to right, keeping a monotonic **increasing** stack. Before
pushing the current digit, pop any strictly larger digit off the top while
removals remain (`k > 0`): a larger digit sitting in a more significant position
always makes the number bigger, so removing it first is optimal. If removals are
left over after the scan (the digits were non-decreasing), drop them from the end.
Finally strip leading zeros and return `"0"` if nothing is left.

### Reference implementation

```python
class Solution:
    def removeKdigits(self, num, k):
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k:
            stack = stack[:-k]
        result = "".join(stack).lstrip("0")
        return result if result else "0"
```
