# Happy Number — Solution

## Optimal Approach

Detect the non-1 cycle with a Hash Set of visited values.

### Reference implementation

```python
class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1
```

### Complexity

Time O(log n) transitions, space O(1) practically.

## Key Insights & Edge Cases

Unhappy numbers all fall into the cycle 4→16→37→58→89→145→42→20→4.
