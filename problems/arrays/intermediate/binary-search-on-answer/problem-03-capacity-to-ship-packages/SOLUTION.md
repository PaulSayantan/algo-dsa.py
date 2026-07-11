# Capacity To Ship Packages Within D Days — Solution

## Brute Force

Try every candidate capacity `c` from `max(weights)` (the smallest capacity that can even hold the heaviest single package) up to `sum(weights)` (a capacity that ships everything in one day). For each `c`, greedily count how many days it takes and return the first `c` that fits within `days`.

```python
def shipWithinDays(weights, days):
    for c in range(max(weights), sum(weights) + 1):
        if days_needed(weights, c) <= days:
            return c
```

- **Time:** O(sum(weights) · n) — up to `sum(weights)` candidates, each an O(n) day count.
- **Space:** O(1).

With `sum(weights)` up to `5 * 10^4 * 500 = 2.5 * 10^7`, scanning every capacity is wasteful.

## Optimal Approach (Binary Search on Answer)

**Answer range.** A capacity must be at least `max(weights)`, otherwise the heaviest package never fits on any day. A capacity of `sum(weights)` trivially ships everything in a single day. So the answer lies in `[max(weights), sum(weights)]`.

**Feasibility predicate.** Given a capacity `c`, greedily fill each day: keep adding packages in order until the next one would overflow `c`, then start a new day. Count the days used.

```python
def days_needed(weights, cap):
    days, cur = 1, 0
    for w in weights:
        if cur + w > cap:      # would overflow → start a new day
            days += 1
            cur = 0
        cur += w
    return days

feasible(c) = days_needed(weights, c) <= days
```

**Monotonicity.** A larger capacity can carry at least as much per day, so `days_needed` is non-increasing in `c`. The predicate flips once from `False` to `True`: `F F ... F T T ... T`. We want the **first** `True` — the smallest capacity that ships within `days` days.

```python
def shipWithinDays(weights, days):
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(weights, mid) <= days:  # feasible → try smaller
            hi = mid
        else:                                   # too small → need bigger ship
            lo = mid + 1
    return lo
```

**Why it is correct.** The invariant is that the optimal capacity is always within `[lo, hi]`. If `mid` is feasible, the answer is `mid` or smaller, so `hi = mid`. If `mid` is infeasible, the answer must be strictly larger, so `lo = mid + 1`. The window shrinks every step; when `lo == hi`, that single value is the least feasible capacity.

The greedy `days_needed` is optimal: since packages cannot be reordered, packing each day as full as possible (without exceeding `c`) minimizes the number of days for that fixed capacity — moving any package to a later day can only increase the day count.

**Step-by-step for `weights = [3,2,2,4,1,4], days = 3`** (range `[4, 16]`):

| lo | hi | mid | days_needed(mid) | <= 3? | action |
|----|----|-----|------------------|-------|--------|
| 4  | 16 | 10  | [3,2,2],[4,1,4] = 2 | yes | hi = 10 |
| 4  | 10 | 7   | [3,2,2],[4,1],[4] = 3 | yes | hi = 7 |
| 4  | 7  | 5   | [3,2],[2],[4,1],[4] = 4 | no | lo = 6 |
| 6  | 7  | 6   | [3,2],[2,4],[1,4] = 3 | yes | hi = 6 |

`lo == hi == 6` → return `6`. Correct.

- **Time:** O(n · log(sum(weights))).
- **Space:** O(1).

## Key Insights & Edge Cases

- **Lower bound must be `max(weights)`, not `0` or `1`:** any capacity below the heaviest package makes shipping impossible, so the search would never find a feasible value if you start too low.
- **Order is fixed:** because packages cannot be reordered, the greedy fill is both correct and simple. If reordering were allowed, this would become a bin-packing (NP-hard) problem.
- **Single day (`days == 1`):** the answer is exactly `sum(weights)`, and the search converges there since no smaller capacity is feasible.
- **`days == len(weights)`:** every package can get its own day, so the answer equals `max(weights)`.
- **This is the same shape as Split Array Largest Sum** (Problem 5): "minimize the maximum group sum with at most `k` contiguous groups." Recognizing that equivalence lets you reuse the exact same template.
