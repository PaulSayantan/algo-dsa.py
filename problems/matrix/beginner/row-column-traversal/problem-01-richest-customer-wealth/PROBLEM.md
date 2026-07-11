# Richest Customer Wealth

**Difficulty:** Easy

**Source:** LeetCode 1672 — Richest Customer Wealth

## Description

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount
of money the `i`-th customer has in the `j`-th bank.

A customer's **wealth** is the total amount of money they have across all of their bank
accounts, i.e. the sum of the values in that customer's row. The **richest customer**
is the one with the maximum wealth.

Return the wealth of the richest customer. (You only need the maximum value, not which
customer it belongs to.)

## Constraints

- `m == accounts.length`
- `n == accounts[i].length`
- `1 <= m, n <= 50`
- `1 <= accounts[i][j] <= 100`

## Examples

### Example 1

```
Input:  accounts = [[1,2,3],[3,2,1]]
Output: 6
```

**Explanation:** Customer 0 has wealth `1 + 2 + 3 = 6`. Customer 1 has wealth
`3 + 2 + 1 = 6`. Both have wealth 6, so the maximum is 6.

### Example 2

```
Input:  accounts = [[1,5],[7,3],[3,5]]
Output: 10
```

**Explanation:** Customer 0 has `1 + 5 = 6`, customer 1 has `7 + 3 = 10`, customer 2
has `3 + 5 = 8`. The richest customer's wealth is 10.

### Example 3

```
Input:  accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
```

**Explanation:** The row sums are `2+8+7 = 17`, `7+1+3 = 11`, and `1+9+5 = 15`. The
maximum is 17.

## Hint

Use **Row/Column Traversal**: walk the grid one row at a time, accumulate the sum of
each row (the inner column loop), and track the largest row sum you have seen.
