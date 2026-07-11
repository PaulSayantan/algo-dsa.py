# Find the Smallest Divisor Given a Threshold — Solution

## Brute Force

Try every divisor `d` from `1` upward. For each `d`, compute `sum(ceil(num / d) for num in nums)` and return the first `d` whose sum is `<= threshold`.

```python
def smallestDivisor(nums, threshold):
    d = 1
    while True:
        total = sum((num + d - 1) // d for num in nums)
        if total <= threshold:
            return d
        d += 1
```

- **Time:** O(max(nums) · n) — up to `max(nums)` candidate divisors, each an O(n) sum.
- **Space:** O(1).

With `nums[i]` up to `10^6`, scanning every divisor is too slow.

## Optimal Approach (Binary Search on Answer)

**Answer range.** The smallest positive divisor is `1`. Once the divisor reaches `max(nums)`, every term `ceil(num / d)` equals `1`, so the sum is exactly `n`, and the constraints guarantee `threshold >= n` — meaning `d = max(nums)` is always feasible. So the answer lives in `[1, max(nums)]`.

**Feasibility predicate.**

```
compute_sum(d) = sum(ceil(num / d) for num in nums)   # ceil = (num + d - 1) // d
feasible(d)    = compute_sum(d) <= threshold
```

**Monotonicity.** As `d` increases, each `ceil(num / d)` term is non-increasing, so `compute_sum(d)` is non-increasing. The predicate flips once from `False` to `True`: `F F ... F T T ... T`. We want the **first** `True` — the smallest feasible divisor.

```python
def smallestDivisor(nums, threshold):
    def compute_sum(d):
        return sum((num + d - 1) // d for num in nums)

    lo, hi = 1, max(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if compute_sum(mid) <= threshold:  # feasible → try smaller divisor
            hi = mid
        else:                              # sum too big → need a larger divisor
            lo = mid + 1
    return lo
```

**Why it is correct.** The invariant is that the answer always lies within `[lo, hi]`. When `mid` is feasible, `mid` may be optimal, so `hi = mid`. When `mid` is infeasible, a larger divisor is required, so `lo = mid + 1`. The range strictly shrinks; at `lo == hi` the single remaining value is the smallest feasible divisor.

**Step-by-step for `nums = [1, 2, 5, 9], threshold = 6`** (range `[1, 9]`):

| lo | hi | mid | compute_sum(mid) | <= 6? | action |
|----|----|-----|------------------|-------|--------|
| 1  | 9  | 5   | 1+1+1+2 = 5      | yes   | hi = 5 |
| 1  | 5  | 3   | 1+1+2+3 = 7      | no    | lo = 4 |
| 4  | 5  | 4   | 1+1+2+3 = 7      | no    | lo = 5 |

`lo == hi == 5` → return `5`. Correct.

- **Time:** O(n · log(max(nums))).
- **Space:** O(1).

## Key Insights & Edge Cases

- **Ceiling division:** compute `ceil(num / d)` as `(num + d - 1) // d` to avoid floating-point error on large numbers.
- **Upper bound `max(nums)` is tight:** beyond it the sum stays fixed at `n`, so searching higher is pointless. Any larger bound still yields the correct answer, just with a couple of extra iterations.
- **Threshold very large (Example 3):** if even divisor `1` satisfies the threshold, the search collapses to `lo = 1` immediately.
- **Threshold equals `n` (Example 2):** every term must round to exactly `1`, which forces the divisor up to `max(nums)`.
- **This is the same first-True template** used in Koko Eating Bananas — the only change is the feasibility predicate. Recognizing the shared shape ("smallest `d` with a monotone, non-increasing cost `<= budget`") makes these interchangeable.
