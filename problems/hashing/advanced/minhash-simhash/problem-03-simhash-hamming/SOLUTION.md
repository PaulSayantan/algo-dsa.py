# SimHash Hamming Distance — Solution

## Optimal Approach

Accumulate a signed vote per bit across tokens, threshold at zero to form the fingerprint, then XOR-and-popcount two fingerprints for their Hamming distance.

### Reference implementation

```python
class SimHash:
    """64-bit SimHash of a token multiset via arithmetic hashing."""

    _MASK = 0xFFFFFFFFFFFFFFFF

    def _hash64(self, token):
        h = 1469598103934665603      # 64-bit FNV-1a
        for ch in token:
            h ^= ord(ch)
            h = (h * 1099511628211) & self._MASK
        return h

    def fingerprint(self, tokens):
        v = [0] * 64
        for tok, w in Counter(tokens).items():
            hv = self._hash64(tok)
            for i in range(64):
                v[i] += w if (hv >> i) & 1 else -w
        f = 0
        for i in range(64):
            if v[i] > 0:
                f |= (1 << i)
        return f

    def hamming_distance(self, doc1, doc2):
        return bin(self.fingerprint(doc1) ^ self.fingerprint(doc2)).count("1")
```

### Complexity

O(64 * #distinct tokens) to fingerprint; O(1) to compare.

## Key Insights & Edge Cases

Identical documents give distance 0. Documents sharing most tokens stay close: swapping just one of four tokens (d -> e) moves only 2 of 64 bits, while replacing two of three tokens pushes the distance to 33 (near the ~32 expected for unrelated 64-bit strings). This locality is what makes SimHash a near-duplicate detector.
