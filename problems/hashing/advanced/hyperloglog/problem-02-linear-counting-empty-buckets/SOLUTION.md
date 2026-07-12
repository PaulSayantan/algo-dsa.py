# Linear Counting: Empty Buckets — Solution

## Optimal Approach

With `m = 10`, `2654435761 mod 10 = 1`, `40503 mod 10 = 3`, so `h(x) = (x + 3) mod 10`.

### Reference implementation

```python
class LinearCounter:
    def __init__(self, m=10):
        self.m = m
        self.buckets = [0] * m

    def _hash(self, x):
        return (x * 2654435761 + 40503) % self.m

    def add(self, x):
        self.buckets[self._hash(x)] = 1

    def filled_buckets(self):
        return sum(self.buckets)

    def empty_buckets(self):
        return self.m - sum(self.buckets)
```

### Complexity

add is O(1); space is O(m) bits.

## Key Insights & Edge Cases

Buckets: h(1)=4, h(2)=5, h(3)=6, h(8)=1 -> four distinct bits set, so filled=4, empty=6. h(11)=(11+3) mod 10=4, colliding with bucket 4 (from item 1), so the bitmap is unchanged: still filled=4, empty=6. This collision is exactly why linear counting UNDER-counts distinct items — we verify the exact bucket bookkeeping, not the fuzzy estimate.
