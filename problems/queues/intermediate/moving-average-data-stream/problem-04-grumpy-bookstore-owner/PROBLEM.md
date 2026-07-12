# Grumpy Bookstore Owner

**Difficulty:** Medium

**Source:** LeetCode 1052 — Grumpy Bookstore Owner

## Description

A bookstore owner is open for `n` minutes. `customers[i]` customers arrive at minute `i` and all leave at the end of that minute. `grumpy[i]` is `1` if the owner is grumpy during minute `i` and `0` otherwise; customers are satisfied only if the owner is not grumpy that minute.

The owner can use a secret technique that keeps them calm for `minutes` consecutive minutes exactly once. Return the maximum number of customers that can be satisfied.

Constraints: `1 <= minutes <= n <= 2 * 10^4`, `0 <= customers[i] <= 1000`, `grumpy[i]` is `0` or `1`.

## Examples

### Example 1

```
Input:  customers=[1,0,1,2,1,1,7,5], grumpy=[0,1,0,1,0,1,0,1], minutes=3
Output: 16
```

**Explanation:** Customers already satisfied (non-grumpy minutes) total 1+1+1+7 = 10. Placing the calm window over the last 3 minutes recovers 1+7+5 minus already-counted 7, i.e. adds 6 more, for 16.

## Hint

The always-satisfied customers are fixed; slide a fixed size-`minutes` window over the grumpy minutes as a moving sum to find the window that recovers the most extra customers.
