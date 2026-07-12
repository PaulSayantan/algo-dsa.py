# Jump Hash Bucket Distribution — Solution

## Optimal Approach

Apply the O(log n) jump hash per key; the mapping is stable and near-uniform.

### Reference implementation

```python
class Solution:
    def jumpConsistentHash(self, key, num_buckets):
        key &= 0xFFFFFFFFFFFFFFFF
        b, j = -1, 0
        while j < num_buckets:
            b = j
            key = (key * 2862933555777941757 + 1) & 0xFFFFFFFFFFFFFFFF
            j = int((b + 1) * ((1 << 31) / ((key >> 33) + 1)))
        return b

    def buckets(self, keys, num_buckets):
        return [self.jumpConsistentHash(k, num_buckets) for k in keys]
```

### Complexity

O(K log num_buckets) for K keys.

## Key Insights & Edge Cases

Every returned bucket is within range and reproducible. Growing num_buckets from n to n+1 moves only about 1/(n+1) of the keys to the new bucket and leaves the rest fixed — the consistent-hashing property, achieved with zero stored state.
