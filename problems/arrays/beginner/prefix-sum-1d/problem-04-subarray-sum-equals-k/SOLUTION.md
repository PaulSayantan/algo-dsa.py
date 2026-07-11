# Solution — Subarray Sum Equals K

## Brute Force

Try every start index; extend the end index and accumulate the sum, counting
each time it hits `k`.

```python
def subarraySum(nums, k):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1
    return count
```

- **Time:** O(n^2).
- **Space:** O(1).

Fine for small inputs, but with `n` up to `2 * 10^4` this is ~4 * 10^8
operations in the worst case — too slow.

> Note: a sliding window will **not** work, because `nums` can contain negatives
> and zeros. Shrinking or growing the window does not change the sum
> monotonically, so there is no valid pointer-advancement rule.

## Optimal Approach (Prefix Sum, 1D + Hash Map)

Let `prefix[j]` be the sum of the first `j` elements (`prefix[0] = 0`). The sum
of the subarray covering indices `i .. j-1` is `prefix[j] - prefix[i]`. We want
this to equal `k`:

```
prefix[j] - prefix[i] = k   <=>   prefix[i] = prefix[j] - k
```

So, as we sweep `j` from left to right, the number of valid subarrays ending at
position `j` is the number of earlier prefix values equal to `prefix[j] - k`.
Keep a hash map `count[v] = how many times prefix value v has been seen so far`.

Reference implementation:

```python
from collections import defaultdict

def subarraySum(nums, k):
    count = 0
    running = 0
    seen = defaultdict(int)
    seen[0] = 1  # empty prefix: enables subarrays starting at index 0
    for x in nums:
        running += x
        count += seen[running - k]
        seen[running] += 1
    return count
```

**Why it is correct:** at each step `running` equals `prefix[j+1]`, the sum of
everything seen so far. `seen` holds the multiset of all strictly-earlier prefix
values (including the empty prefix `0`). Every earlier index `i` with
`prefix[i] = running - k` yields a subarray `nums[i..j]` summing to `k`, so we
add `seen[running - k]`. Seeding `seen[0] = 1` accounts for subarrays that start
at index 0 (where the "earlier prefix" is the empty one). We record `running`
*after* counting so a subarray must be non-empty.

**Step by step** on `nums = [1, -1, 0]`, `k = 0`:

| x  | running | need = running - k | seen[need] | count | seen after                |
|----|---------|--------------------|------------|-------|---------------------------|
| -  | 0       | -                  | -          | 0     | {0: 1}                     |
| 1  | 1       | 1                  | 0          | 0     | {0: 1, 1: 1}               |
| -1 | 0       | 0                  | 1          | 1     | {0: 2, 1: 1}               |
| 0  | 0       | 0                  | 2          | 3     | {0: 3, 1: 1}               |

Final count = 3, matching the three zero-sum subarrays.

- **Time:** O(n) — single pass, O(1) expected hash-map operations.
- **Space:** O(n) for the hash map in the worst case.

## Key Insights & Edge Cases

- The pivotal identity is `prefix[i] = prefix[j] - k`. Reframing "find a
  subarray summing to k" as "find an earlier prefix equal to a known value" is
  the reusable trick behind this whole family of problems.
- **Seed `seen[0] = 1`.** Forgetting it undercounts every subarray that begins
  at index 0. This is the single most common bug.
- **Count, don't just detect.** Use `seen[running - k]` (the frequency), not a
  boolean, because the same prefix value can occur multiple times and each
  occurrence is a distinct subarray.
- **Negatives and zeros** are handled naturally — this is exactly why prefix sum
  plus hash map beats a sliding window here.
- **Overflow:** not an issue in Python (arbitrary precision); in fixed-width
  languages use a 64-bit type for the running sum.
