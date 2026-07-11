# Solution — Maximum Sum Subarray of Size K

## Brute Force

For every possible starting index `i` from `0` to `n - k`, sum the `k` elements
`nums[i..i+k-1]` and track the maximum.

```python
best = float("-inf")
for i in range(len(nums) - k + 1):
    best = max(best, sum(nums[i:i + k]))
return best
```

Each window sum re-adds `k` elements, and there are about `n - k + 1` windows.

- **Time:** O(n·k)
- **Space:** O(1)

## Optimal Approach (Sliding Window, Fixed Size)

The key observation: two adjacent windows overlap in `k - 1` elements. Going from the
window starting at `i` to the one starting at `i + 1`, only one element leaves
(`nums[i]`) and one element enters (`nums[i + k]`). So we can update the running sum
in O(1) instead of recomputing it.

1. Compute `window_sum = sum(nums[0..k-1])` for the first window. Set `best = window_sum`.
2. For each `right` from `k` to `n - 1`:
   - Add the entering element: `window_sum += nums[right]`.
   - Remove the leaving element: `window_sum -= nums[right - k]`.
   - Update `best = max(best, window_sum)`.
3. Return `best`.

```python
def max_sum_subarray(nums: List[int], k: int) -> int:
    window_sum = sum(nums[:k])
    best = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)
    return best
```

**Why it is correct:** After processing index `right`, `window_sum` holds exactly the
sum of `nums[right-k+1 .. right]` — a valid length-`k` window — because we added every
element as it entered and subtracted every element as it left. We take the max over
every window that ever appears, and every length-`k` window appears exactly once, so
the answer is the global maximum.

**Step by step** on `nums = [2, 1, 5, 1, 3, 2], k = 3`:

1. Initial window `[2,1,5]` → `window_sum = 8`, `best = 8`.
2. `right=3`: `+nums[3]=1`, `-nums[0]=2` → `8+1-2 = 7` (window `[1,5,1]`), `best = 8`.
3. `right=4`: `+nums[4]=3`, `-nums[1]=1` → `7+3-1 = 9` (window `[5,1,3]`), `best = 9`.
4. `right=5`: `+nums[5]=2`, `-nums[2]=5` → `9+2-5 = 6` (window `[1,3,2]`), `best = 9`.

Answer: `9`.

- **Time:** O(n) — every element is added once and removed at most once.
- **Space:** O(1) — a single running sum and the best-so-far.

## Key Insights & Edge Cases

- **Initialize `best` from the first window, not `0`.** With all-negative inputs (see
  Example 3), starting at `0` would wrongly return `0`. Seed `best` with the first
  window sum (or `float("-inf")`).
- **`k == len(nums)`:** there is exactly one window (the whole array); the loop body
  never runs and `best` is that single sum — correct.
- **`k == 1`:** the answer degenerates to the maximum single element, which the
  pattern still handles.
- **The O(1) update** `window_sum += nums[right] - nums[right - k]` is the heart of the
  technique; forgetting the subtraction is the classic bug.
