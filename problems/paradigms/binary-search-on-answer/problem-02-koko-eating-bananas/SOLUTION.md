# Solution - Koko Eating Bananas

## Brute Force

Try every speed from `1` upward and return the first that finishes in time.

```python
def hours_needed(k):
    return sum((p + k - 1) // k for p in piles)   # ceil division

for k in range(1, max(piles) + 1):
    if hours_needed(k) <= h:
        return k
```

- **Time:** `O(max(piles) * n)` — up to `max(piles)` candidate speeds, each
  costing `O(n)` to evaluate.
- **Space:** `O(1)`.

With `piles[i]` up to `10^9`, scanning every speed is far too slow.

## Optimal Approach (Binary Search on Answer)

The answer is a speed `k` in the range `[1, max(piles)]`. Speed `1` might need a
huge number of hours; speed `max(piles)` clears each pile in exactly one hour, so
it needs `n` hours, and `h >= n` is guaranteed by the constraints — meaning the
top of the range is always feasible.

Key monotonicity: **`hours_needed(k)` is non-increasing as `k` grows.** Faster
eating never costs more hours. Therefore `check(k) = (hours_needed(k) <= h)` has
the pattern `F F ... F T T ... T`, and we want the **first** `True`.

```python
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def hours_needed(k: int) -> int:
        return sum((p + k - 1) // k for p in piles)  # sum of ceil(p / k)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:   # feasible → try slower (smaller k)
            hi = mid
        else:                        # too slow → must eat faster
            lo = mid + 1
    return lo
```

### Why it is correct

`ceil(p / k)` is a non-increasing step function of `k` for each pile, so their
sum `hours_needed(k)` is non-increasing. Once a speed is fast enough to finish
within `h`, every faster speed also finishes within `h`. That gives a single
`False → True` boundary, exactly what the "first True" template locates. The loop
invariant "the smallest feasible speed lies in `[lo, hi]`" holds throughout, and
the interval halves each step until `lo == hi`.

### Step-by-step (piles = [3, 6, 7, 11], h = 8)

Range `[1, 11]`.

| lo | hi | mid | hours(mid)         | <= 8 | action  |
|----|----|-----|--------------------|------|---------|
| 1  | 11 | 6   | 1+1+2+2 = 6        | yes  | hi = 6  |
| 1  | 6  | 3   | 1+2+3+4 = 10       | no   | lo = 4  |
| 4  | 6  | 5   | 1+2+2+3 = 8        | yes  | hi = 5  |
| 4  | 5  | 4   | 1+2+2+3 = 8        | yes  | hi = 4  |
| 4  | 4  | —   | —                  | stop | ret 4   |

Answer: `4`.

- **Time:** `O(n * log(max(piles)))` — each of `O(log range)` iterations does an
  `O(n)` predicate evaluation.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Ceiling division without floats:** `ceil(p / k) == (p + k - 1) // k`. Avoid
  `math.ceil(p / k)` on large integers — float rounding can give wrong results.
- **Lower bound `1`, upper bound `max(piles)`:** speed `0` is meaningless, and no
  speed above `max(piles)` ever helps because each pile already finishes in one
  hour at `max(piles)`.
- **`h == len(piles)`** forces `k = max(piles)` (Example 2): one pile must be
  cleared per hour, so the speed must cover the biggest pile.
- **Feasibility of the top is guaranteed** by `h >= piles.length`, so the search
  always terminates on a valid answer; no "impossible" case to handle.
- **This is a "minimize the maximum-effort parameter" template** — the same shape
  reappears in ship-capacity and split-array problems.
