# Digit-Square Sequence Length — Solution

## Optimal Approach

Set of visited values; the size at the first repeat is the answer.

### Reference implementation

```python
class Solution:
    def digitSquareCycle(self, start):
        seen = set()
        n = start
        while n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return len(seen)
```

### Complexity

Time O(states), space O(states).

## Key Insights & Edge Cases

From 1: transform(1)=1 repeats immediately → 1 distinct value.
