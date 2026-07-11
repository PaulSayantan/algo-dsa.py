# Maximum Ice Cream Bars

**Difficulty:** Medium

**Source:** LeetCode 1833 — Maximum Ice Cream Bars

## Description

It is a sweltering summer day, and a boy wants to buy some ice cream bars. At the store there
are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the
price of the `i`-th ice cream bar in coins. The boy initially has `coins` coins to spend, and
he wants to buy as **many** ice cream bars as possible.

Return the **maximum** number of ice cream bars the boy can buy. You may buy the ice cream
bars in any order.

The greedy strategy is to always buy the cheapest remaining bar. That requires the costs in
ascending order — and since prices are bounded integers, you can produce that order in linear
time by counting how many bars exist at each price.

## Constraints

- `costs.length == n`
- `1 <= n <= 10^5`
- `1 <= costs[i] <= 10^5`
- `1 <= coins <= 10^8`

## Examples

### Example 1

```
Input:  costs = [1,3,2,4,1], coins = 7
Output: 4
```

**Explanation:** In ascending price order the bars cost `1, 1, 2, 3, 4`. Buying `1 + 1 + 2 + 3
= 7` uses all the coins for 4 bars; the last bar costing `4` is unaffordable.

### Example 2

```
Input:  costs = [10,6,8,7,7,8], coins = 5
Output: 0
```

**Explanation:** The cheapest bar costs `6`, which already exceeds the `5` coins available, so
the boy can buy nothing.

### Example 3

```
Input:  costs = [1,6,3,1,2,5], coins = 20
Output: 6
```

**Explanation:** In ascending order the prices are `1, 1, 2, 3, 5, 6`, summing to `18 <= 20`,
so the boy can afford every bar — all 6.

## Hint

Buying cheapest-first is optimal, so you need the prices sorted ascending. Prices are bounded
by `10^5`, so use **Counting Sort**: tally how many bars have each price, then sweep prices
from lowest to highest, buying `count[p]` bars at price `p` while coins remain.
