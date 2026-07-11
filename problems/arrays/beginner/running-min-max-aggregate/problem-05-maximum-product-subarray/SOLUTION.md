# Solution — Maximum Product Subarray

## Brute Force

Enumerate every start `i` and end `j`, multiply the slice, keep the max.

```python
best = float("-inf")
for i in range(len(nums)):
    prod = 1
    for j in range(i, len(nums)):
        prod *= nums[j]
        best = max(best, prod)
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach (Running Max AND Min Together)

The wrinkle versus Maximum Subarray: multiplying by a **negative** number turns
a large positive product into a large negative one, and — crucially — turns the
*most negative* product into the *largest positive* one. So the max product
ending here can come from either the previous max **or** the previous min.

Carry two running values that describe subarrays ending at the current index:

- `cur_max` = largest product of a subarray ending here,
- `cur_min` = smallest (most negative) product of a subarray ending here.

For each element `x`, the three candidates are `x` (start fresh),
`cur_max * x`, and `cur_min * x`. Then:

```
cur_max = max(x, cur_max * x, cur_min * x)
cur_min = min(x, cur_max_old * x, cur_min * x)
```

Reference implementation (compute new values from the *old* pair):

```python
def maxProduct(nums):
    best = cur_max = cur_min = nums[0]
    for x in nums[1:]:
        # A negative x swaps the roles of max and min, so compute candidates
        # from the OLD cur_max and cur_min before overwriting either.
        cand1, cand2 = cur_max * x, cur_min * x
        cur_max = max(x, cand1, cand2)
        cur_min = min(x, cand1, cand2)
        best = max(best, cur_max)
    return best
```

**Why it is correct.** Any subarray ending at index `i` is either just
`nums[i]`, or a subarray ending at `i-1` extended by `nums[i]`. The extended
product is `(product ending at i-1) * nums[i]`. To maximize it we must consider
both extremes of the previous products: multiplying by a positive keeps order
(so `cur_max` matters), while multiplying by a negative reverses it (so
`cur_min * x` can become the new maximum). Tracking both extremes captures every
case, including `x == 0`, which resets both `cur_max` and `cur_min` to `0` (the
`max/min` with the standalone `x` handles this). The running `best` records the
largest `cur_max` over all endpoints.

**Step-by-step** on `[-2, 3, -4]`:

| i | x  | old (max, min) | cand = (max*x, min*x) | new max | new min | best |
| - | -- | -------------- | --------------------- | ------- | ------- | ---- |
| 0 | -2 | init           | –                     | -2      | -2      | -2   |
| 1 |  3 | (-2, -2)       | (-6, -6)              | max(3,-6,-6)=3 | min(3,-6,-6)=-6 | 3 |
| 2 | -4 | (3, -6)        | (-12, 24)             | max(-4,-12,24)=24 | min(-4,-12,24)=-12 | 24 |

Result: **24**.

- **Time:** O(n) — single pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- The defining trick: **keep the running minimum alongside the running maximum**
  because a negative multiplier can promote the min to the top.
- You must compute both new values from the *old* pair. Overwriting `cur_max`
  first and then reusing it to compute `cur_min` is a classic bug — snapshot
  `cur_max * x` and `cur_min * x` first (as above).
- **Zeros** act as barriers: they reset both running products, effectively
  restarting the scan after the zero. Including `x` itself among the candidates
  handles this automatically.
- Seed all three variables with `nums[0]` (not `1` and not `0`) so single-element
  and all-negative arrays are handled correctly.
- An alternative to tracking min: run Kadane-style products left-to-right and
  right-to-left and take the overall max — the sign issues cancel out because a
  zero-free array has an even or odd count of negatives handled from one end.
