# Solution — Best Time to Buy and Sell Stock

## Brute Force

Try every ordered pair of days `(buy, sell)` with `buy < sell` and take the
largest `prices[sell] - prices[buy]`.

```python
best = 0
for buy in range(len(prices)):
    for sell in range(buy + 1, len(prices)):
        best = max(best, prices[sell] - prices[buy])
return best
```

- **Time:** O(n^2) — every pair of days.
- **Space:** O(1).

Too slow for `n` up to 10^5 (~10^10 operations).

## Optimal Approach (Running Minimum)

Observation: if we decide to sell on day `i`, the *best* possible profit for
that sell day is `prices[i] - (minimum price on any earlier day)`. So we never
need to remember all earlier prices — only the smallest one seen so far.

Sweep left to right maintaining:

- `min_price` = the running minimum of `prices[0..i]`, and
- `best` = the maximum profit found so far.

At each day: update `best` using `prices[i] - min_price` (profit if we sell
today at the best earlier buy price), then fold today's price into
`min_price`.

Reference implementation:

```python
def maxProfit(prices):
    min_price = float("inf")
    best = 0
    for p in prices:
        best = max(best, p - min_price)   # sell today vs. cheapest earlier day
        min_price = min(min_price, p)     # update running minimum
    return best
```

**Why it is correct.** For any optimal pair `(buy*, sell*)`, when the loop
reaches `sell*` the variable `min_price` equals the minimum of
`prices[0..sell*]`, which is `<= prices[buy*]`. Hence
`prices[sell*] - min_price >= prices[sell*] - prices[buy*]`, so `best` is at
least the optimal profit. Conversely every value we ever assign to `best` is a
real `prices[j] - prices[k]` with `k <= j` (since `min_price` came from an
earlier or equal day), so `best` never exceeds a legal profit. Ordering matters:
we compute the profit *before* updating `min_price`, guaranteeing the buy day is
strictly earlier than the sell day (buying and selling on the same day yields 0,
which never hurts the answer).

**Step-by-step** on `[7, 1, 5, 3, 6, 4]`:

| day | price | min_price (before update) | p - min_price | best |
| --- | ----- | ------------------------- | ------------- | ---- |
| 0 | 7 | inf | -inf | 0 |
| 1 | 1 | 7   | -6  | 0 |
| 2 | 5 | 1   | 4   | 4 |
| 3 | 3 | 1   | 2   | 4 |
| 4 | 6 | 1   | 5   | 5 |
| 5 | 4 | 1   | 3   | 5 |

Result: **5**.

- **Time:** O(n) — single pass.
- **Space:** O(1).

## Key Insights & Edge Cases

- This is the classic "running min / running best" pairing: one scalar tracks
  the best *input* seen so far, another tracks the best *answer* built from it.
- Monotonically decreasing prices (`[7,6,4,3,1]`) yield `0`: every
  `p - min_price` is `<= 0`, and `best` starts at `0`, so no loss is ever taken.
- A single day (`len == 1`) returns `0`: you cannot both buy and sell.
- Initializing `min_price` to `+infinity` makes the first iteration produce a
  negative candidate that cannot beat the initial `best = 0` — clean and
  branchless. Alternatively initialize `min_price = prices[0]` and start the
  loop at index 1.
- Because you can buy and sell on the "same" conceptual day for 0 profit, you
  never need to special-case "no transaction"; `best` starting at 0 covers it.
