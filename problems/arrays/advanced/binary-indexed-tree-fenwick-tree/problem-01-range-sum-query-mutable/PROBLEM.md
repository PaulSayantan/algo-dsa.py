# Range Sum Query - Mutable

**Difficulty:** Medium

**Source:** LeetCode 307 — Range Sum Query - Mutable

## Description

Given an integer array `nums`, handle multiple queries of the following two types:

1. **Update** the value of an element in `nums`.
2. Calculate the **sum** of the elements of `nums` between indices `left` and `right`
   inclusive, where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` initializes the object with the integer array `nums`.
- `void update(int index, int val)` updates the value of `nums[index]` to be `val`.
- `int sumRange(int left, int right)` returns the sum of the elements of `nums` between
  indices `left` and `right` inclusive (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

The queries arrive interleaved, and there can be many of each type, so a solution must
handle both updates and range-sum queries efficiently rather than recomputing from scratch.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `0 <= index < nums.length`
- `-100 <= val <= 100`
- `0 <= left <= right < nums.length`
- At most `3 * 10^4` calls will be made to `update` and `sumRange`.

## Examples

### Example 1

```
Input:
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]

Output:
[null, 9, null, 8]
```

**Explanation:**
- `NumArray([1, 3, 5])` builds the structure over `[1, 3, 5]`.
- `sumRange(0, 2)` returns `1 + 3 + 5 = 9`.
- `update(1, 2)` changes `nums[1]` from `3` to `2`, so the array is `[1, 2, 5]`.
- `sumRange(0, 2)` now returns `1 + 2 + 5 = 8`.

### Example 2

```
Input:
["NumArray", "sumRange", "update", "sumRange", "sumRange"]
[[[2, 4, 1, 7]], [1, 3], [2, 10], [1, 3], [0, 0]]

Output:
[null, 12, null, 21, 2]
```

**Explanation:**
- Build over `[2, 4, 1, 7]`.
- `sumRange(1, 3)` = `4 + 1 + 7 = 12`.
- `update(2, 10)` sets index `2` to `10`; array becomes `[2, 4, 10, 7]`.
- `sumRange(1, 3)` = `4 + 10 + 7 = 21`.
- `sumRange(0, 0)` = `2`.

## Hint

Maintain prefix sums that stay cheap to update. A **Binary Indexed Tree (Fenwick Tree)**
supports both point updates and prefix-sum queries in O(log n), so `sumRange(l, r)` becomes
`prefix(r) - prefix(l - 1)`.
