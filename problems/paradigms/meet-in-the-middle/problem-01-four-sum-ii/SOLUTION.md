# 4Sum II — Solution

## Brute Force

Loop over all four index positions and count the tuples that sum to zero.

```python
count = 0
for a in nums1:
    for b in nums2:
        for c in nums3:
            for d in nums4:
                if a + b + c + d == 0:
                    count += 1
```

- **Time:** `O(n^4)` — with `n = 200` that is `1.6 * 10^9` iterations, too slow.
- **Space:** `O(1)`.

## Optimal Approach (Meet in the Middle)

The four arrays are symmetric, so split them into two independent **pairs**:
the left pair `(nums1, nums2)` and the right pair `(nums3, nums4)`.

A tuple sums to zero exactly when

```
(nums1[i] + nums2[j])  +  (nums3[k] + nums4[l])  ==  0
        left pair sum              right pair sum
```

i.e. the right pair sum must equal `-(left pair sum)`.

**Step by step**

1. Enumerate every pair sum `a + b` for `a in nums1`, `b in nums2` and store
   its frequency in a hash map `left`. This is `n^2` entries.
2. Enumerate every pair sum `c + d` for `c in nums3`, `d in nums4`. For each,
   the number of left pairs that complete a zero total is `left[-(c + d)]`.
   Add that to the answer.

```python
from collections import Counter

def fourSumCount(nums1, nums2, nums3, nums4):
    left = Counter(a + b for a in nums1 for b in nums2)
    total = 0
    for c in nums3:
        for d in nums4:
            total += left[-(c + d)]   # Counter returns 0 for missing keys
    return total
```

Why it is correct: every zero-sum tuple `(i, j, k, l)` is counted exactly
once — when the loop reaches `(c, d) = (nums3[k], nums4[l])`, the term
`left[-(c + d)]` includes precisely the `(i, j)` pairs whose sum is the
required complement, and no tuple is double counted because left and right
index sets are disjoint by construction.

- **Time:** `O(n^2)` to build `left` plus `O(n^2)` to scan the right pair =
  `O(n^2)`. For `n = 200` that is `~8 * 10^4` operations.
- **Space:** `O(n^2)` for the hash map of left pair sums.

This is the essence of MITM: `O(n^4)` search collapses to two independent
`O(n^2)` enumerations glued together by an `O(1)` hash lookup.

## Key Insights & Edge Cases

- **Count, don't dedupe.** The problem counts index tuples, so equal values at
  different indices are separate tuples. A `Counter` (multiset) — not a set —
  is essential: `left[s]` may be greater than 1.
- **Use the complement direction consistently.** Store left sums, look up
  `-(right sum)`. Storing the negation on the wrong side is a common slip but
  still works as long as you are consistent.
- **`Counter` returns 0 for missing keys**, so no explicit membership check is
  needed; a plain `dict` would need `left.get(key, 0)`.
- **Overflow is a non-issue in Python** (arbitrary precision ints); in C++/Java
  the pair sums fit in 32-bit but are safest kept in 64-bit.
- **Symmetry of the split:** any 2 + 2 grouping works. Grouping 1 + 3 would
  give `O(n)` + `O(n^3)`, which is worse — balance the halves for the best
  speedup, the guiding principle behind every MITM split.
