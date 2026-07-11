# Solution - Most Beautiful Item for Each Query

## Brute Force

For each query, scan every item and take the maximum beauty among items whose
price fits the budget.

```python
def maximumBeauty(self, items, queries):
    answer = []
    for q in queries:
        best = 0
        for price, beauty in items:
            if price <= q:
                best = max(best, beauty)
        answer.append(best)
    return answer
```

- **Time:** `O(n * q)` — every query rescans all `n` items. With `n = q = 10^5`
  that is `10^10` operations, far too slow.
- **Space:** `O(1)` extra (besides the output).

## Optimal Approach (Offline Query Processing)

Key observation: the set of affordable items only **grows** as the budget grows.
If budget `b1 <= b2`, then every item affordable under `b1` is also affordable
under `b2`. So the answer is *monotonic non-decreasing* in the budget. That means
if we process budgets from smallest to largest, we never need to remove an item —
we only ever add items and keep a running maximum beauty.

Because the queries are not given in sorted order, we process them **offline**:

1. **Sort the items by price** ascending.
2. **Sort the query indices by their budget** ascending — but remember each
   query's *original position* so we can place its answer correctly.
3. **Sweep** a single pointer `i` over the sorted items. For each query (in
   increasing budget order), advance `i` past every item whose price is `<=` the
   budget, updating `best = max(best, beauty)` as you go. The current `best` is
   the answer for that query.
4. **Scatter** each computed answer back into `answer[original_index]`.

```python
def maximumBeauty(self, items, queries):
    items.sort(key=lambda it: it[0])          # sort by price
    order = sorted(range(len(queries)), key=lambda j: queries[j])
    answer = [0] * len(queries)
    i = 0
    best = 0
    for j in order:                            # ascending budget
        budget = queries[j]
        while i < len(items) and items[i][0] <= budget:
            best = max(best, items[i][1])
            i += 1
        answer[j] = best                       # write to original slot
    return answer
```

### Why it is correct

The pointer `i` is **monotone**: it only moves forward across all queries
combined. When we reach a query with budget `b`, every item with price `<= b`
has already been folded into `best` (items are sorted by price, and all earlier,
smaller-budget queries advanced `i` at most as far). No affordable item is missed
because we advance `i` until the next item's price exceeds `b`; no unaffordable
item is counted because we stop exactly at the first price `> b`. `best` therefore
equals the maximum beauty over `{beauty : price <= b}`, which is the definition of
the answer. If no item fits, `best` remains its initial `0`, matching the
"no such item" rule.

### Step-by-step (Example 1)

`items` sorted by price: `[1,2], [2,4], [3,2], [3,5], [5,6]`.
Queries sorted ascending: `1, 2, 3, 4, 5, 6` (already sorted here).

| budget | items absorbed (price<=budget) | best | answer |
|--------|--------------------------------|------|--------|
| 1      | `[1,2]`                        | 2    | 2      |
| 2      | `[2,4]`                        | 4    | 4      |
| 3      | `[3,2]`, `[3,5]`               | 5    | 5      |
| 4      | (none new)                     | 5    | 5      |
| 5      | `[5,6]`                        | 6    | 6      |
| 6      | (none new)                     | 6    | 6      |

Scattering back to original positions gives `[2,4,5,5,6,6]`.

- **Time:** `O(n log n + q log q)` — sorting items and queries dominates; the
  sweep itself is `O(n + q)` because `i` advances at most `n` times total.
- **Space:** `O(n + q)` for the sort order and the answer array.

## Key Insights & Edge Cases

- **Monotonicity is what makes "add only" valid.** If the query asked for an
  *exact* price band `[lo, hi]` instead of `price <= budget`, adds alone would not
  suffice and you would need a Fenwick tree or two sweeps.
- **Never lose the original order.** The single most common bug is sorting the
  queries and returning answers in *sorted* order. Always carry the original index
  (via `sorted(range(len(queries)), key=...)` or by pairing `(budget, index)`).
- **No affordable item:** initialize `best = 0`; this directly yields the required
  `0` for tight budgets like Example 3.
- **Duplicate prices / budgets:** handled naturally — the `while` loop absorbs all
  items with price `<= budget`, ties included, and repeated budgets simply reuse
  the same `best` without moving `i`.
- **Alternative:** you could keep items sorted and, for each query, binary-search
  the price plus a *prefix-max* array of beauties. That is also offline-friendly
  and `O((n + q) log n)`, but the monotone sweep avoids the per-query log factor.
