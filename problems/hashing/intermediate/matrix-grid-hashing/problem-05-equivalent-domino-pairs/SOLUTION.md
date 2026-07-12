# Number of Equivalent Domino Pairs — Solution

## Optimal Approach

Order-normalize, then count equal-key pairs incrementally.

### Reference implementation

```python
class Solution:
    def numEquivDominoPairs(self, dominoes):
        cnt = defaultdict(int)
        total = 0
        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            total += cnt[key]
            cnt[key] += 1
        return total
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

Three [1,2]-equivalent dominoes give C(3,2)=3 pairs.
