# Range Count of Elements Not Exceeding K (with Point Updates)

**Difficulty:** Hard

**Source:** Classic competitive-programming problem (SPOJ "RACETIME"; the
sorted-blocks / sqrt-decomposition-with-binary-search pattern from
cp-algorithms).

## Description

Design a data structure over an integer array `nums` that supports:

- `update(index, val)` — set `nums[index] = val`.
- `query(left, right, k)` — return **how many** elements with index in
  `[left, right]` (inclusive) have value **less than or equal to** `k`.

Scanning the whole `[left, right]` range and comparing each element to `k` costs
`O(n)` per query, which is too slow when there are many interleaved updates and
queries. You need both operations to run in sublinear time on average.

Implement the `RangeCountLE` class:

- `RangeCountLE(int[] nums)` — initializes the structure.
- `void update(int index, int val)` — assigns `nums[index] = val`.
- `int query(int left, int right, int k)` — returns the count of in-range
  elements `<= k`.

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= index < nums.length`
- `-10^9 <= val <= 10^9`
- `0 <= left <= right < nums.length`
- `-10^9 <= k <= 10^9`
- At most `5 * 10^4` calls total to `update` and `query`.

## Examples

### Example 1
- **Input:**
  ```
  ["RangeCountLE", "query", "update", "query", "query"]
  [[[2, 1, 5, 3, 4, 6]], [0, 5, 3], [2, 0], [0, 5, 3], [1, 4, 3]]
  ```
- **Output:** `[null, 3, null, 4, 3]`
- **Explanation:**
  - `query(0, 5, 3)`: values `[2, 1, 5, 3, 4, 6]`; those `<= 3` are `2, 1, 3` →
    `3`.
  - `update(2, 0)` changes the array to `[2, 1, 0, 3, 4, 6]`.
  - `query(0, 5, 3)`: those `<= 3` are `2, 1, 0, 3` → `4`.
  - `query(1, 4, 3)`: subarray `[1, 0, 3, 4]`; those `<= 3` are `1, 0, 3` → `3`.

### Example 2
- **Input:**
  ```
  ["RangeCountLE", "query", "query", "update", "query"]
  [[[10, 20, 30, 40, 50]], [0, 4, 25], [2, 4, 50], [0, 100], [0, 2, 50]]
  ```
- **Output:** `[null, 2, 3, null, 2]`
- **Explanation:**
  - `query(0, 4, 25)`: those `<= 25` are `10, 20` → `2`.
  - `query(2, 4, 50)`: subarray `[30, 40, 50]`; all `<= 50` → `3`.
  - `update(0, 100)` changes the array to `[100, 20, 30, 40, 50]`.
  - `query(0, 2, 50)`: subarray `[100, 20, 30]`; those `<= 50` are `20, 30` →
    `2`.

## Hint

Use **Square Root Decomposition** where each block additionally keeps a
**sorted copy** of its elements. For a whole block, the count of values `<= k`
is a single binary search on its sorted copy; the two partial boundary blocks
are scanned directly. A point update removes the old value and inserts the new
one into just one block's sorted copy.
