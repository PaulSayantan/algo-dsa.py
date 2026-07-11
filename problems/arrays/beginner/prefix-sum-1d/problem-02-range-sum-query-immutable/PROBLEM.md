# Range Sum Query - Immutable

**Difficulty:** Easy

**Source:** LeetCode 303 — Range Sum Query - Immutable

## Description

Given an integer array `nums`, handle multiple queries of the following type:

- Calculate the sum of the elements of `nums` between indices `left` and `right`
  **inclusive**, where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` returns the sum of the elements of `nums`
  between indices `left` and `right` inclusive (that is,
  `nums[left] + nums[left + 1] + ... + nums[right]`).

The array is **immutable** — it never changes after construction — and
`sumRange` may be called many times, so each call should be fast.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

## Examples

### Example 1

```
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]

Explanation:
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

### Example 2

```
Input:
["NumArray", "sumRange", "sumRange"]
[[[1, 2, 3, 4, 5]], [1, 3], [0, 4]]
Output:
[null, 9, 15]

Explanation:
NumArray numArray = new NumArray([1, 2, 3, 4, 5]);
numArray.sumRange(1, 3); // 2 + 3 + 4 = 9
numArray.sumRange(0, 4); // 1 + 2 + 3 + 4 + 5 = 15
```

## Hint

Precompute a **Prefix Sum (1D)** array once in the constructor. Then any
`sumRange(left, right)` becomes a single subtraction of two prefix values.
