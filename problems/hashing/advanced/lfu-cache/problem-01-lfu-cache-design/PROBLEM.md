# LFU Cache

**Difficulty:** Hard

**Source:** LeetCode 460 — LFU Cache

## Description

Design an LFU cache with a positive `capacity`. `get(key)` returns the value (and increments its use frequency) or `-1`. `put(key, value)` inserts or updates the key; on overflow it evicts the key with the smallest use frequency, breaking ties by least-recently-used. Both operations must run in O(1).

## Examples

### Example 1

```
Input:  cap 2; put(1,1),put(2,2),get(1)
Output: 1
```

**Explanation:** freq(1) becomes 2, freq(2) stays 1.

### Example 2

```
Input:  put(3,3) then get(2)
Output: -1
```

**Explanation:** 2 is the least-frequently-used, so it is evicted.

## Hint

value map + freq map + freq->OrderedDict buckets + minfreq; every touch bumps the frequency bucket.
