# Solution - Sqrt(x)

## Brute Force

Count upward until `k * k` exceeds `x`.

```python
k = 0
while (k + 1) * (k + 1) <= x:
    k += 1
return k
```

- **Time:** `O(sqrt(x))` — we take one step per candidate up to the answer.
- **Space:** `O(1)`.

For `x` near `2^31`, `sqrt(x)` is about `46341`, which is fine here but wasteful
and does not generalize to larger ranges.

## Optimal Approach (Binary Search on Answer)

We are looking for the **last** `k` in `[0, x]` for which `check(k) = (k*k <= x)`
holds. The predicate is monotonic: once `k` is large enough that `k*k > x`, every
larger `k` also fails.

Search the answer range `[0, x]` (using `x` as an upper bound is always safe;
`x // 2 + 1` is a tighter one for `x >= 2`). Bias `mid` upward because we want the
*largest* feasible value.

```python
def mySqrt(self, x: int) -> int:
    lo, hi = 0, x
    while lo < hi:
        mid = (lo + hi + 1) // 2   # +1 so mid rounds up; avoids infinite loop
        if mid * mid <= x:         # feasible → answer is mid or larger
            lo = mid
        else:                      # mid too big → answer is smaller
            hi = mid - 1
    return lo
```

### Why it is correct

Define `check(k) = (k * k <= x)`. Because squaring is increasing on
non-negative integers, `check` produces the pattern `T T ... T F F ... F`. The
loop maintains the invariant that the answer lies in `[lo, hi]`:

- If `check(mid)` is `True`, `mid` is a valid answer, and the true answer is `mid`
  or bigger, so we keep the upper half by setting `lo = mid`.
- If `check(mid)` is `False`, `mid` is too big; the answer is strictly below, so
  `hi = mid - 1`.

The interval strictly shrinks each iteration and both branches keep the boundary
inside `[lo, hi]`, so when `lo == hi` it equals the floor of the square root.

### Step-by-step (x = 8)

| lo | hi | mid | mid*mid | mid*mid <= 8 | action     |
|----|----|-----|---------|--------------|------------|
| 0  | 8  | 4   | 16      | no           | hi = 3     |
| 0  | 3  | 2   | 4       | yes          | lo = 2     |
| 2  | 3  | 3   | 9       | no           | hi = 2     |
| 2  | 2  | —   | —       | stop         | return 2   |

Answer: `2`.

- **Time:** `O(log x)` — the interval halves each step.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **The maximize template needs `mid = (lo + hi + 1) // 2`.** Without the `+1`,
  when `hi == lo + 1` and the `True` branch runs `lo = mid`, `mid` would equal
  `lo` and the loop would spin forever.
- **Overflow:** in languages with fixed-width integers, `mid * mid` can overflow
  for `x` near `2^31`. Use a 64-bit type or compare via `mid <= x // mid`. Python
  integers are unbounded, so this is not an issue here.
- **`x = 0` and `x = 1`** are handled without special-casing: the range collapses
  and returns `0` and `1` respectively.
- **Alternative (first-false framing):** you could instead find the first `k`
  with `k*k > x` and subtract one; both are the same boundary viewed from either
  side.
