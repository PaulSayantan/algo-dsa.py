# Best Time to Buy and Sell Stock

**Difficulty:** Easy

**Source:** LeetCode 121 — Best Time to Buy and Sell Stock

## Description

You are given an array `prices` where `prices[i]` is the price of a given stock
on day `i`.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day *in the future* to sell that stock.

Return the maximum profit you can achieve from this transaction. If no profit
is possible (prices only go down or stay flat), return `0`.

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
- You must buy before you sell (buy day index < sell day index).

## Examples

### Example 1

```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 1 (price = 1) and sell on day 4 (price = 6),
profit = 6 - 1 = 5. You cannot buy on day 1 and sell on day 0
because you must buy before you sell.
```

### Example 2

```
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Prices only fall, so no transaction is profitable.
The best choice is to make no transaction, giving profit 0.
```

### Example 3

```
Input:  prices = [2, 4, 1]
Output: 2
Explanation: Buy on day 0 (price = 2) and sell on day 1 (price = 4),
profit = 2. Selling at the later low price of 1 would be worse.
```

## Hint

Sweep once, keeping the **Running Minimum** price seen so far. At each day the
best profit if you sell today is `today's price - running minimum`; track the
best of those.
