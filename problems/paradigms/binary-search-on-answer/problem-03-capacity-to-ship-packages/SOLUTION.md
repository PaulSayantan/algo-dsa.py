# Solution - Capacity To Ship Packages Within D Days

## Brute Force

Try every capacity from `max(weights)` upward and return the first one that ships
within `days` days.

```python
def days_needed(cap):
    d, cur = 1, 0
    for w in weights:
        if cur + w > cap:
            d += 1
            cur = w
        else:
            cur += w
    return d

for cap in range(max(weights), sum(weights) + 1):
    if days_needed(cap) <= days:
        return cap
```

- **Time:** `O((sum - max) * n)` — one greedy pass per candidate capacity.
- **Space:** `O(1)`.

The capacity range can be up to `sum(weights) ≈ 2.5 * 10^7`, so a linear scan is
far too slow.

## Optimal Approach (Binary Search on Answer)

The answer lives in `[max(weights), sum(weights)]`:

- **Lower bound `max(weights)`:** the capacity must fit the single heaviest
  package, or that package can never be loaded.
- **Upper bound `sum(weights)`:** a capacity equal to the total weight ships
  everything in one day.

Monotonicity: **`days_needed(cap)` is non-increasing as `cap` grows.** A bigger
ship never needs more days. So `check(cap) = (days_needed(cap) <= days)` has the
pattern `F F ... F T T ... T`; we want the **first** `True`.

```python
def shipWithinDays(self, weights: List[int], days: int) -> int:
    def days_needed(cap: int) -> int:
        d, cur = 1, 0
        for w in weights:
            if cur + w > cap:   # start a new day with this package
                d += 1
                cur = w
            else:
                cur += w
        return d

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(mid) <= days:   # feasible → try a smaller ship
            hi = mid
        else:                          # too small → need more capacity
            lo = mid + 1
    return lo
```

### Why it is correct

`days_needed` uses the greedy rule "pack as much as fits, then start a new day,"
which is optimal for a fixed capacity because packages must ship in order and
adding a package to the current day is never worse than deferring it. Increasing
the capacity can only let more (or equal) weight fit per day, so the day count
cannot increase — the predicate is monotonic with a single flip. The "first True"
binary-search template converges on that boundary.

### Step-by-step (weights = [1..10], days = 5)

Range `[10, 55]`.

| lo | hi | mid | days_needed(mid) | <= 5 | action  |
|----|----|-----|------------------|------|---------|
| 10 | 55 | 32  | 2                | yes  | hi = 32 |
| 10 | 32 | 21  | 3                | yes  | hi = 21 |
| 10 | 21 | 15  | 5                | yes  | hi = 15 |
| 10 | 15 | 12  | 6                | no   | lo = 13 |
| 13 | 15 | 14  | 6                | no   | lo = 15 |
| 15 | 15 | —   | —                | stop | ret 15  |

Answer: `15`.

- **Time:** `O(n * log(sum(weights)))` — an `O(n)` greedy check per iteration.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **The lower bound must be `max(weights)`, not `1`.** A capacity below the
  heaviest package is infeasible for *any* number of days, and the greedy checker
  would loop a package into its own day forever conceptually — starting the search
  at `max(weights)` sidesteps that entirely.
- **Same family as Koko / Split Array Largest Sum:** all are "minimize the
  maximum load so that a monotonic count stays within budget."
- **`days == 1`** forces the answer to `sum(weights)`; **`days == len(weights)`**
  (or more) forces `max(weights)`. Both fall out naturally.
- **Greedy check correctness** relies on the fixed package order — this is *not*
  the bin-packing / subset problem, so no NP-hardness sneaks in.
