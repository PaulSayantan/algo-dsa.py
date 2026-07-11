# Reverse Pairs

**Difficulty:** Hard

Source: **LeetCode 493** — "Reverse Pairs".

## Description

Given an integer array `nums`, a pair `(i, j)` is called an **important reverse
pair** if:

```
0 <= i < j < n   and   nums[i] > 2 * nums[j]
```

Return the total number of important reverse pairs in the array.

## Constraints

- `1 <= n == nums.length <= 5 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples

### Example 1
```
Input:  nums = [1, 3, 2, 3, 1]
Output: 2
Explanation: The important reverse pairs are:
  - (1, 4): nums[1] = 3 > 2 * nums[4] = 2 * 1 = 2   -> valid (3 > 2)
  - (3, 4): nums[3] = 3 > 2 * nums[4] = 2 * 1 = 2   -> valid (3 > 2)
  No other pair (i, j) with i < j satisfies nums[i] > 2 * nums[j].
  Total = 2.
```

### Example 2
```
Input:  nums = [2, 4, 3, 5, 1]
Output: 3
Explanation: The important reverse pairs are:
  - (1, 4): nums[1] = 4 > 2 * 1 = 2   -> valid
  - (2, 4): nums[2] = 3 > 2 * 1 = 2   -> valid
  - (3, 4): nums[3] = 5 > 2 * 1 = 2   -> valid
  Total = 3.
```

## Hint

Build a **Wavelet Tree** over `nums`. Sweep `j` from left to right; before you
"insert" position `j`, all positions `i < j` are already the prefix `[0, j)`.
The number of valid `i` for this `j` is the count of prefix values strictly
greater than `2 * nums[j]` — a range "count of values `> threshold`" query
(equivalently `(j) - rangeCountLeq(0, j, 2 * nums[j])`).
