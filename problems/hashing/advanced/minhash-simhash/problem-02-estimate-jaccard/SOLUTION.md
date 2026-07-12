# Estimate Jaccard Similarity — Solution

## Optimal Approach

Build both signatures, count agreeing coordinates, divide by k.

### Reference implementation

```python
class MinHash:
    """MinHash sketch with a FIXED family of universal hashes (seeded)."""

    _P = 2147483647

    def __init__(self, k=8):
        random.seed(101)
        self._k = k
        self._params = [
            (random.randrange(1, self._P), random.randrange(0, self._P))
            for _ in range(k)
        ]

    def signature(self, elements):
        sig = []
        for a, b in self._params:
            sig.append(min(((a * x + b) % self._P) for x in elements))
        return sig

    def estimate_jaccard(self, s1, s2):
        sig1, sig2 = self.signature(s1), self.signature(s2)
        matches = sum(1 for x, y in zip(sig1, sig2) if x == y)
        return matches / self._k
```

### Complexity

O(k * |set|) to sketch, O(k) to compare.

## Key Insights & Edge Cases

Identical sets always give 1.0 (every coordinate agrees) and disjoint sets tend toward 0.0 — here exactly 0.0. The middle case has true Jaccard 3/7 ~ 0.43; with only k=8 hashes the estimate (0.25) is a coarse but unbiased sample — accuracy improves as ~1/sqrt(k).
