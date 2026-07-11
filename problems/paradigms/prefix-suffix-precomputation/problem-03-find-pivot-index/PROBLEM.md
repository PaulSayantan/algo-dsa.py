# Find Pivot Index

**Difficulty:** Easy

**Source:** LeetCode 724 — Find Pivot Index

## Description

Given an array of integers `nums`, calculate the **pivot index** of this array.

The pivot index is the index where the sum of all the numbers **strictly to the
left** of the index is equal to the sum of all the numbers **strictly to the right**
of the index.

If the index is on the left edge of the array, then the left sum is `0` because
there are no elements to the left. This also applies to the right edge of the array.

Return the **leftmost** pivot index. If no such index exists, return `-1`.

## Constraints

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

## Examples

### Example 1

```
Input:  nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: The pivot index is 3.
             Left sum  = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
             Right sum = nums[4] + nums[5]           = 5 + 6     = 11
             They are equal, and 3 is the leftmost such index.
```

### Example 2

```
Input:  nums = [1, 2, 3]
Output: -1
Explanation: There is no index that satisfies the condition:
             index 0 -> left 0, right 2+3=5
             index 1 -> left 1, right 3
             index 2 -> left 1+2=3, right 0
             None match, so return -1.
```

### Example 3

```
Input:  nums = [2, 1, -1]
Output: 0
Explanation: At index 0 the left sum is 0 (no elements to the left) and the
             right sum is nums[1] + nums[2] = 1 + (-1) = 0. They match, so 0 is
             the leftmost (and here only) pivot index.
```

## Hint

Use **Prefix / Suffix Precomputation**: the right sum at index `i` equals
`total - prefix[i] - nums[i]`, so knowing the total and a running left sum lets you
test every index in one pass.
