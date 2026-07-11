# Solution - Magnetic Force Between Two Balls

## Brute Force

Try every possible minimum gap `d` from large to small (or enumerate all ways to
choose `m` of the `n` baskets). Enumerating subsets is `O(C(n, m))`, which is
exponential and hopeless for `n = 10^5`. Even scanning every integer `d` in
`[1, max - min]` and greedily checking is:

- **Time:** `O((max - min) * n)` — up to `10^9` candidate gaps, each an `O(n)`
  greedy pass.
- **Space:** `O(1)` beyond the sort.

Far too slow given positions up to `10^9`.

## Optimal Approach (Binary Search on Answer)

First **sort** `position`. We binary-search the answer `d` = the minimum gap.

Monotonicity (the crux of *maximize-the-min*): **if we can place all `m` balls at
least `d` apart, we can certainly place them at least `d - 1` apart.** So
`check(d) = "m balls fit with pairwise gap >= d"` has the pattern
`T T ... T F F ... F`, and we want the **last** `True` (the largest feasible `d`).

The greedy checker places the first ball at the leftmost basket, then walks right
placing a ball whenever the next basket is at least `d` beyond the last placed
ball. If it manages to place `>= m` balls, `d` is feasible.

```python
def maxDistance(self, position: List[int], m: int) -> int:
    position.sort()

    def can_place(d: int) -> bool:
        count = 1              # first ball at the leftmost basket
        last = position[0]
        for x in position[1:]:
            if x - last >= d:  # far enough → place a ball here
                count += 1
                last = x
                if count == m:
                    return True
        return count >= m

    lo, hi = 1, position[-1] - position[0]   # gap range
    while lo < hi:
        mid = (lo + hi + 1) // 2   # bias up: we want the largest feasible d
        if can_place(mid):
            lo = mid               # feasible → try a bigger gap
        else:
            hi = mid - 1           # infeasible → shrink the gap
    return lo
```

### Why it is correct

The greedy "place as early as possible" is optimal for a fixed `d`: placing the
next ball at the earliest basket that is `>= d` away leaves the most room for the
remaining balls, so if any valid placement exists, greedy finds one. That makes
`can_place` an exact feasibility test. Since a smaller required gap is never
harder to satisfy, the predicate flips from `True` to `False` exactly once, and
the maximize template (`mid` rounded up, keep the feasible half) converges to the
largest `d` that still works.

### Step-by-step (position sorted = [1, 2, 3, 4, 7], m = 3)

Range `[1, 6]`.

| lo | hi | mid | placement (gap >= mid)        | count | >= 3 | action  |
|----|----|-----|-------------------------------|-------|------|---------|
| 1  | 6  | 4   | 1, then 7 (2,3,4 too close)   | 2     | no   | hi = 3  |
| 1  | 3  | 2   | 1, 3, 7                       | 3     | yes  | lo = 2  |
| 2  | 3  | 3   | 1, 4, 7                       | 3     | yes  | lo = 3  |
| 3  | 3  | —   | —                             | —     | stop | ret 3   |

Answer: `3`.

- **Time:** `O(n log n)` for the sort plus `O(n * log(max - min))` for the search.
- **Space:** `O(1)` extra (in-place sort), or `O(n)` if the sort copies.

## Key Insights & Edge Cases

- **Maximize-the-min uses the upward-biased mid** `(lo + hi + 1) // 2` and keeps
  the *feasible* (upper) half. Contrast with minimize problems (Koko, ship
  capacity) that use `(lo + hi) // 2` and keep the lower half.
- **You must sort first** — the greedy placement and the gap arithmetic rely on
  positions being in increasing order.
- **`m == 2`** reduces to "the two extreme baskets," giving
  `position[-1] - position[0]` (Example 2).
- **`m == n`** forces every basket to be used; the answer is the *minimum
  adjacent gap* in the sorted array.
- **Search range:** the smallest sensible gap is `1` (positions are distinct
  integers) and the largest is `position[-1] - position[0]`.
- This is the textbook **"Aggressive Cows"** problem; recognizing the
  maximize-the-min shape is the whole game.
