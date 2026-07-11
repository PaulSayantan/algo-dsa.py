# Solution — Maximum Subset Value Under Weight Limit (MITM Knapsack)

## Brute Force

Enumerate all `2^n` subsets; for each, sum the weights, and if it fits within `capacity`
track the maximum value.

- **Time:** `O(2^n)` — ~`10^12` for `n = 40`, TLE.
- **Space:** `O(1)`.

The textbook 0/1-knapsack DP runs in `O(n · capacity)`, but here `capacity` can be
`10^15`, so a weight-indexed table is utterly infeasible in both time and memory.

## Optimal Approach — Meet in the Middle with a monotone "best value" array

Split the items into halves `L` and `R`. A chosen subset takes some items from `L`
(weight `wl`, value `vl`) and some from `R` (weight `wr`, value `vr`). It is feasible iff
`wl + wr <= capacity`, i.e. `wr <= capacity - wl`, and its value is `vl + vr`. So for each
left subset we want the **maximum-value** right subset whose weight is at most
`capacity - wl`.

1. Enumerate all `(weight, value)` pairs for subsets of `R`.
2. **Sort** those pairs by weight, then build a **prefix-max of value**: `bestVal[i]` =
   the largest value among all right subsets with weight `<= sortedWeight[i]`. This makes
   "best value achievable within weight budget `b`" a single binary search + array lookup.
3. Enumerate all `(wl, vl)` for subsets of `L`. If `wl > capacity`, skip. Otherwise binary
   search the largest index `i` with `sortedWeight[i] <= capacity - wl`; the best right
   value is `bestVal[i]` (or 0 if no right subset fits). Update the answer with
   `vl + bestVal[i]`.

```python
from bisect import bisect_right

def subset_pairs(weights, values):
    pairs = [(0, 0)]                       # (weight, value); empty subset
    for w, v in zip(weights, values):
        pairs += [(pw + w, pv + v) for pw, pv in pairs]
    return pairs

def max_value_under_weight(weights, values, capacity):
    n = len(weights)
    mid = n // 2
    right = subset_pairs(weights[mid:], values[mid:])
    right.sort()                            # by weight
    # prefix maximum of value over increasing weight
    rw = [w for w, _ in right]
    best_val = []
    cur = 0
    for _, v in right:
        cur = max(cur, v)
        best_val.append(cur)

    ans = 0
    for wl, vl in subset_pairs(weights[:mid], values[:mid]):
        if wl > capacity:
            continue
        budget = capacity - wl
        i = bisect_right(rw, budget) - 1    # last right subset with weight <= budget
        rv = best_val[i] if i >= 0 else 0
        ans = max(ans, vl + rv)
    return ans
```

### Why it is correct

Each feasible knapsack selection splits uniquely into its `L`-part and `R`-part, and the
two parts are chosen independently. For a fixed left part `(wl, vl)`, the best completion
is the highest-value right subset with weight `<= capacity - wl` — exactly what the
prefix-max-of-value array returns via binary search. Because the right pairs are sorted by
weight and `best_val` is the running maximum of value over that order, `best_val[i]`
correctly reports the optimum among *all* right subsets within the budget (not merely the
one at index `i`). Maximizing `vl + best_val[i]` over every left subset gives the global
optimum. The empty subset appears in both halves (the `(0,0)` seed), so "take nothing" is
always considered.

### Complexity

- **Time:** `O(2^(n/2) · (n/2))` — enumerate + sort each half (`2^20 log` for `n = 40`)
  and one binary search per left subset. ~`10^6 · 20` operations.
- **Space:** `O(2^(n/2))` for the right half's pairs and prefix-max array.

## Key Insights & Edge Cases

- **Prefix-max, not just the matching weight.** A heavier right subset can be *less*
  valuable, so you must take the best value over *all* weights `<= budget`, not the value
  at the exact insertion point. Building the monotone `best_val` array captures this. (An
  equivalent alternative is to first discard dominated pairs — those with higher weight but
  no higher value — then binary search directly.)
- **Weights and capacity are huge.** Keep everything in native big integers (Python handles
  this automatically); the weight-indexed DP is intentionally impossible.
- **All items too heavy.** If every single item exceeds `capacity`, only the empty subset
  fits and the answer is `0` (Example 3). The `(0,0)` seed and the `wl > capacity` skip
  handle this.
- **Zero values / duplicate weights** cause no problems; ties in weight are resolved fine
  by the prefix-max.
- Balance the split so neither half exceeds `~2^20` subsets.
