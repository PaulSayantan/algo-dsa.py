# Maximum Number After Removing K Digits — Solution

## Optimal Approach

Mirror of Remove K Digits. To *maximize*, keep a monotonic **decreasing** stack:
when a larger digit arrives, pop smaller tops while removal budget `k` remains. If
`k` is still positive after the scan, the smallest surviving digits sit at the end,
so trim them off.

### Reference implementation

```python
class Solution:
    def removeKdigitsMax(self, num, k):
        stack = []
        for d in num:
            while k and stack and stack[-1] < d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k:
            stack = stack[:len(stack) - k]
        return ''.join(stack)
```
