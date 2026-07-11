# Maximum Ice Cream Bars — Solution

## Brute Force

Sort the costs ascending with a comparison sort, then greedily buy from the front until the
next bar is unaffordable.

```python
def maxIceCream(costs, coins):
    costs.sort()
    bought = 0
    for c in costs:
        if coins < c:
            break
        coins -= c
        bought += 1
    return bought
```

- **Time:** `O(n log n)` dominated by the sort.
- **Space:** `O(1)` extra (or `O(n)` if the sort is not in place).

The greedy choice — always take the cheapest remaining bar — is provably optimal (exchange
argument: swapping any bought expensive bar for an unbought cheaper one never reduces the
count and never increases spend). The only cost is the sort, and we can make that linear.

## Optimal Approach (Counting Sort subroutine)

Prices lie in `[1, 10^5]`, so replace the comparison sort with counting sort. We never need
the fully materialized sorted array — we just need to iterate prices from cheapest to most
expensive, which a count array gives us directly.

**Steps:**

1. Let `m = max(costs)`. Build `count[0..m]` where `count[p]` is the number of bars priced
   `p`.
2. Sweep `p` from `1` to `m` (ascending = cheapest first). At price `p` there are `count[p]`
   identical bars. Buy as many as affordable: `take = min(count[p], coins // p)`.
3. Add `take` to the answer and subtract `take * p` from `coins`. If at any price `p` you
   cannot afford even one bar (`coins < p`), stop — every later price is even higher.

```python
def maxIceCream(costs, coins):
    m = max(costs)
    count = [0] * (m + 1)
    for c in costs:
        count[c] += 1

    bought = 0
    for p in range(1, m + 1):
        if coins < p:
            break
        if count[p] == 0:
            continue
        take = min(count[p], coins // p)
        bought += take
        coins -= take * p
    return bought
```

**Why it is correct:** Sweeping prices in increasing order realizes the greedy cheapest-first
order. Bars at the same price are interchangeable, so buying `min(count[p], coins // p)` of
them at once is exactly what the one-at-a-time greedy would do. Breaking when `coins < p` is
safe because prices only grow from there.

- **Time:** `O(n + m)` where `m = max(costs) <= 10^5`. Counting is `O(n)`; the sweep is
  `O(m)`.
- **Space:** `O(m)` for the count array.

## Key Insights & Edge Cases

- **Counting sort as a subroutine.** The interesting values aren't sorted for their own sake —
  counting sort just supplies the cheapest-first iteration order that the greedy needs, in
  linear time.
- **Batch buying.** Because equal-priced bars are identical, take `min(count[p], coins // p)`
  in one step instead of looping bar by bar; this keeps the inner work `O(1)` per price.
- **Nothing affordable** (Example 2): the loop breaks at the first price above `coins`,
  returning `0`.
- **Everything affordable** (Example 3): the loop buys all bars and returns `n`.
- **Integer overflow** is a non-issue in Python; in languages with fixed-width ints, `take * p`
  fits comfortably since `coins <= 10^8`.
- Sizing the array to `max(costs) + 1` (rather than a hard-coded `10^5 + 1`) keeps memory
  proportional to the actual largest price.
