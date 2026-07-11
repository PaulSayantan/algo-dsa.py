# Richest Customer Wealth

**Difficulty:** Easy-Medium

**Source:** LeetCode 1672 — "Richest Customer Wealth"

## Description

You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount
of money the `i`-th customer has in the `j`-th bank. A customer's **wealth** is the
sum of all the money across their bank accounts (the sum of one row).

Return the **wealth of the richest customer** — that is, the maximum row sum.

Note that a customer can have multiple bank accounts, and different customers may hold
different amounts.

## Constraints

- `m == accounts.length`
- `n == accounts[i].length`
- `1 <= m, n <= 50`
- `1 <= accounts[i][j] <= 100`

## Examples

### Example 1

```
Input:  accounts = [[1, 2, 3], [3, 2, 1]]
Output: 6
```

**Explanation:** Customer 0 has wealth 1 + 2 + 3 = 6. Customer 1 has wealth
3 + 2 + 1 = 6. Both are equally rich, so the richest wealth is 6.

### Example 2

```
Input:  accounts = [[1, 5], [7, 3], [3, 5]]
Output: 10
```

**Explanation:** Wealths are 1+5 = 6, 7+3 = 10, 3+5 = 8. The maximum is 10
(customer 1).

### Example 3

```
Input:  accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
Output: 17
```

**Explanation:** Wealths are 2+8+7 = 17, 7+1+3 = 11, 1+9+5 = 15. The richest customer
has wealth 17 (customer 0).

## Hint

Use **Linear Search** over the rows: compute each customer's total, and keep a running
maximum of the wealth seen so far.
