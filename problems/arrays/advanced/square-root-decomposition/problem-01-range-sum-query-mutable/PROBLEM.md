# Range Sum Query - Mutable

**Difficulty:** Medium

**Source:** LeetCode 307 — Range Sum Query - Mutable

## Description

Given an integer array `nums`, handle multiple queries of the following two
types:

1. **Update** the value of an element in `nums`.
2. Calculate the **sum** of the elements of `nums` between indices `left` and
   `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` — initializes the object with the integer array
  `nums`.
- `void update(int index, int val)` — updates the value of `nums[index]` to
  be `val`.
- `int sumRange(int left, int right)` — returns the sum of the elements of
  `nums` between indices `left` and `right` inclusive (that is,
  `nums[left] + nums[left + 1] + ... + nums[right]`).

Both operations must be efficient because `update` and `sumRange` can each be
called up to tens of thousands of times, so a naive linear recomputation per
`sumRange` is too slow.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `0 <= index < nums.length`
- `-100 <= val <= 100`
- `0 <= left <= right < nums.length`
- At most `3 * 10^4` calls will be made to `update` and `sumRange`.

## Examples

### Example 1
- **Input:**
  ```
  ["NumArray", "sumRange", "update", "sumRange"]
  [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
  ```
- **Output:** `[null, 9, null, 8]`
- **Explanation:**
  - `NumArray([1, 3, 5])` builds the structure.
  - `sumRange(0, 2)` returns `1 + 3 + 5 = 9`.
  - `update(1, 2)` changes the array to `[1, 2, 5]`.
  - `sumRange(0, 2)` returns `1 + 2 + 5 = 8`.

### Example 2
- **Input:**
  ```
  ["NumArray", "sumRange", "update", "sumRange", "sumRange"]
  [[[-1, 3, 5]], [0, 2], [0, 2], [0, 2], [1, 1]]
  ```
- **Output:** `[null, 7, null, 10, 3]`
- **Explanation:**
  - `NumArray([-1, 3, 5])` builds the structure.
  - `sumRange(0, 2)` returns `-1 + 3 + 5 = 7`.
  - `update(0, 2)` changes the array to `[2, 3, 5]`.
  - `sumRange(0, 2)` returns `2 + 3 + 5 = 10`.
  - `sumRange(1, 1)` returns `3`.

## Hint

Use **Square Root Decomposition**: split `nums` into contiguous blocks of size
about `sqrt(n)` and store a running sum for each block. A range sum touches at
most two partial blocks plus a handful of whole blocks, and a point update only
adjusts one block's stored sum.
