# Solution — Richest Customer Wealth

## Brute Force

A "two-phase" approach: first compute and store every customer's wealth in a separate
list, then do a second pass (or call `max`) to find the largest. This works but uses an
extra O(m) array and two passes.

- **Time:** O(m · n) — you still sum every cell once.
- **Space:** O(m) for the list of per-customer sums.

## Optimal Approach (Linear Search)

Combine both phases into a single linear scan over the rows. For each customer, sum
their row, then compare against a running maximum — exactly the "best so far" pattern
from finding a maximum, applied to computed row sums instead of raw elements.

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        best = 0
        for row in accounts:
            wealth = sum(row)
            if wealth > best:
                best = wealth
        return best
```

**Why it is correct:** Invariant — after processing the first `k` customers, `best`
holds the maximum wealth among them. Since every wealth is `>= 1` (constraints give
`accounts[i][j] >= 1` and `n >= 1`), initializing `best = 0` is safe: the first real
customer will always exceed it. Each iteration updates `best` only when a richer
customer appears, so after all rows `best` is the global maximum.

**Step by step** on `[[1, 5], [7, 3], [3, 5]]`:

- Row `[1,5]` → wealth 6, `best` = 6
- Row `[7,3]` → wealth 10 > 6, `best` = 10
- Row `[3,5]` → wealth 8, `best` stays 10

Final answer: **10**.

- **Time:** O(m · n) — every cell is visited exactly once (unavoidable; you must read
  all the money to sum it).
- **Space:** O(1) — only the running maximum.

## Key Insights & Edge Cases

- This is a **2D linear search**: the outer loop scans customers, the inner sum scans
  banks. The "best so far" accumulator is the same idea as finding an array maximum.
- **`best = 0` is safe here** only because all values are positive. In a general
  max-subarray-sum-style problem with possible negatives you would initialize from the
  first computed value or `float("-inf")`.
- **Single customer / single bank:** handled naturally (loop runs once, returns that
  wealth).
- One-liner: `return max(sum(row) for row in accounts)` — still an O(m·n) linear scan,
  just expressed with built-ins.
