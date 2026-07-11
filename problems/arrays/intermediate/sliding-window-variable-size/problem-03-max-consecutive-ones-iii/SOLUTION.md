# Solution — Max Consecutive Ones III

## Brute Force

For every start `l`, extend `r` while the count of zeros in `nums[l..r]` stays
`<= k`; record the longest such window.

```python
def longestOnes(nums, k):
    n = len(nums)
    best = 0
    for l in range(n):
        zeros = 0
        for r in range(l, n):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                break
            best = max(best, r - l + 1)
    return best
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

## Optimal Approach (Sliding Window, variable size)

Reframe the problem: "flip at most `k` zeros to get all ones" is exactly "find the
longest window containing **at most `k` zeros**." The only state we need is a count
of zeros inside the window.

**Algorithm (longest-window flavor):**

1. Keep `left = 0` and `zeros = 0`.
2. For each `right`, if `nums[right] == 0`, increment `zeros` (grow the window).
3. **While** `zeros > k` (window invalid), if `nums[left] == 0` decrement `zeros`,
   then advance `left` (shrink).
4. The window `[left, right]` now holds `<= k` zeros; update
   `best = max(best, right - left + 1)`.

```python
def longestOnes(nums, k):
    left = 0
    zeros = 0
    best = 0
    for right, x in enumerate(nums):
        if x == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Why it is correct.** The invariant "window has at most `k` zeros" means the
window is achievable with the allowed flips. Adding `nums[right]` can push the
zero count to `k+1` at most; we then shrink from the left just until it is `<= k`
again. Because both pointers only move forward and we record the length whenever
the window is valid, we consider the widest valid window ending at each `right`.

**Trace of Example 1** (`nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`):

| right | x | zeros | shrink? | window `[l,r]` | length | best |
|------:|--:|------:|---------|----------------|-------:|-----:|
| 0 | 1 | 0 | no | [0,0] | 1 | 1 |
| 1 | 1 | 0 | no | [0,1] | 2 | 2 |
| 2 | 1 | 0 | no | [0,2] | 3 | 3 |
| 3 | 0 | 1 | no | [0,3] | 4 | 4 |
| 4 | 0 | 2 | no | [0,4] | 5 | 5 |
| 5 | 0 | 3 | yes -> drop idx0..2 (all 1s) then idx3 (a 0), zeros=2, l=4 | [4,5] | 2 | 5 |
| 6 | 1 | 2 | no | [4,6] | 3 | 5 |
| 7 | 1 | 2 | no | [4,7] | 4 | 5 |
| 8 | 1 | 2 | no | [4,8] | 5 | 5 |
| 9 | 1 | 2 | no | [4,9] | 6 | 6 |
| 10 | 0 | 3 | yes -> drop idx4 (0), zeros=2, l=5 | [5,10] | 6 | 6 |

Result: `6`.

- **Time:** `O(n)` — each index enters and leaves the window at most once.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **`k = 0`** means "no zeros allowed" — the window becomes the longest run of
  consecutive `1`s (and returns `0` when there are none, as in Example 3).
- This is the canonical "at most `k` bad elements" window; the same shape solves
  "longest subarray with at most `k` of some property."
- Only decrement `zeros` when the element leaving (`nums[left]`) is actually a
  zero — a frequent off-by-one bug.
- A neat one-liner variant never shrinks below the best-so-far width (uses `if`
  instead of `while`), returning `n - left` at the end; but the explicit `while`
  version above is clearer to reason about.
