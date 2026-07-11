# Sqrt(x) — Solution

## Brute Force

Iterate `k` from `0` upward while `k * k <= x`, and return the last `k` that satisfied the condition (or, equivalently, stop and return `k - 1` once `k * k > x`).

```python
def mySqrt(x: int) -> int:
    k = 0
    while (k + 1) * (k + 1) <= x:
        k += 1
    return k
```

- **Time:** O(sqrt(x)) — we walk up to floor(sqrt(x)) iterations.
- **Space:** O(1).

For `x` near `2^31 - 1`, `sqrt(x)` is about 46341 iterations — fine here, but it does not generalize when the feasibility check is expensive.

## Optimal Approach (Binary Search on Answer)

The answer `k` must lie in `[0, x]`. Define the predicate:

```
feasible(k)  ==  (k * k <= x)
```

This predicate is **monotonic**: if `k * k <= x`, then every smaller value also squares to `<= x`; once `k * k > x`, every larger value also exceeds `x`. So the value space looks like `T T T ... T F F ... F`, and we want the **last** `T` — the largest `k` with `k * k <= x`.

Binary search for that boundary:

```python
def mySqrt(x: int) -> int:
    lo, hi = 0, x
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:      # feasible → record and try larger
            ans = mid
            lo = mid + 1
        else:                   # too big → shrink
            hi = mid - 1
    return ans
```

**Why it is correct.** The loop maintains the invariant that `ans` is the best feasible value seen so far, and that the true answer is always within `[lo, hi]`. Each iteration halves the range: when `mid` is feasible we know the answer is `>= mid`, so we push `lo` up and remember `mid`; when `mid` is infeasible the answer is `< mid`, so we pull `hi` down. When `lo > hi` the range is empty and `ans` holds the last feasible value — exactly floor(sqrt(x)).

**Step-by-step for `x = 8`:**

| lo | hi | mid | mid*mid | mid*mid <= 8? | action | ans |
|----|----|-----|---------|---------------|--------|-----|
| 0  | 8  | 4   | 16      | no            | hi = 3 | 0   |
| 0  | 3  | 1   | 1       | yes           | lo = 2, ans = 1 | 1 |
| 2  | 3  | 2   | 4       | yes           | lo = 3, ans = 2 | 2 |
| 3  | 3  | 3   | 9       | no            | hi = 2 | 2   |

`lo (3) > hi (2)` → stop, return `2`. Correct: floor(sqrt(8)) = 2.

- **Time:** O(log x).
- **Space:** O(1).

## Key Insights & Edge Cases

- **`x = 0` and `x = 1`:** With `lo = hi = x` the loop still runs correctly and returns `0` and `1` respectively. Initializing `ans = 0` covers `x = 0` even if the body never records anything.
- **Overflow:** `mid * mid` can be large. In Python integers are unbounded so this is safe; in languages with fixed-width ints, use `mid <= x // mid` or a 64-bit type to avoid overflow.
- **Last-True boundary pattern:** Because we want the *largest* feasible value, the feasible branch moves `lo` up and records `ans`. If instead you wanted the smallest feasible value, you would record on the infeasible-to-feasible flip and move `hi` down.
- **Never use `mid = (lo + hi) // 2` assuming no overflow in fixed-width languages** — prefer `lo + (hi - lo) // 2`. In Python it does not matter.
