# Flajolet-Martin Trailing-Zero Register — Solution

## Optimal Approach

With `mod = 256`, `2654435761 mod 256 = 177`, `40503 mod 256 = 55`, so `h(x) = (177*x + 55) mod 256`.

### Reference implementation

```python
class FMSketch:
    def __init__(self, mod=256):
        self.mod = mod
        self.max_zeros = 0

    def _hash(self, x):
        return (x * 2654435761 + 40503) % self.mod

    def _trailing_zeros(self, v):
        if v == 0:
            return self.mod.bit_length() - 1
        z = 0
        while v & 1 == 0:
            z += 1
            v >>= 1
        return z

    def add(self, x):
        z = self._trailing_zeros(self._hash(x))
        if z > self.max_zeros:
            self.max_zeros = z

    def max_trailing_zeros(self):
        return self.max_zeros

    def estimate(self):
        return 2 ** self.max_zeros
```

### Complexity

add is O(bit-width); the register is a single small integer.

## Key Insights & Edge Cases

Hashes: h(1)=232 (binary 11101000, 3 trailing zeros), h(2)=153 (odd, 0), h(3)=74 (1001010, 1), h(7)=14 (1110, 1). The maximum trailing-zero run is 3, so estimate = 2^3 = 8. We assert the EXACT register value, not a rounded cardinality — the point is the deterministic mechanic. A zero hash would contribute the full bit-width (log2 m).
