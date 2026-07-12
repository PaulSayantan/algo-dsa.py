# Counting Bloom Filter with Delete — Solution

## Optimal Approach

Counters make removal safe as long as it mirrors a prior add. The `contains` guard on `remove` prevents underflowing counters shared with other items.

### Reference implementation

```python
class CountingBloomFilter:
    def __init__(self, size=100, num_hashes=3):
        self.size = size
        self.k = num_hashes
        self.counts = [0] * size

    def _hashes(self, x):
        return [(x * 2654435761 + s * 40503) % self.size
                for s in range(1, self.k + 1)]

    def add(self, x):
        for h in self._hashes(x):
            self.counts[h] += 1

    def remove(self, x):
        if self.contains(x):
            for h in self._hashes(x):
                if self.counts[h] > 0:
                    self.counts[h] -= 1

    def contains(self, x):
        return all(self.counts[h] > 0 for h in self._hashes(x))
```

### Complexity

add / remove / contains are O(k); space is O(m) counters.

## Key Insights & Edge Cases

Hand-traced counters (m=100): 5 -> {8,11,14}, 7 -> {30,33,36}, 25 -> {28,31,34}. 5 and 7 share NO position, so removing 5 (counters 8,11,14 back to 0) leaves 7 fully present. contains(25) is False throughout since {28,31,34} were never touched. The disjoint hash sets are what make this trace unambiguous.
