# Koko Eating Bananas — Solution

## Brute Force

Try every candidate speed `k` from `1` up to `max(piles)`. For each `k`, compute the total hours needed as `sum(ceil(pile / k) for pile in piles)` and return the first `k` whose total is `<= h`.

```python
def minEatingSpeed(piles, h):
    for k in range(1, max(piles) + 1):
        hours = sum((pile + k - 1) // k for pile in piles)
        if hours <= h:
            return k
```

- **Time:** O(max(piles) · n) — up to `max(piles)` candidate speeds, each costing an O(n) scan.
- **Space:** O(1).

With `piles[i]` up to `10^9`, this is far too slow.

## Optimal Approach (Binary Search on Answer)

**Answer range.** The slowest useful speed is `1`. The fastest speed we would ever need is `max(piles)`: at that speed every pile is eaten in a single hour, giving `n` hours, and since the constraints guarantee `h >= n`, `k = max(piles)` is always feasible. So the answer lives in `[1, max(piles)]`.

**Feasibility predicate.** Define:

```
hours_needed(k) = sum(ceil(pile / k) for pile in piles)
feasible(k)     = hours_needed(k) <= h
```

`ceil(pile / k)` in integer math is `(pile + k - 1) // k`.

**Monotonicity.** As `k` increases, each `ceil(pile / k)` term is non-increasing, so `hours_needed(k)` is non-increasing. Therefore `feasible` flips exactly once from `False` to `True` as `k` grows: `F F F ... F T T ... T`. We want the **first** `True` — the smallest feasible speed.

```python
def minEatingSpeed(piles, h):
    def hours_needed(k):
        return sum((pile + k - 1) // k for pile in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:   # feasible → answer is mid or smaller
            hi = mid
        else:                        # too slow → need a strictly larger speed
            lo = mid + 1
    return lo
```

**Why it is correct.** The invariant is that the answer always lies within `[lo, hi]`. When `mid` is feasible, `mid` itself might be the answer, so we keep it in range with `hi = mid`. When `mid` is infeasible, the answer must be strictly greater, so `lo = mid + 1`. The range strictly shrinks each iteration, and when `lo == hi` the interval is a single value: the first feasible speed.

**Step-by-step for `piles = [3, 6, 7, 11], h = 8`** (range `[1, 11]`):

| lo | hi | mid | hours(mid) | <= 8? | action |
|----|----|-----|------------|-------|--------|
| 1  | 11 | 6   | 1+1+2+2 = 6 | yes  | hi = 6 |
| 1  | 6  | 3   | 1+2+3+4 = 10 | no  | lo = 4 |
| 4  | 6  | 5   | 1+2+2+3 = 8 | yes  | hi = 5 |
| 4  | 5  | 4   | 1+2+2+3 = 8 | yes  | hi = 4 |

`lo == hi == 4` → return `4`. Correct.

- **Time:** O(n · log(max(piles))).
- **Space:** O(1).

## Key Insights & Edge Cases

- **Ceiling division:** Use `(pile + k - 1) // k` rather than `math.ceil(pile / k)` to avoid floating-point rounding errors on large values.
- **Upper bound choice:** `hi = max(piles)` is the tightest safe upper bound. Using something larger (e.g. `10^9`) still works but wastes a couple of iterations.
- **First-True boundary pattern:** Since we minimize, use the `lo < hi` loop with `hi = mid` on success and `lo = mid + 1` on failure, then return `lo`. This converges to the first feasible value and never overshoots.
- **Single pile / `h == n`:** When `h` equals the number of piles, every pile must be finished in one hour, forcing `k = max(piles)` (see Example 2). The binary search naturally lands there because no smaller speed is feasible.
- **Do not confuse hours with piles:** Each hour Koko eats from only one pile, and leftover capacity within an hour is wasted — that is exactly why the per-pile cost is a ceiling, not `pile / k`.
