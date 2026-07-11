# Maximum Subset Value Under Weight Limit (0/1 Knapsack, few items)

**Difficulty:** Hard

Source: Classic "0/1 knapsack with large capacity, small item count" — competitive-programming
staple (e.g. Codeforces "K-th sum" / AtCoder-style MITM knapsack).

## Description

You have `n` items. Item `i` has a positive integer weight `weights[i]` and a
non-negative integer value `values[i]`. You are also given a knapsack capacity
`capacity`.

Choose a subset of the items whose **total weight is at most `capacity`** so as to
**maximize the total value**. Return that maximum total value. Choosing nothing (value 0)
is always allowed.

The catch: the standard `O(n · capacity)` knapsack DP is impossible here because
`capacity` can be as large as `10^15`. But `n` is at most 40, which is the signal for
**Meet in the Middle**.

## Constraints

- `1 <= n <= 40`
- `len(weights) == len(values) == n`
- `1 <= weights[i] <= 10^15`
- `0 <= values[i] <= 10^9`
- `1 <= capacity <= 10^15`

## Examples

### Example 1
```
Input:  weights = [3, 4, 5, 2], values = [4, 5, 6, 3], capacity = 7
Output: 9
Explanation: Pick items {0, 1} with weight 3 + 4 = 7 <= 7 and value 4 + 5 = 9.
No feasible subset achieves a higher value within weight 7.
```

### Example 2
```
Input:  weights = [5, 4, 6, 2, 3], values = [10, 40, 30, 50, 20], capacity = 10
Output: 110
Explanation: Pick items {1, 3, 4} with weight 4 + 2 + 3 = 9 <= 10 and
value 40 + 50 + 20 = 110. Any heavier-value pick would exceed the capacity.
```

### Example 3
```
Input:  weights = [8, 9, 10], values = [100, 120, 130], capacity = 5
Output: 0
Explanation: Every item weighs more than the capacity of 5, so the only feasible
choice is the empty subset, with value 0.
```

## Hint

Capacity is astronomically large, ruling out the weight-indexed DP, but `n <= 40`. Split
the items into two halves, enumerate each half's (weight, value) subsets, and combine so
that for each left subset you fetch the best-value right subset that still fits. This is
**Meet in the Middle** with a "best value for weight ≤ w" prefix.
