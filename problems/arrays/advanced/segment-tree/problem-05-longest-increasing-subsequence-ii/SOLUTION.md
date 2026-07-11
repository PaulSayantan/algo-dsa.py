# Longest Increasing Subsequence II — Solution

## Brute Force

Classic `O(n^2)` LIS DP: `dp[i]` = longest valid subsequence ending at index `i`.

```
dp[i] = 1 + max(dp[j] for j < i if 0 < nums[i] - nums[j] <= k)   (0 if none)
```

- Time: `O(n^2)` — `~10^10` at `n = 10^5`. Too slow.
- Space: `O(n)`.

The bottleneck is the inner `max` over all earlier compatible elements. If we could
answer "best subsequence length among values in `[nums[i] - k, nums[i] - 1]`" in
`O(log n)`, the whole DP drops to `O(n log n)`.

## Optimal Approach — Range-Max Segment Tree over the Value Domain

Re-index the DP by **value** rather than by array position:

```
best[v] = length of the longest valid subsequence that ends with an element of value v
```

Process `nums` left to right (respecting subsequence order). For the current value
`x = nums[i]`, any valid predecessor must have value in `[x - k, x - 1]` (strictly
smaller, within gap `k`). So:

```
cur = 1 + max(best[v] for v in [x - k, x - 1])      (the max is 0 if empty)
best[x] = max(best[x], cur)
answer  = max(answer, cur)
```

The `max` over a contiguous **value range** and the point update to `best[x]` are
exactly a **range-max segment tree** indexed by value.

### Why it is correct

`best[v]` always reflects only elements seen **so far** (earlier in `nums`), because
we update after querying and iterate in array order — preserving subsequence order.
Querying `[x - k, x - 1]` gives the longest chain we can legally extend by appending
`x`: strictly increasing (values `< x`) and adjacent gap `<= k` (values `>= x - k`).
Adding 1 accounts for `x` itself. Taking the running `answer` max captures the global
optimum.

### Value domain / bounds

Values are in `[1, 10^5]`, so we can index the tree directly over `[1, MAX]` with
`MAX = 10^5`, or compress. The query lower bound is clamped: `max(1, x - k)`.

### Reference implementation

```python
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        MAX = max(nums)                       # value domain [1, MAX]
        size = MAX + 1                        # index by value directly
        tree = [0] * (2 * size)               # range-max segment tree, identity 0

        def update(pos: int, val: int) -> None:
            i = pos + size
            if tree[i] >= val:                # keep the best only
                return
            tree[i] = val
            i //= 2
            while i >= 1:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i //= 2

        def query(l: int, r: int) -> int:     # max over values [l, r] inclusive
            if l > r:
                return 0
            res, l, r = 0, l + size, r + size + 1
            while l < r:
                if l & 1:
                    res = max(res, tree[l]); l += 1
                if r & 1:
                    r -= 1; res = max(res, tree[r])
                l //= 2; r //= 2
            return res

        ans = 0
        for x in nums:
            best_prev = query(max(1, x - k), x - 1)
            cur = best_prev + 1
            update(x, cur)
            ans = max(ans, cur)
        return ans
```

### Complexity

- Time: `O(n log V)` where `V` is the value range (or `O(n log n)` with compression).
- Space: `O(V)` (or `O(n)` compressed).

## Key Insights & Edge Cases

- **DP indexed by value, not position.** This is the essential move: it turns the
  "best compatible predecessor" search into a *contiguous value-range* query, which a
  segment tree answers in `O(log n)`.
- **Range-max aggregate, identity 0.** Disjoint / empty windows return 0, correctly
  representing "no predecessor," so a fresh element starts a length-1 chain.
- **Clamp the lower bound** to `max(1, x - k)` (or `0` in a compressed domain) so the
  query does not read out of range; the upper bound `x - 1` enforces *strictly*
  increasing (excludes equal values, so duplicates never chain to themselves).
- **Update keeps the maximum** (`if tree[i] >= val: return`), because multiple array
  elements can share a value and we only care about the longest chain ending there.
- **`k` too small / gap too large** (Example 3): the window `[x - k, x - 1]` is empty,
  every element is its own chain, answer `1`.
- **Process in array order** and update *after* querying to respect subsequence order;
  querying against not-yet-seen elements would break the "predecessor comes earlier"
  requirement.
- If `k` were effectively infinite (`k >= MAX`), this reduces to standard LIS solvable
  by the `O(n log n)` patience-sorting method; the segment tree generalizes it to a
  bounded gap.
