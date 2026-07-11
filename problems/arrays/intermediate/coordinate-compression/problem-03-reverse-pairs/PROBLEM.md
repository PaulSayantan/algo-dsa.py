# Reverse Pairs

**Difficulty:** Hard

**Source:** LeetCode 493 — Reverse Pairs

## Description

Given an integer array `nums`, return the number of **reverse pairs**.

A reverse pair is a pair `(i, j)` where:

- `0 <= i < j < nums.length`, and
- `nums[i] > 2 * nums[j]`.

Because the comparison involves `2 * nums[j]`, both the raw values `nums[j]` **and** the
doubled values `2 * nums[j]` participate in the ordering. If you want to use a Fenwick tree
indexed by value, you must compress *both* sets of numbers together into one shared
coordinate system so that a value and its double land on comparable indices. Values can be
up to `2^31 - 1`, and `2 * nums[j]` can exceed the 32-bit range, so a direct value-indexed
array is impossible — compression is essential.

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
- `(1, 4)`: `nums[1] = 3 > 2 * nums[4] = 2 * 1 = 2`.
- `(3, 4)`: `nums[3] = 3 > 2 * nums[4] = 2 * 1 = 2`.

### Example 2

```
Input:  nums = [2, 4, 3, 5, 1]
Output: 3
```

**Explanation:** The reverse pairs are `(1, 4)` with `4 > 2*1`, `(2, 4)` with `3 > 2*1`,
and `(3, 4)` with `5 > 2*1`. No other pair satisfies `nums[i] > 2 * nums[j]`.

### Example 3

```
Input:  nums = [5, 5, 5]
Output: 0
```

**Explanation:** For any pair, `5 > 2 * 5 = 10` is false, so there are no reverse pairs.

## Hint

Use **Coordinate Compression** over the union of all `nums[i]` and all `2 * nums[i]`, then
count qualifying pairs with a Fenwick tree (BIT).
