# Solution — Longest Increasing Subsequence

## Brute Force (Dynamic Programming)

Let `dp[i]` be the length of the longest strictly increasing subsequence **ending at index `i`**.
Then `dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])`, defaulting to 1. The answer is
`max(dp)`.

```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

- **Time:** `O(n^2)` — nested loops.
- **Space:** `O(n)`.

Fine for `n = 2500`, but it does not meet the `O(n log n)` target and does not scale.

## Optimal Approach — Patience Sorting + Lower Bound (bisect)

Maintain an array `tails`, where `tails[k]` is the **smallest possible tail value** of any strictly
increasing subsequence of length `k + 1` seen so far. Key facts:

- `tails` is always **strictly increasing** (sorted), so we can binary-search it.
- Its **length** equals the length of the current LIS.

Process each `num` left to right. Find the **lower bound** of `num` in `tails` (the first index `i`
with `tails[i] >= num`):

- If `i == len(tails)`, `num` extends the best subsequence → **append** it (`tails` grows by 1).
- Otherwise, `num` can form a length-`(i+1)` subsequence with a **smaller (or equal) tail** than the
  current `tails[i]`, so **overwrite** `tails[i] = num` to keep tails as small as possible.

```python
from bisect import bisect_left

def lengthOfLIS(nums):
    tails = []
    for num in nums:
        i = bisect_left(tails, num)   # lower bound: first tails[i] >= num
        if i == len(tails):
            tails.append(num)         # num extends the LIS
        else:
            tails[i] = num            # num gives a smaller tail for that length
    return len(tails)
```

Hand-rolled lower bound (identical to `bisect_left`):

```python
def lower_bound(tails, x):        # first index i with tails[i] >= x
    lo, hi = 0, len(tails)
    while lo < hi:
        mid = (lo + hi) // 2
        if tails[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

### Why lower bound (and why *strictly* increasing)

We want a **strictly** increasing subsequence, so a value equal to an existing tail cannot extend
that subsequence — it must **replace** the equal tail (shortening nothing, but never appending on a
duplicate). Lower bound (`bisect_left`) returns the position of the first element `>= num`, so an
equal element maps onto itself and is overwritten rather than appended. That is exactly what keeps
duplicates from inflating the length (see Example 3).

> If the problem asked for the *non-decreasing* longest subsequence, you would switch to **upper
> bound** (`bisect_right`) so equal values *can* extend the run. The choice of bound literally
> encodes "strict" vs "non-strict."

### Why the result length is correct

`tails` never shrinks; it grows by exactly one each time a `num` is strictly greater than every
current tail, which happens iff `num` can extend the longest run found so far. Overwrites keep each
length's tail minimal, which maximizes the chance that future elements can extend. A standard
exchange argument shows `len(tails)` equals the true LIS length at every step. (Note: `tails` itself
is **not** necessarily a valid subsequence of `nums` — only its *length* is meaningful.)

### Step-by-step on `nums = [10, 9, 2, 5, 3, 7, 101, 18]`

| num | lower bound in tails | action           | tails after   |
|-----|----------------------|------------------|---------------|
| 10  | 0 (empty)            | append           | [10]          |
| 9   | 0 (`10 >= 9`)        | overwrite idx 0  | [9]           |
| 2   | 0 (`9 >= 2`)         | overwrite idx 0  | [2]           |
| 5   | 1 (past end)         | append           | [2, 5]        |
| 3   | 1 (`5 >= 3`)         | overwrite idx 1  | [2, 3]        |
| 7   | 2 (past end)         | append           | [2, 3, 7]     |
| 101 | 3 (past end)         | append           | [2, 3, 7, 101]|
| 18  | 3 (`101 >= 18`)      | overwrite idx 3  | [2, 3, 7, 18] |

Final `len(tails) = 4`. ✓

- **Time:** `O(n log n)` — one lower-bound search per element.
- **Space:** `O(n)` for `tails`.

## Key Insights & Edge Cases

- **`i == len(tails)` means "past the end" → append.** This is the lower bound returning `n`, the
  signal that `num` is greater than every current tail. Treat it the same way as the insertion-index
  cases in Problem 1.
- **All-equal input** (Example 3, `[7,7,...]`): every `7` has lower bound `0` and overwrites
  `tails[0]`; the array never grows past length 1, giving the correct answer `1`. This is where
  `bisect_left` (strict) vs `bisect_right` (non-strict) makes a visible difference.
- **`tails` is a helper, not the actual subsequence.** After processing, `tails` may contain values
  that never co-occur in one real subsequence; only its length is the answer. Recovering the actual
  subsequence needs extra parent-pointer bookkeeping.
- **Single element / already sorted / reverse sorted** all fall out correctly: sorted ascending
  appends every time (length `n`); reverse sorted overwrites `tails[0]` every time (length 1).
- The array is guaranteed non-empty, so `len(tails) >= 1` always holds by the end.
