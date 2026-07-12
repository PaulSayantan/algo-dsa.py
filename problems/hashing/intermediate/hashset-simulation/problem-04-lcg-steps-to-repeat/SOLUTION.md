# Steps Until a Sequence Repeats — Solution

## Optimal Approach

Iterate the map, counting transitions until a state recurs.

### Reference implementation

```python
class Solution:
    def stepsToRepeat(self, start, a, c, m):
        seen = set()
        x = start
        steps = 0
        while x not in seen:
            seen.add(x)
            x = (a * x + c) % m
            steps += 1
        return steps
```

### Complexity

Time O(period), space O(period).

## Key Insights & Edge Cases

(0,2,3,7): 0→3→2→0 revisits 0 after 3 steps. (1,0,0,10): 1→0→0 repeats after 2 steps.
