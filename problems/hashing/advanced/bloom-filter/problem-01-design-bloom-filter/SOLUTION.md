# Design a Bloom Filter — Solution

## Optimal Approach

With `m = 100`, `k = 3`, seeds 1..3, and `2654435761 mod 100 = 61`, `40503 mod 100 = 3`, the bit set for value `x` is `{(61*x + 3s) mod 100 : s = 1,2,3}`.

### Reference implementation

```python
class BloomFilter:
    def __init__(self, size=100, num_hashes=3):
        self.size = size
        self.k = num_hashes
        self.bits = [0] * size

    def _hashes(self, x):
        return [(x * 2654435761 + s * 40503) % self.size
                for s in range(1, self.k + 1)]

    def add(self, x):
        for h in self._hashes(x):
            self.bits[h] = 1

    def contains(self, x):
        return all(self.bits[h] for h in self._hashes(x))
```

### Complexity

add / contains are O(k); space is O(m) bits.

## Key Insights & Edge Cases

Hand-traced bits: 10 -> {13,16,19}, 20 -> {23,26,29}, 30 -> {33,36,39}, so the union of set bits is {13,16,19,23,26,29,33,36,39}. contains(40) hashes to {43,46,49} (none set) -> False; contains(15) -> {18,21,24} (none set) -> False. contains(110): 110*61 mod 100 = 10, so bits {13,16,19} — identical to 10's — all set -> True, a genuine false positive. This shows the one-sided error: no false negatives, but collisions on all k bits fool contains().
