# Coin Change

**Difficulty:** Medium

**Source:** LeetCode 322 (Coin Change)

## Description

You are given an integer array `coins` representing coins of different denominations and
an integer `amount` representing a total amount of money.

Return the **fewest number of coins** that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an **infinite** number of each kind of coin.

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Examples

### Example 1

```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1, which uses 3 coins — no combination uses fewer.
```

### Example 2

```
Input: coins = [2], amount = 3
Output: -1
Explanation: Only even totals are reachable with a coin of value 2, so 3 is impossible.
```

### Example 3

```
Input: coins = [1], amount = 0
Output: 0
Explanation: Zero coins are needed to make amount 0.
```

## Hint

Use **Dynamic Programming (memoization / tabulation)**: the fewest coins for `amount` is
`1 + min(fewest for amount - c)` over each coin `c`. Many target amounts recur, so cache
the answer for each amount.
