# Solution — Count Occurrences of a Value

## Brute Force

There is no meaningfully worse-than-linear "brute force" here that produces the right
answer — you must look at every element to count matches. A wasteful variant would
sort the array first (`O(n log n)`) and then count a contiguous run, but sorting buys
nothing for a plain count.

- Sort-then-count: **Time** O(n log n), **Space** O(1)–O(n).

## Optimal Approach (Linear Search)

Scan the whole array once, incrementing a counter each time an element equals the
target. Unlike a "find" search, you do **not** return early — you must examine every
element to know the total.

```python
class Solution:
    def count_occurrences(self, nums: List[int], target: int) -> int:
        count = 0
        for value in nums:
            if value == target:
                count += 1
        return count
```

**Why it is correct:** Invariant — after processing the first `k` elements, `count`
equals the number of matches among them. Each element either matches (add 1) or not
(no change). After the full pass `k = n`, so `count` is the total number of
occurrences.

**Step by step** on `[1, 2, 3, 2, 4, 2, 5], target = 2`:

`count` goes 0 → 0 → 1 → 1 → 2 → 2 → 3 → 3. Final answer: **3**.

- **Time:** O(n) — a full pass is mandatory for a count.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Do not early-exit.** Counting differs from "find first": stopping at the first
  match would undercount. This is the classic mistake to avoid.
- **Empty array:** the loop never runs, so it correctly returns 0.
- **Target absent:** counter stays 0.
- **All elements match:** the count equals `len(nums)`.
- In Python you could write `nums.count(target)` or `sum(1 for v in nums if v == target)`,
  but both are still O(n) linear scans under the hood — the explicit loop makes the
  technique visible.
