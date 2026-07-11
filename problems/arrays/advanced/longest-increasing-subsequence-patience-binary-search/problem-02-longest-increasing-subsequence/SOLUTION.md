# Solution — Longest Increasing Subsequence

## Brute Force

Enumerate every subsequence and keep the longest increasing one. There are
`2^n` subsequences, so this is `O(2^n)` time — hopeless beyond ~20 elements.

A standard improvement is the `O(n^2)` dynamic program: let `dp[i]` be the
length of the longest increasing subsequence that **ends at index `i`**.
Then `dp[i] = 1 + max(dp[j])` over all `j < i` with `nums[j] < nums[i]`
(or `1` if none). The answer is `max(dp)`.

- `O(n^2)` time, `O(n)` space. Fine for `n <= 2500`, but the follow-up wants
  `O(n log n)`.

## Optimal Approach (patience sorting + binary search)

Maintain an array `tails`, where `tails[i]` is the **smallest possible tail
value** of any strictly increasing subsequence of length `i + 1` found so far.

Key fact: `tails` is always sorted in strictly increasing order. That is the
invariant that lets us binary search.

Process each `x = nums[i]` left to right:

1. Binary search `tails` for the **leftmost** index `pos` with
   `tails[pos] >= x` (a lower-bound / `bisect_left`).
2. If `pos == len(tails)`, `x` is larger than every current tail, so it
   extends the longest run: append `x` (open a new patience pile).
3. Otherwise overwrite `tails[pos] = x`. We just found an increasing
   subsequence of length `pos + 1` with a smaller (or equal-position) tail,
   which can only help future extensions.

The answer is `len(tails)` at the end.

### Why it is correct

- **Sorted invariant.** `tails` starts empty. Each step either appends a value
  strictly larger than the last element (keeps it sorted) or replaces the
  first element `>= x` with `x`, which is `<=` its old value and still
  `>` the previous slot (since that slot was `< x`, otherwise the search would
  have stopped earlier). So the array stays strictly increasing.
- **`tails[i]` is the minimal tail of a length-`(i+1)` subsequence.** By using
  the smallest achievable tail for each length, we maximize the chance that a
  future element can extend it. This greedy choice never sacrifices an optimum.
- **Length = LIS length.** Whenever we append, we have exhibited an increasing
  subsequence one longer than before (its tail is `x`, its prefix is witnessed
  by the values that filled the earlier slots at the time they were set).
  Replacements never change the length. So the final length equals the LIS
  length. (Note: the `tails` array itself is generally *not* a valid LIS — see
  the reconstruction note below.)

Use `bisect_left` for **strictly** increasing subsequences. For a
non-decreasing variant (longest *non-decreasing* subsequence), use
`bisect_right` instead.

### Reference implementation

```python
import bisect

def lengthOfLIS(self, nums: List[int]) -> int:
    tails: List[int] = []
    for x in nums:
        pos = bisect.bisect_left(tails, x)   # leftmost tails[pos] >= x
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)
```

- **Time:** `O(n log n)` — `n` iterations, each doing one `O(log n)` binary
  search.
- **Space:** `O(n)` for `tails`.

### Reconstructing the actual subsequence

`tails` gives only the length. To recover one witnessing subsequence, keep two
extra arrays as you go:

- `idx_at_len[L]` = index in `nums` of the element currently sitting at
  `tails[L]`.
- `parent[i]` = index in `nums` of the predecessor chosen for `nums[i]`
  (the element at `tails[pos - 1]` when `nums[i]` was placed at position
  `pos`), or `-1` if `pos == 0`.

After processing, start from `idx_at_len[len(tails) - 1]` and follow `parent`
pointers backward, then reverse.

```python
def reconstruct_lis(nums):
    tails_idx = []          # tails_idx[L] = index of smallest tail for length L+1
    parent = [-1] * len(nums)
    for i, x in enumerate(nums):
        # binary search over VALUES nums[tails_idx[..]] for leftmost >= x
        lo, hi = 0, len(tails_idx)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[tails_idx[mid]] >= x:
                hi = mid
            else:
                lo = mid + 1
        pos = lo
        parent[i] = tails_idx[pos - 1] if pos > 0 else -1
        if pos == len(tails_idx):
            tails_idx.append(i)
        else:
            tails_idx[pos] = i
    # walk parent pointers from the last pile's index
    seq, k = [], tails_idx[-1]
    while k != -1:
        seq.append(nums[k])
        k = parent[k]
    return seq[::-1]
```

## Key Insights & Edge Cases

- **`tails` is not the subsequence.** Its values can come from positions that
  are out of order; only its *length* is meaningful. Reconstruction needs the
  parent-pointer trick above.
- **Duplicates / strictness.** `[7,7,7]` → 1. `bisect_left` ensures an equal
  value overwrites rather than extends, enforcing strict increase.
- **Single element / empty.** A one-element array returns 1; an empty array
  (outside the constraints here) returns 0 naturally.
- **Negatives** are handled without any special casing.
- **Dilworth connection.** The number of patience piles (= LIS length) also
  equals the minimum number of strictly decreasing... more precisely, by
  Dilworth's theorem the minimum number of non-increasing subsequences needed
  to cover the array equals the length of the longest strictly increasing
  subsequence. Patience sorting realizes this: each pile is non-increasing and
  the pile count is minimized.
