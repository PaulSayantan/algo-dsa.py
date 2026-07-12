# Cycle Length in a Functional Graph — Solution

## Optimal Approach

A step-index map turns the first revisit into an exact cycle length.

### Reference implementation

```python
class Solution:
    def cycleLength(self, succ, start):
        seen = {}
        node = start
        step = 0
        while node not in seen:
            seen[node] = step
            node = succ[node]
            step += 1
        return step - seen[node]
```

### Complexity

Time O(path), space O(path).

## Key Insights & Edge Cases

0→1→2→3→4→2: the cycle 2→3→4→2 has length 3.
