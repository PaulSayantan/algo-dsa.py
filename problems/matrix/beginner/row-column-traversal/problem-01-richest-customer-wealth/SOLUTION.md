# Solution — Richest Customer Wealth

## Brute Force

There is no meaningfully "worse" algorithm here: to know any customer's wealth you must
read every entry of their row, and to find the richest customer you must consider every
customer. A naive framing might compute all row sums, store them in a list, then take
the max in a second pass.

- **Time:** O(m * n) — every cell is read once.
- **Space:** O(m) — to hold the list of row sums.

## Optimal Approach (Row/Column Traversal)

Walk the grid in row-major order. The outer loop fixes a row; the inner loop sums that
row's columns. Keep a single running `best` that tracks the largest row sum seen so
far, so no auxiliary list is required.

```python
def maximumWealth(self, accounts: List[List[int]]) -> int:
    best = 0
    for row in accounts:            # outer: pick a customer (row)
        wealth = 0
        for money in row:           # inner: walk the banks (columns)
            wealth += money
        best = max(best, wealth)
    return best
```

Or more concisely with `sum`:

```python
def maximumWealth(self, accounts: List[List[int]]) -> int:
    return max(sum(row) for row in accounts)
```

**Why it is correct:** `wealth` is exactly the definition of a customer's wealth (the
sum over that customer's banks), and `best` is the running maximum, so after visiting
every row `best` equals the maximum wealth over all customers.

**Step by step** on `[[1,5],[7,3],[3,5]]`:

1. Row `[1,5]` -> wealth `6`; `best = 6`.
2. Row `[7,3]` -> wealth `10`; `best = 10`.
3. Row `[3,5]` -> wealth `8`; `best` stays `10`.
4. Return `10`.

- **Time:** O(m * n) — each of the `m * n` cells is touched once.
- **Space:** O(1) — only the two scalars `best` and `wealth`.

## Key Insights & Edge Cases

- Because all values are `>= 1`, initializing `best = 0` is safe; any real row sum will
  exceed it. If negatives were allowed, initialize `best = float("-inf")`.
- There is always at least one row (`m >= 1`), so `max(...)` never sees an empty
  sequence.
- The direction of traversal does not matter for a sum, but here rows are the natural
  grouping, so rows-then-columns (row-major) is the clean choice.
- The single-scalar running-max version avoids the O(m) list without changing the
  asymptotic time.
