# Solution — Subarray Sum Equals K

## Brute Force

Enumerate every start index `i` and every end index `j >= i`, accumulate the
sum of `nums[i..j]`, and increment a counter whenever it equals `k`.

```python
count = 0
for i in range(len(nums)):
    running = 0
    for j in range(i, len(nums)):
        running += nums[j]
        if running == k:
            count += 1
return count
```

- **Time:** O(n^2) — two nested loops (the inner running sum avoids a third).
- **Space:** O(1).

This is fine for small inputs but too slow when `n` approaches 2 * 10^4 and
this routine is called many times.

## Optimal Approach — Prefix Sum + Hash Map

Let `prefix[j]` be the sum of `nums[0..j]`. The sum of the subarray ending at
index `j` and starting at index `i` is:

```
sum(nums[i..j]) = prefix[j] - prefix[i-1]
```

We want this to equal `k`, i.e. `prefix[i-1] = prefix[j] - k`. So while
scanning to index `j`, the number of subarrays ending at `j` with sum `k` is
exactly **how many earlier prefix sums equal `prefix[j] - k`**.

Maintain a hash map `seen` mapping each prefix-sum value to the number of
indices where it occurred. Seed it with `{0: 1}` to represent the empty prefix
(sum `0` before any element), so subarrays that start at index `0` are counted.

```python
from collections import defaultdict

def subarraySum(nums, k):
    seen = defaultdict(int)
    seen[0] = 1          # empty prefix
    running = 0
    count = 0
    for x in nums:
        running += x
        count += seen[running - k]   # subarrays ending here with sum k
        seen[running] += 1           # record this prefix sum
    return count
```

### Why it is correct

- `running` after processing index `j` equals `prefix[j]`.
- `seen[running - k]` is the count of previous indices `i-1` (including the
  virtual index `-1` for the empty prefix) with `prefix[i-1] = running - k`.
  Each such index yields a distinct subarray `nums[i..j]` summing to `k`.
- We add to `count` **before** inserting `running`, which guarantees the
  subarray is non-empty (we never pair a prefix with itself at the same index).

### Step by step on `nums = [1, 2, 3], k = 3`

| x | running | need = running - k | seen[need] | count | seen after |
|---|---------|--------------------|------------|-------|------------|
| — | 0       | —                  | —          | 0     | {0:1}      |
| 1 | 1       | -2                 | 0          | 0     | {0:1, 1:1} |
| 2 | 3       | 0                  | 1          | 1     | {0:1,1:1,3:1} |
| 3 | 6       | 3                  | 1          | 2     | {...,6:1}  |

Result: **2** ✓ (subarrays `[1,2]` and `[3]`).

- **Time:** O(n) — single pass, O(1) expected map operations.
- **Space:** O(n) — up to `n` distinct prefix sums in the map.

## Key Insights & Edge Cases

- **Seed `{0: 1}`** is essential; forgetting it drops every subarray that
  begins at index 0.
- **Add before insert.** Updating `count` before recording the current prefix
  sum keeps subarrays non-empty and, when `k == 0`, avoids counting the
  zero-length range.
- **Negatives and zeros are handled naturally** because we rely on prefix-sum
  equality, not on a monotonic window. This is the main reason to prefer the
  hash-map approach over a sliding window here.
- **Duplicate prefix sums** are common (e.g. after a `+x, -x` pair); counting
  occurrences rather than storing a single index is what makes the count
  correct.
