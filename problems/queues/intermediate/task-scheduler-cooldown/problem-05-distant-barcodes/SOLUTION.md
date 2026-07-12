# Distant Barcodes — Solution

## Optimal Approach

The same greedy idea as Reorganize String, specialized to `n = 1` on integers. Count each code and process codes from most frequent to least (ties broken by value for determinism). Write them into the result starting at index 0, stepping by 2 to fill all even positions first; when the index runs off the end, wrap to index 1 and continue filling odd positions. Because the most frequent code is spread across the even slots before any repeat can collide, no two equal codes end up adjacent.

### Reference implementation

```python
class Solution:
    def rearrangeBarcodes(self, barcodes):
        counts = Counter(barcodes)
        n = len(barcodes)
        order = sorted(counts, key=lambda x: (-counts[x], x))
        result = [0] * n
        idx = 0
        for val in order:
            for _ in range(counts[val]):
                result[idx] = val
                idx += 2
                if idx >= n:
                    idx = 1  # wrap to the odd positions
        return result
```

### Complexity

O(n log a) time (the sort over the alphabet), O(n) space.
