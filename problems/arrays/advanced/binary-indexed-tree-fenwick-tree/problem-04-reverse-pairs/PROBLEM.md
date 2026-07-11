# Reverse Pairs

**Difficulty:** Hard

**Source:** LeetCode 493 — Reverse Pairs

## Description

Given an integer array `nums`, return the number of **reverse pairs** in the array.

A **reverse pair** is a pair `(i, j)` where:

- `0 <= i < j < nums.length`, and
- `nums[i] > 2 * nums[j]`.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples

### Example 1

```
Input:  nums = [1, 3, 2, 3, 1]
Output: 2
```

**Explanation:** The reverse pairs are:
- `(1, 4)` because `nums[1] = 3 > 2 * nums[4] = 2 * 1 = 2`.
- `(3, 4)` because `nums[3] = 3 > 2 * nums[4] = 2 * 1 = 2`.

No other index pair satisfies `nums[i] > 2 * nums[j]`, so the answer is `2`.

### Example 2

```
Input:  nums = [2, 4, 3, 5, 1]
Output: 3
```

**Explanation:** The reverse pairs are:
- `(1, 4)` because `4 > 2 * 1 = 2`.
- `(2, 4)` because `3 > 2 * 1 = 2`.
- `(3, 4)` because `5 > 2 * 1 = 2`.

### Example 3

```
Input:  nums = [5, 4, 3, 2, 1]
Output: 4
```

**Explanation:** The reverse pairs are `(0, 3)` (`5 > 2*2`), `(0, 4)` (`5 > 2*1`),
`(1, 4)` (`4 > 2*1`), and `(2, 4)` (`3 > 2*1`). Note `(1, 3)` fails because `4 > 2*2 = 4`
is false (strict inequality), so the total is `4`.

## Hint

Sweep the array left to right. Before inserting `nums[j]`, you want to know how many already
seen `nums[i]` satisfy `nums[i] > 2 * nums[j]` — a **suffix count** over already-inserted
values. A **Binary Indexed Tree (Fenwick Tree)** over coordinate-compressed values gives
that count in O(log n); watch the `2 * nums[j]` threshold and 64-bit overflow.
