# Minimum Size Subarray Sum — Solution

## Brute Force

Try every start index `i` and extend `j` until the running sum reaches `target`,
recording the shortest qualifying length.

```python
best = float("inf")
for i in range(len(nums)):
    s = 0
    for j in range(i, len(nums)):
        s += nums[j]
        if s >= target:
            best = min(best, j - i + 1)
            break
return 0 if best == float("inf") else best
```

- **Time:** O(n^2) in the worst case.
- **Space:** O(1).

A prefix-sum + binary-search variant achieves O(n log n): build prefix sums, then for
each start use binary search to find the earliest end whose prefix difference is
`>= target`. But Sliding Window does even better in O(n).

## Optimal Approach (Sliding Window)

Because every element is **positive**, extending the window strictly increases the
sum and shrinking it strictly decreases the sum. This monotonicity is what makes the
two-pointer window valid.

1. Initialize `left = 0`, `window_sum = 0`, `best = infinity`.
2. For each `right` from `0` to `n - 1`:
   - Add `nums[right]` to `window_sum` (grow the window).
   - **While** `window_sum >= target`: the window `[left, right]` qualifies. Record
     `best = min(best, right - left + 1)`, then subtract `nums[left]` and increment
     `left` to try a shorter window.
3. Return `best` if it changed, otherwise `0`.

**Why it is correct:** For each right endpoint we shrink from the left as much as
possible while still meeting the target, so we find the *shortest* qualifying window
ending at every `right`. The overall minimum across all right endpoints is the global
answer. Positivity guarantees that once the sum drops below `target` after shrinking,
extending `left` further can only keep it below — so we can safely stop shrinking.

```python
left = 0
window_sum = 0
best = float("inf")
for right in range(len(nums)):
    window_sum += nums[right]
    while window_sum >= target:
        best = min(best, right - left + 1)
        window_sum -= nums[left]
        left += 1
return 0 if best == float("inf") else best
```

- **Time:** O(n) — `left` and `right` each advance at most `n` times total, so the
  inner `while` is amortized O(1) per step.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Positivity is essential.** With negative numbers the sum is no longer monotonic,
  so this exact window fails; you would need prefix sums plus a monotonic deque
  (LeetCode 862, the "hard" generalization).
- **Shrink *while* qualifying, not just *if*.** A single element could exceed a small
  `target`, so the `while` may run several times in one step.
- **No qualifying subarray:** keep a sentinel (`infinity`) and convert it to `0` at
  the end. Do not initialize `best = 0`.
- **Answer found early:** if a single element already `>= target`, the window length
  is 1 — the minimum possible.
- **Sum magnitude:** with `target` up to `10^9` and values up to `10^4`, sums stay
  well within 64-bit range.
