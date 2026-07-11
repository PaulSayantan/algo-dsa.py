# Count of Smaller Numbers After Self

**Difficulty:** Hard

**Source:** LeetCode 315 — Count of Smaller Numbers After Self

## Description

You are given an integer array `nums`. Return an integer array `counts` where `counts[i]`
is the number of elements to the **right** of `nums[i]` that are strictly **smaller** than
`nums[i]`.

Formally, `counts[i] = |{ j : j > i and nums[j] < nums[i] }|`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Examples

### Example 1

```
Input:  nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

**Explanation:**
- To the right of `5` there are `2` and `1`, both smaller → count `2`.
- To the right of `2` there is `1`, which is smaller → count `1`.
- To the right of `6` there is `1`, which is smaller → count `1`.
- To the right of `1` there is nothing → count `0`.

### Example 2

```
Input:  nums = [-1, -1]
Output: [0, 0]
```

**Explanation:**
- To the right of the first `-1` there is only another `-1`, which is **not strictly
  smaller** → count `0`.
- The last element has nothing to its right → count `0`.

### Example 3

```
Input:  nums = [7, 6, 5, 4, 3]
Output: [4, 3, 2, 1, 0]
```

**Explanation:** The array is strictly decreasing, so every element is larger than all
elements to its right; counts are `4, 3, 2, 1, 0`.

## Hint

Process the array from **right to left** and, for each value, ask "how many values already
seen are strictly smaller than this one?" A **Binary Indexed Tree (Fenwick Tree)** indexed
by **coordinate-compressed value** answers that as a prefix-count query in O(log n), while
inserting the current value is a point update.
