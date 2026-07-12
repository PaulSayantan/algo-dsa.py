# MinHash Signature — Solution

## Optimal Approach

One pass over the set per hash function computes each coordinate's minimum; the k-vector is the set's sketch.

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

O(k * |set|) to build a length-k signature.

## Key Insights & Edge Cases

The signature is a fixed-length fingerprint regardless of set size, so comparing two sets becomes an O(k) coordinate comparison. Both example sets share element 5 and part of {3,4,5}; note the two signatures already agree in some positions (e.g. index 3 and the last coordinate) — those agreements are exactly what the Jaccard estimate counts.
