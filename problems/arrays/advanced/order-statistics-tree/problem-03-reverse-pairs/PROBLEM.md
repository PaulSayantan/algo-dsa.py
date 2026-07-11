# Reverse Pairs

**Difficulty:** Hard

**Source:** LeetCode 493 — Reverse Pairs

## Description

Given an integer array `nums`, return the number of **reverse pairs**.

A reverse pair is a pair `(i, j)` where:

- `0 <= i < j < nums.length`, and
- `nums[i] > 2 * nums[j]`.

Equivalently, for each element we want to count how many *earlier* elements are more
than twice its value. Scanning left to right and inserting each value into a dynamic
multiset, the count for a new `nums[j]` is "how many stored keys are strictly greater
than `2 * nums[j]`?" — a **rank / order-count** query on an order-statistics tree
with a scaled threshold.

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
- `(1, 4)` -> `nums[1] = 3 > 2 * nums[4] = 2 * 1 = 2`.
- `(3, 4)` -> `nums[3] = 3 > 2 * nums[4] = 2 * 1 = 2`.

No other pair `(i, j)` with `i < j` satisfies `nums[i] > 2 * nums[j]`.

### Example 2

```
Input:  nums = [2, 4, 3, 5, 1]
Output: 3
```

**Explanation:** The reverse pairs are:
- `(1, 4)` -> `4 > 2 * 1 = 2`.
- `(2, 4)` -> `3 > 2 * 1 = 2`.
- `(3, 4)` -> `5 > 2 * 1 = 2`.

## Hint

Scan left to right, inserting each value into an **Order-Statistics Tree**. Before
inserting `nums[j]`, count how many already-inserted keys are strictly greater than
`2 * nums[j]` using the subtree-size augmentation (a rank query with a scaled
threshold). Use 64-bit arithmetic for `2 * nums[j]`.
