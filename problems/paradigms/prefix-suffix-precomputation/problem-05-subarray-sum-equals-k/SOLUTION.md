# Solution — Subarray Sum Equals K

## Brute Force

Try every start index, extend to every end index, and accumulate the running sum
(so the inner loop is O(1) per step rather than re-summing).

```python
def subarraySum(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]        # sum of nums[i..j]
            if s == k:
                count += 1
    return count
```

- **Time:** O(n^2) — two nested loops over start/end.
- **Space:** O(1).

With `n` up to `2 * 10^4`, `n^2` is up to `4 * 10^8` — borderline-to-too-slow. We
want O(n).

### Why not a sliding window?

Sliding window requires that growing the window monotonically changes the sum. Since
`nums` can contain negatives and zeros, adding an element can *decrease* the sum, so
you cannot decide when to shrink. Prefix sums + a hash map handle negatives cleanly.

## Optimal Approach (Prefix Sums + Hash Map)

Let `prefix[t]` be the sum of the first `t` elements (`prefix[0] = 0`). A subarray
`nums[i..j]` sums to `k` exactly when

```
prefix[j+1] - prefix[i] == k     <=>     prefix[i] == prefix[j+1] - k
```

So while scanning and maintaining the running prefix sum `cur = prefix[j+1]`, the
number of valid subarrays *ending at index `j`* is the number of earlier prefix
values equal to `cur - k`. Keep a hash map `seen` mapping each prefix-sum value to
**how many times** it has occurred so far.

```python
from collections import defaultdict

def subarraySum(nums, k):
    seen = defaultdict(int)
    seen[0] = 1          # empty prefix: enables subarrays starting at index 0
    cur = 0
    count = 0
    for x in nums:
        cur += x                    # cur is now prefix sum up to current index
        count += seen[cur - k]      # add subarrays ending here that sum to k
        seen[cur] += 1              # record this prefix sum for future indices
    return count
```

**Why it is correct.** When we reach the end index `j` with running sum
`cur = prefix[j+1]`, every earlier position `i` with `prefix[i] == cur - k` yields a
subarray `nums[i..j]` summing to `k`. `seen[cur - k]` counts exactly those positions.
The initialization `seen[0] = 1` accounts for the empty prefix, so a subarray that
starts at index `0` (i.e. `prefix[i] = prefix[0] = 0`) is counted. We record `cur`
*after* querying, so a subarray must be non-empty (an index cannot pair with itself).

**Step by step** on `nums = [1, -1, 0]`, `k = 0`:

| x  | cur | need = cur - k | seen[need] | count | seen after |
|----|-----|----------------|------------|-------|------------|
| —  | 0   | —              | —          | 0     | {0:1} |
| 1  | 1   | 1              | 0          | 0     | {0:1, 1:1} |
| -1 | 0   | 0              | 1          | 1     | {0:2, 1:1} |
| 0  | 0   | 0              | 2          | 3     | {0:3, 1:1} |

Result: `3` — matching `[1,-1]`, `[1,-1,0]`, `[0]`.

- **Time:** O(n) — single pass, O(1) expected hash-map operations.
- **Space:** O(n) for the hash map in the worst case (all distinct prefix sums).

## Key Insights & Edge Cases

- The core identity is the same `prefix[j+1] - prefix[i]` used in Range Sum Query,
  but here we **invert the search**: instead of asking "what is the sum of a given
  range?", we ask "how many earlier prefixes make this range equal `k`?" — answered
  by a hash map rather than a subtraction.
- **`seen[0] = 1` is essential.** Forget it and you miss every subarray that starts at
  index 0.
- **Insert `cur` after the query.** Querying first guarantees non-empty subarrays and
  prevents an element from matching itself when `k = 0`.
- Handles **negatives and zeros** correctly — the whole reason we prefer this over a
  sliding window. Duplicate prefix sums (common with zeros) are why the map stores
  *counts*, not just presence.
- This counts subarrays; a closely related variant (LeetCode 325 / "longest subarray
  sum k") stores the **first index** of each prefix sum instead of a count to recover
  lengths.
