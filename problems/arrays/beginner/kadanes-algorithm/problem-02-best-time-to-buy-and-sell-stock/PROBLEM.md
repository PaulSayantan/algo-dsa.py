# Best Time to Buy and Sell Stock

**Difficulty:** Easy

**Source:** LeetCode 121 — Best Time to Buy and Sell Stock

## Description

You are given an array `prices` where `prices[i]` is the price of a given stock
on the `i`-th day.

You want to maximize your profit by choosing a **single** day to buy one stock
and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit (prices only fall), return `0`.

**Why this is a Kadane problem.** Let `d[i] = prices[i] - prices[i-1]` be the
day-to-day change. Buying on day `b` and selling on day `s > b` yields profit
`prices[s] - prices[b] = d[b+1] + d[b+2] + ... + d[s]`, i.e. the sum of a
contiguous subarray of `d`. So the maximum profit is the maximum subarray sum of
`d`, clamped to be at least `0` (you may decline to trade).

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Examples

### Example 1

```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
             The daily differences are [-6, 4, -2, 3, -2]; the max subarray [4, -2, 3] sums to 5.
```

### Example 2

```
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Prices only decrease, so no profitable transaction exists; the best choice
             is to not trade at all, giving profit 0.
```

## Constraints on the transaction

- You must buy before you sell (a subarray of differences is inherently ordered).
- At most one buy and one sell.

## Hint

Transform prices into consecutive differences and find the maximum-sum
contiguous run of those differences using **Kadane's Algorithm** — a positive
run of differences is exactly a profitable buy-then-sell window.
