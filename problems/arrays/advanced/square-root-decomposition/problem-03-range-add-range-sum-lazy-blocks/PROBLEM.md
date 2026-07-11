# Range Add & Range Sum (Lazy Blocks)

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (cp-algorithms "sqrt
decomposition", the range-update variant).

## Description

Design a data structure over an integer array `nums` that supports **range
updates** and **range queries**:

- `range_add(left, right, delta)` — add `delta` to **every** element with index
  in `[left, right]` (inclusive).
- `range_sum(left, right)` — return the sum of all elements with index in
  `[left, right]` (inclusive).

A naive `range_add` that touches every element in the range is `O(n)` per call,
which is too slow when both operations are issued many times. You must make the
average cost of each operation sublinear.

Implement the `RangeAddSum` class:

- `RangeAddSum(int[] nums)` — initializes the structure.
- `void range_add(int left, int right, int delta)` — adds `delta` across the
  range.
- `int range_sum(int left, int right)` — returns the range sum.

## Constraints

- `1 <= nums.length <= 1 * 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `0 <= left <= right < nums.length`
- `-10^4 <= delta <= 10^4`
- At most `1 * 10^5` calls total to `range_add` and `range_sum`.

## Examples

### Example 1
- **Input:**
  ```
  ["RangeAddSum", "range_sum", "range_add", "range_sum", "range_sum"]
  [[[1, 2, 3, 4, 5]], [0, 4], [1, 3, 10], [0, 4], [2, 2]]
  ```
- **Output:** `[null, 15, null, 45, 13]`
- **Explanation:**
  - `range_sum(0, 4)` = `1 + 2 + 3 + 4 + 5 = 15`.
  - `range_add(1, 3, 10)` changes the array to `[1, 12, 13, 14, 5]`.
  - `range_sum(0, 4)` = `1 + 12 + 13 + 14 + 5 = 45`.
  - `range_sum(2, 2)` = `13`.

### Example 2
- **Input:**
  ```
  ["RangeAddSum", "range_add", "range_sum", "range_add", "range_sum"]
  [[[0, 0, 0, 0]], [0, 2, 5], [0, 3], [1, 3, 2], [1, 2]]
  ```
- **Output:** `[null, null, 15, null, 14]`
- **Explanation:**
  - `range_add(0, 2, 5)` changes the array to `[5, 5, 5, 0]`.
  - `range_sum(0, 3)` = `5 + 5 + 5 + 0 = 15`.
  - `range_add(1, 3, 2)` changes the array to `[5, 7, 7, 2]`.
  - `range_sum(1, 2)` = `7 + 7 = 14`.

## Hint

Use **Square Root Decomposition** with a per-block **lazy add**: divide the
array into blocks of size about `sqrt(n)`. Adding `delta` to a *whole* block is
recorded once as a pending `block_add[k]`, while the two partial boundary blocks
are updated element by element. A range sum combines each partial element, the
stored block sums, and the pending lazy contributions.
