# Combination Sum

**Difficulty:** Medium

**Source:** LeetCode 39 — "Combination Sum"

## Description

Given an array of **distinct** integers `candidates` and a target integer
`target`, return *a list of all **unique combinations** of `candidates` where
the chosen numbers sum to `target`*. You may return the combinations in any
order.

The **same number may be chosen from `candidates` an unlimited number of
times**. Two combinations are unique if the multiset of chosen numbers is
different (order does not matter, so `[2,2,3]` and `[2,3,2]` count as the same
combination).

It is guaranteed that the number of unique combinations that sum up to `target`
is fewer than `150` for the given input.

## Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

## Examples

### Example 1

```
Input:  candidates = [2, 3, 6, 7], target = 7
Output: [[2,2,3], [7]]
Explanation: 2 + 2 + 3 = 7 (2 is reused), and 7 = 7. No other multiset of
these candidates sums to 7, so there are exactly two combinations.
```

### Example 2

```
Input:  candidates = [2, 3, 5], target = 8
Output: [[2,2,2,2], [2,3,3], [3,5]]
Explanation: 2+2+2+2 = 8, 2+3+3 = 8, and 3+5 = 8. These are the only three
multisets of {2,3,5} that total 8.
```

## Hint

Use **Backtracking**: extend the current combination by candidates at index
`start` or later (allowing the same index again so numbers can repeat), and
prune any branch whose running sum already exceeds `target`.
