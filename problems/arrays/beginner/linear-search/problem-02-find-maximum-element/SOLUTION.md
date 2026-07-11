# Solution — Find the Maximum Element

## Brute Force

A naive approach: for each element, check whether it is greater than or equal to
every other element; if so, it is the maximum. This uses two nested loops.

- **Time:** O(n²) — for each of n elements you compare against all n.
- **Space:** O(1)

This is wasteful — we re-compare the same pairs repeatedly.

## Optimal Approach (Linear Search)

Treat this as a linear scan that maintains a running answer. Initialize `best` to the
first element, then walk through the rest of the array; whenever the current element
exceeds `best`, update `best`.

```python
class Solution:
    def find_max(self, nums: List[int]) -> int:
        best = nums[0]
        for value in nums[1:]:
            if value > best:
                best = value
        return best
```

**Why it is correct:** Loop invariant — after processing the first `k` elements,
`best` holds the maximum of those `k` elements. Initialization makes it true for
`k=1`. Each step either keeps `best` (current value is not larger) or replaces it with
a strictly larger value, preserving the invariant. When the loop ends, `k = n`, so
`best` is the maximum of the whole array.

**Step by step** on `[3, 41, 52, 26, 38, 57, 9, 49]`:

`best` starts at 3 → 41 → 52 → 52 → 52 → 57 → 57 → 57. Final answer: **57**.

- **Time:** O(n) — one pass, one comparison per element.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Initialize from the data, not from 0.** Starting `best = 0` breaks on all-negative
  arrays (e.g. `[-7, -3, -2]` would wrongly return 0). Start from `nums[0]` (or from
  negative infinity).
- **Single element:** returns that element — the initialization already handles it.
- **Duplicates / ties:** using `>` keeps the first maximum; `>=` keeps the last. Either
  yields the same maximum *value*.
- Finding the maximum inherently requires inspecting every element, so O(n) is optimal.
