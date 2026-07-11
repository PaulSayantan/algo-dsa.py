# Range Minimum Query with Point Updates

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (SPOJ / cp-algorithms
"sqrt decomposition"); the RMQ variant of LeetCode 307.

## Description

Design a data structure over an integer array `nums` that supports two
operations efficiently and interchangeably:

- `update(index, val)` — set `nums[index] = val`.
- `query(left, right)` — return the **minimum** value among
  `nums[left], nums[left + 1], ..., nums[right]` (inclusive, `left <= right`).

Recomputing the minimum by scanning the whole range on every `query` is `O(n)`
per call, which is too slow when there are many interleaved updates and
queries. You need a structure where both operations are sublinear on average.

Implement the `RangeMinQuery` class:

- `RangeMinQuery(int[] nums)` — initializes the structure.
- `void update(int index, int val)` — assigns `nums[index] = val`.
- `int query(int left, int right)` — returns the minimum on `[left, right]`.

## Constraints

- `1 <= nums.length <= 1 * 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= index < nums.length`
- `-10^9 <= val <= 10^9`
- `0 <= left <= right < nums.length`
- At most `1 * 10^5` calls total to `update` and `query`.

## Examples

### Example 1
- **Input:**
  ```
  ["RangeMinQuery", "query", "update", "query"]
  [[[1, 3, 2, 7, 9, 11]], [1, 5], [2, 10], [1, 5]]
  ```
- **Output:** `[null, 2, null, 3]`
- **Explanation:**
  - `query(1, 5)` = min(3, 2, 7, 9, 11) = `2`.
  - `update(2, 10)` changes the array to `[1, 3, 10, 7, 9, 11]`.
  - `query(1, 5)` = min(3, 10, 7, 9, 11) = `3`.

### Example 2
- **Input:**
  ```
  ["RangeMinQuery", "query", "query", "update", "query"]
  [[[5, 2, 8, 1, 9]], [0, 4], [0, 1], [3, 100], [2, 4]]
  ```
- **Output:** `[null, 1, 2, null, 8]`
- **Explanation:**
  - `query(0, 4)` = min(5, 2, 8, 1, 9) = `1`.
  - `query(0, 1)` = min(5, 2) = `2`.
  - `update(3, 100)` changes the array to `[5, 2, 8, 100, 9]`.
  - `query(2, 4)` = min(8, 100, 9) = `8`.

## Hint

Use **Square Root Decomposition**: cut the array into blocks of size about
`sqrt(n)` and store the minimum of each block. A range minimum scans the two
partial boundary blocks element by element and combines them with the
precomputed minima of the whole blocks in between. A point update only forces
a recompute of the single block that contains the changed index.
