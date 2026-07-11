# Range Sum Query - Mutable

**Difficulty:** Medium

**Source:** LeetCode 307 — Range Sum Query - Mutable

## Description

Given an integer array `nums`, implement a data structure `NumArray` that supports
the following two operations, which may be interleaved and called many times:

- `update(index, val)` — replace the element at position `index` with `val`.
- `sumRange(left, right)` — return the sum of the elements of `nums` between indices
  `left` and `right` **inclusive**, i.e. `nums[left] + nums[left + 1] + ... + nums[right]`.

You must handle both operations efficiently; a naive recomputation of the sum on
every query is too slow when there are many interleaved updates and queries.

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
- `sumRange(0, 2)` → `1 + 3 + 5 = 9`.
- `update(1, 2)` → array becomes `[1, 2, 5]`.
- `sumRange(0, 2)` → `1 + 2 + 5 = 8`.

### Example 2

```
Input:
["NumArray", "sumRange", "update", "sumRange"]
[[[9, -8]], [1, 1], [1, -3], [0, 1]]

Output:
[null, -8, null, 6]
```

**Explanation:**
- Build over `[9, -8]`.
- `sumRange(1, 1)` → `-8` (single element).
- `update(1, -3)` → array becomes `[9, -3]`.
- `sumRange(0, 1)` → `9 + (-3) = 6`.

## Hint

Use a **Segment Tree** whose nodes store the sum of a range: point updates and range
queries then each cost `O(log n)`.
