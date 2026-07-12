# Jump Consistent Hash — Solution

## Optimal Approach

Rather than materialize a ring, jump hashing computes, for an increasing bucket count, the next bucket index at which the key would 'jump' to a new bucket, skipping the runs where it stays. Expected O(log num_buckets) iterations.

### Reference implementation

```python
class Solution:
    def jumpConsistentHash(self, key, num_buckets):
        # Lamping & Veach's jump consistent hash: O(1) memory, O(log n) time.
        key &= 0xFFFFFFFFFFFFFFFF
        b, j = -1, 0
        while j < num_buckets:
            b = j
            key = (key * 2862933555777941757 + 1) & 0xFFFFFFFFFFFFFFFF
            j = int((b + 1) * ((1 << 31) / ((key >> 33) + 1)))
        return b
```

### Complexity

Time O(log num_buckets); memory O(1).

## Key Insights & Edge Cases

With `num_buckets == 1` the loop runs once and returns bucket 0 for every key — a clean invariant to sanity-check the LCG wiring. The 64-bit masking is essential: on a fixed-width machine the multiply wraps mod 2^64, and `key >> 33` extracts the high 31 bits that drive the jump distribution.
