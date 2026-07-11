# Solution — Best Time to Buy and Sell Stock

## Brute Force

Try every pair of days `(b, s)` with `b < s` and take the best `prices[s] -
prices[b]`.

```python
best = 0
for b in range(len(prices)):
    for s in range(b + 1, len(prices)):
        best = max(best, prices[s] - prices[b])
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Kadane's Algorithm

### Reframing profit as a subarray sum

Define the difference array `d[i] = prices[i] - prices[i-1]` for `i >= 1`.
Buying on day `b` and selling on day `s` gives

```
prices[s] - prices[b] = d[b+1] + d[b+2] + ... + d[s]
```

which is the sum of the contiguous block `d[b+1 .. s]`. Therefore **maximum
profit = maximum subarray sum of `d`**, floored at `0` because the empty
transaction (no trade) is always allowed.

### Reference implementation (explicit Kadane on differences)

```python
def maxProfit(prices):
    best = 0   # profit is allowed to be 0 (no trade)
    cur = 0    # best subarray sum of differences ending "today"
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        cur = max(0, cur + diff)   # resetting to 0 == choosing a new buy day
        best = max(best, cur)
    return best
```

Because we clamp `cur` at `0`, "restart the subarray" is literally the same as
"pick a new, cheaper buy day." That is why the popular *track-the-minimum-price*
solution and Kadane-on-differences are the same algorithm in disguise:

```python
def maxProfit(prices):
    min_price = prices[0]
    best = 0
    for p in prices[1:]:
        best = max(best, p - min_price)   # sell today against cheapest so far
        min_price = min(min_price, p)     # or move the buy day here
    return best
```

### Why it is correct

`cur` holds the best profit of a transaction that **sells on the current day**.
Extending (`cur + diff`) keeps the same buy day; resetting to `0` abandons a
loss-making prefix and re-buys today. Every day is considered as a potential
sell day, so the global maximum over all valid `(buy, sell)` pairs is captured
in `best`.

### Step-by-step on `[7, 1, 5, 3, 6, 4]`

Differences: `[-6, 4, -2, 3, -2]`.

| diff | cur = max(0, cur+diff) | best |
| ---- | ---------------------- | ---- |
| -6   | 0                      | 0    |
| 4    | 4                      | 4    |
| -2   | 2                      | 4    |
| 3    | 5                      | 5    |
| -2   | 3                      | 5    |

Answer: **5**.

- **Time:** O(n).
- **Space:** O(1).

## Key Insights & Edge Cases

- **Clamp at 0, not `nums[0]`:** unlike vanilla Maximum Subarray, the empty
  transaction is legal, so the running sum resets to `0` and the answer is never
  negative.
- **Monotonically decreasing prices** (Example 2): every `diff` is negative,
  `cur` never rises above `0`, and the answer is `0`.
- **Single day or empty prices:** no transaction is possible; return `0`. The
  loop starting at `i = 1` handles this automatically.
- **Buy-before-sell constraint** is free here: a subarray of differences is
  ordered in time, so a sell can never precede its buy.
