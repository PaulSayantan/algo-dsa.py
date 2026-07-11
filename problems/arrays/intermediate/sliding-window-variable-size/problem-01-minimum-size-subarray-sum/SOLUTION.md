# Solution — Minimum Size Subarray Sum

## Brute Force

Try every start index `l`, then extend `r` forward accumulating the sum until it
reaches `target`, recording the length `r - l + 1`.

```python
def minSubArrayLen(target, nums):
    n = len(nums)
    best = float("inf")
    for l in range(n):
        s = 0
        for r in range(l, n):
            s += nums[r]
            if s >= target:
                best = min(best, r - l + 1)
                break
    return 0 if best == float("inf") else best
```

- **Time:** `O(n^2)` — for each of `n` starts we may scan to the end.
- **Space:** `O(1)`.

A prefix-sum + binary-search approach gets this to `O(n log n)`, but the sliding
window is simpler and faster.

## Optimal Approach (Sliding Window, variable size)

Because all elements are **positive**, the window sum is **monotonic** in the
window bounds: pushing `right` forward only increases the sum, and pulling `left`
forward only decreases it. That monotonicity means we never need to re-examine a
start index — the classic condition for a two-pointer window.

**Algorithm (shortest-window flavor):**

1. Keep a running `window_sum = 0` and `left = 0`.
2. For each `right`, add `nums[right]` to `window_sum` (grow the window).
3. **While** `window_sum >= target`, the window is valid: record
   `best = min(best, right - left + 1)`, then subtract `nums[left]` and advance
   `left` (shrink) to search for an even shorter valid window.
4. After the loop, return `best` (or `0` if it was never updated).

```python
def minSubArrayLen(target, nums):
    left = 0
    window_sum = 0
    best = float("inf")
    for right, x in enumerate(nums):
        window_sum += x
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if best == float("inf") else best
```

**Why it is correct.** When we stop shrinking, the window is the shortest valid
window that *ends at or before* `right` and *starts at* the current `left`; any
shorter window ending at `right` would have sum `< target`. Because we consider
every `right` and shrink maximally each time, we examine every candidate shortest
window exactly once. Positivity guarantees that once shrinking makes the sum drop
below `target`, extending `left` further can never make it valid again for this
`right`, so stopping is safe.

**Trace of Example 1** (`target = 7`, `nums = [2,3,1,2,4,3]`):

| right | x | window | sum | action | best |
|------:|--:|--------|----:|--------|-----:|
| 0 | 2 | [2] | 2 | grow | inf |
| 1 | 3 | [2,3] | 5 | grow | inf |
| 2 | 1 | [2,3,1] | 6 | grow | inf |
| 3 | 2 | [2,3,1,2] | 8 | valid: len 4; shrink -> [3,1,2] sum 6 | 4 |
| 4 | 4 | [3,1,2,4] | 10 | valid: len 4; shrink -> [1,2,4] sum 7; len 3; shrink -> [2,4] sum 6 | 3 |
| 5 | 3 | [2,4,3] | 9 | valid: len 3; shrink -> [4,3] sum 7; len 2; shrink -> [3] sum 3 | 2 |

Result: `2`.

- **Time:** `O(n)` — `right` advances `n` times and `left` advances at most `n`
  times total, so the pointers do `O(n)` combined work.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Monotonicity is the enabler.** This exact window trick works only because the
  values are positive. With negative numbers the sum is no longer monotonic and
  you would need prefix sums + a deque or other techniques.
- **No qualifying subarray:** if even the total sum is `< target`, `best` stays
  `inf` — return `0`.
- **Single element already big enough:** the `while` shrinks down to length `1`
  correctly (Example 2).
- **Use `>=`, not `>`**, when checking against `target`, and record the length
  *before* shrinking so you don't miss the boundary window.
- Advancing `left` past `right` cannot happen here because once `left == right+1`
  the window is empty with sum `0 < target`, ending the inner loop.
