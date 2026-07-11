# Solution — Koko Eating Bananas

## Brute Force

The answer is somewhere between speed `1` and speed `max(piles)` (going faster
than the biggest pile never helps, because each hour touches only one pile). Try
every candidate speed from slow to fast and return the first one that fits in
`h` hours.

```python
def hours_for(k):
    return sum((p + k - 1) // k for p in piles)   # ceil(p / k)

for k in range(1, max(piles) + 1):
    if hours_for(k) <= h:
        return k
```

- **Time:** O(max(piles) * n) — up to `max(piles)` candidate speeds, each costing
  O(n) to evaluate. With `piles[i]` up to 1e9 this is far too slow.
- **Space:** O(1).

## Optimal Approach (Binary Search on the Answer)

The array here is **not** the thing we search — we search over the space of
**possible answers** (eating speeds). The trick works because the feasibility
predicate is **monotonic**:

> Define `feasible(k)` = "`hours_needed(k) <= h`". If speed `k` works, then any
> speed `k' > k` also works (eating faster never takes more hours). So as `k`
> increases the predicate goes `False, False, ..., True, True` — exactly the
> monotone shape binary search needs.

Where `hours_needed(k) = sum(ceil(p / k) for p in piles)`.

We binary search for the **leftmost** `k` in `[1, max(piles)]` where
`feasible(k)` is true, using the half-open boundary template.

1. `lo = 1`, `hi = max(piles)`.
2. While `lo < hi`:
   - `mid = lo + (hi - lo) // 2`.
   - If `feasible(mid)` (fits in `h` hours), it is a candidate — try to go
     slower: `hi = mid`.
   - Else it is too slow — must go faster: `lo = mid + 1`.
3. Return `lo`.

```python
import math

def minEatingSpeed(piles, h):
    def hours_needed(k):
        return sum(math.ceil(p / k) for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if hours_needed(mid) <= h:
            hi = mid          # feasible: search for a smaller speed
        else:
            lo = mid + 1      # infeasible: need a larger speed
    return lo
```

**Why it is correct.** Because `feasible` is monotonic, the smallest feasible
speed is a well-defined boundary. Binary search maintains the invariant that
`hi` is always feasible and everything below `lo` is infeasible, narrowing until
`lo == hi` lands exactly on the minimum feasible speed. The upper bound
`max(piles)` is always feasible: at that speed every pile takes exactly one
hour, totaling `n` hours, and the constraints guarantee `h >= n`.

- **Time:** O(n log(max(piles))) — `O(log(max piles))` binary-search steps, each
  an O(n) feasibility check.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Search the answer, not the array.** The signature move is recognizing a
  monotone `feasible(x)` and binary-searching the range of possible `x`. This
  generalizes to "minimum capacity," "minimum days," "split array largest sum,"
  and many others.
- **Ceiling division for hours:** `ceil(p / k)` = `(p + k - 1) // k`; do not use
  plain integer division, which would undercount partial piles.
- **Bounds:** `lo = 1` (speed 0 is meaningless) and `hi = max(piles)` (faster is
  never necessary because only one pile is eaten per hour). `hi` is guaranteed
  feasible since `h >= len(piles)`.
- **`h == len(piles)`** (`[30,11,23,4,20]`, h=5): every pile needs its own hour,
  forcing `k = max(piles) = 30`.
- **Slack hours** (`[30,11,23,4,20]`, h=6): the extra hour lets the biggest pile
  span two hours, dropping the answer to 23.
- **Use `hi = mid` (not `mid - 1`)** on the feasible branch so the current
  feasible candidate is never discarded; `lo = mid + 1` on the infeasible branch
  guarantees progress and termination.
