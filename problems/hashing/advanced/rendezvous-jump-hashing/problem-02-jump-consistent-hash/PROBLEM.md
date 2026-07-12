# Jump Consistent Hash

**Difficulty:** Medium

**Source:** Classic — Lamping & Veach, 'A Fast, Minimal Memory, Consistent Hash Algorithm'

## Description

Implement `jumpConsistentHash(key, num_buckets)` from the Lamping & Veach paper: given a 64-bit integer `key` and a positive bucket count `num_buckets`, return the bucket in `[0, num_buckets)` the key maps to. The algorithm advances a linear-congruential generator seeded by the key (multiplier constant `2862933555777941757`) and jumps forward while the probabilistic test says the key stays put. It uses O(1) memory and is fully deterministic.

## Examples

### Example 1

```
Input:  key=0, num_buckets=1
Output: 0
```

**Explanation:** With a single bucket every key maps to bucket 0.

## Hint

b=-1, j=0; while j < num_buckets: b=j; key = key*2862933555777941757 + 1 (mod 2^64); j = floor((b+1) * 2^31 / ((key >> 33) + 1)). Return b.
